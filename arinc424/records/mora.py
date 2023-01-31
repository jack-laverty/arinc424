
class Mora():

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Section Code",                        r[4:6]),
            ("Starting Latitude",                   r[13:16]),
            ("Starting Longitude",                  r[16:20]),
            ("MORA",                                r[30:33]),
            ("MORA",                                r[33:36]),
            ("MORA",                                r[36:39]),
            ("MORA",                                r[39:42]),
            ("MORA",                                r[42:45]),
            ("MORA",                                r[45:48]),
            ("MORA",                                r[48:51]),
            ("MORA",                                r[51:54]),
            ("MORA",                                r[54:57]),
            ("MORA",                                r[57:60]),
            ("MORA",                                r[60:63]),
            ("MORA",                                r[63:66]),
            ("MORA",                                r[66:69]),
            ("MORA",                                r[69:72]),
            ("MORA",                                r[72:75]),
            ("MORA",                                r[75:78]),
            ("MORA",                                r[78:81]),
            ("MORA",                                r[81:84]),
            ("MORA",                                r[84:87]),
            ("MORA",                                r[87:90]),
            ("MORA",                                r[90:93]),
            ("MORA",                                r[93:96]),
            ("MORA",                                r[96:99]),
            ("MORA",                                r[99:102]),
            ("MORA",                                r[102:105]),
            ("MORA",                                r[105:108]),
            ("MORA",                                r[108:111]),
            ("MORA",                                r[111:114]),
            ("MORA",                                r[114:117]),
            ("MORA",                                r[117:120]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read(self, line):
        return self.read_primary(line)
