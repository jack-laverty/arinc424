import arinc424.decoder as decode


class Marker():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",            r[0],       decode.record])
        fields.append(["Customer / Area Code",   r[1:4],     decode.text])
        fields.append(["Section Code",           r[4:6],     decode.section])
        fields.append(["Marker Identifier",      r[13:17],   decode.text])
        fields.append(["ICAO Code",              r[19:21],   decode.text])
        fields.append(["Continuation Record No", r[21],      decode.cont])
        fields.append(["Marker Code",            r[22:26],   decode.text])
        fields.append(["Marker Shape",           r[27],      decode.mk_shape])
        fields.append(["Marker Power",           r[28],      decode.mk_power])
        fields.append(["Marker Latitude",        r[32:41],   decode.gps])
        fields.append(["Marker Longitude",       r[41:51],   decode.gps])
        fields.append(["Minor Axis",             r[51:55],   decode.text])
        fields.append(["Magnetic Variation",     r[74:79],   decode.text])
        fields.append(["Facility Elevation",     r[79:84],   decode.text])
        fields.append(["Datum Code",             r[84:87],   decode.text])
        fields.append(["Marker Name",            r[93:123],  decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",            r[0],       decode.record])
        fields.append(["Customer / Area Code",   r[1:4],     decode.text])
        fields.append(["Section Code",           r[4:6],     decode.section])
        fields.append(["ICAO Code",              r[10:12],   decode.text])
        fields.append(["Subsection Code",        r[12],      decode.text])
        fields.append(["ICAO Code",              r[19:21],   decode.text])
        fields.append(["Continuation Record No", r[21],      decode.cont])
        fields.append(["Application Type",       r[22],      decode.app])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
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
                case _:
                    print("Unsupported Application Type")
                    return []
