
class ControlledAirspace():

    cont_idx = 24
    app_idx = 25

    def read(self, r):
        if int(r[self.cont_idx]) < 2:
            # primary record
            return [
                ("Record Type",                         r[0]),
                ("Customer / Area Code",                r[1:4]),
                ("Section Code",                        r[4:6]),
                ("ICAO Code",                           r[6:8]),
                ("Airspace Type",                       r[9]),
                ("Airspace Center",                     r[9:14]),
                ("Section Code",                        r[14:16]),
                ("Airspace Classification",             r[16]),
                ("Multiple Code",                       r[19]),
                ("Sequence Number",                     r[20:24]),
                ("Continuation Record No",              r[24]),
                ("Level",                               r[25]),
                ("Time Code",                           r[26]),
                ("NOTAM",                               r[27]),
                ("Boundary Via",                        r[30:32]),
                ("Latitude",                            r[32:41]),
                ("Longitude",                           r[41:51]),
                ("Arc Origin Latitude",                 r[51:60]),
                ("Arc Origin Longitude",                r[60:70]),
                ("Arc Distance",                        r[70:74]),
                ("Arc Bearing",                         r[74:78]),
                ("RNP",                                 r[78:81]),
                ("Lower Limit",                         r[81:86]),
                ("Unit Indicator",                      r[86]),
                ("Upper Limit",                         r[87:92]),
                ("Unit Indicator",                      r[92]),
                ("Controlled Airspace Name",            r[93:123]),
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
                        ("Section Code",                        r[4:6]),
                        ("ICAO Code",                           r[6:8]),
                        ("Airspace Type",                       r[9]),
                        ("Airspace Center",                     r[9:14]),
                        ("Section Code",                        r[14:16]),
                        ("Airspace Classification",             r[16]),
                        ("Multiple Code",                       r[19]),
                        ("Sequence Number",                     r[20:24]),
                        ("Continuation Record No",              r[24]),
                        ("Application Type",                    r[25]),
                        ("Time Code",                           r[26]),
                        ("NOTAM",                               r[27]),
                        ("Time Indicator",                      r[28]),
                        ("Time of Operations",                  r[29:39]),
                        ("Time of Operations",                  r[39:49]),
                        ("Time of Operations",                  r[49:59]),
                        ("Time of Operations",                  r[59:69]),
                        ("Time of Operations",                  r[69:79]),
                        ("Time of Operations",                  r[79:89]),
                        ("Time of Operations",                  r[89:99]),
                        ("Controlling Agency",                  r[99:123]),
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
