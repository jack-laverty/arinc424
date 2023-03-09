
class NDBNavaid():

    def read_primary(self, r):
        return {
            "Record Type":                     r[0],
            "Customer / Area Code":            r[1:4],
            "Section Code":                    r[4:6],
            "Airport ICAO Identifier":         r[6:10],
            "ICAO Code":                       r[10:12],
            "NDB Identifier":                  r[13:17],
            "ICAO Code (2)":                   r[19:21],
            "Continuation Record No":          r[21],
            "NDB Frequency":                   r[22:27],
            "NDB Class Facility":              r[27:29],
            "NDB Class Power":                 r[29],
            "NDB Class Info":                  r[30],
            "NDB Class Collocation":           r[31],
            "NDB Latitude":                    r[32:41],
            "NDB Longitude":                   r[41:51],
            "Magnetic Variation":              r[74:79],
            "Datum Code":                      r[90:93],
            "NDB Name":                        r[93:123],
            "File Record No":                  r[123:128],
            "Cycle Date":                      r[128:132]
        }

    def read_cont(self, r):
        return {
            "Record Type":                     r[0],
            "Customer / Area Code":            r[1:4],
            "Section Code":                    r[4:6],
            "Airport ICAO Identifier":         r[6:10],
            "ICAO Code":                       r[10:12],
            "NDB Identifier":                  r[13:17],
            "ICAO Code (2)":                   r[19:21],
            "Continuation Record No":          r[21],
            "Application Type":                r[22],
            "Notes":                           r[23:92],
            "Reserved (Expansion)":            r[92:123],
            "File Record No":                  r[123:128],
            "Cycle Date":                      r[128:132]
        }

    def read_sim(self, r):
        return {
            "Record Type":                     r[0],
            "Customer / Area Code":            r[1:4],
            "Section Code":                    r[4:6],
            "Airport ICAO Identifier":         r[6:10],
            "ICAO Code":                       r[10:12],
            "NDB Identifier":                  r[13:17],
            "ICAO Code (2)":                   r[19:21],
            "Continuation Record No":          r[21],
            "Application Type":                r[22],
            "Facility Characteristics":        r[27:32],
            "Facility elevation":              r[79:84],
            "File Record No":                  r[123:128],
            "Cycle Date":                      r[128:132],
        }

    def read_flight_plan0(self, r):
        return {
            "Record Type":                     r[0],
            "Customer / Area Code":            r[1:4],
            "Section Code":                    r[4:6],
            "Airport ICAO Identifier":         r[6:10],
            "ICAO Code":                       r[10:12],
            "VOR Identifier":                  r[13:17],
            "ICAO Code (2)":                   r[19:21],
            "Continuation Record No":          r[21],
            "Application Type":                r[22],
            "FIR Identifier":                  r[23:27],
            "UIR Identifier":                  r[28:31],
            "Start/End Indicator":             r[32],
            "Start/End Date":                  r[32:43],
            "Reserved (Expansion)":            r[43:123],
            "File Record No":                  r[123:128],
            "Cycle Date":                      r[128:132]
        }

    def read_flight_plan1(self, r):
        return {
            "Record Type":                     r[0],
            "Customer / Area Code":            r[1:4],
            "Section Code":                    r[4:6],
            "Airport ICAO Identifier":         r[6:10],
            "ICAO Code":                       r[10:12],
            "NDB Identifier":                  r[13:17],
            "ICAO Code (2)":                   r[19:21],
            "Continuation Record No":          r[21],
            "NDB Frequency":                   r[22:27],
            "NDB Class Facility":              r[27:29],
            "NDB Class Power":                 r[29],
            "NDB Class Info":                  r[30],
            "NDB Class Collocation":           r[31],
            "NDB Latitude":                    r[32:41],
            "NDB Longitude":                   r[41:51],
            "Magnetic Variation":              r[74:79],
            "Datum Code":                      r[90:93],
            "NDB Name":                        r[93:123],
            "File Record No":                  r[123:128],
            "Cycle Date":                      r[128:132]
        }

    def read(self, line):
        if int(line[21]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[22]:
                case 'A':
                    return self.read_cont(line)
                case 'C':
                    return
                case 'E':
                    return
                case 'L':
                    return
                case 'N':
                    return
                case 'T':
                    return
                case 'U':
                    return
                case 'V':
                    return
                case 'P':
                    return self.read_flight_plan0(line)
                case 'Q':
                    return self.read_flight_plan1(line)
                case 'S':
                    return self.read_sim(line)
                case _:
                    raise ValueError('Unknown Application Type')
