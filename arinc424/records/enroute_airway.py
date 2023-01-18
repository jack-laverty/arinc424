import arinc424.decoder as decode


class Airway():

    def read_primary(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4:6],     decode.section),
            ("Route Identifier",                r[13:18],   decode.text),
            ("Sequence Number",                 r[25:29],   decode.text),
            ("Fix Identifier",                  r[29:34],   decode.text),
            ("ICAO Code",                       r[34:36],   decode.text),
            ("Section Code",                    r[36:38],   decode.section),
            ("Continuation Record No",          r[38],      decode.cont),
            ("Waypoint Desc Code",              r[39:43],   decode.text),
            ("Boundary Code",                   r[43],      decode.text),
            ("Route Type",                      r[26:29],   decode.waypoint),
            ("Level",                           r[29:31],   decode.text),
            ("Direction Restriction",           r[32:41],   decode.text),
            ("Cruise Table Indicator",          r[41:51],   decode.text),
            ("EU Indicator",                    r[74:79],   decode.text),
            ("Recommended NAVAID",              r[84:87],   decode.text),
            ("ICAO Code",                       r[95:98],   decode.nfi),
            ("RNP",                             r[98:123],  decode.text),
            ("Theta",                           r[98:123],  decode.text),
            ("Rho",                             r[98:123],  decode.text),
            ("Outbound Magnetic Course",        r[98:123],  decode.text),
            ("Route Distance From",             r[98:123],  decode.text),
            ("Inbound Magnetic Course",         r[98:123],  decode.text),
            ("Minimum Altitude",                r[98:123],  decode.text),
            ("Minimum Altitude",                r[98:123],  decode.text),
            ("Maximum Altitude",                r[98:123],  decode.text),
            ("Fix Radius Transition Indicator", r[98:123],  decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4:6],     decode.section),
            ("Route Identifier",                r[13:18],   decode.text),
            ("Sequence Number",                 r[25:29],   decode.text),
            ("Fix Identifier",                  r[29:34],   decode.text),
            ("ICAO Code",                       r[34:36],   decode.text),
            ("Section Code",                    r[36:38],   decode.section),
            ("Continuation Record No",          r[38],      decode.cont),
            ("Notes",                           r[40:109],  decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read_flight_plan0(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4:6],     decode.section),
            ("Route Identifier",                r[13:18],   decode.text),
            ("Sequence Number",                 r[25:29],   decode.text),
            ("Fix Identifier",                  r[29:34],   decode.text),
            ("ICAO Code",                       r[34:36],   decode.text),
            ("Section Code",                    r[36:38],   decode.section),
            ("Application Type",                r[39],      decode.app),
            ("Start/End Indicator",             r[40],      decode.text),
            ("Start/End Date",                  r[41:52],   decode.text),
            ("Restr. Air ICAO Code",            r[66:68],   decode.text),
            ("Restr. Air Type",                 r[68],      decode.text),
            ("Restr. Air Designation",          r[69:79],   decode.text),
            ("Restr. Air Multiple Code",        r[79],      decode.text),
            ("Restr. Air ICAO Code",            r[80:82],   decode.text),
            ("Restr. Air Type",                 r[82],      decode.text),
            ("Restr. Air Designation",          r[83:93],   decode.text),
            ("Restr. Air Multiple Code",        r[93],      decode.app),
            ("Restr. Air ICAO Code",            r[94:96],   decode.text),
            ("Restr. Air Type",                 r[96],      decode.text),
            ("Restr. Air Designation",          r[97:107],  decode.text),
            ("Restr. Air Multiple Code",        r[107],     decode.app),
            ("Restr. Air ICAO Code",            r[108:110], decode.text),
            ("Restr. Air Type",                 r[110],     decode.text),
            ("Restr. Air Designation",          r[111:121], decode.text),
            ("Restr. Air Multiple Code",        r[121],     decode.app),
            ("Restr. Air Link Continuation",    r[122],     decode.app),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read_flight_plan1(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4:6],     decode.section),
            ("Route Identifier",                r[13:18],   decode.text),
            ("Sequence Number",                 r[25:29],   decode.text),
            ("Fix Identifier",                  r[29:34],   decode.text),
            ("ICAO Code",                       r[34:36],   decode.text),
            ("Section Code",                    r[36:38],   decode.section),
            ("Continuation Record No",          r[38],      decode.cont),
            ("Waypoint Desc Code",              r[39:43],   decode.text),
            ("Boundary Code",                   r[43],      decode.text),
            ("Route Type",                      r[26:29],   decode.waypoint),
            ("Level",                           r[29:31],   decode.text),
            ("Direction Restriction",           r[32:41],   decode.gps),
            ("Cruise Table Indicator",          r[41:51],   decode.gps),
            ("EU Indicator",                    r[74:79],   decode.text),
            ("Recommended NAVAID",              r[84:87],   decode.text),
            ("ICAO Code",                       r[95:98],   decode.nfi),
            ("RNP",                             r[98:123],  decode.text),
            ("Theta",                           r[98:123],  decode.text),
            ("Rho",                             r[98:123],  decode.text),
            ("Outbound Magnetic Course",        r[98:123],  decode.text),
            ("Route Distance From",             r[98:123],  decode.text),
            ("Inbound Magnetic Course",         r[98:123],  decode.text),
            ("Minimum Altitude",                r[98:123],  decode.text),
            ("Minimum Altitude",                r[98:123],  decode.text),
            ("Maximum Altitude",                r[98:123],  decode.text),
            ("Fix Radius Transition Indicator", r[98:123],  decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle)
        ]

    def read(self, line):
        if int(line[38]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[39]:
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
                    return self.read_flight_plan0(line)
                case 'Q':
                    return self.read_flight_plan1(line)
                case 'S':
                    return
                case _:
                    raise ValueError('Unknown Application Type')
