import arinc424.decoder as decode


class Runway():

    def read_primary(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Airport ICAO Identifier",         r[6:10],    decode.text),
            ("ICAO Code",                       r[10:12],   decode.text),
            ("Runway Identifier",               r[13:18],   decode.text),
            ("Continuation Records No",         r[21],      decode.cont),
            ("Runway Length",                   r[22:27],   decode.text),
            ("Runway Magnetic Bearing",         r[27:31],   decode.text),
            ("Runway Latitude",                 r[32:41],   decode.gps),
            ("Runway Longitude",                r[41:51],   decode.gps),
            ("Runway Gradient",                 r[51:56],   decode.text),
            ("Landing Threshold Elevation",     r[66:71],   decode.text),
            ("Displaced Threshold Dist",        r[71:75],   decode.text),
            ("Threshold Crossing Height",       r[75:77],   decode.text),
            ("Runway Width",                    r[77:80],   decode.text),
            ("TCH Value Indicator",             r[80],      decode.text),
            ("Localizer/MLS/GLS Ref Path Ident", r[81:85],  decode.text),
            ("Localizer/MLS/GLS Category/Class", r[85],     decode.text),
            ("Stopway",                         r[86:90],   decode.text),
            ("Localizer/MLS/GLS Ref Path Ident (2)", r[90:94], decode.text),
            ("Localizer/MLS/GLS Category/Class (2)", r[94], decode.text),
            ("Runway Description",              r[101:123], decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Airport ICAO Identifier",         r[6:10],    decode.text),
            ("ICAO Code",                       r[10:12],   decode.text),
            ("Runway Identifier",               r[13:18],   decode.text),
            ("Continuation Records No",         r[21],      decode.cont),
            ("Notes",                           r[23:92],   decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read_sim(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Airport ICAO Identifier",         r[6:10],    decode.text),
            ("ICAO Code",                       r[10:12],   decode.text),
            ("Runway Identifier",               r[13:18],   decode.text),
            ("Continuation Records No",         r[21],      decode.cont),
            ("Application Type",                r[22],      decode.app),
            ("Runway True Bearing",             r[51:56],   decode.text),
            ("True Bearing Source",             r[56],      decode.text),
            ("TDZE Location",                   r[65],      decode.text),
            ("Touchdown Zone Elevation",        r[66:71],   decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle),
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
