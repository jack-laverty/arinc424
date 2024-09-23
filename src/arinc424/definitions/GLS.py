from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.29 GLS Record (PT)
class GLS():

  cont_idx = 21
  app_idx = 22
  continuations = ['A']
  name = 'GLS'

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

  # 4.1.29.1 GLS Primary Records
  def read_primary(self, r):
      return [
          Field("Record Type",                         r[0],          decoder.field_002),
          Field("Customer / Area Code",                r[1:4],        decoder.field_003),
          Field("Section Code",                        r[4]+r[12],    decoder.field_004),
          Field("Airport and Heliport Identifier",     r[6:10],       decoder.field_006),
          Field("ICAO Code",                           r[10:12],      decoder.field_014),
          Field("GLS Ref Path Identifier",             r[13:17],      decoder.field_044),
          Field("GLS Category",                        r[17],         decoder.field_080),
          Field("Continuation Record No",              r[18:21],      decoder.field_016),
          Field("GLS Channel",                         r[22:27],      decoder.field_244),
          Field("Runway Identifier",                   r[27:32],      decoder.field_046),
          Field("GLS Approach Bearing",                r[51:55],      decoder.field_047),
          Field("Station Latitude",                    r[55:64],      decoder.field_036),
          Field("Station Longitude",                   r[64:74],      decoder.field_037),
          Field("GLS Station Ident",                   r[74:78],      decoder.field_243),
          Field("Service Volume Radius",               r[83:85],      decoder.field_245),
          Field("TDMA Slots",                          r[85:87],      decoder.field_246),
          Field("GLS Approach Slope",                  r[87:90],      decoder.field_052),
          Field("Magnetic Variation",                  r[90:95],      decoder.field_039),
          Field("Station Elevation",                   r[97:102],     decoder.field_074),
          Field("Datum Code",                          r[102:105],    decoder.field_197),
          Field("Station Type",                        r[105:108],    decoder.field_247),
          Field("Station Elevation WGS",               r[110:115],    decoder.field_248),
          Field("File Record No",                      r[123:128],    decoder.field_031),
          Field("Cycle Date",                          r[128:132],    decoder.field_032)
      ]

  # 4.1.29.2 GLS Continuation Records
  def read_cont(self, r):
      return [
          Field("Record Type",                         r[0],          decoder.field_002),
          Field("Customer / Area Code",                r[1:4],        decoder.field_003),
          Field("Section Code",                        r[4]+r[12],    decoder.field_004),
          Field("Airport and Heliport Identifier",     r[6:10],       decoder.field_006),
          Field("ICAO Code",                           r[10:12],      decoder.field_014),
          Field("GLS Ref Path Identifier",             r[13:17],      decoder.field_044),
          Field("GLS Category",                        r[17],         decoder.field_080),
          Field("Continuation Record No",              r[18:21],      decoder.field_016),
          Field("Application Type",                    r[22],         decoder.field_091),
          Field("File Record No",                      r[123:128],    decoder.field_031),
          Field("Cycle Date",                          r[128:132],    decoder.field_032)
      ]