
class Sid():

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport Identifier",                  r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("SID/STAR/Approach Identifier",        r[13:19]),
            ("Procedure Type",                      r[19]),
            ("Runway Transition Identifier",        r[20:25]),
            ("Runway Transition Fix",               r[25:30]),
            ("ICAO Code",                           r[30:32]),
            ("Section Code",                        r[32:34]),
            ("Runway Transition Along Track Dist",  r[34:37]),
            ("Common Segment Transition Fix",       r[37:42]),
            ("ICAO Code",                           r[42:44]),
            ("Section Code",                        r[44:46]),
            ("Common Segment Along Track Dist",     r[46:49]),
            ("Enroute Transition Identifier",       r[49:54]),
            ("Enroute Transition Fix",              r[54:59]),
            ("ICAO Code",                           r[59:61]),
            ("Section Code",                        r[61:63]),
            ("Enroute Transition Along Track Dist", r[63:66]),
            ("Sequence Number",                     r[66:69]),
            ("Continuation Number",                 r[69]),
            ("Number of Engines",                   r[70:74]),
            ("Turboprop/Jet Indicator",             r[74]),
            ("RNAV Flag",                           r[75]),
            ("ATC Weight Category",                 r[76]),
            ("ATC Identifier",                      r[77:84]),
            ("Time Code",                           r[84]),
            ("Procedure Description",               r[85:100]),
            ("Leg Type Code",                       r[100:102]),
            ("Reporting Code",                      r[102]),
            ("Initial Departure Magnetic Course",   r[103:107]),
            ("Altitude Description",                r[107]),
            ("Altitude",                            r[108:111]),
            ("Altitude",                            r[111:114]),
            ("Speed Limit",                         r[114:117]),
            ("Initial Cruise Table",                r[117:119]),
            ("Speed Limit Description",             r[119]),
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
                    return
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
                    return
                case 'Q':
                    return
                case 'S':
                    return
                case _:
                    raise ValueError('Unknown Application Type')
