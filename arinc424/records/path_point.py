
class PathPoint():

    def read(self, r):
        if int(r[26]) < 2:
            # primary record
            return {
                "Record Type":                             r[0],
                "Customer / Area Code":                    r[1:4],
                "Section Code":                            r[4]+r[12],
                "Airport Identifier":                      r[6:10],
                "ICAO Code":                               r[10:12],
                "Approach Procedure Ident":                r[13:19],
                "Runway or Helipad Ident":                 r[19:24],
                "Operation Type":                          r[24:26],
                "Continuation Record No":                  r[26],
                "Route Identifier":                        r[27],
                "SBAS Service Provider Ident":             r[28:30],
                "Reference Path Data Selector":            r[30:32],
                "Reference Path Identifier":               r[32:36],
                "Approach Performance Designator":         r[36],
                "Landing Threshold Point Latitude":        r[37:48],
                "Landing Threshold Point Longitude":       r[48:60],
                "(LTP) Ellipsoid Height":                  r[60:66],
                "Glide Path Angle":                        r[66:70],
                "Flight Path Alignment Point Latitude":    r[70:81],
                "Flight Path Alignment Point Longitude":   r[81:93],
                "Course Width at Threshold Note 4":        r[93:98],
                "Length Offset":                           r[98:102],
                "Path Point TCH":                          r[102:108],
                "TCH Units Indicator":                     r[108],
                "HAL":                                     r[109:112],
                "VAL":                                     r[112:115],
                "SBAS FAS Data CRC Remainder":             r[115:123],
                "File Record No":                          r[123:128],
                "Cycle Date":                              r[128:132]
            }
        else:
            # continuation record
            match r[27]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return
                case 'B':
                    # combined controlling agency/call sign and formatted
                    # time of operation
                    return
                case 'C':
                    # call sign/controlling agency continuation
                    return
                case 'E':
                    # primary record extension
                    return {
                        "Record Type":                      r[0],
                        "Customer / Area Code":             r[1:4],
                        "Section Code":                     r[4]+r[12],
                        "Airport Identifier":               r[6:10],
                        "ICAO Code":                        r[10:12],
                        "Approach Procedure Ident":         r[13:19],
                        "Runway or Helipad Ident":          r[19:24],
                        "Operation Type":                   r[24:26],
                        "Continuation Record No":           r[26],
                        "Application Type":                 r[27],
                        "(FPAP) Ellipsoid Height":          r[28:34],
                        "(FPAP) Orthometric Height":        r[34:40],
                        "(LTP) Orthometric Height":         r[40:46],
                        "Approach Type Identifier":         r[46:56],
                        "GNSS Channel Number":              r[56:61],
                        "Helicopter Procedure Course":      r[71:123],
                        "File Record No":                   r[123:128],
                        "Cycle Date":                       r[128:132]
                    }
                case 'L':
                    # VHF Navaid Limitation Continuation
                    return
                case 'N':
                    # A sector narrative continuation
                    return
                case 'T':
                    # a time of operations continuation
                    # 'formatted time data'
                    return
                case 'U':
                    # a time of operations continuation
                    # 'narrative time data'
                    return
                case 'V':
                    # a time of operations continuation
                    # start/end date
                    return
                case 'P':
                    # a flight planning application continuation
                    return
                case 'Q':
                    # NOTE: ARINC spec appears to give conflicting info here:

                    # 4.1.9.4 - "Flight Planning continuation records are
                    # designed to carry off-cycle updates to the
                    # primary record, and cannot carry an Application
                    # Type column."

                    # 5.91 - Continuation Record Application Type
                    # 'Q' = Flight Planning Application Primary
                    # Data Continuation

                    # which is it? do they not carry an application type
                    # column, or do they carry an application type column
                    # set to 'Q'?
                    return
                case 'S':
                    # simulation application continuation
                    return
                case 'W':
                    # an airport or heliport procedure data continuation
                    # with SBAS use authorization information
                    return
                case _:
                    # a flight planning application primary data continuation
                    # see notes above for case 'Q'
                    # TODO make this less sketchy
                    return
