
class HeliportTerminalWaypoint():

    cont_idx = 21
    app_idx = 22

    def read(self, r):
        if int(r[self.cont_idx]) < 2:
            # primary record
            return [
                ("Record Type",                         r[0]),
                ("Customer / Area Code",                r[1:4]),
                ("Section Code",                        r[4]+r[12]),
                ("Heliport Identifier",                 r[6:10]),
                ("ICAO Code",                           r[10:12]),
                ("Waypoint Identifier",                 r[13:18]),
                ("ICAO Code",                           r[19:21]),
                ("Continuation Record No",              r[21]),
                ("Waypoint Type",                       r[26:29]),
                ("Waypoint Usage",                      r[29:31]),
                ("Waypoint Latitude",                   r[32:41]),
                ("Waypoint Longitude",                  r[41:51]),
                ("Dynamic Magnetic Variation",          r[74:79]),
                ("Datum Code",                          r[84:87]),
                ("Name Format Indicator",               r[95:98]),
                ("Waypoint Name/Description",           r[98:123]),
                ("File Record No",                      r[123:128]),
                ("Cycle Date",                          r[128:132])
            ]
        else:
            # continuation record
            match r[self.app_idx]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4]+r[12]),
                        ("Heliport Identifier",                 r[6:10]),
                        ("ICAO Code",                           r[10:12]),
                        ("Waypoint Identifier",                 r[13:18]),
                        ("ICAO Code",                           r[19:21]),
                        ("Continuation Record No",              r[21]),
                        ("Application Type",                    r[22]),
                        ("Notes",                               r[23:92]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
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
