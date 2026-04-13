from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.15 Airways Marker Records (EM)
class AirwaysMarker():

  cont_idx = 21
  app_idx = 22
  continuations = ['A']
  name = 'Airways Marker'

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

  # 4.1.15.1 Airways Marker Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("Marker Identifier",                   r[13:17],      decoder.field_110),
      Field("ICAO Code",                           r[19:21],      decoder.field_014),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Marker Code",                         r[22:26],      decoder.field_111),
      Field("Marker Shape",                        r[27],         decoder.field_112),
      Field("Marker Power",                        r[28],         decoder.field_113),
      Field("Marker Latitude",                     r[32:41],      decoder.field_036),
      Field("Marker Longitude",                    r[41:51],      decoder.field_037),
      Field("Minor Axis",                          r[51:55],      decoder.field_100),
      Field("Magnetic Variation",                  r[74:79],      decoder.field_039),
      Field("Facility Elevation",                  r[79:84],      decoder.field_092),
      Field("Datum Code",                          r[84:87],      decoder.field_197),
      Field("Marker Name",                         r[93:123],     decoder.field_071),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.15.2 Airways Marker Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("Marker Identifier",                   r[13:17],      decoder.field_110),
      Field("ICAO Code",                           r[19:21],      decoder.field_014),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]