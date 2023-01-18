import arinc424.decoder as decode


class Airport():

    def read_primary(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Airport ICAO Identifier",         r[6:10],    decode.text),
            ("ICAO Code",                       r[10:12],   decode.text),
            ("ATA/IATA Designator",             r[13:16],   decode.text),
            ("PAD Identifier",                  r[16:21],   decode.text),
            ("Continuation Records No",         r[21],      decode.cont),
            ("Speed Limit Altitude",            r[22:27],   decode.text),
            ("Longest Runway",                  r[27:30],   decode.text),
            ("IFR Capability",                  r[30],      decode.text),
            ("Longest Runway Surface Code",     r[31],      decode.text),
            ("Airport Reference Pt. Latitude",  r[32:41],   decode.gps),
            ("Airport Reference Pt. Longitude", r[41:51],   decode.gps),
            ("Magnetic Variation",              r[51:56],   decode.text),
            ("Airport Elevation",               r[56:61],   decode.text),
            ("Speed Limit",                     r[61:64],   decode.text),
            ("Recommended Navaid",              r[64:68],   decode.text),
            ("ICAO Code",                       r[68:70],   decode.text),
            ("Transition Altitude",             r[70:75],   decode.text),
            ("Transition Level",                r[75:80],   decode.text),
            ("Public Military Indicator",       r[80],      decode.text),
            ("Time Zone",                       r[81:84],   decode.text),
            ("Daylight Indicator",              r[84],      decode.text),
            ("Magnetic/True Indicator",         r[85],      decode.text),
            ("Datum Code",                      r[86:89],   decode.text),
            ("Airport Name",                    r[93:123],  decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle),
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Heliport Identifier",             r[6:10],    decode.text),
            ("ICAO Code",                       r[10:12],   decode.text),
            ("ATA/IATA Designator",             r[13:16],   decode.text),
            ("PAD Identifier",                  r[16:21],   decode.text),
            ("Continuation Records No",         r[21],      decode.cont),
            ("Application Type",                r[22],      decode.app),
            ("Notes",                           r[23:92],   decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read_flight0(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Heliport Identifier",             r[6:10],    decode.text),
            ("ICAO Code",                       r[10:12],   decode.text),
            ("ATA/IATA Designator",             r[13:16],   decode.text),
            ("PAD Identifier",                  r[16:21],   decode.text),
            ("Continuation Records No",         r[21],      decode.cont),
            ("Application Type",                r[22],      decode.app),
            ("FIR Identifier",                  r[23:27],   decode.text),
            ("UIR Identifier",                  r[27:31],   decode.text),
            ("Start/End Indicator",             r[31],      decode.text),
            ("Start/End Date/Time",             r[32:43],   decode.text),
            ("Controlled A/S Indicator",        r[66],      decode.text),
            ("Controlled A/S Airport Indent",   r[67:71],   decode.text),
            ("Controlled A/S Airport ICAO",     r[71:73],   decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read_flight1(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Heliport Identifier",             r[6:10],    decode.text),
            ("ICAO Code",                       r[10:12],   decode.text),
            ("ATA/IATA Designator",             r[13:16],   decode.text),
            ("PAD Identifier",                  r[16:21],   decode.text),
            ("Continuation Records No",         r[21],      decode.cont),
            ("Application Type",                r[22],      decode.app),
            ("Notes",                           r[23:92],   decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
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
                    return self.read_flight0(line)
                case 'Q':
                    return self.read_flight1(line)
                case 'S':
                    return
                case _:
                    raise ValueError('Unknown Application Type')
