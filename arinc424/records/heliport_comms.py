
class HeliportComms():

    cont_idx = 25
    app_idx = 26

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                # case '?':
                #     return self.read_cont1(line)
                case _:
                    raise ValueError('Unknown Application Type')

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Heliport Identifier",                 r[6:10]),
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
            ("Section Code",                        r[85:87]),
            ("Distance Description",                r[87]),
            ("Communications Distance",             r[88:90]),
            ("Remote Facility",                     r[90:94]),
            ("ICAO Code",                           r[94:96]),
            ("Section Code",                        r[96:98]),
            ("Call Sign",                           r[98:123]),
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

    def read_cont1(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Heliport Identifier",                 r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Communications Type",                 r[13:16]),
            ("Communications Freq",                 r[16:23]),
            ("Guard/Transmit",                      r[23]),
            ("Frequency Units",                     r[24]),
            ("Continuation Record No",              r[25]),
            ("Application Type",                    r[26]),
            ("Time Code",                           r[27]),
            ("NOTAM",                               r[28]),
            ("Time Indicator",                      r[29]),
            ("Time of Operation",                   r[30:40]),
            ("Time of Operation",                   r[40:50]),
            ("Time of Operation",                   r[50:60]),
            ("Time of Operation",                   r[60:70]),
            ("Time of Operation",                   r[70:80]),
            ("Time of Operation",                   r[80:90]),
            ("Time of Operation",                   r[90:100]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]
