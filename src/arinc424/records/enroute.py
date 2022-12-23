import arinc424.decoder as decode


class Waypoint():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",            r[0],       decode.record])
        fields.append(["Customer / Area Code",   r[1:4],     decode.text])
        fields.append(["Section Code",           r[4:6],     decode.section])
        fields.append(["Region Code",            r[6:10],    decode.text])
        fields.append(["ICAO Code",              r[10:12],   decode.text])
        fields.append(["Subsection Code",        r[12],      decode.text])
        fields.append(["Waypoint Identifier",    r[13:18],   decode.text])
        fields.append(["ICAO Code",              r[19:21],   decode.text])
        fields.append(["Continuation Record No", r[21],      decode.cont])
        fields.append(["Waypoint Type",          r[26:29],   decode.waypoint])
        fields.append(["Waypoint Usage",         r[29:31],   decode.text])
        fields.append(["Waypoint Latitude",      r[32:41],   decode.gps])
        fields.append(["Waypoint Longitude",     r[41:51],   decode.gps])
        fields.append(["Dynamic Mag. Variation", r[74:79],   decode.text])
        fields.append(["Datum Code",             r[84:87],   decode.text])
        fields.append(["Name Format Indicator",  r[95:98],   decode.text])
        fields.append(["Waypoint Name / Desc",   r[98:123],  decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4:6],     decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["VOR Identifier",          r[13:17],   decode.text])
        fields.append(["ICAO Code (2)",           r[19:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["Notes",                   r[23:92],   decode.text])
        fields.append(["Reserved (Expansion)",    r[92:123],  decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_sim(self, r):
        fields = []
        fields.append(["Record Type",              r[0],       decode.record])
        fields.append(["Customer / Area Code",     r[1:4],     decode.text])
        fields.append(["Section Code",             r[4:6],     decode.section])
        fields.append(["Airport ICAO Identifier",  r[6:10],    decode.text])
        fields.append(["ICAO Code",                r[10:12],   decode.text])
        fields.append(["VOR Identifier",           r[13:17],   decode.text])
        fields.append(["ICAO Code (2)",            r[19:21],   decode.text])
        fields.append(["Continuation Records No",  r[21],      decode.cont])
        fields.append(["Application Type",         r[22],      decode.app])
        fields.append(["Facility Characteristics", r[27:32],   decode.text])
        fields.append(["Reserved (Spacing)",       r[32:74],   decode.text])
        fields.append(["File Record No",           r[123:128], decode.text])
        fields.append(["Cycle Date",               r[128:132], decode.cycle])
        return fields

    # This Continuation Record is used to indicate the FIR and
    # UIR within which the VHF NAVAID defined in the
    # Primary Record is located and the Start/End validity
    # dates/times of the Primary Record.
    def read_flight_plan0(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4:6],     decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["VOR Identifier",          r[13:17],   decode.text])
        fields.append(["ICAO Code (2)",           r[19:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["FIR Identifier",          r[23:27],   decode.text])
        fields.append(["UIR Identifier",          r[28:31],   decode.text])
        fields.append(["Start/End Indicator",     r[32],      decode.text])
        fields.append(["Start/End Date",          r[32:43],   decode.text])
        fields.append(["Reserved (Expansion)",    r[43:123],  decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    # This Continuation Record is used to indicate the fields of
    # the Primary Record that are changed. Used in conjunction
    # with flight_plan0.
    def read_flight_plan1(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4:6],     decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["VOR Identifier",          r[13:17],   decode.text])
        fields.append(["ICAO Code (2)",           r[19:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["Frequency",               r[22:27],   decode.text])
        fields.append(["Class",                   r[27:32],   decode.text])
        fields.append(["VOR Latitude",            r[32:41],   decode.text])
        fields.append(["VOR Longitude",           r[41:51],   decode.text])
        fields.append(["DME Ident",               r[51:55],   decode.text])
        fields.append(["DME Latitude",            r[55:64],   decode.text])
        fields.append(["DME Longitude",           r[64:74],   decode.text])
        fields.append(["Station Declination",     r[74:79],   decode.text])
        fields.append(["DME Elevation",           r[79:84],   decode.text])
        fields.append(["Figure of Merit",         r[84],      decode.text])
        fields.append(["ILS/DME Bias",            r[85:87],   decode.text])
        fields.append(["Frequency Protection",    r[87:90],   decode.text])
        fields.append(["Datum Code",              r[90:93],   decode.text])
        fields.append(["VOR Name",                r[93:123],  decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_lim(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4:6],     decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["VOR Identifier",          r[13:17],   decode.text])
        fields.append(["ICAO Code (2)",           r[19:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["Navaid Limitation Code",  r[23],      decode.text])
        fields.append(["Component Affected Indicator", r[24], decode.text])
        fields.append(["Sequence Number",         r[25:27],   decode.text])
        fields.append(["Sector From/Sector To",   r[27:29],   decode.text])
        fields.append(["Distance Description",    r[29],      decode.text])
        fields.append(["Distance Limiation",      r[30:36],   decode.text])
        fields.append(["Altitude Description",    r[36],      decode.text])
        fields.append(["Altitude Limiation",      r[37:43],   decode.text])
        fields.append(["Sector From/Sector To",   r[43:45],   decode.text])
        fields.append(["Distance Description",    r[45],      decode.text])
        fields.append(["Distance Limiation",      r[46:52],   decode.text])
        fields.append(["Altitude Description",    r[52],      decode.text])
        fields.append(["Altitude Limiation",      r[53:59],   decode.text])
        fields.append(["Sector From/Sector To",   r[59:61],   decode.text])
        fields.append(["Distance Description",    r[61],      decode.text])
        fields.append(["Distance Limiation",      r[62:68],   decode.text])
        fields.append(["Altitude Description",    r[68],      decode.text])
        fields.append(["Altitude Limiation",      r[69:75],   decode.text])
        fields.append(["Sector From/Sector To",   r[75:77],   decode.text])
        fields.append(["Distance Description",    r[77],      decode.text])
        fields.append(["Distance Limiation",      r[79:84],   decode.text])
        fields.append(["Altitude Description",    r[84],      decode.text])
        fields.append(["Altitude Limiation",      r[85:91],   decode.text])
        fields.append(["Sector From/Sector To",   r[91:93],   decode.text])
        fields.append(["Distance Description",    r[93],      decode.text])
        fields.append(["Distance Limiation",      r[94:100],  decode.text])
        fields.append(["Altitude Description",    r[101],     decode.text])
        fields.append(["Altitude Limiation",      r[101:107], decode.text])
        fields.append(["Sequence End Indicator",  r[107],     decode.text])
        fields.append(["Blank (Spacing)",         r[108:123], decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read(self, line):
        if int(line[21]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        # else:
        #     match line[22]:
        #         case 'P':
        #             return self.read_flight_plan0(line)
        #         case 'S':
        #             return self.read_sim(line)
        #         case _:
        #             # print("ERROR: invalid application type", line[22])
        #             return []
