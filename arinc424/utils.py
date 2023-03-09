import os
import arinc424.record as a424


def read_folder(path):
    for file in os.scandir(path):
        read_file(path + '/' + file.name)


def read_file(file):
    print("reading: {}".format(file))
    with open(file) as f:
        for line in f.readlines():
            r = a424.Record()
            r.read(line)


def read_file_and_dec(file):
    with open(file) as f:
        for line in f.readlines():
            r = a424.Record()
            if r.read(line):
                print("\n{}".format(r.decode()))


def filter(line, sub) -> bool:
    return sub in line
