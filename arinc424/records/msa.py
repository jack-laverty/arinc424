
class MSA():

    cont_idx = 38
    app_idx = 39

    def __init__(self, heliport) -> None:
        self.heliport = heliport

    def read(self, r):
        if int(r[self.cont_idx]) < 2:
            # primary record
            return {
                "Record Type":                         r[0],
                "Customer / Area Code":                r[1:4],
                "Section Code":                        r[4]+r[12],
                "Airport Identifier" if self.heliport is False
                else "Heliport Identifier":
                r[6:10],
                "ICAO Code":                           r[10:12],
                "MSA Center":                          r[13:17],
                "ICAO Code (2)":                       r[18:20],
                "Section Code (2)":                    r[20:22],
                "Multiple Code":                       r[22],
                "Continuation Record No":              r[39],
                "Sector Bearing":                      r[42:48],
                "Sector Altitude":                     r[48:51],
                "Sector Radius":                       r[51:53],
                "Sector Bearing (2)":                  r[53:59],
                "Sector Altitude (2)":                 r[59:62],
                "Sector Radius (2)":                   r[62:64],
                "Sector Bearing (3)":                  r[64:70],
                "Sector Altitude (3)":                 r[70:73],
                "Sector Radius (3)":                   r[73:75],
                "Sector Bearing (4)":                  r[75:81],
                "Sector Altitude (4)":                 r[81:84],
                "Sector Radius (4)":                   r[84:86],
                "Sector Bearing (5)":                  r[86:92],
                "Sector Altitude (5)":                 r[92:95],
                "Sector Radius (5)":                   r[95:97],
                "Sector Bearing (6)":                  r[97:103],
                "Sector Altitude (6)":                 r[103:106],
                "Sector Radius (6)":                   r[106:108],
                "Sector Bearing (7)":                  r[108:114],
                "Sector Altitude (7)":                 r[114:117],
                "Sector Radius (7)":                   r[117:119],
                "Magnetic/True Bearing":               r[119],
                "File Record No":                      r[123:128],
                "Cycle Date":                          r[128:132]
            }
        else:
            # continuation record
            match r[self.app_idx]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return {
                        "Record Type":                         r[0],
                        "Customer / Area Code":                r[1:4],
                        "Section Code":                        r[4]+r[12],
                        "Airport Identifier" if self.heliport is False
                        else "Heliport Identifier":
                        r[6:10],
                        "ICAO Code (2)":                       r[10:12],
                        "MSA Center":                          r[13:17],
                        "ICAO Code (3)":                       r[18:20],
                        "Section Code (2)":                    r[20:22],
                        "Multiple Code":                       r[22],
                        "Continuation Record No":              r[39],
                        "Notes":                               r[40:109],
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
