
class GLS():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport and Heliport Identifier",     r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("GLS Ref Path Identifier",             r[13:17]),
            ("GLS Category",                        r[17]),
            ("Continuation Record No",              r[18:21]),
            ("GLS Channel",                         r[22:27]),
            ("Runway Identifier",                   r[27:32]),
            ("GLS Approach Bearing",                r[51:55]),
            ("Station Latitude",                    r[55:64]),
            ("Station Longitude",                   r[64:74]),
            ("GLS Station Ident",                   r[74:78]),
            ("Service Volume Radius",               r[83:85]),
            ("TDMA Slots",                          r[85:87]),
            ("GLS Approach Slope",                  r[87:90]),
            ("Magnetic Variation",                  r[90:95]),
            ("Station Elevation",                   r[97:102]),
            ("Datum Code",                          r[102:105]),
            ("Station Type",                        r[105:108]),
            ("Station Elevation WGS",               r[110:115]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport and Heliport Identifier",     r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("GLS Ref Path Identifier",             r[13:17]),
            ("GLS Category",                        r[17]),
            ("Continuation Record No",              r[18:21]),
            ("Application Type",                    r[22]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]
