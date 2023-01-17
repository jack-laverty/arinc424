import arinc424.decoder as decode


class Runway():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["Runway Identifier",       r[13:18],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Runway Length",           r[22:27],   decode.text])
        fields.append(["Runway Magnetic Bearing", r[27:31],   decode.text])
        fields.append(["Runway Latitude",         r[32:41],   decode.gps])
        fields.append(["Runway Longitude",        r[41:51],   decode.gps])
        fields.append(["Runway Gradient",         r[51:56],   decode.text])
        fields.append(["Landing Threshold Elevation",
                      r[66:71], decode.text])
        fields.append(["Displaced Threshold Dist",
                      r[71:75], decode.text])
        fields.append(["Threshold Crossing Height",
                      r[75:77], decode.text])
        fields.append(["Runway Width",            r[77:80],   decode.text])
        fields.append(["TCH Value Indicator",     r[80],      decode.text])
        fields.append(["Localizer/MLS/GLS Ref Path Ident",
                      r[81:85], decode.text])
        fields.append(["Localizer/MLS/GLS Category/Class",
                      r[85], decode.text])
        fields.append(["Stopway",                 r[86:90],   decode.text])
        fields.append(["Localizer/MLS/GLS Ref Path Ident (2)", 
                      r[90:94], decode.text])
        fields.append(["Localizer/MLS/GLS Category/Class (2)", 
                      r[94], decode.text])
        fields.append(["Runway Description",      r[101:123], decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["Runway Identifier",       r[13:18],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Notes",                   r[23:92],   decode.notes])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_sim(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4]+r[12], decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["Runway Identifier",       r[13:18],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["Runway True Bearing",     r[51:56],   decode.text])
        fields.append(["True Bearing Source",     r[56],      decode.text])
        fields.append(["TDZE Location",           r[65],      decode.text])
        fields.append(["Touchdown Zone Elevation",
                      r[66:71], decode.text])
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
                case 'S':
                    return self.read_sim(line)
                case _:
                    #TODO raise ValueError('Unknown Application Type')
                    return
