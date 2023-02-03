
class SIDSTARApp():

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport Identifier",                  r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("SID/STAR/Approach Identifier",        r[13:19]),
            ("Route Type",                          r[19]),
            ("Transition Identifier",               r[20:25]),
            ("Sequence Number",                     r[26:29]),
            ("Fix Identifier",                      r[29:34]),
            ("ICAO Code",                           r[34:36]),
            ("Section Code",                        r[36:38]),
            ("Continuation Record Number",          r[38]),
            ("Waypoint Description Code",           r[39:43]),
            ("Turn Direction",                      r[43]),
            ("RNP",                                 r[44:47]),
            ("Path and Termination",                r[47:49]),
            ("Turn Direction Valid",                r[49]),
            ("Recommended Navaid",                  r[50:54]),
            ("ICAO Code",                           r[54:56]),
            ("ARC Radius",                          r[56:62]),
            ("Theta",                               r[62:66]),
            ("Rho",                                 r[66:70]),
            ("Magnetic Course",                     r[70:74]),
            ("Route / Holding Distance or Time",    r[74:78]),
            ("RECD NAV Section",                    r[78:80]),
            ("Altitude Description",                r[82]),
            ("ATC Indicator",                       r[83]),
            ("Altitude",                            r[84:89]),
            ("Altitude",                            r[89:94]),
            ("Transition Altitude",                 r[94:99]),
            ("Speed Limit",                         r[99:102]),
            ("Vertical Angle",                      r[102:106]),
            ("Center Fix or TAA Procedure Turn Indicator", r[106:111]),
            ("Multiple Code or TAA Sector Identifier", r[111]),
            ("ICAO Code",                           r[112:113]),
            ("Section Code",                        r[114:116]),
            ("GNSS/FMS Indication",                 r[116]),
            ("Speed Limit Description",             r[117]),
            ("Apch Route Qualifier 1",              r[118]),
            ("Apch Route Qualifier 2",              r[119]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read(self, line):
        return self.read_primary(line)
