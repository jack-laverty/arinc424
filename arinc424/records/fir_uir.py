
class FirUir():

    def read(self, r):
        if int(r[19]) < 2:
            # primary record
            return [
                ("Record Type",                         r[0]),
                ("Customer / Area Code",                r[1:4]),
                ("Section Code",                        r[4:6]),
                ("FIR/UIR Identifier",                  r[6:10]),
                ("FIR/UIR Address",                     r[10:14]),
                ("FIR/UIR Indicator",                   r[14]),
                ("Sequence Number",                     r[15:19]),
                ("Continuation Record No",              r[19]),
                ("Adjacent FIR Identifier",             r[20:24]),
                ("Adjacent UIR Identifier",             r[24:28]),
                ("Reporting Units Speed",               r[28]),
                ("Reporting Units Altitude",            r[29]),
                ("Entry Report",                        r[30]),
                ("Boundary Via",                        r[32:34]),
                ("FIR/UIR Latitude",                    r[34:43]),
                ("FIR/UIR Longitude",                   r[43:53]),
                ("Arc Origin Latitude",                 r[53:62]),
                ("Arc Origin Longitude",                r[62:72]),
                ("Arc Distance",                        r[72:76]),
                ("Arc Bearing",                         r[76:80]),
                ("FIR Upper Limit",                     r[80:85]),
                ("UIR Lower Limit",                     r[85:90]),
                ("UIR Upper Limit",                     r[90:95]),
                ("Cruise Table Ind",                    r[95:97]),
                ("FIR/UIR Name",                        r[98:123]),
                ("File Record No",                      r[123:128]),
                ("Cycle Date",                          r[128:132])
            ]
        else:
            # continuation record
            match r[20]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4:6]),
                        ("FIR/UIR Identifier",                  r[6:10]),
                        ("FIR/UIR Address",                     r[10:14]),
                        ("FIR/UIR Indicator",                   r[14]),
                        ("Sequence Number",                     r[15:19]),
                        ("Continuation Record No",              r[19]),
                        ("Application Type",                    r[20]),
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
