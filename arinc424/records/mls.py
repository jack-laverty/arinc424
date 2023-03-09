
class MLS():

    def read(self, r):
        if int(r[21]) < 2:
            # primary record
            return {
                "Record Type":                         r[0],
                "Customer / Area Code":                r[1:4],
                "Section Code":                        r[4]+r[12],
                "Airport Identifier":                  r[6:10],
                "ICAO Code":                           r[10:12],
                "MLS Identifier":                      r[13:17],
                "MLS Category":                        r[17],
                "Continuation Record No":              r[21],
                "Channel":                             r[22:25],
                "Runway Identifier":                   r[27:32],
                "Azimuth Latitude":                    r[32:41],
                "Azimuth Longitude":                   r[41:51],
                "Azimuth Bearing":                     r[51:55],
                "Elevation Latitude":                  r[55:64],
                "Elevation Longitude":                 r[64:74],
                "Azimuth Position":                    r[74:78],
                "Azimuth Position Reference":          r[78],
                "Elevation Position":                  r[79:83],
                "Azimuth Proportional Angle Right":    r[83:86],
                "Azimuth Proportional Angle Left":     r[86:89],
                "Azimuth Coverage Right":              r[89:92],
                "Azimuth Coverage Left":               r[92:95],
                "Elevation Angle Span":                r[95:98],
                "Magnetic Variation":                  r[98:103],
                "EL Elevation":                        r[103:108],
                "Nominal Elevation Angle":             r[108:112],
                "Minimum Glide Path Angle":            r[112:115],
                "Supporting Facility Identifier":      r[115:119],
                "Supporting Facility ICAO Code":       r[119:121],
                "Supporting Facility Section":         r[121:123],
                "File Record No":                      r[123:128],
                "Cycle Date":                          r[128:132]
            }
        else:
            # continuation record
            match r[22]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return {
                        "Record Type":                         r[0],
                        "Customer / Area Code":                r[1:4],
                        "Section Code":                        r[4]+r[12],
                        "Airport Identifier":                  r[6:10],
                        "ICAO Code":                           r[10:12],
                        "MLS Identifier":                      r[13:17],
                        "MLS Category":                        r[17],
                        "Continuation Record No":              r[21],
                        "Application Type":                    r[22],
                        "Facility Characteristics":            r[27:32],
                        "Back Azimuth Latitude":               r[32:41],
                        "Back Azimuth Longitude":              r[41:51],
                        "Back Azimuth Bearing":                r[51:55],
                        "MLS Datum Point Latitude":            r[55:64],
                        "MLS Datum Point Longitude":           r[64:74],
                        "Back Azimuth Position":               r[74:78],
                        "Back Azimuth Position Reference":     r[78],
                        "Back Azimuth Proportional Angle Right":
                        r[83:86],
                        "Back Azimuth Proportional Angle Left":
                        r[86:89],
                        "Back Azimuth Coverage Right":         r[89:92],
                        "Back Azimuth Coverage Left":          r[92:95],
                        "Back Azimuth True Bearing":           r[95:98],
                        "Back Azimuth Bearing Source":         r[100],
                        "Azimuth True Bearing":                r[101:106],
                        "Azimuth Bearing Source":              r[106],
                        "Glide Path Height at Landing Threshold":
                        r[107:109],
                        "File Record No":                      r[123:128],
                        "Cycle Date":                          r[128:132]
                    }
                case 'B':
                    # combined controlling agency/call sign and formatted
                    # time of operation
                    return
                case 'C':
                    # call sign/controlling agency continuation
                    return
                case 'E':
                    # primary record extension
                    return
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
