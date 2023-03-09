import os
import arinc424.record as a424


def scan_folder(path):
    os.remove("./unknown_records")
    for file in os.scandir(path):
        scan_file(path + '/' + file.name)


def scan_file(file):
    k, t = 0, 0
    print("reading: {}".format(file))
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
    with open(file) as f:
        for line in f.readlines():
            r = a424.Record()
            if r.validate(line):
                if r.read(line):
                    print("\n{}".format(r.decode()))


def filter(line, sub) -> bool:
    return sub in line
