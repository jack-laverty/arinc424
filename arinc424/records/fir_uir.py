
class FIR_UIR():

    cont_idx = 19
    app_idx = 20

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    def read_primary(self, r):
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":                        r[4:6],
            "FIR/UIR Identifier":                  r[6:10],
            "FIR/UIR Address":                     r[10:14],
            "FIR/UIR Indicator":                   r[14],
            "Sequence Number":                     r[15:19],
            "Continuation Record No":              r[19],
            "Adjacent FIR Identifier":             r[20:24],
            "Adjacent UIR Identifier":             r[24:28],
            "Reporting Units Speed":               r[28],
            "Reporting Units Altitude":            r[29],
            "Entry Report":                        r[30],
            "Boundary Via":                        r[32:34],
            "FIR/UIR Latitude":                    r[34:43],
            "FIR/UIR Longitude":                   r[43:53],
            "Arc Origin Latitude":                 r[53:62],
            "Arc Origin Longitude":                r[62:72],
            "Arc Distance":                        r[72:76],
            "Arc Bearing":                         r[76:80],
            "FIR Upper Limit":                     r[80:85],
            "UIR Lower Limit":                     r[85:90],
            "UIR Upper Limit":                     r[90:95],
            "Cruise Table Ind":                    r[95:97],
            "FIR/UIR Name":                        r[98:123],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }

    def read_cont(self, r):
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":                        r[4:6],
            "FIR/UIR Identifier":                  r[6:10],
            "FIR/UIR Address":                     r[10:14],
            "FIR/UIR Indicator":                   r[14],
            "Sequence Number":                     r[15:19],
            "Continuation Record No":              r[19],
            "Application Type":                    r[20],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }
