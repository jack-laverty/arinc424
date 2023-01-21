
class Airway():

    def read_primary(self, r):
        return [
            ("Record Type",                             r[0]),
            ("Customer / Area Code",                    r[1:4]),
            ("Section Code",                            r[4:6]),
            ("Route Identifier",                        r[13:18]),
            ("Sequence Number",                         r[25:29]),
            ("Fix Identifier",                          r[29:34]),
            ("ICAO Code",                               r[34:36]),
            ("Section Code",                            r[36:38]),
            ("Continuation Record No",                  r[38]),
            ("Waypoint Desc Code",                      r[39:43]),
            ("Boundary Code",                           r[43]),
            ("Route Type",                              r[26:29]),
            ("Level",                                   r[29:31]),
            ("Direction Restriction",                   r[32:41]),
            ("Cruise Table Indicator",                  r[41:51]),
            ("EU Indicator",                            r[74:79]),
            ("Recommended NAVAID",                      r[84:87]),
            ("ICAO Code",                               r[95:98]),
            ("RNP",                                     r[98:123]),
            ("Theta",                                   r[98:123]),
            ("Rho",                                     r[98:123]),
            ("Outbound Magnetic Course",                r[98:123]),
            ("Route Distance From",                     r[98:123]),
            ("Inbound Magnetic Course",                 r[98:123]),
            ("Minimum Altitude",                        r[98:123]),
            ("Minimum Altitude",                        r[98:123]),
            ("Maximum Altitude",                        r[98:123]),
            ("Fix Radius Transition Indicator",         r[98:123]),
            ("File Record No",                          r[123:128]),
            ("Cycle Date",                              r[128:132])
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                             r[0]),
            ("Customer / Area Code",                    r[1:4]),
            ("Section Code",                            r[4:6]),
            ("Route Identifier",                        r[13:18]),
            ("Sequence Number",                         r[25:29]),
            ("Fix Identifier",                          r[29:34]),
            ("ICAO Code",                               r[34:36]),
            ("Section Code",                            r[36:38]),
            ("Continuation Record No",                  r[38]),
            ("Notes",                                   r[40:109]),
            ("File Record No",                          r[123:128]),
            ("Cycle Date",                              r[128:132])
        ]

    def read_flight_plan0(self, r):
        return [
            ("Record Type",                             r[0]),
            ("Customer / Area Code",                    r[1:4]),
            ("Section Code",                            r[4:6]),
            ("Route Identifier",                        r[13:18]),
            ("Sequence Number",                         r[25:29]),
            ("Fix Identifier",                          r[29:34]),
            ("ICAO Code",                               r[34:36]),
            ("Section Code",                            r[36:38]),
            ("Application Type",                        r[39]),
            ("Start/End Indicator",                     r[40]),
            ("Start/End Date",                          r[41:52]),
            ("Restr. Air ICAO Code",                    r[66:68]),
            ("Restr. Air Type",                         r[68]),
            ("Restr. Air Designation",                  r[69:79]),
            ("Restr. Air Multiple Code",                r[79]),
            ("Restr. Air ICAO Code",                    r[80:82]),
            ("Restr. Air Type",                         r[82]),
            ("Restr. Air Designation",                  r[83:93]),
            ("Restr. Air Multiple Code",                r[93]),
            ("Restr. Air ICAO Code",                    r[94:96]),
            ("Restr. Air Type",                         r[96]),
            ("Restr. Air Designation",                  r[97:107]),
            ("Restr. Air Multiple Code",                r[107]),
            ("Restr. Air ICAO Code",                    r[108:110]),
            ("Restr. Air Type",                         r[110]),
            ("Restr. Air Designation",                  r[111:121]),
            ("Restr. Air Multiple Code",                r[121]),
            ("Restr. Air Link Continuation",            r[122]),
            ("File Record No",                          r[123:128]),
            ("Cycle Date",                              r[128:132])
        ]

    def read_flight_plan1(self, r):
        return [
            ("Record Type",                             r[0]),
            ("Customer / Area Code",                    r[1:4]),
            ("Section Code",                            r[4:6]),
            ("Route Identifier",                        r[13:18]),
            ("Sequence Number",                         r[25:29]),
            ("Fix Identifier",                          r[29:34]),
            ("ICAO Code",                               r[34:36]),
            ("Section Code",                            r[36:38]),
            ("Continuation Record No",                  r[38]),
            ("Waypoint Desc Code",                      r[39:43]),
            ("Boundary Code",                           r[43]),
            ("Route Type",                              r[26:29]),
            ("Level",                                   r[29:31]),
            ("Direction Restriction",                   r[32:41]),
            ("Cruise Table Indicator",                  r[41:51]),
            ("EU Indicator",                            r[74:79]),
            ("Recommended NAVAID",                      r[84:87]),
            ("ICAO Code",                               r[95:98]),
            ("RNP",                                     r[98:123]),
            ("Theta",                                   r[98:123]),
            ("Rho",                                     r[98:123]),
            ("Outbound Magnetic Course",                r[98:123]),
            ("Route Distance From",                     r[98:123]),
            ("Inbound Magnetic Course",                 r[98:123]),
            ("Minimum Altitude",                        r[98:123]),
            ("Minimum Altitude",                        r[98:123]),
            ("Maximum Altitude",                        r[98:123]),
            ("Fix Radius Transition Indicator",         r[98:123]),
            ("File Record No",                          r[123:128]),
            ("Cycle Date",                              r[128:132])
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
