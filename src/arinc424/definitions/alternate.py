from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.30 Alternate Record (RA)
class Alternate():

  # 4.1.30.1 Alternate Primary Records
  def read(self, r, primary):
    return [
      Field("Record Type",                            r[0],          decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],        decoder.field_003),
      Field("Section Code",                           r[4:6],        decoder.field_004),
      Field("Alternate Related Airport to Fix",       r[6:11],       decoder.field_075),
      Field("Alternate Related ICAO Code",            r[11:13],      decoder.field_014),
      Field("Alternate Section",                      r[13:15],      decoder.field_004),
      Field("Alternate Record Type",                  r[15:17],      decoder.field_250),
      Field("Distance to Alternate",                  r[19:22],      decoder.field_251),
      Field("Alternate Type",                         r[22],         decoder.field_252),
      Field("Primary Alternate Identifier",           r[23:33],      decoder.field_253),
      Field("Distance to Alternate (2)",              r[35:38],      decoder.field_251),
      Field("Alternate Type (2)",                     r[38],         decoder.field_252),
      Field("Additional Alternate Identifier One",    r[39:49],      decoder.field_253),
      Field("Distance to Alternate (3)",              r[51:54],      decoder.field_251),
      Field("Alternate Type (3)",                     r[54],         decoder.field_252),
      Field("Additional Alternate Identifier Two",    r[55:65],      decoder.field_253),
      Field("Distance to Alternate (3)",              r[67:70],      decoder.field_251),
      Field("Alternate Type (3)",                     r[70],         decoder.field_252),
      Field("Additional Alternate Identifier (3))",   r[71:81],      decoder.field_253),
      Field("Distance to Alternate (4)",              r[83:86],      decoder.field_251),
      Field("Alternate Type (4)",                     r[86],         decoder.field_252),
      Field("Additional Alternate Identifier (4)",    r[87:97],      decoder.field_253),
      Field("Distance to Alternate (5)",              r[99:102],     decoder.field_251),
      Field("Alternate Type (5)",                     r[102],        decoder.field_252),
      Field("Additional Alternate Identifier (5)",    r[103:113],    decoder.field_253),
      Field("File Record No",                         r[123:128],    decoder.field_031),
      Field("Cycle Date",                             r[128:132],    decoder.field_032)
    ]