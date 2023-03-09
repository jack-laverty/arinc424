
class MORA():

    def read_primary(self, r):
        return {
            "Record Type":                         r[0],
            "Section Code":                        r[4:6],
            "Starting Latitude":                   r[13:16],
            "Starting Longitude":                  r[16:20],
            "MORA":                                r[30:33],
            "MORA (2)":                            r[33:36],
            "MORA (3)":                            r[36:39],
            "MORA (4)":                            r[39:42],
            "MORA (5)":                            r[42:45],
            "MORA (6)":                            r[45:48],
            "MORA (7)":                            r[48:51],
            "MORA (8)":                            r[51:54],
            "MORA (9)":                            r[54:57],
            "MORA (10)":                           r[57:60],
            "MORA (11)":                           r[60:63],
            "MORA (12)":                           r[63:66],
            "MORA (13)":                           r[66:69],
            "MORA (14)":                           r[69:72],
            "MORA (15)":                           r[72:75],
            "MORA (16)":                           r[75:78],
            "MORA (17)":                           r[78:81],
            "MORA (18)":                           r[81:84],
            "MORA (19)":                           r[84:87],
            "MORA (21)":                           r[87:90],
            "MORA (22)":                           r[90:93],
            "MORA (23)":                           r[93:96],
            "MORA (24)":                           r[96:99],
            "MORA (25)":                           r[99:102],
            "MORA (26)":                           r[102:105],
            "MORA (27)":                           r[105:108],
            "MORA (28)":                           r[108:111],
            "MORA (29)":                           r[111:114],
            "MORA (30)":                           r[114:117],
            "MORA (31)":                           r[117:120],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }

    def read(self, line):
        return self.read_primary(line)
