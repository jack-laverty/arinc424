import os
import sys
import records.navaid as nav
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
        
        section, subsection = sections.parse_section(line)
        if section == 'Navaid':
            nr = nav.Navaid()
            nr.parse_record(line)
            # nr.dump()
            w.write(nr.json())
            print(nr.json(False))
