import arinc424.decoder as decode


class Marker():

    def read_primary(self, r):
        return [
            ("Record Type",            r[0],       decode.record),
            ("Customer / Area Code",   r[1:4],     decode.text),
            ("Section Code",           r[4:6],     decode.section),
            ("Marker Identifier",      r[13:17],   decode.text),
            ("ICAO Code",              r[19:21],   decode.text),
            ("Continuation Record No", r[21],      decode.cont),
            ("Marker Code",            r[22:26],   decode.text),
            ("Marker Shape",           r[27],      decode.mk_shape),
            ("Marker Power",           r[28],      decode.mk_power),
            ("Marker Latitude",        r[32:41],   decode.gps),
            ("Marker Longitude",       r[41:51],   decode.gps),
            ("Minor Axis",             r[51:55],   decode.text),
            ("Magnetic Variation",     r[74:79],   decode.text),
            ("Facility Elevation",     r[79:84],   decode.text),
            ("Datum Code",             r[84:87],   decode.text),
            ("Marker Name",            r[93:123],  decode.text),
            ("File Record No",         r[123:128], decode.text),
            ("Cycle Date",             r[128:132], decode.cycle)
        ]

    def read_cont(self, r):
        return [
            ("Record Type",            r[0],       decode.record),
            ("Customer / Area Code",   r[1:4],     decode.text),
            ("Section Code",           r[4:6],     decode.section),
            ("ICAO Code",              r[10:12],   decode.text),
            ("Subsection Code",        r[12],      decode.text),
            ("ICAO Code",              r[19:21],   decode.text),
            ("Continuation Record No", r[21],      decode.cont),
            ("Application Type",       r[22],      decode.app),
            ("File Record No",         r[123:128], decode.text),
            ("Cycle Date",             r[128:132], decode.cycle)
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
