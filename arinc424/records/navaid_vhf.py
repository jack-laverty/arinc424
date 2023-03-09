
class VHFNavaid():

    def read_primary(self, r):
        return {
            "Record Type":                 r[0],
            "Customer / Area Code":        r[1:4],
            "Section Code":                r[4:6],
            "Airport ICAO Identifier":     r[6:10],
            "ICAO Code":                   r[10:12],
            "VOR Identifier":              r[13:17],
            "ICAO Code (2)":               r[19:21],
            "Continuation Record No":      r[21],
            "Frequency":                   r[22:27],
            "Class Facility":              r[27:29],
            "Class Power":                 r[29],
            "Class Info":                  r[30],
            "Class Collocation":           r[31],
            "VOR Latitude":                r[32:41],
            "VOR Longitude":               r[41:51],
            "DME Ident":                   r[51:55],
            "DME Latitude":                r[55:64],
            "DME Longitude":               r[64:74],
            "Station Declination":         r[74:79],
            "DME Elevation":               r[79:84],
            "Figure of Merit":             r[84],
            "ILS/DME Bias":                r[85:87],
            "Frequency Protection":        r[87:90],
            "Datum Code":                  r[90:93],
            "VOR Name":                    r[93:123],
            "File Record No":              r[123:128],
            "Cycle Date":                  r[128:132]
        }

    def read_cont(self, r):
        return {
            "Record Type":                 r[0],
            "Customer / Area Code":        r[1:4],
            "Section Code":                r[4:6],
            "Airport ICAO Identifier":     r[6:10],
            "ICAO Code":                   r[10:12],
            "VOR Identifier":              r[13:17],
            "ICAO Code (2)":               r[19:21],
            "Continuation Record No":      r[21],
            "Application Type":            r[22],
            "Notes":                       r[23:92],
            "File Record No":              r[123:128],
            "Cycle Date":                  r[128:132],
        }

    def read_sim(self, r):
        return {
            "Record Type":                 r[0],
            "Customer / Area Code":        r[1:4],
            "Section Code":                r[4:6],
            "Airport ICAO Identifier":     r[6:10],
            "ICAO Code":                   r[10:12],
            "VOR Identifier":              r[13:17],
            "ICAO Code (2)":               r[19:21],
            "Continuation Record No":      r[21],
            "Application Type":            r[22],
            "Facility Characteristics":    r[27:32],
            "File Record No":              r[123:128],
            "Cycle Date":                  r[128:132]
        }

    def read_flight_plan0(self, r):
        return {
            "Record Type":                 r[0],
            "Customer / Area Code":        r[1:4],
            "Section Code":                r[4:6],
            "Airport ICAO Identifier":     r[6:10],
            "ICAO Code":                   r[10:12],
            "VOR Identifier":              r[13:17],
            "ICAO Code (2)":               r[19:21],
            "Continuation Record No":      r[21],
            "Application Type":            r[22],
            "FIR Identifier":              r[23:27],
            "UIR Identifier":              r[28:31],
            "Start/End Indicator":         r[32],
            "Start/End Date":              r[32:43],
            "File Record No":              r[123:128],
            "Cycle Date":                  r[128:132]
        }

    def read_flight_plan1(self, r):
        return {
            "Record Type":                 r[0],
            "Customer / Area Code":        r[1:4],
            "Section Code":                r[4:6],
            "Airport ICAO Identifier":     r[6:10],
            "ICAO Code":                   r[10:12],
            "VOR Identifier":              r[13:17],
            "ICAO Code (2)":               r[19:21],
            "Continuation Record No":      r[21],
            "Application Type":            r[22],
            "Frequency":                   r[22:27],
            "Class":                       r[27:32],
            "VOR Latitude":                r[32:41],
            "VOR Longitude":               r[41:51],
            "DME Ident":                   r[51:55],
            "DME Latitude":                r[55:64],
            "DME Longitude":               r[64:74],
            "Station Declination":         r[74:79],
            "DME Elevation":               r[79:84],
            "Figure of Merit":             r[84],
            "ILS/DME Bias":                r[85:87],
            "Frequency Protection":        r[87:90],
            "Datum Code":                  r[90:93],
            "VOR Name":                    r[93:123],
            "File Record No":              r[123:128],
            "Cycle Date":                  r[128:132]
        }

    def read_lim(self, r):
        return {
            "Record Type":                 r[0],
            "Customer / Area Code":        r[1:4],
            "Section Code":                r[4:6],
            "Airport ICAO Identifier":     r[6:10],
            "ICAO Code":                   r[10:12],
            "VOR Identifier":              r[13:17],
            "ICAO Code (2)":               r[19:21],
            "Continuation Record No":      r[21],
            "Application Type":            r[22],
            "Navaid Limitation Code":      r[23],
            "Component Affected Indicator": r[24],
            "Sequence Number":             r[25:27],
            "Sector From/Sector To":       r[27:29],
            "Distance Description":        r[29],
            "Distance Limitation":         r[30:36],
            "Altitude Description":        r[36],
            "Altitude Limitation":         r[37:43],
            "Sector From/Sector To (2)":   r[43:45],
            "Distance Description (2)":    r[45],
            "Distance Limitation (2)":     r[46:52],
            "Altitude Description (2)":    r[52],
            "Altitude Limitation (2)":     r[53:59],
            "Sector From/Sector To (3)":   r[59:61],
            "Distance Description (3)":    r[61],
            "Distance Limitation (3)":     r[62:68],
            "Altitude Description (3)":    r[68],
            "Altitude Limitation (3)":     r[69:75],
            "Sector From/Sector To (4)":   r[75:77],
            "Distance Description (4)":    r[77],
            "Distance Limitation (4)":     r[79:84],
            "Altitude Description (4)":    r[84],
            "Altitude Limitation (4)":     r[85:91],
            "Sector From/Sector To (5)":   r[91:93],
            "Distance Description (5)":    r[93],
            "Distance Limitation (5)":     r[94:100],
            "Altitude Description (5)":    r[101],
            "Altitude Limitation (5)":     r[101:107],
            "Sequence End Indicator":      r[107],
            "File Record No":              r[123:128],
            "Cycle Date":                  r[128:132]
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
                    return self.lim(line)
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
                    return
                case 'S':
                    return self.read_sim(line)
                case _:
                    return self.read_flight_plan1(line)
