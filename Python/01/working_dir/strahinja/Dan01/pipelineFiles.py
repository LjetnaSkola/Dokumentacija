# -*- coding: UTF-8 -*-
import os


def find_files(topdir):
    for path, dirname, filelist in os.walk(topdir):
        for name in filelist:
            yield os.path.join(path, name)


def filter_files(files):
    for file in files:
        if file.endswith(".txt") or file.endswith(".py"):
            yield file


def opener(filenames):
    for name in filenames:
        try:
            with open(name, 'r') as file:
                lines = file.readlines()
                if name.endswith(".py"):
                    for line in [l for l in lines if "print(" in l and "'print(" not in l and "\"print(" not in l]:
                        text = line.split('print(')[1].rsplit(')', 1)[0]
                        if text and not text.isspace():
                            yield text.strip()
                elif name.endswith(".txt"):
                    for line in [l for l in lines if l and not l.isspace()]:
                        yield line.strip()
        except:
            pass


if __name__ == "__main__":
    files = find_files(".")
    pyAndTextOnly = filter_files(files)
    for line in opener(pyAndTextOnly):
        print(line)
