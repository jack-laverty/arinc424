
class AirportCommunication():

    def read(self, r):
        if int(r[25]) < 2:
            # primary record
            return [
                ("Record Type",                         r[0]),
                ("Customer / Area Code",                r[1:4]),
                ("Section Code",                        r[4]+r[12]),
                ("Airport Identifier",                  r[6:10]),
                ("ICAO Code",                           r[10:12]),
                ("Communications Type",                 r[13:16]),
                ("Communications Freq",                 r[16:23]),
                ("Guard/Transmit",                      r[23]),
                ("Frequency Units",                     r[24]),
                ("Continuation Record No",              r[25]),
                ("Service Indicator",                   r[26:29]),
                ("Radar Service",                       r[29]),
                ("Modulation",                          r[30]),
                ("Signal Emission",                     r[31]),
                ("Latitude",                            r[32:41]),
                ("Longitude",                           r[41:51]),
                ("Magnetic Variation",                  r[51:56]),
                ("Facility Elevation",                  r[56:61]),
                ("H24 Indicator",                       r[61]),
                ("Sectorization",                       r[62:68]),
                ("Altitude Description",                r[68]),
                ("Communication Altitude",              r[69:74]),
                ("Communication Altitude",              r[74:79]),
                ("Sector Facility",                     r[79:83]),
                ("ICAO Code",                           r[83:85]),
                ("Section",                             r[85:87]),
                ("Distance Description",                r[87]),
                ("Communications Distance",             r[88:90]),
                ("Remote Facility",                     r[90:94]),
                ("ICAO Code",                           r[94:96]),
                ("Section",                             r[96:98]),
                ("Call Sign",                           r[98:123]),
                ("File Record No",                      r[123:128]),
                ("Cycle Date",                          r[128:132])
            ]
        else:
            # continuation record
            match r[26]:
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
                    return
                case 'L':
                    # VHF Navaid Limitation Continuation
                    return
                case 'N':
                    # A sector narrative continuation
                    return [
                        ("Record Type",                         r[0]),
                        ("Customer / Area Code",                r[1:4]),
                        ("Section Code",                        r[4]+r[12]),
                        ("Airport Identifier",                  r[6:10]),
                        ("ICAO Code",                           r[10:12]),
                        ("Communications Type",                 r[13:16]),
                        ("Communications Freq",                 r[16:23]),
                        ("Guard/Transmit",                      r[23]),
                        ("Frequency Units",                     r[24]),
                        ("Continuation Record No",              r[25]),
                        ("Application Type",                    r[26]),
                        ("Narrative",                           r[27:87]),
                        ("File Record No",                      r[123:128]),
                        ("Cycle Date",                          r[128:132])
                    ]
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
                    return
