from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.28  Path Point Records (PP)
class PathPoint():

  cont_idx = 26
  app_idx = 27
  continuations = ['E']
  name = 'Path Point'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'E':
        return self.read_cont(line)
      case _:
        raise ValueError("bad path point", line[self.app_idx])

  # 4.1.28.1 Path Point Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                            r[0],           decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
      Field("Section Code",                           r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                     r[6:10],        decoder.field_006),
      Field("ICAO Code",                              r[10:12],       decoder.field_014),
      Field("Approach Procedure Ident",               r[13:19],       decoder.field_010),
      Field("Runway or Helipad Ident",                r[19:24],       decoder.field_046),  # TODO or 180
      Field("Operation Type",                         r[24:26],       decoder.field_223),
      Field("Continuation Record No",                 r[26],          decoder.field_016),
      Field("Route Identifier",                       r[27],          decoder.field_224),
      Field("SBAS Service Provider Ident",            r[28:30],       decoder.field_255),
      Field("Reference Path Data Selector",           r[30:32],       decoder.field_256),
      Field("Reference Path Identifier",              r[32:36],       decoder.field_257),
      Field("Approach Performance Designator",        r[36],          decoder.field_258),
      Field("Landing Threshold Point Latitude",       r[37:48],       decoder.field_267),
      Field("Landing Threshold Point Longitude",      r[48:60],       decoder.field_268),
      Field("(LTP) Ellipsoid Height",                 r[60:66],       decoder.field_225),
      Field("Glide Path Angle",                       r[66:70],       decoder.field_226),
      Field("Flight Path Alignment Point Latitude",   r[70:81],       decoder.field_267),
      Field("Flight Path Alignment Point Longitude",  r[81:93],       decoder.field_268),
      Field("Course Width at Threshold Note 4",       r[93:98],       decoder.field_228),
      Field("Length Offset",                          r[98:102],      decoder.field_259),
      Field("Path Point TCH",                         r[102:108],     decoder.field_265),
      Field("TCH Units Indicator",                    r[108],         decoder.field_266),
      Field("HAL",                                    r[109:112],     decoder.field_263),
      Field("VAL",                                    r[112:115],     decoder.field_264),
      Field("SBAS FAS Data CRC Remainder",            r[115:123],     decoder.field_229),
      Field("File Record No",                         r[123:128],     decoder.field_031),
      Field("Cycle Date",                             r[128:132],     decoder.field_032)
    ]

  # 4.1.28.2  Path Point Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                            r[0],           decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
      Field("Section Code",                           r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                     r[6:10],        decoder.field_006),
      Field("ICAO Code",                              r[10:12],       decoder.field_014),
      Field("Approach Procedure Ident",               r[13:19],       decoder.field_010),
      Field("Runway or Helipad Ident",                r[19:24],       decoder.field_046),  # TODO or 180
      Field("Operation Type",                         r[24:26],       decoder.field_223),
      Field("Continuation Record No",                 r[26],          decoder.field_016),
      Field("Application Type",                       r[27],          decoder.field_091),
      Field("(FPAP) Ellipsoid Height",                r[28:34],       decoder.field_225),
      Field("(FPAP) Orthometric Height",              r[34:40],       decoder.field_227),
      Field("(LTP) Orthometric Height",               r[40:46],       decoder.field_227),
      Field("Approach Type Identifier",               r[46:56],       decoder.field_262),
      Field("GNSS Channel Number",                    r[56:61],       decoder.field_244),
      Field("Helicopter Procedure Course",            r[71:74],       decoder.field_269),
      Field("File Record No",                         r[123:128],     decoder.field_031),
      Field("Cycle Date",                             r[128:132],     decoder.field_032)
    ]