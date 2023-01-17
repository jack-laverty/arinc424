import arinc424.decoder as decode


class NDBNavaid():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4:6],     decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["NDB Identifier",          r[13:17],   decode.text])
        fields.append(["ICAO Code",               r[19:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["NDB Frequency",           r[22:27],   decode.freq])
        fields.append(["NDB Class Facility",      r[27:29],   decode.facility])
        fields.append(["NDB Class Power",         r[29],      decode.power])
        fields.append(["NDB Class Info",          r[30],      decode.info])
        fields.append(["NDB Class Collocation",   r[31],      decode.colloc])
        fields.append(["NDB Latitude",            r[32:41],   decode.gps])
        fields.append(["NDB Longitude",           r[41:51],   decode.gps])
        fields.append(["Magnetic Variation",      r[74:79],   decode.text])
        fields.append(["Datum Code",              r[90:93],   decode.text])
        fields.append(["NDB Name",                r[93:123],  decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",             r[0],       decode.record])
        fields.append(["Customer / Area Code",    r[1:4],     decode.text])
        fields.append(["Section Code",            r[4:6],     decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],    decode.text])
        fields.append(["ICAO Code",               r[10:12],   decode.text])
        fields.append(["NDB Identifier",          r[13:17],   decode.text])
        fields.append(["ICAO Code",               r[19:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["Application Type",        r[22],      decode.app])
        fields.append(["Notes",                   r[23:92],   decode.text])
        fields.append(["Reserved (Expansion)",    r[92:123],  decode.text])
        fields.append(["File Record No",          r[123:128], decode.text])
        fields.append(["Cycle Date",              r[128:132], decode.cycle])
        return fields

    def read_sim(self, r):
        fields = []
        fields.append(["Record Type",             r[0],        decode.record])
        fields.append(["Customer / Area Code",    r[1:4],      decode.text])
        fields.append(["Section Code",            r[4:6],      decode.section])
        fields.append(["Airport ICAO Identifier", r[6:10],     decode.text])
        fields.append(["ICAO Code",               r[10:12],    decode.text])
        fields.append(["NDB Identifier",          r[13:17],    decode.text])
        fields.append(["ICAO Code",               r[19:21],    decode.text])
        fields.append(["Continuation Records No",  r[21],      decode.cont])
        fields.append(["Application Type",         r[22],      decode.app])
        fields.append(["Facility Characteristics", r[27:32],   decode.text])
        fields.append(["Facility elevation",       r[79:84],   decode.text])
        fields.append(["File Record No",           r[123:128], decode.text])
        fields.append(["Cycle Date",               r[128:132], decode.cycle])
        return fields

    # This Continuation Record is used to indicate the FIR and
    # UIR within which the NDB NAVAID defined in the
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
        fields.append(["NDB Identifier",          r[13:17],   decode.text])
        fields.append(["ICAO Code",               r[19:21],   decode.text])
        fields.append(["Continuation Records No", r[21],      decode.cont])
        fields.append(["NDB Frequency",           r[22:27],   decode.freq])
        fields.append(["NDB Class Facility",      r[27:29],   decode.facility])
        fields.append(["NDB Class Power",         r[29],      decode.power])
        fields.append(["NDB Class Info",          r[30],      decode.info])
        fields.append(["NDB Class Collocation",   r[31],      decode.colloc])
        fields.append(["NDB Latitude",            r[32:41],   decode.gps])
        fields.append(["NDB Longitude",           r[41:51],   decode.gps])
        fields.append(["Magnetic Variation",      r[74:79],   decode.text])
        fields.append(["Datum Code",              r[90:93],   decode.text])
        fields.append(["NDB Name",                r[93:123],  decode.text])
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
                case 'P':
                    return self.read_flight_plan0(line)
                case 'S':
                    return self.read_sim(line)
                case _:
                    #TODO raise ValueError('Unknown Application Type')
                    return
