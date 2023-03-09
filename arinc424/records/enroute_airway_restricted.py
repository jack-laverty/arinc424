
class AirwayRestricted():

    def read(self, line):

        if int(line[17]) < 2:
            match line[15:17]:
                case 'AE':
                    return self.primary_altitude_exclude(line)
                case 'TC':
                    return self.primary_cruise_table(line)
                case 'SC':
                    return self.primary_seasonal_closure(line)
                case 'NR':
                    return self.primary_note_restriction(line)
                case _:
                    raise ValueError("Unknown Restricted Airway Type")
        else:
            match line[15:17]:
                case 'AE':
                    return self.cont_altitude_exclude(line)
                case 'TC':
                    return self.cont_cruise_table(line)
                case 'NR':
                    return self.cont_note_restriction(line)
                case _:
                    raise ValueError("Unknown Restricted Airway Type")

    def primary_altitude_exclude(self, r):
        # TODO finish this
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4:6],
            "Route Identifier":                        r[6:11],
            "Restriction Identifier":                  r[12:15],
            "Restriction Type":                        r[15:17],
            "Continuation Record No":                  r[17],
            "Start Fix Identifier":                    r[18:23],
            "Start Fix ICAO Code":                     r[23:25],
            "Start Fix Section Code":                  r[25:27],
            "Route Type":                              r[26:29],
            "Level":                                   r[29:31],
            "Direction Restriction":                   r[32:41],
            "Cruise Table Indicator":                  r[41:51],
            "EU Indicator":                            r[74:79],
            "Recommended NAVAID":                      r[84:87],
            "ICAO Code":                               r[95:98],
            "RNP":                                     r[98:123],
            "Theta":                                   r[98:123],
            "Rho":                                     r[98:123],
            "Outbound Magnetic Course":                r[98:123],
            "Route Distance From":                     r[98:123],
            "Inbound Magnetic Course":                 r[98:123],
            "Minimum Altitude":                        r[98:123],
            "Minimum Altitude (2)":                    r[98:123],
            "Maximum Altitude":                        r[98:123],
            "Fix Radius Transition Indicator":         r[98:123],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def cont_altitude_exclude(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4:6],
            "Continuation Record No":                  r[17],
            "Application Type":                        r[18],
            "Time Code":                               r[51],
            "Time Indicator":                          r[52],
            "Time of Operation":                       r[53:63],
            "Time of Operation (2)":                   r[63:73],
            "Time of Operation (3)":                   r[73:83],
            "Time of Operation (4)":                   r[83:93],
            "Exclusion Operator":                      r[93],
            "Units of Altitude":                       r[94],
            "Restriction Altitude":                    r[95:98],
            "Block Indicator":                         r[98],
            "Restriction Altitude (2)":                r[99:102],
            "Block Indicator (2)":                     r[102],
            "Restriction Altitude (3)":                r[103:106],
            "Block Indicator (3)":                     r[106],
            "Restriction Altitude (4)":                r[107:110],
            "Block Indicator (4)":                     r[110],
            "Restriction Altitude (5)":                r[111:114],
            "Block Indicator (5)":                     r[114],
            "Restriction Altitude (6)":                r[115:118],
            "Block Indicator (6)":                     r[118],
            "Restriction Altitude (7)":                r[119:122],
            "Block Indicator (7)":                     r[122],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def primary_note_restriction(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4:6],
            "Route Identifier":                        r[7:11],
            "Restriction Identifier":                  r[12:15],
            "Restriction Type":                        r[15:17],
            "Continuation Record No":                  r[17],
            "Start Fix Identifier":                    r[18:23],
            "Start Fix ICAO Code":                     r[23:25],
            "Start Fix Section Code":                  r[25],
            "End Fix Identifier":                      r[27:32],
            "End Fix ICAO Code":                       r[32:34],
            "End Fix Section Code":                    r[34:36],
            "Start Date":                              r[37:44],
            "End Date":                                r[44:51],
            "Restriction Notes":                       r[51:120],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def cont_note_restriction(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4:6],
            "Route Identifier":                        r[7:11],
            "Restriction Identifier":                  r[12:15],
            "Restriction Type":                        r[15:17],
            "Continuation Record No":                  r[17],
            "Application Type":                        r[18],
            "Restriction Notes":                       r[51:120],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def primary_seasonal_closure(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4:6],
            "Route Identifier":                        r[6:11],
            "Restriction Identifier":                  r[12:15],
            "Restriction Type":                        r[15:17],
            "Continuation Record No":                  r[17],
            "Start Fix Identifier":                    r[18:23],
            "Start Fix ICAO Code":                     r[23:25],
            "Start Fix Section Code":                  r[25:27],
            "End Fix Identifier":                      r[27:32],
            "End Fix ICAO Code":                       r[32:34],
            "End Fix Section Code":                    r[34:36],
            "Start Date":                              r[37:44],
            "End Date":                                r[44:51],
            "Time Code":                               r[51],
            "Time of Operation":                       r[53:63],
            "Time of Operation (2)":                   r[63:73],
            "Time of Operation (3)":                   r[73:83],
            "Time of Operation (4)":                   r[83:93],
            "Cruise Table Ident":                      r[93:95],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def primary_cruise_table(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4:6],
            "Route Identifier":                        r[6:11],
            "Restriction Identifier":                  r[12:15],
            "Restriction Type":                        r[15:17],
            "Continuation Record No":                  r[17],
            "Start Fix Identifier":                    r[18:23],
            "Start Fix ICAO Code":                     r[23:25],
            "Start Fix Section Code":                  r[25:27],
            "End Fix Identifier":                      r[27:32],
            "End Fix ICAO Code":                       r[32:34],
            "End Fix Section Code":                    r[34:36],
            "Start Date":                              r[37:44],
            "End Date":                                r[44:51],
            "Time Code":                               r[51],
            "Time of Operation":                       r[53:63],
            "Time of Operation (2)":                   r[63:73],
            "Time of Operation (3)":                   r[73:83],
            "Time of Operation (4)":                   r[83:93],
            "Cruise Table Ident":                      r[93:95],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def cont_cruise_table(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4:6],
            "Route Identifier":                        r[6:11],
            "Restriction Identifier":                  r[12:15],
            "Restriction Type":                        r[15:17],
            "Continuation Record No":                  r[17],
            "Application Type":                        r[18],
            "Time Code":                               r[51],
            "Time of Operation":                       r[53:63],
            "Time of Operation (2)":                   r[63:73],
            "Time of Operation (3)":                   r[73:83],
            "Time of Operation (4)":                   r[83:93],
            "Cruise Table Ident":                      r[93:95],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }
