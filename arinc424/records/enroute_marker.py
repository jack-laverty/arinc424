
class Marker():

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4:6]),
            ("Marker Identifier",                   r[13:17]),
            ("ICAO Code",                           r[19:21]),
            ("Continuation Record No",              r[21]),
            ("Marker Code",                         r[22:26]),
            ("Marker Shape",                        r[27]),
            ("Marker Power",                        r[28]),
            ("Marker Latitude",                     r[32:41]),
            ("Marker Longitude",                    r[41:51]),
            ("Minor Axis",                          r[51:55]),
            ("Magnetic Variation",                  r[74:79]),
            ("Facility Elevation",                  r[79:84]),
            ("Datum Code",                          r[84:87]),
            ("Marker Name",                         r[93:123]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4:6]),
            ("ICAO Code",                           r[10:12]),
            ("Subsection Code",                     r[12]),
            ("ICAO Code",                           r[19:21]),
            ("Continuation Record No",              r[21]),
            ("Application Type",                    r[22]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read(self, line):
        if int(line[21]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[22]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []
