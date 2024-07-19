import os
import fnmatch
import re


def find_files(topdir):
    for path, _, filelist in os.walk(topdir):
        for name in filelist:
            yield os.path.join(path, name)


def filter_files(filenames):
    for name in filenames:
        if fnmatch.fnmatch(name, "*.txt") or fnmatch.fnmatch(name, "*.py"):
            yield name


def opener(filenames):
    for name in filenames:
        f = open(name, 'r', encoding='utf-8')
        yield f, name


def cat(filelist):
    for f, filename in filelist:
        with f:
            line_number = 0
            for line in f:
                line_number += 1
                yield line, filename, line_number


def grep(pattern, lines):
    for line, filename, line_number in lines:
        if pattern in line:
            yield line, filename, line_number


def process_lines(lines):
    for line, filename, line_number in lines:
        if filename.endswith(".py"):
            matches = re.findall(r'print\((.*?)\)', line)
            for match in matches:
                print(f"{filename}: Line {line_number}: {match.strip().upper()}")
        elif filename.endswith(".txt"):
            if line.strip():
                print(f"{filename}: Line {line_number}: {line.strip().upper()}")


def pipeline(topdir):
    file_paths = find_files(topdir)
    filtered_files = filter_files(file_paths)
    files = opener(filtered_files)
    lines = cat(files)
    filtered_lines = grep("print", lines)
    process_lines(filtered_lines)


pipeline(".")
