import os
import arinc424.record as a424


def scan_folder(path):
    for file in os.scandir(path):
        scan_file(file)


def scan_file(file):
    k, t = 0, 0
    with open(file) as f:
        for line in f.readlines():
            r = a424.Record()
            if r.validate(line):
                t = t+1
                if r.read(line):
                    k = k+1
    print('\n{}\n{:9}{}\n{:9}{}'.format(file.name,
                                        'Parsed:', k,
                                        'Unknown:', t-k))
