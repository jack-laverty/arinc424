from arinc424.decoder import Field
import arinc424.decoder as decoder


class MSA():

  cont_idx = 38
  app_idx = 39
  continuations = ['A']
  name = 'MSA'

  def application_type(self, line):
    return line[self.app_idx]

  def __init__(self, heliport) -> None:
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

  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field(self.id_name,                          r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("MSA Center",                          r[13:17],      decoder.field_144),
      Field("ICAO Code (2)",                       r[18:20],      decoder.field_014),
      Field("Section Code (2)",                    r[20:22],      decoder.field_004),
      Field("Multiple Code",                       r[22],         decoder.field_130),
      Field("Continuation Record No",              r[38],         decoder.field_016),
      Field("Sector Bearing",                      r[42:48],      decoder.field_146),
      Field("Sector Altitude",                     r[48:51],      decoder.field_147),
      Field("Sector Radius",                       r[51:53],      decoder.field_145),
      Field("Sector Bearing (2)",                  r[53:59],      decoder.field_146),
      Field("Sector Altitude (2)",                 r[59:62],      decoder.field_147),
      Field("Sector Radius (2)",                   r[62:64],      decoder.field_145),
      Field("Sector Bearing (3)",                  r[64:70],      decoder.field_146),
      Field("Sector Altitude (3)",                 r[70:73],      decoder.field_147),
      Field("Sector Radius (3)",                   r[73:75],      decoder.field_145),
      Field("Sector Bearing (4)",                  r[75:81],      decoder.field_146),
      Field("Sector Altitude (4)",                 r[81:84],      decoder.field_147),
      Field("Sector Radius (4)",                   r[84:86],      decoder.field_145),
      Field("Sector Bearing (5)",                  r[86:92],      decoder.field_146),
      Field("Sector Altitude (5)",                 r[92:95],      decoder.field_147),
      Field("Sector Radius (5)",                   r[95:97],      decoder.field_145),
      Field("Sector Bearing (6)",                  r[97:103],     decoder.field_146),
      Field("Sector Altitude (6)",                 r[103:106],    decoder.field_147),
      Field("Sector Radius (6)",                   r[106:108],    decoder.field_145),
      Field("Sector Bearing (7)",                  r[108:114],    decoder.field_146),
      Field("Sector Altitude (7)",                 r[114:117],    decoder.field_147),
      Field("Sector Radius (7)",                   r[117:119],    decoder.field_145),
      Field("Magnetic/True Bearing",               r[119],        decoder.field_165),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field(self.id_name,                          r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("MSA Center",                          r[13:17],      decoder.field_144),
      Field("ICAO Code (2)",                       r[18:20],      decoder.field_014),
      Field("Section Code (2)",                    r[20:22],      decoder.field_004),
      Field("Multiple Code",                       r[22],         decoder.field_130),
      Field("Continuation Record No",              r[38],         decoder.field_016),
      Field("Application Type",                    r[39],         decoder.field_091),
      Field("Notes",                               r[40:109],     decoder.field_061),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]