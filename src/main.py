import os
import sys
import records.navaid as nav
import records.airport as airport
import sections
import json

class Config():
    input = ''
    search = ''
    def init():
        return

if __name__ == "__main__":

    # reading .config file
    config = Config()
    with open("../.config") as f:
        for line in f.readlines():
            line = line.strip().split()
            if line[0] == 'FILE':
                config.input = line[1]
            elif line[0] == 'SEARCH':
                config.search = line[1]
    f.close()

    if config.input != '':
        f = open(config.input)
    else:
        print("invalid .config: no input file")
        exit()

    dir = os.path.join("..", "output")
    if not os.path.exists(dir):
        os.mkdir(dir)

    w = open(dir + "\\" + config.search + ".json", 'w')
    for line in f.readlines():
        
        if line.startswith('S' or 'T') == False:
            continue
        
        if config.search not in line:
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

