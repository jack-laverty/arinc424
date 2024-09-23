from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.31 Airport TAA (PK)
class TAA():

  # cont_idx = 38
  # app_idx = 39
  cont_idx = 29
  app_idx = 30
  continuations = ['A']
  name = 'TAA'

  def application_type(self, line):
    return line[self.app_idx]

  def __init__(self, heliport=False):
    self.heliport = heliport
    if self.heliport is False:
      self.id_name = "Airport Identifier"
    else:
      self.id_name = "Heliport Identifier"

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'A':
        return self.read_cont(line)
      case _:
        return []

  # 4.1.31.1 Airport TAA Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                        r[0],           decoder.field_002),
      Field("Customer / Area Code",               r[1:4],         decoder.field_003),
      Field("Section Code",                       r[4]+r[12],     decoder.field_004),
      Field(self.id_name,                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                          r[10:12],       decoder.field_014),
      Field("Approach Identifier",                r[13:19],       decoder.field_010),
      Field("TAA Waypoint",                       r[19:24],       decoder.field_273),
      Field("TAA Procedure Turn",                 r[20:24],       decoder.field_271),
      Field("ICAO Code (2)",                      r[24:26],       decoder.field_014),
      Field("Section Code (2)",                   r[26:28],       decoder.field_004),
      Field("TAA Fix Position Indicator",         r[28],          decoder.field_272),
      Field("Continuation Record No",             r[29],          decoder.field_016),
      Field("Mag/True Indicator",                 r[40],          decoder.field_165),
      Field("Sector Radius",                      r[41:45],       decoder.field_274),
      Field("Sector Bearing",                     r[45:51],       decoder.field_146),
      Field("Sector Minimum Altitude",            r[51:54],       decoder.field_147),
      Field("Sector Radius (2)",                  r[54:58],       decoder.field_274),
      Field("Sector Bearing (2)",                 r[58:64],       decoder.field_146),
      Field("Sector Minimum Altitude (2)",        r[64:67],       decoder.field_147),
      Field("Sector Radius (3)",                  r[67:71],       decoder.field_274),
      Field("Sector Bearing (3)",                 r[71:77],       decoder.field_146),
      Field("Sector Minimum Altitude (3)",        r[77:80],       decoder.field_147),
      Field("Sector Radius (4)",                  r[80:84],       decoder.field_274),
      Field("Sector Bearing (4)",                 r[84:90],       decoder.field_146),
      Field("Sector Minimum Altitude (4)",        r[90:93],       decoder.field_147),
      Field("Sector Radius (5)",                  r[93:97],       decoder.field_274),
      Field("Sector Bearing (5)",                 r[97:103],      decoder.field_146),
      Field("Sector Minimum Altitude (5)",        r[103:106],     decoder.field_147),
      Field("Sector Radius (6)",                  r[106:110],     decoder.field_274),
      Field("Sector Bearing (6)",                 r[110:116],     decoder.field_146),
      Field("Sector Minimum Altitude (6)",        r[116:119],     decoder.field_147),
      Field("File Record No",                     r[123:128],     decoder.field_031),
      Field("Cycle Date",                         r[128:132],     decoder.field_032)
    ]

  # 4.1.31.2 Airport Terminal Arrival Altitude Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                        r[0],           decoder.field_002),
      Field("Customer / Area Code",               r[1:4],         decoder.field_003),
      Field("Section Code",                       r[4]+r[12],     decoder.field_004),
      Field(self.id_name,                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                          r[10:12],       decoder.field_014),
      Field("Approach Identifier",                r[13:19],       decoder.field_010),
      Field("TAA Sector Identifier",              r[19],          decoder.field_272),
      Field("TAA Procedure Turn",                 r[20:24],       decoder.field_271),
      Field("TAA IAF Waypoint",                   r[29:34],       decoder.field_273),
      Field("ICAO Code (2)",                      r[10:12],       decoder.field_014),
      Field("Section Code (2)",                   r[36:38],       decoder.field_004),
      Field("Continuation Record No",             r[38],          decoder.field_016),
      Field("Application Notes",                  r[39],          decoder.field_091),
      Field("Notes",                              r[50:109],      decoder.field_061),
      Field("File Record No",                     r[123:128],     decoder.field_031),
      Field("Cycle Date",                         r[128:132],     decoder.field_032)
    ]