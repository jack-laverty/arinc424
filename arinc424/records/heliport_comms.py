import arinc424.decoder as decode


class HeliportComms():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Heliport Identifier",     r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["Communications Type",     r[13:16],   decode.text])
        fields.append(["Communications Freq",     r[16:23],   decode.text])
        fields.append(["Guard/Transmit",          r[23],      decode.text])
        fields.append(["Frequency Units",         r[24],      decode.text])
        fields.append(["Continuation Records No", r[25],      decode.cont])
        fields.append(["Service Indicator",       r[26:29],   decode.text])
        fields.append(["Radar Service",           r[29],      decode.text])
        fields.append(["Modulation",              r[30],      decode.text])
        fields.append(["Signal Emission",         r[31],      decode.text])
        fields.append(["Latitude",                r[32:41],   decode.gps])
        fields.append(["Longitude",               r[41:51],   decode.gps])
        fields.append(["Magnetic Variation",      r[51:56],   decode.text])
        fields.append(["Facility Elevation",      r[56:61],   decode.text])
        fields.append(["H24 Indicator",           r[61],      decode.text])
        fields.append(["Sectorization",           r[62:68],   decode.text])
        fields.append(["Altitude Description",    r[68],      decode.text])
        fields.append(["Communication Altitude",  r[69:74],   decode.text])
        fields.append(["Communication Altitude",  r[74:79],   decode.text])
        fields.append(["Sector Facility",         r[79:83],   decode.text])
        fields.append(["ICAO Code",               r[83:85],   decode.text])
        fields.append(["Section Code",            r[85:87],   decode.text]) # TODO
        fields.append(["Distance Description",    r[87],      decode.text])
        fields.append(["Communications Distance", r[88:90],   decode.text])
        fields.append(["Remote Facility",         r[90:94],   decode.text])
        fields.append(["ICAO Code",               r[94:96],   decode.text])
        fields.append(["Section Code",            r[96:98],   decode.text])
        fields.append(["Call Sign",               r[98:123],  decode.text])
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
        fields.append(["Communications Type",     r[13:16],   decode.text])
        fields.append(["Communications Freq",     r[16:23],   decode.text])
        fields.append(["Guard/Transmit",          r[23],      decode.text])
        fields.append(["Frequency Units",         r[24],      decode.text])
        fields.append(["Continuation Records No", r[25],      decode.cont])
        fields.append(["Application Type",        r[26],      decode.app])
        fields.append(["Narrative",               r[27:87],   decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_cont1(self, r): # ??
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Heliport Identifier",     r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["Communications Type",     r[13:16],   decode.text])
        fields.append(["Communications Freq",     r[16:23],   decode.text])
        fields.append(["Guard/Transmit",          r[23],      decode.text])
        fields.append(["Frequency Units",         r[24],      decode.text])
        fields.append(["Continuation Records No", r[25],      decode.cont])
        fields.append(["Application Type",        r[26],      decode.app])
        fields.append(["Time Code",               r[27],      decode.text])
        fields.append(["NOTAM",                   r[28],      decode.text])
        fields.append(["Time Indicator",          r[29],      decode.text])
        fields.append(["Time of Operation",       r[30:40],   decode.text])
        fields.append(["Time of Operation",       r[40:50],   decode.text])
        fields.append(["Time of Operation",       r[50:60],   decode.text])
        fields.append(["Time of Operation",       r[60:70],   decode.text])
        fields.append(["Time of Operation",       r[70:80],   decode.text])
        fields.append(["Time of Operation",       r[80:90],   decode.text])
        fields.append(["Time of Operation",       r[90:100],  decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields
    
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
                    return self.read_flight0(line)
                case 'Q':
                    return self.read_flight1(line)
                case 'S':
                    return
                case _:
                    raise ValueError('Unknown Application Type')
