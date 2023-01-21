
class Heliport():

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Heliport Identifier",                 r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("ATA/IATA Designator",                 r[13:16]),
            ("PAD Identifier",                      r[16:21]),
            ("Continuation Record No",              r[21]),
            ("Speed Limit Altitude",                r[22:27]),
            ("Datum Code",                          r[27:30]),
            ("IFR Indicator",                       r[30]),
            ("Latitude",                            r[32:41]),
            ("Longitude",                           r[41:51]),
            ("Magnetic Variation",                  r[51:56]),
            ("Heliport Elevation",                  r[56:61]),
            ("Speed Limit",                         r[61:64]),
            ("Recommended VHF Navaid",              r[64:68]),
            ("ICAO Code",                           r[68:70]),
            ("Transition Altitude",                 r[70:75]),
            ("Transition Level",                    r[75:80]),
            ("Public Military Indicator",           r[80]),
            ("Time Zone",                           r[81:84]),
            ("Daylight Indicator",                  r[84]),
            ("Pad Dimensions",                      r[85:91]),
            ("Magnetic/True Indicator",             r[91]),
            ("Heliport Name",                       r[93:123]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Heliport Identifier",                 r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("ATA/IATA Designator",                 r[13:16]),
            ("PAD Identifier",                      r[16:21]),
            ("Continuation Record No",              r[21]),
            ("Application Type",                    r[22]),
            ("Notes",                               r[23:92]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_flight0(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Heliport Identifier",                 r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("ATA/IATA Designator",                 r[13:16]),
            ("PAD Identifier",                      r[16:21]),
            ("Continuation Record No",              r[21]),
            ("Application Type",                    r[22]),
            ("FIR Identifier",                      r[23:27]),
            ("UIR Identifier",                      r[27:31]),
            ("Start/End Indicator",                 r[31]),
            ("Start/End Date/Time",                 r[32:43]),
            ("Controlled A/S Indicator",            r[66]),
            ("Controlled A/S Airport Indentifier",  r[67:71]),
            ("Controlled A/S Airport ICAO",         r[71:73]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132]),
        ]

    def read_flight1(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Heliport Identifier",                 r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("ATA/IATA Designator",                 r[13:16]),
            ("PAD Identifier",                      r[16:21]),
            ("Continuation Record No",              r[21]),
            ("Application Type",                    r[22]),
            ("Notes",                               r[23:92]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

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
                    return self.read_flight0(line)
                case 'Q':
                    return self.read_flight1(line)
                case 'S':
                    return
                case _:
                    raise ValueError('Unknown Application Type')
