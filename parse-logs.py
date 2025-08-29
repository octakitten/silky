import glob
import re
from file_read_backwards import FileReadBackwards
import pathlib

def main():

    # read through all the log files written during model training and extract info about the victories
    # and saved models.
    filenames = glob.glob("./logs/*log.txt")
    phrase1 = re.compile(r'victory! it took this many turns:')
    phrase2 = "victory! a winning model was found! it took this many iterations:"
    victories = []

    for file in filenames:
        with FileReadBackwards(file, encoding="utf-8") as open_file:
            lines = []
            for i in range(4):
                lines.append(open_file.readline())
            for line in lines:
                if phrase1.search(line):
                    victories.append((lines[0], lines[2]))

    # then save that info to disk in a summary file which we can read later
    # the lines in the summary file contain first
    # the number of turns a victory took in the game
    # and then the number of iterations it took to find a winning model that run
    output = pathlib.Path("./logs/summary.txt")
    directory = pathlib.Path("./logs")
    backup = pathlib.Path("./logs/summary-prev.txt")
    
    if directory.exists():
        if output.exists():
            output.replace(backup)
        output.touch()
        with open("logs/summary.txt", 'w') as summary:
            for entry in victories:
                summary.write(entry[0] + entry[1] + "\n")

if __name__ == "__main__":
    main()
