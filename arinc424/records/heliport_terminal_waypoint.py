from arinc424.decoder import Field
import arinc424.decoder as decoder


class HeliportTerminalWaypoint():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    raise ValueError('Unknown Application Type')

    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Waypoint Type",                       r[26:29],      decoder.field_042),
            Field("Waypoint Usage",                      r[29:31],      decoder.field_082),
            Field("Waypoint Latitude",                   r[32:41],      decoder.field_036),
            Field("Waypoint Longitude",                  r[41:51],      decoder.field_037),
            Field("Dynamic Magnetic Variation",          r[74:79],      decoder.field_039),
            Field("Datum Code",                          r[84:87],      decoder.field_197),
            Field("Name Format Indicator",               r[95:98],      decoder.field_196),
            Field("Waypoint Name/Description",           r[98:123],     decoder.field_043),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("Notes",                               r[23:92],      decoder.field_061),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]
