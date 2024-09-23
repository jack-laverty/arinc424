from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.13 Localizer Marker Records
class LocalizerMarker():

  cont_idx = 21
  app_idx = 22
  continuations = ['A']
  name = 'Localizer Marker'

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

  # 4.1.13.1
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport Identifier",                  r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Localizer Identifier",                r[13:17],      decoder.field_044),
      Field("Marker Type",                         r[17:20],      decoder.field_099),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Locator Frequency",                   r[22:27],      decoder.field_034),
      Field("Runway Identifier",                   r[27:32],      decoder.field_046),
      Field("Marker Latitude",                     r[32:41],      decoder.field_036),
      Field("Marker Longitude",                    r[41:51],      decoder.field_037),
      Field("Minor Axis Bearing",                  r[51:55],      decoder.field_100),
      Field("Locator Latitude",                    r[55:64],      decoder.field_036),
      Field("Locator Longitude",                   r[64:74],      decoder.field_037),
      Field("Localizer Class",                     r[74:79],      decoder.field_035),
      Field("Localizer Facility Characteristics",  r[79:83],      decoder.field_093),
      Field("Localizer Identifier (2)",            r[84:88],      decoder.field_033),
      Field("Magnetic Variation",                  r[90:95],      decoder.field_039),
      Field("Facility Elevation",                  r[97:102],     decoder.field_092),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.13.2
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport Identifier",                  r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Localizer Identifier",                r[13:17],      decoder.field_044),
      Field("Marker Type",                         r[17:20],      decoder.field_099),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]