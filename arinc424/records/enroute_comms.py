
class EnrouteComms():

    def read(self, r):
        if int(r[55]) < 2:
            # primary record
            return [
                ("Record Type",                         r[0]),
                ("Customer / Area Code",                r[1:4]),
                ("Section Code",                        r[4:6]),
                ("FIR/RDO Ident",                       r[6:10]),
                ("FIR/UIR Address",                     r[10:14]),
                ("Indicator",                           r[14]),
                ("Remote Name",                         r[18:43]),
                ("Communications Type",                 r[43:46]),
                ("Comm Frequency",                      r[46:53]),
                ("Guard/Transmit",                      r[53]),
                ("Frequency Units",                     r[54]),
                ("Continuation Record No",              r[55]),
                ("Service Indicator",                   r[56:59]),
                ("Radar Service",                       r[59]),
                ("Modulation",                          r[60]),
                ("Signal Emission",                     r[61]),
                ("Latitude",                            r[62:71]),
                ("Longitude",                           r[71:81]),
                ("Magnetic Variation",                  r[81:86]),
                ("Facility Elevation",                  r[86:91]),
                ("H24 Indicator",                       r[91]),
                ("Altitude Description",                r[92]),
                ("Communication Altitude",              r[93:98]),
                ("Communication Altitude",              r[98:103]),
                ("Remote Facility",                     r[103:107]),
                ("ICAO Code",                           r[107:109]),
                ("Section Code",                        r[109:111]),
                ("File Record No",                      r[123:128]),
                ("Cycle Date",                          r[128:132])
            ]
        else:
            # continuation record
            match r[56]:
                case 'A':
                    # standard ARINC continuation containing notes or other
                    # formatted data
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4:6]),
                        ("FIR/RDO Ident",                       r[6:10]),
                        ("FIR/UIR Address",                     r[10:14]),
                        ("Indicator",                           r[14]),
                        ("Remote Name",                         r[18:43]),
                        ("Communications Type",                 r[43:46]),
                        ("Comm Frequency",                      r[46:53]),
                        ("Guard/Transmit",                      r[53]),
                        ("Frequency Units",                     r[54]),
                        ("Continuation Record No",              r[55]),
                        ("Application Type",                    r[56]),
                        ("Time Code",                           r[57]),
                        ("NOTAM",                               r[58]),
                        ("Time Indicator",                      r[59]),
                        ("Time of Operation",                   r[60:70]),
                        ("Call Sign",                           r[93:123]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
                case 'B':
                    # combined controlling agency/call sign and formatted
                    # time of operation
                    # print("ERROR: Found Continuation Record 'B' unhandled")
                    return
                case 'C':
                    # call sign/controlling agency continuation
                    # print("ERROR: Found Continuation Record 'C' unhandled")
                    return
                case 'E':
                    # primary record extension
                    # print("ERROR: Found Continuation Record 'E' unhandled")
                    return
                case 'L':
                    # VHF Navaid Limitation Continuation
                    # print("ERROR: Found Continuation Record 'L' unhandled")
                    return
                case 'N':
                    # A sector narrative continuation
                    # print("ERROR: Found Continuation Record 'N' unhandled")
                    return
                case 'T':
                    # a time of operations continuation
                    # 'formatted time data'
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4:6]),
                        ("FIR/RDO Ident",                       r[6:10]),
                        ("FIR/UIR Address",                     r[10:14]),
                        ("Indicator",                           r[14]),
                        ("Remote Name",                         r[18:43]),
                        ("Communications Type",                 r[43:46]),
                        ("Comm Frequency",                      r[46:53]),
                        ("Guard/Transmit",                      r[53]),
                        ("Frequency Units",                     r[54]),
                        ("Continuation Record No",              r[55]),
                        ("Application Type",                    r[56]),
                        ("Time of Operation",                   r[60:70]),
                        ("Time of Operation",                   r[70:80]),
                        ("Time of Operation",                   r[80:90]),
                        ("Time of Operation",                   r[90:100]),
                        ("Time of Operation",                   r[100:110]),
                        ("Time of Operation",                   r[110:120]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
                    return
                case 'U':
                    # a time of operations continuation
                    # 'narrative time data'
                    # print("ERROR: Found Continuation Record 'U' unhandled")
                    return
                case 'V':
                    # a time of operations continuation
                    # start/end date
                    # print("ERROR: Found Continuation Record 'V' unhandled")
                    return
                case 'P':
                    # a flight planning application continuation
                    # print("ERROR: Found Continuation Record 'P' unhandled")
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
                    # print("ERROR: Found Continuation Record 'Q' unhandled")
                    return
                case 'S':
                    # simulation application continuation
                    # print("ERROR: Found Continuation Record 'S' unhandled")
                    return
                case 'W':
                    # an airport or heliport procedure data continuation
                    # with SBAS use authorization information
                    # print("ERROR: Found Continuation Record 'W' unhandled")
                    return
                case _:
                    # a flight planning application primary data continuation
                    # see notes above for case 'Q'
                    # TODO make this less sketchy
                    # print("ERROR: Found Continuation Record {} unhandled"
                    #       .format(r[56]))
                    return
