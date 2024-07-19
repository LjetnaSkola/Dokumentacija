# -*- coding: UTF-8 -*-
import os
import sys
import fnmatch
import gzip, bz2

def find_files(topdir, pattern):
	for path, dirname, filelist in os.walk(topdir):
		for name in filelist:
			if fnmatch.fnmatch(name, pattern):
				yield os.path.join(path,name)

def opener(filenames):
    for name in filenames:
        if name.endswith(".gz"):
            f = gzip.open(name)
        elif name.endswith(".bz2"):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
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

putanje = find_files(".","1*") # putanje svih fajlova iz trenutnog foldera koje pocinju sa 1
files = opener(putanje) # otvori ih ili kao obican tekstualni ili kao zip fajl. Fajl po fajl
lines = cat(files) # procitaj liniju po liniju iz fajla
pylines = grep("print", lines) # filter nad linijom - daj samo one koje imaju print u sebi
for line, filename, line_number in pylines:
   print(f"{filename}: Line {line_number}: {line.strip()}")

# prosiriti ovaj primjer tako da se odstampa prvo fajl, pa broj linije u fajlu, pa tek onda linija
