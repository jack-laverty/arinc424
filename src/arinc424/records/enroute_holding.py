import arinc424.decoder as decode


class Holding():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",            r[0],       decode.record])
        fields.append(["Customer / Area Code",   r[1:4],     decode.text])
        fields.append(["Section Code",           r[4:6],     decode.section])
        fields.append(["Region Code",            r[6:10],    decode.text])
        fields.append(["ICAO Code",              r[10:12],   decode.text])
        fields.append(["Duplicate Identifier",   r[27:29],   decode.text])
        fields.append(["Fix Identifier",         r[29:34],   decode.text])
        fields.append(["ICAO Code",              r[34:36],   decode.text])
        fields.append(["Section Code",           r[36:38],   decode.section])
        fields.append(["Continuation Record No", r[38],      decode.cont])
        fields.append(["Inbound Holding Course", r[39:43],   decode.text])
        fields.append(["Turn Direction",         r[43],      decode.text])
        fields.append(["Leg Length",             r[44:47],   decode.text])
        fields.append(["Leg Time",               r[47:49],   decode.text])
        fields.append(["Minimum Altitude",       r[49:54],   decode.text])
        fields.append(["Maximum Altitude",       r[54:59],   decode.text])
        fields.append(["Holding Speed",          r[59:62],   decode.text])
        fields.append(["RNP",                    r[62:65],   decode.text])
        fields.append(["Arc Radius",             r[65:71],   decode.text])
        fields.append(["Name",                   r[98:123],  decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",            r[0],       decode.record])
        fields.append(["Customer / Area Code",   r[1:4],     decode.text])
        fields.append(["Section Code",           r[4:6],     decode.section])
        fields.append(["Region Code",            r[6:10],    decode.text])
        fields.append(["ICAO Code",              r[10:12],   decode.text])
        fields.append(["Duplicate Identifier",   r[27:29],   decode.text])
        fields.append(["Fix Identifier",         r[29:34],   decode.text])
        fields.append(["ICAO Code",              r[34:36],   decode.text])
        fields.append(["Section Code",           r[36:38],   decode.section])
        fields.append(["Continuation Record No", r[38],      decode.cont])
        fields.append(["Application Type",       r[40],      decode.app])
        fields.append(["Notes",                  r[40:109],  decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    def read(self, line):
        return self.read_primary(line)
        # if int(line[38]) < 2:
        #     # continuation record # 0 = primary record with no continuation
        #     # continuation record # 1 = primary record with continuation
        #     return self.read_primary(line)
        # else:
        #     match line[40]:
        #         case 'A':
        #             return self.read_cont(line)
        #         case _:
        #             print("Unsupported Application Type")
        #             return []
