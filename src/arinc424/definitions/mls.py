from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.22 Airport and Heliport MLS (Azimuth, Elevation
# and Back Azimuth) Records
class MLS():

  cont_idx = 21
  app_idx = 22
  continuations = ['A']
  name = 'MLS'

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

  # 4.1.22.1 Airport and Heliport MLS Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport Identifier",                  r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("MLS Identifier",                      r[13:17],      decoder.field_044),
      Field("MLS Category",                        r[17],         decoder.field_080),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Channel",                             r[22:25],      decoder.field_166),
      Field("Runway Identifier",                   r[27:32],      decoder.field_046),
      Field("Azimuth Latitude",                    r[32:41],      decoder.field_036),
      Field("Azimuth Longitude",                   r[41:51],      decoder.field_037),
      Field("Azimuth Bearing",                     r[51:55],      decoder.field_167),
      Field("Elevation Latitude",                  r[55:64],      decoder.field_036),
      Field("Elevation Longitude",                 r[64:74],      decoder.field_037),
      Field("Azimuth Position",                    r[74:78],      decoder.field_048),
      Field("Azimuth Position Reference",          r[78],         decoder.field_049),
      Field("Elevation Position",                  r[79:83],      decoder.field_050),
      Field("Azimuth Proportional Angle Right",    r[83:86],      decoder.field_168),
      Field("Azimuth Proportional Angle Left",     r[86:89],      decoder.field_168),
      Field("Azimuth Coverage Right",              r[89:92],      decoder.field_172),
      Field("Azimuth Coverage Left",               r[92:95],      decoder.field_172),
      Field("Elevation Angle Span",                r[95:98],      decoder.field_169),
      Field("Magnetic Variation",                  r[98:103],     decoder.field_039),
      Field("EL Elevation",                        r[103:108],    decoder.field_074),
      Field("Nominal Elevation Angle",             r[108:112],    decoder.field_173),
      Field("Minimum Glide Path Angle",            r[112:115],    decoder.field_052),
      Field("Supporting Facility Identifier",      r[115:119],    decoder.field_033),
      Field("Supporting Facility ICAO Code",       r[119:121],    decoder.field_014),
      Field("Supporting Facility Section",         r[121:123],    decoder.field_004),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.22.2 Airport and Heliport MLS Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport Identifier",                  r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("MLS Identifier",                      r[13:17],      decoder.field_044),
      Field("MLS Category",                        r[17],         decoder.field_080),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("Facility Characteristics",            r[27:32],      decoder.field_093),
      Field("Back Azimuth Latitude",               r[32:41],      decoder.field_036),
      Field("Back Azimuth Longitude",              r[41:51],      decoder.field_037),
      Field("Back Azimuth Bearing",                r[51:55],      decoder.field_167),
      Field("MLS Datum Point Latitude",            r[55:64],      decoder.field_036),
      Field("MLS Datum Point Longitude",           r[64:74],      decoder.field_037),
      Field("Back Azimuth Position",               r[74:78],      decoder.field_048),
      Field("Back Azimuth Position Reference",     r[78],         decoder.field_049),
      Field("Back Azimuth Proportional Angle Right", r[83:86],    decoder.field_168),
      Field("Back Azimuth Proportional Angle Left", r[86:89],     decoder.field_168),
      Field("Back Azimuth Coverage Right",         r[89:92],      decoder.field_172),
      Field("Back Azimuth Coverage Left",          r[92:95],      decoder.field_172),
      Field("Back Azimuth True Bearing",           r[95:98],      decoder.field_094),
      Field("Back Azimuth Bearing Source",         r[100],        decoder.field_095),
      Field("Azimuth True Bearing",                r[101:106],    decoder.field_094),
      Field("Azimuth Bearing Source",              r[106],        decoder.field_095),
      Field("Glide Path Height at Landing Threshold", r[107:109], decoder.field_067),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]