from arinc424.decoder import Field
import arinc424.decoder as decoder


class Waypoint():

    cont_idx = 21
    app_idx = 22

    def __init__(self, enrt) -> None:
        self.enrt = enrt

    def read(self, line) -> list:
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'P':
                    return self.read_flight_plan0(line)
                case 'Q':
                    return self.read_flight_plan1(line)
                case _:
                    raise ValueError("bad waypoint record")

    def read_primary(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Waypoint Type",                       r[26:29],      decoder.field_042),
            Field("Waypoint Usage",                      r[29:31],      decoder.field_082),
            Field("Waypoint Latitude",                   r[32:41],      decoder.field_036),
            Field("Waypoint Longitude",                  r[41:51],      decoder.field_037),
            Field("Dynamic Mag. Variation",              r[74:79],      decoder.field_039),
            Field("Datum Code",                          r[84:87],      decoder.field_197),
            Field("Name Format Indicator",               r[95:98],      decoder.field_196),
            Field("Waypoint Name / Desc",                r[98:123],     decoder.field_043),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_cont(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("Notes",                               r[23:123],     decoder.field_061),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_flight_plan0(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("FIR Identifier",                      r[23:27],      decoder.field_116),
            Field("UIR Identifier",                      r[27:31],      decoder.field_116),
            Field("Start/End Indicator",                 r[31],         decoder.field_152),
            Field("Start/End Date",                      r[32:43],      decoder.field_153),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_flight_plan1(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Waypoint Type",                       r[26:29],      decoder.field_042),
            Field("Waypoint Usage",                      r[29:31],      decoder.field_082),
            Field("Waypoint Latitude",                   r[32:41],      decoder.field_036),
            Field("Waypoint Longitude",                  r[41:51],      decoder.field_037),
            Field("Dynamic Mag. Variation",              r[74:79],      decoder.field_039),
            Field("Datum Code",                          r[84:87],      decoder.field_197),
            Field("Name Format Indicator",               r[95:98],      decoder.field_196),
            Field("Waypoint Name / Desc",                r[98:123],     decoder.field_043),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]
