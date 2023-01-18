import arinc424.decoder as decode


class HeliportComms():

    def read_primary(self, r):
        return [
            ("Record Type",             r[0],       decode.record),
            ("Customer / Area Code",    r[1:4],     decode.text),
            ("Section Code",            r[4]+r[12], decode.section),
            ("Heliport Identifier",     r[6:10],    decode.text),
            ("ICAO Code",               r[10:12],   decode.text),
            ("Communications Type",     r[13:16],   decode.text),
            ("Communications Freq",     r[16:23],   decode.text),
            ("Guard/Transmit",          r[23],      decode.text),
            ("Frequency Units",         r[24],      decode.text),
            ("Continuation Records No", r[25],      decode.cont),
            ("Service Indicator",       r[26:29],   decode.text),
            ("Radar Service",           r[29],      decode.text),
            ("Modulation",              r[30],      decode.text),
            ("Signal Emission",         r[31],      decode.text),
            ("Latitude",                r[32:41],   decode.gps),
            ("Longitude",               r[41:51],   decode.gps),
            ("Magnetic Variation",      r[51:56],   decode.text),
            ("Facility Elevation",      r[56:61],   decode.text),
            ("H24 Indicator",           r[61],      decode.text),
            ("Sectorization",           r[62:68],   decode.text),
            ("Altitude Description",    r[68],      decode.text),
            ("Communication Altitude",  r[69:74],   decode.text),
            ("Communication Altitude",  r[74:79],   decode.text),
            ("Sector Facility",         r[79:83],   decode.text),
            ("ICAO Code",               r[83:85],   decode.text),
            ("Section Code",            r[85:87],   decode.text),
            ("Distance Description",    r[87],      decode.text),
            ("Communications Distance", r[88:90],   decode.text),
            ("Remote Facility",         r[90:94],   decode.text),
            ("ICAO Code",               r[94:96],   decode.text),
            ("Section Code",            r[96:98],   decode.text),
            ("Call Sign",               r[98:123],  decode.text),
            ("File Record No",          r[123:128], decode.text),
            ("Cycle Date",              r[128:132], decode.cycle)
        ]

    def read_cont(self, r):
        return [
            ("Record Type",             r[0],       decode.record),
            ("Customer / Area Code",    r[1:4],     decode.text),
            ("Section Code",            r[4]+r[12], decode.section),
            ("Heliport Identifier",     r[6:10],    decode.text),
            ("ICAO Code",               r[10:12],   decode.text),
            ("Communications Type",     r[13:16],   decode.text),
            ("Communications Freq",     r[16:23],   decode.text),
            ("Guard/Transmit",          r[23],      decode.text),
            ("Frequency Units",         r[24],      decode.text),
            ("Continuation Records No", r[25],      decode.cont),
            ("Application Type",        r[26],      decode.app),
            ("Narrative",               r[27:87],   decode.text),
            ("File Record No",          r[123:128], decode.text),
            ("Cycle Date",              r[128:132], decode.cycle)
        ]

    def read_cont1(self, r):
        return [
            ("Record Type",             r[0],       decode.record),
            ("Customer / Area Code",    r[1:4],     decode.text),
            ("Section Code",            r[4]+r[12], decode.section),
            ("Heliport Identifier",     r[6:10],    decode.text),
            ("ICAO Code",               r[10:12],   decode.text),
            ("Communications Type",     r[13:16],   decode.text),
            ("Communications Freq",     r[16:23],   decode.text),
            ("Guard/Transmit",          r[23],      decode.text),
            ("Frequency Units",         r[24],      decode.text),
            ("Continuation Records No", r[25],      decode.cont),
            ("Application Type",        r[26],      decode.app),
            ("Time Code",               r[27],      decode.text),
            ("NOTAM",                   r[28],      decode.text),
            ("Time Indicator",          r[29],      decode.text),
            ("Time of Operation",       r[30:40],   decode.text),
            ("Time of Operation",       r[40:50],   decode.text),
            ("Time of Operation",       r[50:60],   decode.text),
            ("Time of Operation",       r[60:70],   decode.text),
            ("Time of Operation",       r[70:80],   decode.text),
            ("Time of Operation",       r[80:90],   decode.text),
            ("Time of Operation",       r[90:100],  decode.text),
            ("File Record No",          r[123:128], decode.text),
            ("Cycle Date",              r[128:132], decode.cycle)
        ]

    def read(self, line):
        if int(line[25]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[26]:
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
                    return
                case _:
                    raise ValueError('Unknown Application Type')
