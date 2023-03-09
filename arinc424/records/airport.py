
class Airport():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'P':
                    return self.read_flight0(line)
                case 'Q':
                    return self.read_flight1(line)
                case _:
                    raise ValueError('Unknown Application Type')

    def read_primary(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4]+r[12],
            "Airport ICAO Identifier":                 r[6:10],
            "ICAO Code":                               r[10:12],
            "ATA/IATA Designator":                     r[13:16],
            "PAD Identifier":                          r[16:21],
            "Continuation Record No":                  r[21],
            "Speed Limit Altitude":                    r[22:27],
            "Longest Runway":                          r[27:30],
            "IFR Capability":                          r[30],
            "Longest Runway Surface Code":             r[31],
            "Airport Reference Pt. Latitude":          r[32:41],
            "Airport Reference Pt. Longitude":         r[41:51],
            "Magnetic Variation":                      r[51:56],
            "Airport Elevation":                       r[56:61],
            "Speed Limit":                             r[61:64],
            "Recommended Navaid":                      r[64:68],
            "ICAO Code (2)":                           r[68:70],
            "Transition Altitude":                     r[70:75],
            "Transition Level":                        r[75:80],
            "Public Military Indicator":               r[80],
            "Time Zone":                               r[81:84],
            "Daylight Indicator":                      r[84],
            "Magnetic/True Indicator":                 r[85],
            "Datum Code":                              r[86:89],
            "Airport Name":                            r[93:123],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def read_cont(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4]+r[12],
            "Heliport Identifier":                     r[6:10],
            "ICAO Code":                               r[10:12],
            "ATA/IATA Designator":                     r[13:16],
            "PAD Identifier":                          r[16:21],
            "Continuation Record No":                  r[21],
            "Application Type":                        r[22],
            "Notes":                                   r[23:92],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def read_flight0(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4]+r[12],
            "Heliport Identifier":                     r[6:10],
            "ICAO Code":                               r[10:12],
            "ATA/IATA Designator":                     r[13:16],
            "PAD Identifier":                          r[16:21],
            "Continuation Record No":                  r[21],
            "Application Type":                        r[22],
            "FIR Identifier":                          r[23:27],
            "UIR Identifier":                          r[27:31],
            "Start/End Indicator":                     r[31],
            "Start/End Date/Time":                     r[32:43],
            "Controlled A/S Indicator":                r[66],
            "Controlled A/S Airport Indent":           r[67:71],
            "Controlled A/S Airport ICAO":             r[71:73],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }

    def read_flight1(self, r):
        return {
            "Record Type":                             r[0],
            "Customer / Area Code":                    r[1:4],
            "Section Code":                            r[4]+r[12],
            "Heliport Identifier":                     r[6:10],
            "ICAO Code":                               r[10:12],
            "ATA/IATA Designator":                     r[13:16],
            "PAD Identifier":                          r[16:21],
            "Continuation Record No":                  r[21],
            "Application Type":                        r[22],
            "Notes":                                   r[23:92],
            "File Record No":                          r[123:128],
            "Cycle Date":                              r[128:132]
        }
