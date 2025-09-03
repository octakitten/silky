import glob
import re
#from file_read_backwards import FileReadBackwards
import pathlib

def main():

    # read through all the log files written during model training and extract info about the victories
    # and saved models.
    filenames = glob.glob("./logs/*log.txt")
    phrase1 = re.compile(r'victory! it took this many turns:')
    phrase2 = re.compile(r"victory! a winning model was found! it took this many iterations:")
    victories = []
    phrase3 = re.compile(r'defeat! after this many turns:')
    phrase4 = re.compile(r'game over! number of attempts so far:')
    defeats = []

    # deprecated code, leaving it here incase there's a reason to use it again
    #for file in filenames:
    #    with FileReadBackwards(file, encoding="utf-8") as open_file:
    #        lines = []
    #        for i in range(4):
    #            lines.append(open_file.readline())
    #        for line in lines:
    #            if phrase1.search(line):
    #                victories.append((lines[0], lines[2]))
    
    best_defeat_turns = 0
    best_defeat_iters = 0
    best_defeat_item_number = 0
    best_victory_turns = 1000000
    best_victory_iters = 1000000
    best_victory_item_number = 0

    for file in filenames:
        with open(file, 'r') as open_file:
            for line in open_file:
                if phrase3.search(line):
                    turns = next(open_file)
                if phrase4.search(line):
                    iters = next(open_file)
                    defeats.append((turns, iters))
                    if (int(turns) > int(best_defeat_turns)):
                        best_defeat_turns = turns
                        best_defeat_iters = iters
                if phrase1.search(line):
                    turns = next(open_file)
                if phrase2.search(line):
                    iters = next(open_file)
                    victories.append((turns, iters))
                    if (int(turns) < int(best_victory_turns)):
                        best_victory_turns = turns
                        best_victory_iters = iters


    # then save that info to disk in a summary file which we can read later
    # the lines in the summary file contain first
    # the number of turns a victory took in the game
    # and then the number of iterations it took to find a winning model that run
    directory = pathlib.Path("./logs")
    output = pathlib.Path("./logs/summary-list.txt")
    backup = pathlib.Path("./logs/summary-list-prev.txt")
    output2 = pathlib.Path("./logs/summary.txt")
    backup2 = pathlib.Path("./logs/summary-prev.txt")

    if directory.exists():
        if output.exists():
            output.replace(backup)
        if output2.exists():
            output2.replace(backup2)
        output.touch()
        output2.touch()
        with open("logs/summary-list.txt", 'w') as summary:
            summary.write("VICTORIES:\n")
            for entry in victories:
                summary.write(entry[0] + entry[1] + "\n")
            summary.write("DEFEATS:\n")
            for entry in defeats:
                summary.write(entry[0] + entry[1] + "\n")
        with open("logs/summary.txt", 'w') as summary:
            summary.write("Best victory turns:\n")
            summary.write(str(best_victory_turns) + "\n")
            summary.write("Best victory iters:\n")
            summary.write(str(best_victory_iters) + "\n" + "\n")
            summary.write("Best defeat turns:\n")
            summary.write(str(best_defeat_turns) + "\n")
            summary.write("Best defeat iters:\n")
            summary.write(str(best_defeat_iters) + "\n")


if __name__ == "__main__":
    main()
