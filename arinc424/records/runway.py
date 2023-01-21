
class Runway():

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport ICAO Identifier",             r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Runway Identifier",                   r[13:18]),
            ("Continuation Record No",              r[21]),
            ("Runway Length",                       r[22:27]),
            ("Runway Magnetic Bearing",             r[27:31]),
            ("Runway Latitude",                     r[32:41]),
            ("Runway Longitude",                    r[41:51]),
            ("Runway Gradient",                     r[51:56]),
            ("Landing Threshold Elevation",         r[66:71]),
            ("Displaced Threshold Dist",            r[71:75]),
            ("Threshold Crossing Height",           r[75:77]),
            ("Runway Width",                        r[77:80]),
            ("TCH Value Indicator",                 r[80]),
            ("Localizer/MLS/GLS Ref Path Ident",    r[81:85]),
            ("Localizer/MLS/GLS Category/Class",    r[85]),
            ("Stopway",                             r[86:90]),
            ("Localizer/MLS/GLS Ref Path Ident (2)", r[90:94]),
            ("Localizer/MLS/GLS Category/Class (2)", r[94]),
            ("Runway Description",                  r[101:123]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport ICAO Identifier",             r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Runway Identifier",                   r[13:18]),
            ("Continuation Record No",              r[21]),
            ("Notes",                               r[23:92]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_sim(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport ICAO Identifier",             r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Runway Identifier",                   r[13:18]),
            ("Continuation Record No",              r[21]),
            ("Application Type",                    r[22]),
            ("Runway True Bearing",                 r[51:56]),
            ("True Bearing Source",                 r[56]),
            ("TDZE Location",                       r[65]),
            ("Touchdown Zone Elevation",            r[66:71]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132]),
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
                case 'C':
                    return
                case 'E':
                    return
                case 'L':
                    return
                case 'N':
                    return
                case 'T':
                    return
                case 'U':
                    return
                case 'V':
                    return
                case 'P':
                    return
                case 'Q':
                    return
                case 'S':
                    return self.read_sim(line)
                case _:
                    raise ValueError('Unknown Application Type')
