import os
import re
def find_files():
    files = os.listdir()
    return files

def filter(filenames):
    for file in filenames:
        if file.endswith("txt") or file.endswith(".py"):
            f = open(file)
        yield f

def cat(fileList):
    for file in fileList:
        for line in file:
            if file.name.endswith(".txt") and line != "\n":
                yield line
            elif file.name.endswith(".py") and "print" in line:
                pattern = r'print\s*\((.*)\)'
                matches = re.findall(pattern, line)
                for match in matches:
                        yield match


def main():
    files = find_files()
    filtered = filter(files)
    cated = cat(filtered)
    for file in cated:
        print(file)

if __name__ == "__main__":
    main()
