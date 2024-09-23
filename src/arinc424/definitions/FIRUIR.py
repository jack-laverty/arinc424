from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.17 FIR/UIR Records (UF)
class FIRUIR():

  cont_idx = 19
  app_idx = 20
  continuations = ['A']
  name = 'FIR/UIR'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'A':
        return self.read_cont(line)
      case _:
        return []

  # 4.1.17.1 FIR/UIR Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("FIR/UIR Identifier",                  r[6:10],       decoder.field_116),
      Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
      Field("FIR/UIR Indicator",                   r[14],         decoder.field_117),
      Field("Sequence Number",                     r[15:19],      decoder.field_012),
      Field("Continuation Record No",              r[19],         decoder.field_016),
      Field("Adjacent FIR Identifier",             r[20:24],      decoder.field_116),
      Field("Adjacent UIR Identifier",             r[24:28],      decoder.field_116),
      Field("Reporting Units Speed",               r[28],         decoder.field_122),
      Field("Reporting Units Altitude",            r[29],         decoder.field_123),
      Field("Entry Report",                        r[30],         decoder.field_124),
      Field("Boundary Via",                        r[32:34],      decoder.field_118),
      Field("FIR/UIR Latitude",                    r[34:43],      decoder.field_036),
      Field("FIR/UIR Longitude",                   r[43:53],      decoder.field_037),
      Field("Arc Origin Latitude",                 r[53:62],      decoder.field_036),
      Field("Arc Origin Longitude",                r[62:72],      decoder.field_037),
      Field("Arc Distance",                        r[72:76],      decoder.field_119),
      Field("Arc Bearing",                         r[76:80],      decoder.field_120),
      Field("FIR Upper Limit",                     r[80:85],      decoder.field_121),
      Field("UIR Lower Limit",                     r[85:90],      decoder.field_121),
      Field("UIR Upper Limit",                     r[90:95],      decoder.field_121),
      Field("Cruise Table Ind",                    r[95:97],      decoder.field_134),
      Field("FIR/UIR Name",                        r[98:123],     decoder.field_125),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.17.2 FIR/UIR Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("FIR/UIR Identifier",                  r[6:10],       decoder.field_116),
      Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
      Field("FIR/UIR Indicator",                   r[14],         decoder.field_117),
      Field("Sequence Number",                     r[15:19],      decoder.field_012),
      Field("Continuation Record No",              r[19],         decoder.field_016),
      Field("Application Type",                    r[20],         decoder.field_091),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]