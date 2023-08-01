import os
import arinc424.record as arinc424


def read_folder(path):
    for file in os.scandir(path):
        read_file(path + '/' + file.name)


def read_file(path):
    with open(path) as f:
        for line in f.readlines():
            r = arinc424.Record()
            r.read(line)


def read_file_and_dec(file):
    with open(file) as f:
        for line in f.readlines():
            r = arinc424.Record()
            if r.read(line):
                r.decode()
