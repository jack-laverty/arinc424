import os
import arinc424.record as a424


def read_folder(path):
    for file in os.scandir(path):
        read_file(path + '/' + file.name)


def read_file(path):
    t, k, u = 0, 0, 0
    file = path.rsplit('/', 1)[-1]
    f2 = open('./UNKNOWN_' + file.rsplit('/', 1)[-1], 'w')
    print("\nreading: {}".format(file))
    with open(path) as f:
        for line in f.readlines():
            t += 1
            r = a424.Record()
            q = r.read(line)
            if q == a424.ERR_NONE:
                k += 1
            elif q == a424.ERR_UNKNOWN:
                u += 1
                f2.write(line)
    f2.close()
    print('{:17}{}'.format('lines read', t))
    print('{:17}{}'.format('records found', k))
    print('{:17}{}'.format('unknown records', u))


def read_file_and_dec(file):
    with open(file) as f:
        for line in f.readlines():
            r = a424.Record()
            if r.read(line) == a424.ERR_NONE:
                print("\n{}".format(r.decode()))


def filter(line, sub) -> bool:
    return sub in line
