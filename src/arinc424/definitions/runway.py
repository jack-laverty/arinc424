from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.10.1 Runway Primary Records
class Runway():

  cont_idx = 21
  app_idx = 22
  continuations = ['A', 'S']
  name = 'Runway'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'A':
        return self.read_cont(line)
      case 'S':
        return self.read_sim(line)
      case _:
        return []

  def read_primary(self, r):
    return [
      Field("Record Type",                            r[0],           decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
      Field("Section Code",                           r[4]+r[12],     decoder.field_004),
      Field("Airport ICAO Identifier",                r[6:10],        decoder.field_006),
      Field("ICAO Code",                              r[10:12],       decoder.field_014),
      Field("Runway Identifier",                      r[13:18],       decoder.field_046),
      Field("Continuation Record No",                 r[21],          decoder.field_016),
      Field("Runway Length",                          r[22:27],       decoder.field_057),
      Field("Runway Magnetic Bearing",                r[27:31],       decoder.field_058),
      Field("Runway Latitude",                        r[32:41],       decoder.field_036),
      Field("Runway Longitude",                       r[41:51],       decoder.field_037),
      Field("Runway Gradient",                        r[51:56],       decoder.field_212),
      Field("(LTP) Ellipsoid Height",                 r[60:66],       decoder.field_225),
      Field("Landing Threshold Elevation",            r[66:71],       decoder.field_068),
      Field("Displaced Threshold Dist",               r[71:75],       decoder.field_069),
      Field("Threshold Crossing Height",              r[75:77],       decoder.field_067),
      Field("Runway Width",                           r[77:80],       decoder.field_109),
      Field("TCH Value Indicator",                    r[80],          decoder.field_270),
      Field("Localizer/MLS/GLS Ref Path Ident",       r[81:85],       decoder.field_044),
      Field("Localizer/MLS/GLS Category/Class",       r[85],          decoder.field_080),
      Field("Stopway",                                r[86:90],       decoder.field_079),
      Field("Localizer/MLS/GLS Ref Path Ident (2)",   r[90:94],       decoder.field_044),
      Field("Localizer/MLS/GLS Category/Class (2)",   r[94],          decoder.field_080),
      Field("Runway Description",                     r[101:123],     decoder.field_059),
      Field("File Record No",                         r[123:128],     decoder.field_031),
      Field("Cycle Date",                             r[128:132],     decoder.field_032)
    ]

  def read_cont(self, r):
    return [
      Field("Record Type",                            r[0],           decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
      Field("Section Code",                           r[4]+r[12],     decoder.field_004),
      Field("Airport ICAO Identifier",                r[6:10],        decoder.field_006),
      Field("ICAO Code",                              r[10:12],       decoder.field_014),
      Field("Runway Identifier",                      r[13:18],       decoder.field_046),
      Field("Continuation Record No",                 r[21],          decoder.field_016),
      Field("Notes",                                  r[23:92],       decoder.field_061),
      Field("File Record No",                         r[123:128],     decoder.field_031),
      Field("Cycle Date",                             r[128:132],     decoder.field_032)
    ]

  def read_sim(self, r):
      return [
          Field("Record Type",                            r[0],           decoder.field_002),
          Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
          Field("Section Code",                           r[4]+r[12],     decoder.field_004),
          Field("Airport ICAO Identifier",                r[6:10],        decoder.field_006),
          Field("ICAO Code",                              r[10:12],       decoder.field_014),
          Field("Runway Identifier",                      r[13:18],       decoder.field_046),
          Field("Continuation Record No",                 r[21],          decoder.field_016),
          Field("Application Type",                       r[22],          decoder.field_091),
          Field("Runway True Bearing",                    r[51:56],       decoder.field_094),
          Field("True Bearing Source",                    r[56],          decoder.field_095),
          Field("TDZE Location",                          r[65],          decoder.field_098),
          Field("Touchdown Zone Elevation",               r[66:71],       decoder.field_097),
          Field("File Record No",                         r[123:128],     decoder.field_031),
          Field("Cycle Date",                             r[128:132],     decoder.field_032)
      ]

  # def read_flight1(self, r):
  #     return [
  #         Field("Record Type",                            r[0],           decoder.field_000),
  #         Field("Customer / Area Code",                   r[1:4],         decoder.field_000),
  #         Field("Section Code",                           r[4]+r[12],     decoder.field_000),
  #         Field("Airport Identifier",                     r[6:10],        decoder.field_000),
  #         Field("ICAO Code",                              r[10:12],       decoder.field_000),
  #         Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_000),
  #         Field("Route Type",                             r[19],          decoder.field_000),
  #         Field("Transition Identifier",                  r[20:25],       decoder.field_000),
  #         Field("Sequence Number",                        r[26:29],       decoder.field_000),
  #         Field("Fix Identifier",                         r[29:34],       decoder.field_000),
  #         Field("ICAO Code (2)",                          r[34:36],       decoder.field_000),
  #         Field("Section Code (2)",                       r[36:38],       decoder.field_000),
  #         Field("Continuation Record No",                 r[38],          decoder.field_000),
  #         Field("Application Type",                       r[39],          decoder.field_000),
  #         Field("Start/End Indicator",                    r[40],          decoder.field_000),
  #         Field("Start/End Date",                         r[41:45],       decoder.field_000),
  #         Field("Leg Distance",                           r[74:78],       decoder.field_000),
  #         Field("File Record No",                         r[123:128],     decoder.field_000),
  #         Field("Cycle Date",                             r[128:132],     decoder.field_000)
  #     ]