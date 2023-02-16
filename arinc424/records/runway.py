
class Runway():

    def read(self, r):
        if int(r[21]) < 2:
            # primary record
            return [
                ("Record Type",                         r[0]),
                ("Customer / Area Code",                r[1:4]),
                ("Section Code",                        r[4]+r[12]),
                ("Airport ICAO Identifier",             r[6:10]),
                ("ICAO Code",                           r[10:12]),
                ("Runway Identifier",                   r[13:18]),
                ("Continuation Record No",              r[21]),
                ("Runway Length",                       r[22:27]),
                ("Runway Magnetic Bearing",             r[27:31]),
                ("Runway Latitude",                     r[32:41]),
                ("Runway Longitude",                    r[41:51]),
                ("Runway Gradient",                     r[51:56]),
                ("Landing Threshold Elevation",         r[66:71]),
                ("Displaced Threshold Dist",            r[71:75]),
                ("Threshold Crossing Height",           r[75:77]),
                ("Runway Width",                        r[77:80]),
                ("TCH Value Indicator",                 r[80]),
                ("Localizer/MLS/GLS Ref Path Ident",    r[81:85]),
                ("Localizer/MLS/GLS Category/Class",    r[85]),
                ("Stopway",                             r[86:90]),
                ("Localizer/MLS/GLS Ref Path Ident (2)", r[90:94]),
                ("Localizer/MLS/GLS Category/Class (2)", r[94]),
                ("Runway Description",                  r[101:123]),
                ("File Record No",                      r[123:128]),
                ("Cycle Date",                          r[128:132])
            ]
        else:
            # continuation record
            match r[22]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4]+r[12]),
                        ("Airport ICAO Identifier",             r[6:10]),
                        ("ICAO Code",                           r[10:12]),
                        ("Runway Identifier",                   r[13:18]),
                        ("Continuation Record No",              r[21]),
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
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4]+r[12]),
                        ("Airport ICAO Identifier",             r[6:10]),
                        ("ICAO Code",                           r[10:12]),
                        ("Runway Identifier",                   r[13:18]),
                        ("Continuation Record No",              r[21]),
                        ("Application Type",                    r[22]),
                        ("Runway True Bearing",                 r[51:56]),
                        ("True Bearing Source",                 r[56]),
                        ("TDZE Location",                       r[65]),
                        ("Touchdown Zone Elevation",            r[66:71]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132]),
                    ]
                case 'W':
                    # an airport or heliport procedure data continuation
                    # with SBAS use authorization information
                    return
                case _:
                    # a flight planning application primary data continuation
                    # see notes above for case 'Q'
                    # TODO make this less sketchy
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
                        ("Continuation Record No",              r[38]),
                        ("Application Type",                    r[39]),
                        ("Start/End Indicator",                 r[40]),
                        ("Start/End Date",                      r[41:45]),
                        ("Leg Distance",                        r[74:78]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
