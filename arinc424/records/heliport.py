import arinc424.decoder as decode


class Heliport():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Heliport Identifier",     r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["ATA/IATA Designator",     r[13:16],   decode.text])
        fields.append(["PAD Identifier",          r[16:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Speed Limit Altitude",    r[22:27],   decode.text])
        fields.append(["Datum Code",              r[27:30],   decode.text])
        fields.append(["IFR Indicator",           r[30],      decode.text])
        fields.append(["Latitude",                r[32:41],   decode.gps])
        fields.append(["Longitude",               r[41:51],   decode.gps])
        fields.append(["Magnetic Variation",      r[51:56],   decode.text])
        fields.append(["Heliport Elevation",      r[56:61],   decode.text])
        fields.append(["Speed Limit",             r[61:64],   decode.text])
        fields.append(["Recommended VHF Navaid",  r[64:68],   decode.text])
        fields.append(["ICAO Code",               r[68:70],   decode.text])
        fields.append(["Transition Altitude",     r[70:75],   decode.text])
        fields.append(["Transition Level",        r[75:80],   decode.text])
        fields.append(["Public Military Indicator",
                      r[80], decode.text])
        fields.append(["Time Zone",               r[81:84],   decode.text])
        fields.append(["Daylight Indicator",      r[84],      decode.text])
        fields.append(["Pad Dimensions",          r[85:91],   decode.text])
        fields.append(["Magnetic/True Indicator", r[91],      decode.text])
        fields.append(["Heliport Name",           r[93:123],  decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Heliport Identifier",     r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["ATA/IATA Designator",     r[13:16],   decode.text])
        fields.append(["PAD Identifier",          r[16:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["Notes",                   r[23:92],   decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_flight0(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Heliport Identifier",     r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["ATA/IATA Designator",     r[13:16],   decode.text])
        fields.append(["PAD Identifier",          r[16:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["FIR Identifier",          r[23:27],   decode.text])
        fields.append(["UIR Identifier",          r[27:31],   decode.text])
        fields.append(["Start/End Indicator",     r[31],      decode.text])
        fields.append(["Start/End Date/Time",     r[32:43],   decode.text])
        fields.append(["Controlled A/S Indicator",
                      r[66], decode.text])
        fields.append(["Controlled A/S Airport Indentifier",
                      r[67:71], decode.text])
        fields.append(["Controlled A/S Airport ICAO",
                      r[71:73], decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields
    
    def read_flight1(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Heliport Identifier",     r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["ATA/IATA Designator",     r[13:16],   decode.text])
        fields.append(["PAD Identifier",          r[16:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["Notes",                   r[23:92],   decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

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
