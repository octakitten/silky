import os
import glob
import re
from file_read_backwards import FileReadBackwards

main():

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
                    victories.append((lines[1], lines[3]))
