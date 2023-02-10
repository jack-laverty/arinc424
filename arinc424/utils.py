import os
import arinc424.record as a424


def scan_folder(path):
    for file in os.scandir(path):
        scan_file(file)


def scan_file(file):
    k, t = 0, 0
    f2 = open("debug.txt", "w")
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
    print('\n{}\n{:9}{}\n{:9}{}'.format(file.name,
                                        'Parsed:', k,
                                        'Unknown:', t-k))
