from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.11 Airport and Heliport Localizer and Glide Slope
class LocalizerGlideslope():

  cont_idx = 21
  app_idx = 22
  continuations = ['A', 'S']
  name = 'Localizer and Glide Slope'

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

  # 4.1.11.1  Airport and Heliport Localizer and Glide Slope Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                                r[0],          decoder.field_002),
      Field("Customer / Area Code",                       r[1:4],        decoder.field_003),
      Field("Section Code",                               r[4]+r[12],    decoder.field_004),
      Field("Airport Identifier",                         r[6:10],       decoder.field_006),
      Field("ICAO Code",                                  r[10:12],      decoder.field_014),
      Field("Localizer Identifier",                       r[13:17],      decoder.field_044),
      Field("ILS Category",                               r[17],         decoder.field_080),
      Field("Continuation Record No",                     r[21],         decoder.field_016),
      Field("Localizer Frequency",                        r[22:27],      decoder.field_045),
      Field("Runway Identifier",                          r[27:32],      decoder.field_046),
      Field("Localizer Latitude",                         r[32:41],      decoder.field_036),
      Field("Localizer Longitude",                        r[41:51],      decoder.field_037),
      Field("Localizer Bearing",                          r[51:55],      decoder.field_047),
      Field("Glide Slope Latitude",                       r[55:64],      decoder.field_036),
      Field("Glide Slope Longitude",                      r[64:74],      decoder.field_037),
      Field("Localizer Position",                         r[74:78],      decoder.field_048),
      Field("Localizer Position Reference",               r[78],         decoder.field_049),
      Field("Glide Slope Position",                       r[79:83],      decoder.field_050),
      Field("Localizer Width",                            r[83:87],      decoder.field_051),
      Field("Glide Slope Angle",                          r[87:90],      decoder.field_052),
      Field("Station Declination",                        r[90:95],      decoder.field_066),
      Field("Glide Slope Height at Landing Threshold",    r[95:97],      decoder.field_067),
      Field("Glide Slope Elevation",                      r[97:102],     decoder.field_074),
      Field("Supporting Facility ID Note 1",              r[102:106],    decoder.field_033),
      Field("Supporting Facility ICAO Code Note 1",       r[106:108],    decoder.field_014),
      Field("Supporting Facility Section Code Note 1",    r[108:110],    decoder.field_004),
      Field("File Record No",                             r[123:128],    decoder.field_031),
      Field("Cycle Date",                                 r[128:132],    decoder.field_032)
    ]

  # 4.1.11.2  Airport  and  Heliport  Localizer  and  Glide  Slope Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                                r[0],           decoder.field_002),
      Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
      Field("Section Code",                               r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                                  r[10:12],       decoder.field_014),
      Field("Localizer Identifier",                       r[13:17],       decoder.field_044),
      Field("ILS Category",                               r[17],          decoder.field_080),
      Field("Continuation Record No",                     r[21],          decoder.field_016),
      Field("Notes",                                      r[23:92],       decoder.field_061),
      Field("File Record No",                             r[123:128],     decoder.field_031),
      Field("Cycle Date",                                 r[128:132],     decoder.field_032)
    ]

  # 4.1.11.3  Airport  and  Heliport  Localizer  and  Glide  Slope Simulation Continuation Records
  def read_sim(self, r):
    return [
      Field("Record Type",                                r[0],           decoder.field_002),
      Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
      Field("Section Code",                               r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                                  r[10:12],       decoder.field_014),
      Field("Localizer Identifier",                       r[13:17],       decoder.field_044),
      Field("ILS Category",                               r[17],          decoder.field_080),
      Field("Continuation Record No",                     r[21],          decoder.field_016),
      Field("Application Type",                           r[22],          decoder.field_091),

      Field("Facility Characteristics",                   r[27:32],       decoder.field_093),
      Field("Localizer True Bearing",                     r[51:56],       decoder.field_094),
      Field("Localizer Bearing Source",                   r[56],          decoder.field_095),
      Field("Glide Slope Beam Width",                     r[87:90],       decoder.field_096),
      Field("Approach Route Ident",                       r[90:96],       decoder.field_010),
      Field("Approach Route Ident (2)",                   r[96:102],      decoder.field_010),
      Field("Approach Route Ident (3)",                   r[102:108],     decoder.field_010),
      Field("Approach Route Ident (4)",                   r[108:114],     decoder.field_010),
      Field("Approach Route Ident (5)",                   r[114:120],     decoder.field_010),
      Field("File Record No",                             r[123:128],     decoder.field_031),
      Field("Cycle Date",                                 r[128:132],     decoder.field_032),
    ]