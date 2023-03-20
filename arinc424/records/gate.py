from arinc424.decoder import Field
import arinc424.decoder as decoder


class Gate():

    cont_idx = 21
    app_idx = 22

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
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport ICAO Identifier",             r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Gate Identifier",                     r[13:18],      decoder.field_056),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Gate Latitude",                       r[32:41],      decoder.field_036),
            Field("Gate Longitude",                      r[41:51],      decoder.field_037),
            Field("Name",                                r[98:123],     decoder.field_060),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport ICAO Identifier",             r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Gate Identifier",                     r[13:18],      decoder.field_056),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Notes",                   r[22],         decoder.field_091),
            Field("Notes",                               r[23:92],      decoder.field_061),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]
