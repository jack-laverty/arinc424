from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.16 Cruising Tables Records (TC)
class CruisingTables():

  def read(self, line, primary):
    return self.read_primary(line)

  # 4.1.16.1 Cruising Table Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Cruise Table Identifier",                 r[6:8],        decoder.field_134),
      Field("Sequence Number",                         r[8],          decoder.field_012),
      Field("Course From",                             r[28:32],      decoder.field_135),
      Field("Course To",                               r[32:36],      decoder.field_135),
      Field("Mag/True",                                r[36],         decoder.field_165),
      Field("Cruise Level From",                       r[39:44],      decoder.field_136),
      Field("Vertical Separation",                     r[44:49],      decoder.field_137),
      Field("Cruise Level To ",                        r[49:54],      decoder.field_136),
      Field("Cruise Level From (2)",                   r[54:59],      decoder.field_136),
      Field("Vertical Separation (2)",                 r[59:64],      decoder.field_137),
      Field("Cruise Level To (2)",                     r[64:69],      decoder.field_136),
      Field("Cruise Level From (3)",                   r[69:74],      decoder.field_136),
      Field("Vertical Separation (3)",                 r[74:79],      decoder.field_137),
      Field("Cruise Level To (3)",                     r[79:84],      decoder.field_136),
      Field("Cruise Level From (4)",                   r[84:89],      decoder.field_136),
      Field("Vertical Separation (4)",                 r[89:94],      decoder.field_137),
      Field("Cruise Level To (4)",                     r[94:99],      decoder.field_136),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]