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
        fields.append(["Name Format Indicator",  r[95:98],   decode.nfi])
        fields.append(["Waypoint Name / Desc",   r[98:123],  decode.text])
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
        fields.append(["Subsection Code",        r[12],      decode.text])
        fields.append(["Waypoint Identifier",    r[13:18],   decode.text])
        fields.append(["ICAO Code",              r[19:21],   decode.text])
        fields.append(["Continuation Record No", r[21],      decode.cont])
        fields.append(["Application Type",       r[22],      decode.app])
        fields.append(["Notes",                  r[23:123],  decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    # This Continuation Record is used to indicate the FIR and
    # UIR within which the VHF NAVAID defined in the
    # Primary Record is located and the Start/End validity
    # dates/times of the Primary Record.
    def read_flight_plan0(self, r):
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
        fields.append(["Application Type",       r[22],      decode.app])
        fields.append(["FIR Identifier",         r[23:27],   decode.text])
        fields.append(["UIR Identifier",         r[27:31],   decode.text])
        fields.append(["Start/End Indicator",    r[31],      decode.text])
        fields.append(["Start/End Date",         r[32:43],   decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    # This Continuation Record is used to indicate the fields of
    # the Primary Record that are changed. Used in conjunction
    # with flight_plan0.
    def read_flight_plan1(self, r):
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
        fields.append(["Name Format Indicator",  r[95:98],   decode.nfi])
        fields.append(["Waypoint Name / Desc",   r[98:123],  decode.text])
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
                case 'P':
                    return self.read_flight_plan0(line)
                case 'S':
                    return self.read_sim(line)
                case _:
                    return self.read_flight_plan1(line)  # filthy
