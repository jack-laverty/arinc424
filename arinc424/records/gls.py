
class GLS():

    def read(self, r):
        if int(r[38]) < 2:
            # primary record
            return [
                ("Record Type",                         r[0]),
                ("Customer / Area Code",                r[1:4]),
                ("Section Code",                        r[4]+r[12]),
                ("Airport and Heliport Identifier",     r[6:10]),
                ("ICAO Code",                           r[10:12]),
                ("GLS Ref Path Identifier",             r[13:17]),
                ("GLS Category",                        r[17]),
                ("Continuation Record No",              r[18:21]),
                ("GLS Channel",                         r[22:27]),
                ("Runway Identifier",                   r[27:32]),
                ("GLS Approach Bearing",                r[51:55]),
                ("Station Latitude",                    r[55:64]),
                ("Station Longitude",                   r[64:74]),
                ("GLS Station Ident",                   r[74:78]),
                ("Service Volume Radius",               r[83:85]),
                ("TDMA Slots",                          r[85:87]),
                ("GLS Approach Slope",                  r[87:90]),
                ("Magnetic Variation",                  r[90:95]),
                ("Station Elevation",                   r[97:102]),
                ("Datum Code",                          r[102:105]),
                ("Station Type",                        r[105:108]),
                ("Station Elevation WGS",               r[110:115]),
                ("File Record No",                      r[123:128]),
                ("Cycle Date",                          r[128:132])
            ]
        else:
            # continuation record
            match r[39]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4]+r[12]),
                        ("Airport and Heliport Identifier",     r[6:10]),
                        ("ICAO Code",                           r[10:12]),
                        ("GLS Ref Path Identifier",             r[13:17]),
                        ("GLS Category",                        r[17]),
                        ("Continuation Record No",              r[18:21]),
                        ("Application Type",                    r[22]),
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
