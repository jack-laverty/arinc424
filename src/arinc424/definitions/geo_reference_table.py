from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.26 Geographical Reference Table Records (TG)
#
# The Geographical Reference Table file contains information
# that permits the cross referencing of otherwise undefined
# geographical entities and Route Identifiers in the Preferred
# Route file. The contents are not standardized and may vary
# from data supplier to data supplier. The contents of such a
# file can only be used in conjunction with the Preferred
# Route file of the same database in which the file is
# presented.
#
class GeoReferenceTable():

  cont_idx = 38
  app_idx = 39
  continuations = ['A']
  name = 'Geographical Reference Table'

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

  # 4.1.26.1 Geographical Reference Table Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                        r[0],           decoder.field_002),
      Field("Customer / Area Code",               r[1:4],         decoder.field_003),
      Field("Section Code",                       r[4:6],         decoder.field_004),
      Field("Geographical Ref Table ID",          r[6:8],         decoder.field_218),
      Field("Sequence Number",                    r[8],           decoder.field_012),
      Field("Geographical Entity",                r[9:38],        decoder.field_219),
      Field("Continuation Record No",             r[38],          decoder.field_016),
      Field("Preferred Route Ident",              r[40:50],       decoder.field_008),
      Field("Preferred Route Use Ind",            r[50:52],       decoder.field_220),
      Field("Preferred Route Ident (2)",          r[52:62],       decoder.field_008),
      Field("Preferred Route Use Ind (2)",        r[62:64],       decoder.field_220),
      Field("Preferred Route Ident (3)",          r[64:74],       decoder.field_008),
      Field("Preferred Route Use Ind (3)",        r[74:76],       decoder.field_220),
      Field("Preferred Route Ident (4)",          r[76:86],       decoder.field_008),
      Field("Preferred Route Use Ind (4)",        r[86:88],       decoder.field_220),
      Field("Preferred Route Ident (4)",          r[88:98],       decoder.field_008),
      Field("Preferred Route Use Ind (4)",        r[98:100],      decoder.field_220),
      Field("Preferred Route Ident (5)",          r[100:110],     decoder.field_008),
      Field("Preferred Route Use Ind (5)",        r[110:112],     decoder.field_220),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.26.2 Geographical Reference Table Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                        r[0],           decoder.field_002),
      Field("Customer / Area Code",               r[1:4],         decoder.field_003),
      Field("Section Code",                       r[4:6],         decoder.field_004),
      Field("Geographical Ref Table ID",          r[6:8],         decoder.field_218),
      Field("Sequence Number",                    r[8],           decoder.field_012),
      Field("Geographical Entity",                r[9:38],        decoder.field_219),
      Field("Continuation Record No",             r[38],          decoder.field_016),
      Field("Application Type",                   r[39],          decoder.field_091),
      Field("File Record No",                     r[123:128],     decoder.field_031),
      Field("Cycle Date",                         r[128:132],     decoder.field_032)
    ]