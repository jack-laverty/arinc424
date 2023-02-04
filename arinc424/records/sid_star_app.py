
class SIDSTARApp():

    def read(self, r):
        if int(r[38]) < 2:
            # primary record
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
        else:
            # continuation record
            match r[39]:
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
                        ("Application Type",                    r[39]),
                        ("CAT A Decision Height",               r[40:44]),
                        ("CAT B Decision Height",               r[44:48]),
                        ("CAT C Decision Height",               r[48:52]),
                        ("CAT D Decision Height",               r[52:56]),
                        ("CAT A Minimum Descent Altitude",      r[56:60]),
                        ("CAT B Minimum Descent Altitude",      r[60:64]),
                        ("CAT C Minimum Descent Altitude",      r[64:68]),
                        ("CAT D Minimum Descent Altitude",      r[68:72]),
                        ("Procedure TCH",                       r[72:75]),
                        ("Localizer Only Altitude Desc",        r[75]),
                        ("Localizer Only Altitude",             r[76:81]),
                        ("Localizer Only Vertical Angle",       r[81:85]),
                        ("RNP",                                 r[89:92]),
                        ("Apch Route Qualifier 1",              r[118]),
                        ("Apch Route Qualifier 2",              r[119]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
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
                        ("Application Type",                    r[39]),
                        ("Start/End Indicator",                 r[40]),
                        ("Start/End Date",                      r[41:45]),
                        ("Leg Distance",                        r[74:78]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
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
                        ("Application Type",                    r[39]),
                        ("FAS Block Provided",                  r[40]),
                        ("FAS Block Provided Level of Service Name",
                         r[41:51]),
                        ("LNAV/VNAV Authorized for SBAS",       r[51]),
                        ("LNAV/VNAV Level of Service Name",     r[52:62]),
                        ("LNAV Authorized for SBAS",            r[62]),
                        ("LNAV Level of Service Name",          r[63:73]),
                        ("Apch Route Qualifier 1",              r[118]),
                        ("Apch Route Qualifier 2",              r[119]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
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
                        ("Continuation Record Number",          r[38]),
                        ("Application Type",                    r[39]),
                        ("Start/End Indicator",                 r[40]),
                        ("Start/End Date",                      r[41:45]),
                        ("Leg Distance",                        r[74:78]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
