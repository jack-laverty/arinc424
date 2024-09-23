from arinc424.decoder import Field
import arinc424.decoder as decoder

# 4.1.9  Airport SID/STAR/Approach (PD, PE and PF)
# 4.2.3  Heliport SID/STAR/Approach (HD/HE/HF)
class SIDSTARApproach():

  cont_idx = 38
  app_idx = 39
  continuations = ['E', 'P', 'W']
  name = 'SID/STAR/Approach'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'E':
        return self.read_ext(line)
      case 'P':
        return self.read_flight0(line)
      case 'W':
        return self.read_data(line)
      case _:
        return []

  # 4.1.9.1 Airport SID/STAR/Approach Primary Records
  # 4.2.3.1 Heliport SID/STAR/Approach Primary Records 
  def read_primary(self, r):
    return [
      Field("Record Type",                                r[0],           decoder.field_002),
      Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
      Field("Section Code",                               r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                                  r[10:12],       decoder.field_014),
      Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
      Field("Route Type",                                 r[19],          decoder.field_007),
      Field("Transition Identifier",                      r[20:25],       decoder.field_011),
      Field("Sequence Number",                            r[26:29],       decoder.field_012),
      Field("Fix Identifier",                             r[29:34],       decoder.field_013),
      Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
      Field("Section Code (2)",                           r[36:38],       decoder.field_004),
      Field("Continuation Record No",                     r[38],          decoder.field_016),
      Field("Waypoint Description Code",                  r[39:43],       decoder.field_017),
      Field("Turn Direction",                             r[43],          decoder.field_020),
      Field("RNP",                                        r[44:47],       decoder.field_211),
      Field("Path and Termination",                       r[47:49],       decoder.field_021),
      Field("Turn Direction Valid",                       r[49],          decoder.field_022),
      Field("Recommended Navaid",                         r[50:54],       decoder.field_023),
      Field("ICAO Code (3)",                              r[54:56],       decoder.field_014),
      Field("Arc Radius",                                 r[56:62],       decoder.field_204),
      Field("Theta",                                      r[62:66],       decoder.field_024),
      Field("Rho",                                        r[66:70],       decoder.field_025),
      Field("Magnetic Course",                            r[70:74],       decoder.field_026),
      Field("Route / Holding Distance or Time",           r[74:78],       decoder.field_027),
      Field("Recommended Navaid (2)",                     r[78:80],       decoder.field_004),
      Field("Altitude Description",                       r[82],          decoder.field_029),
      Field("ATC Indicator",                              r[83],          decoder.field_081),
      Field("Altitude",                                   r[84:89],       decoder.field_030),
      Field("Altitude (2)",                               r[89:94],       decoder.field_030),
      Field("Transition Altitude",                        r[94:99],       decoder.field_053),
      Field("Speed Limit",                                r[99:102],      decoder.field_072),
      Field("Vertical Angle",                             r[102:106],     decoder.field_070),
      Field("Center Fix or TAA Procedure Turn Indicator", r[106:111],     decoder.field_144),  # or 271
      Field("Multiple Code or TAA Sector Identifier",     r[111],         decoder.field_130),  # or 272
      Field("ICAO Code (4)",                              r[112:113],     decoder.field_014),
      Field("Section Code (3)",                           r[114:116],     decoder.field_004),
      Field("GNSS/FMS Indication",                        r[116],         decoder.field_222),
      Field("Speed Limit Description",                    r[117],         decoder.field_261),
      Field("Apch Route Qualifier 1",                     r[118],         decoder.field_007),
      Field("Apch Route Qualifier 2",                     r[119],         decoder.field_007),
      Field("File Record No",                             r[123:128],     decoder.field_031),
      Field("Cycle Date",                                 r[128:132],     decoder.field_032)
    ]

  # 4.1.9.2 Airport SID/STAR/ Primary Extension Approach Continuation Records
  # 4.2.3.2 Heliport SID/STAR/Approach Primary Extension Continuation Records
  def read_ext(self, r):
    return [
      Field("Record Type",                                r[0],           decoder.field_002),
      Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
      Field("Section Code",                               r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                                  r[10:12],       decoder.field_014),
      Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
      Field("Route Type",                                 r[19],          decoder.field_007),
      Field("Transition Identifier",                      r[20:25],       decoder.field_011),
      Field("Sequence Number",                            r[26:29],       decoder.field_012),
      Field("Fix Identifier",                             r[29:34],       decoder.field_013),
      Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
      Field("Section Code (2)",                           r[36:38],       decoder.field_004),
      Field("Continuation Record No",                     r[38],          decoder.field_016),
      Field("Application Type",                           r[39],          decoder.field_091),
      Field("CAT A Decision Height",                      r[40:44],       decoder.field_170),
      Field("CAT B Decision Height",                      r[44:48],       decoder.field_170),
      Field("CAT C Decision Height",                      r[48:52],       decoder.field_170),
      Field("CAT D Decision Height",                      r[52:56],       decoder.field_170),
      Field("CAT A Minimum Descent Altitude",             r[56:60],       decoder.field_171),
      Field("CAT B Minimum Descent Altitude",             r[60:64],       decoder.field_171),
      Field("CAT C Minimum Descent Altitude",             r[64:68],       decoder.field_171),
      Field("CAT D Minimum Descent Altitude",             r[68:72],       decoder.field_171),
      Field("Procedure TCH",                              r[72:75],       decoder.field_067),
      Field("Localizer Only Altitude Desc",               r[75],          decoder.field_029),
      Field("Localizer Only Altitude",                    r[76:81],       decoder.field_030),
      Field("Localizer Only Vertical Angle",              r[81:85],       decoder.field_070),
      Field("RNP",                                        r[89:92],       decoder.field_211),
      Field("Apch Route Qualifier 1",                     r[118],         decoder.field_007),
      Field("Apch Route Qualifier 2",                     r[119],         decoder.field_007),
      Field("File Record No",                             r[123:128],     decoder.field_031),
      Field("Cycle Date",                                 r[128:132],     decoder.field_032)
    ]

  # 4.1.9.3 Airport SID/STAR/Approach Flight Planning Continuation Records
  # 4.2.3.3 Heliport SID/STAR/Approach Flight Planning Continuation Records
  def read_flight0(self, r):
    return [
      Field("Record Type",                                r[0],           decoder.field_002),
      Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
      Field("Section Code",                               r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                                  r[10:12],       decoder.field_014),
      Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
      Field("Route Type",                                 r[19],          decoder.field_007),
      Field("Transition Identifier",                      r[20:25],       decoder.field_011),
      Field("Sequence Number",                            r[26:29],       decoder.field_012),
      Field("Fix Identifier",                             r[29:34],       decoder.field_013),
      Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
      Field("Section Code (2)",                           r[36:38],       decoder.field_004),
      Field("Continuation Record No",                     r[38],          decoder.field_016),
      Field("Application Type",                           r[39],          decoder.field_091),
      Field("Start/End Indicator",                        r[40],          decoder.field_152),
      Field("Start/End Date",                             r[41:45],       decoder.field_153),
      Field("Leg Distance",                               r[74:78],       decoder.field_260),
      Field("File Record No",                             r[123:128],     decoder.field_031),
      Field("Cycle Date",                                 r[128:132],     decoder.field_032)
    ]

  # 4.1.9.5 Airport Procedure Data Continuation Record
  # 4.2.3.5 Heliport Procedure Data Continuation Record
  def read_data(self, r):
    return [
      Field("Record Type",                                r[0],           decoder.field_002),
      Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
      Field("Section Code",                               r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                         r[6:10],        decoder.field_006),
      Field("ICAO Code",                                  r[10:12],       decoder.field_014),
      Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
      Field("Route Type",                                 r[19],          decoder.field_007),
      Field("Transition Identifier",                      r[20:25],       decoder.field_011),
      Field("Sequence Number",                            r[26:29],       decoder.field_012),
      Field("Fix Identifier",                             r[29:34],       decoder.field_013),
      Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
      Field("Section Code (2)",                           r[36:38],       decoder.field_004),
      Field("Continuation Record No",                     r[38],          decoder.field_016),
      Field("Application Type",                           r[39],          decoder.field_091),
      Field("FAS Block Provided",                         r[40],          decoder.field_276),
      Field("FAS Block Provided Level of Service Name",   r[41:51],       decoder.field_275),
      Field("LNAV/VNAV Authorized for SBAS",              r[51],          decoder.field_276),
      Field("LNAV/VNAV Level of Service Name",            r[52:62],       decoder.field_275),
      Field("LNAV Authorized for SBAS",                   r[62],          decoder.field_276),
      Field("LNAV Level of Service Name",                 r[63:73],       decoder.field_275),
      Field("Apch Route Qualifier 1",                     r[118],         decoder.field_007),
      Field("Apch Route Qualifier 2",                     r[119],         decoder.field_007),
      Field("File Record No",                             r[123:128],     decoder.field_031),
      Field("Cycle Date",                                 r[128:132],     decoder.field_032)
    ]