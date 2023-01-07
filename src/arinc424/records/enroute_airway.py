import arinc424.decoder as decode


class Airway():

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",            r[0],       decode.record])
        fields.append(["Customer / Area Code",   r[1:4],     decode.text])
        fields.append(["Section Code",           r[4:6],     decode.section])
        fields.append(["Route Identifier",       r[13:18],   decode.text])
        fields.append(["Sequence Number",        r[25:29],   decode.text])
        fields.append(["Fix Identifier",         r[29:34],   decode.text])
        fields.append(["ICAO Code",              r[34:36],   decode.text])
        fields.append(["Section Code",           r[36:38],   decode.section])
        fields.append(["Continuation Record No", r[38],      decode.cont])
        fields.append(["Waypoint Desc Code",     r[39:43],   decode.text])
        fields.append(["Boundary Code",          r[43],      decode.text])
        fields.append(["Route Type",             r[26:29],   decode.waypoint])
        fields.append(["Level",                  r[29:31],   decode.text])
        fields.append(["Direction Restriction",  r[32:41],   decode.gps])
        fields.append(["Cruise Table Indicator", r[41:51],   decode.gps])
        fields.append(["EU Indicator",           r[74:79],   decode.text])
        fields.append(["Recommended NAVAID",     r[84:87],   decode.text])
        fields.append(["ICAO Code",              r[95:98],   decode.nfi])
        fields.append(["RNP",                    r[98:123],  decode.text])
        fields.append(["Theta",                  r[98:123],  decode.text])
        fields.append(["Rho",                    r[98:123],  decode.text])
        fields.append(["Outbound Magnetic Course",
                      r[98:123],
                      decode.text])
        fields.append(["Route Distance From",    r[98:123],  decode.text])
        fields.append(["Inbound Magnetic Course",
                      r[98:123],
                      decode.text])
        fields.append(["Minimum Altitude",       r[98:123],  decode.text])
        fields.append(["Minimum Altitude",       r[98:123],  decode.text])
        fields.append(["Maximum Altitude",       r[98:123],  decode.text])
        fields.append(["Fix Radius Transition Indicator",
                      r[98:123],
                      decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",            r[0],       decode.record])
        fields.append(["Customer / Area Code",   r[1:4],     decode.text])
        fields.append(["Section Code",           r[4:6],     decode.section])
        fields.append(["Route Identifier",       r[13:18],   decode.text])
        fields.append(["Sequence Number",        r[25:29],   decode.text])
        fields.append(["Fix Identifier",         r[29:34],   decode.text])
        fields.append(["ICAO Code",              r[34:36],   decode.text])
        fields.append(["Section Code",           r[36:38],   decode.section])
        fields.append(["Continuation Record No", r[38],      decode.cont])
        fields.append(["Notes",                  r[40:109],  decode.text])
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
        fields.append(["Route Identifier",       r[13:18],   decode.text])
        fields.append(["Sequence Number",        r[25:29],   decode.text])
        fields.append(["Fix Identifier",         r[29:34],   decode.text])
        fields.append(["ICAO Code",              r[34:36],   decode.text])
        fields.append(["Section Code",           r[36:38],   decode.section])
        fields.append(["Application Type",       r[39],      decode.app])
        fields.append(["Start/End Indicator",    r[40],      decode.text])
        fields.append(["Start/End Date",         r[41:52],   decode.text])
        fields.append(["Restr. Air ICAO Code",   r[66:68],   decode.text])
        fields.append(["Restr. Air Type",        r[68],      decode.text])
        fields.append(["Restr. Air Designation", r[69:79],   decode.text])
        fields.append(["Restr. Air Multiple Code",
                      r[79],
                      decode.text])
        fields.append(["Restr. Air ICAO Code",   r[80:82],   decode.text])
        fields.append(["Restr. Air Type",        r[82],      decode.text])
        fields.append(["Restr. Air Designation", r[83:93],   decode.text])
        fields.append(["Restr. Air Multiple Code",
                      r[93],
                      decode.app])
        fields.append(["Restr. Air ICAO Code",   r[94:96],   decode.text])
        fields.append(["Restr. Air Type",        r[96],      decode.text])
        fields.append(["Restr. Air Designation", r[97:107],  decode.text])
        fields.append(["Restr. Air Multiple Code",
                      r[107],
                      decode.app])
        fields.append(["Restr. Air ICAO Code",   r[108:110], decode.text])
        fields.append(["Restr. Air Type",        r[110],     decode.text])
        fields.append(["Restr. Air Designation", r[111:121], decode.text])
        fields.append(["Restr. Air Multiple Code",
                      r[121],
                      decode.app])
        fields.append(["Restr. Air Link Continuation",
                      r[122],
                      decode.app])
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
        fields.append(["Route Identifier",       r[13:18],   decode.text])
        fields.append(["Sequence Number",        r[25:29],   decode.text])
        fields.append(["Fix Identifier",         r[29:34],   decode.text])
        fields.append(["ICAO Code",              r[34:36],   decode.text])
        fields.append(["Section Code",           r[36:38],   decode.section])
        fields.append(["Continuation Record No", r[38],      decode.cont])
        fields.append(["Waypoint Desc Code",     r[39:43],   decode.text])
        fields.append(["Boundary Code",          r[43],      decode.text])
        fields.append(["Route Type",             r[26:29],   decode.waypoint])
        fields.append(["Level",                  r[29:31],   decode.text])
        fields.append(["Direction Restriction",  r[32:41],   decode.gps])
        fields.append(["Cruise Table Indicator", r[41:51],   decode.gps])
        fields.append(["EU Indicator",           r[74:79],   decode.text])
        fields.append(["Recommended NAVAID",     r[84:87],   decode.text])
        fields.append(["ICAO Code",              r[95:98],   decode.nfi])
        fields.append(["RNP",                    r[98:123],  decode.text])
        fields.append(["Theta",                  r[98:123],  decode.text])
        fields.append(["Rho",                    r[98:123],  decode.text])
        fields.append(["Outbound Magnetic Course",
                      r[98:123],
                      decode.text])
        fields.append(["Route Distance From",    r[98:123],  decode.text])
        fields.append(["Inbound Magnetic Course",
                      r[98:123],
                      decode.text])
        fields.append(["Minimum Altitude",       r[98:123],  decode.text])
        fields.append(["Minimum Altitude",       r[98:123],  decode.text])
        fields.append(["Maximum Altitude",       r[98:123],  decode.text])
        fields.append(["Fix Radius Transition Indicator",
                      r[98:123],
                      decode.text])
        fields.append(["File Record No",         r[123:128], decode.text])
        fields.append(["Cycle Date",             r[128:132], decode.cycle])
        return fields

    def read(self, line):
        if int(line[38]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[39]:
                case 'A':
                    return self.read_cont(line)
                case 'P':
                    return self.read_flight_plan0(line)
                case _:
                    return self.read_flight_plan1(line)  # filthy
