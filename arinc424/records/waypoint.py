
class Waypoint():

    def __init__(self, enrt) -> None:
        self.enrt = enrt

    def read_primary(self, r) -> list:
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":
            r[4:6] if self.enrt is True else r[4]+r[12],
            "Region Code":                         r[6:10],
            "ICAO Code":                           r[10:12],
            "Waypoint Identifier":                 r[13:18],
            "ICAO Code (2)":                       r[19:21],
            "Continuation Record No":              r[21],
            "Waypoint Type":                       r[26:29],
            "Waypoint Usage":                      r[29:31],
            "Waypoint Latitude":                   r[32:41],
            "Waypoint Longitude":                  r[41:51],
            "Dynamic Mag. Variation":              r[74:79],
            "Datum Code":                          r[84:87],
            "Name Format Indicator":               r[95:98],
            "Waypoint Name / Desc":                r[98:123],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }

    def read_cont(self, r) -> list:
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":
            r[4:6] if self.enrt is True else r[4]+r[12],
            "Region Code":                         r[6:10],
            "ICAO Code":                           r[10:12],
            "Waypoint Identifier":                 r[13:18],
            "ICAO Code (2)":                       r[19:21],
            "Continuation Record No":              r[21],
            "Application Type":                    r[22],
            "Notes":                               r[23:123],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }

    def read_flight_plan0(self, r) -> list:
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":
            r[4:6] if self.enrt is True else r[4]+r[12],
            "Region Code":                         r[6:10],
            "ICAO Code":                           r[10:12],
            "Waypoint Identifier":                 r[13:18],
            "ICAO Code (2)":                       r[19:21],
            "Continuation Record No":              r[21],
            "Application Type":                    r[22],
            "FIR Identifier":                      r[23:27],
            "UIR Identifier":                      r[27:31],
            "Start/End Indicator":                 r[31],
            "Start/End Date":                      r[32:43],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }

    def read_flight_plan1(self, r) -> list:
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":
            r[4:6] if self.enrt is True else r[4]+r[12],
            "Region Code":                         r[6:10],
            "ICAO Code":                           r[10:12],
            "Waypoint Identifier":                 r[13:18],
            "ICAO Code (2)":                       r[19:21],
            "Continuation Record No":              r[21],
            "Waypoint Type":                       r[26:29],
            "Waypoint Usage":                      r[29:31],
            "Waypoint Latitude":                   r[32:41],
            "Waypoint Longitude":                  r[41:51],
            "Dynamic Mag. Variation":              r[74:79],
            "Datum Code":                          r[84:87],
            "Name Format Indicator":               r[95:98],
            "Waypoint Name / Desc":                r[98:123],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }

    def read(self, line) -> list:
        if int(line[21]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[22]:
                case 'A':
                    return self.read_cont(line)
                case 'C':
                    return []
                case 'E':
                    return []
                case 'L':
                    return []
                case 'N':
                    return []
                case 'T':
                    return []
                case 'U':
                    return []
                case 'V':
                    return []
                case 'P':
                    return self.read_flight_plan0(line)
                case 'Q':
                    return self.read_flight_plan1(line)
                case 'S':
                    return []
                case _:
                    return []
