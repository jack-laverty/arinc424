import os
import sys
import records.navaid as nav
import records.airport as airport
import sections
import json

class Config():
    input = None
    search = None
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
    f.close()

    # try to open the input file
    if config.input != None:
        f = open(config.input)
    else:
        print("invalid .config: no input file")
        exit()

    # read search term
    if len(sys.argv) > 1:
        config.search = sys.argv[1] 

    # create an output folder
    dir = os.path.join("..", "output")
    if not os.path.exists(dir):
        os.mkdir(dir)

    # create an output file
    out_file = "output"
    if config.search != None:
        out_file += ("_" + config.search)
    w = open(dir + "\\" + out_file + ".json", 'w')

    # read the records
    for line in f.readlines():
        if line.startswith('S' or 'T') == False:
            continue
        if config.search not in line and config.search != None:
            continue
        section = sections.Section()
        section.read(line)
        # print("Record Type:", section.decode())
        if section.is_navaid():
            nr = nav.Navaid()
            nr.read(line, section)
        elif section.is_airport():
            ap = airport.Airport()
            ap.read(line, section)
            w.write(ap.json(False))
