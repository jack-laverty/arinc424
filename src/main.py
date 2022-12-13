import os
import sys
import records.navaid as nav
import records.airport as airport
import sections
import json

if __name__ == "__main__":
    f = open("../.config")
    conf = f.readline().split()
    f.close()
    if conf[0] == 'FILE':
        f = open(conf[1])
    else:
        print("invalid .config")
        exit()

    dir = os.path.join("..", "output")
    if not os.path.exists(dir):
        os.mkdir(dir)

    w = open(dir + "\YPTN.json", 'w')
    for line in f.readlines():
        
        if line.startswith('S' or 'T') == False:
            continue
        
        if 'YPTN' not in line:
            continue

        section = sections.Section()
        section.read(line)
        print("Record Type:", section.decode())
        if section.is_navaid():
            nr = nav.Navaid()
            nr.read(line, section)
        elif section.is_airport():
            ap = airport.Airport()
            ap.read(line, section)
            w.write(ap.json(False))

