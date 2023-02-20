import os
import arinc424.record as a424


def scan_folder(path):
    for file in os.scandir(path):
        scan_file(file)


def scan_file(file):
    k, t = 0, 0
    print("reading: {}".format(file.name))
    f2 = open("./unknown_records", "a")
    with open(file) as f:
        for line in f.readlines():
            r = a424.Record()
            if r.validate(line):
                t = t+1
                if r.read(line):
                    k = k+1
                else:
                    f2.write('{}\n{}'.format(r.parse_code(), line))
    f2.close()


def scan_file_and_dec(file):
    k, t = 0, 0
    with open(file) as f:
        for line in f.readlines():
            r = a424.Record()
            if r.validate(line):
                t = t+1
                if r.read(line):
                    k = k+1
                    print("\n{}".format(r.decode()))


def filter(line, sub) -> bool:
    return sub in line
