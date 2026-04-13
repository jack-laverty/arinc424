from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.21 Enroute Airways Restriction Records (EU)
class EnrouteAirwaysRestriction():

  continuations = ['AE', 'TC', 'NR']
  name = 'Enroute Airways'

  def application_type(self, line):
    return line[15:17]

  def read(self, line, primary) -> list:

    application = self.application_type(line)

    if primary:
      match application:
        case 'AE':
          return self.primary_altitude_exclude(line)
        case 'TC':
          return self.primary_cruise_table(line)
        case 'SC':
          return self.primary_seasonal_closure(line)
        case 'NR':
          return self.primary_note_restriction(line)
        case _:
          raise ValueError("Unknown Restricted Airway Type")
    else:
      match application:
        case 'AE':
          return self.cont_altitude_exclude(line)
        case 'TC':
          return self.cont_cruise_table(line)
        case 'NR':
          return self.cont_note_restriction(line)
        case _:
          raise ValueError("Unknown Restricted Airway Type")

  # 4.1.21.1 Enroute Airways Restriction Altitude Exclusion Primary Records
  #
  # Note 1: The standard length for the Route Identifier is
  # five characters. Some users envisage the need for
  # a six-character field. This reserved column will
  # permit this usage.
  #
  def primary_altitude_exclude(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[6:11],       decoder.field_008),
      Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
      Field("Restriction Type",                        r[15:17],      decoder.field_201),
      Field("Continuation Record No",                  r[17],         decoder.field_016),
      Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
      Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
      Field("Start Fix Section Code",                  r[25:27],      decoder.field_004),
      Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
      Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
      Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
      Field("Start Date",                              r[37:44],      decoder.field_157),
      Field("End Date",                                r[44:51],      decoder.field_157),
      Field("Time Code",                               r[51],         decoder.field_131),
      Field("Time Indicator",                          r[52],         decoder.field_138),
      Field("Time of Operation",                       r[53:63],      decoder.field_195),
      Field("Time of Operation",                       r[63:73],      decoder.field_195),
      Field("Time of Operation",                       r[73:83],      decoder.field_195),
      Field("Time of Operation",                       r[83:93],      decoder.field_195),
      Field("Exclusion Indicator",                     r[93],         decoder.field_202),
      Field("Units of Altitude",                       r[94],         decoder.field_160),
      Field("Restriction Altitude",                    r[95:98],      decoder.field_161),
      Field("Block Indicator",                         r[98],         decoder.field_203),
      Field("Restriction Altitude",                    r[99:102],     decoder.field_161),
      Field("Block Indicator",                         r[102],        decoder.field_203),
      Field("Restriction Altitude",                    r[103:106],    decoder.field_161),
      Field("Block Indicator",                         r[106],        decoder.field_203),
      Field("Restriction Altitude",                    r[107:110],    decoder.field_161),
      Field("Block Indicator",                         r[110],        decoder.field_203),
      Field("Restriction Altitude",                    r[111:114],    decoder.field_161),
      Field("Block Indicator",                         r[114],        decoder.field_203),
      Field("Restriction Altitude",                    r[115:118],    decoder.field_161),
      Field("Block Indicator",                         r[118],        decoder.field_203),
      Field("Restriction Altitude",                    r[119:122],    decoder.field_161),
      Field("Block Indicator",                         r[122],        decoder.field_203),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  def cont_altitude_exclude(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[6:11],       decoder.field_008),
      Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
      Field("Restriction Type",                        r[15:17],      decoder.field_201),
      Field("Continuation Record No",                  r[17],         decoder.field_016),
      Field("Application Type",                        r[18],         decoder.field_091),
      Field("Time Code",                               r[51],         decoder.field_131),
      Field("Time Indicator",                          r[52],         decoder.field_138),
      Field("Time of Operation",                       r[53:63],      decoder.field_195),
      Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
      Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
      Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
      Field("Exclusion Operator",                      r[93],         decoder.field_202),
      Field("Units of Altitude",                       r[94],         decoder.field_160),
      Field("Restriction Altitude",                    r[95:98],      decoder.field_161),
      Field("Block Indicator",                         r[98],         decoder.field_203),
      Field("Restriction Altitude (2)",                r[99:102],     decoder.field_161),
      Field("Block Indicator (2)",                     r[102],        decoder.field_203),
      Field("Restriction Altitude (3)",                r[103:106],    decoder.field_161),
      Field("Block Indicator (3)",                     r[106],        decoder.field_203),
      Field("Restriction Altitude (4)",                r[107:110],    decoder.field_161),
      Field("Block Indicator (4)",                     r[110],        decoder.field_203),
      Field("Restriction Altitude (5)",                r[111:114],    decoder.field_161),
      Field("Block Indicator (5)",                     r[114],        decoder.field_203),
      Field("Restriction Altitude (6)",                r[115:118],    decoder.field_161),
      Field("Block Indicator (6)",                     r[118],        decoder.field_203),
      Field("Restriction Altitude (7)",                r[119:122],    decoder.field_161),
      Field("Block Indicator (7)",                     r[122],        decoder.field_203),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.21A.1 Enroute Airways Restriction Note Restriction Primary Records
  #
  # Note 1: The standard length for the Route Identifier is
  # five characters. Some users envisage the need
  # for a six-character field. This reserved column
  # will permit this usage.
  #
  def primary_note_restriction(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[7:11],       decoder.field_008),
      Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
      Field("Restriction Type",                        r[15:17],      decoder.field_201),
      Field("Continuation Record No",                  r[17],         decoder.field_016),
      Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
      Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
      Field("Start Fix Section Code",                  r[25],         decoder.field_004),
      Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
      Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
      Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
      Field("Start Date",                              r[37:44],      decoder.field_157),
      Field("End Date",                                r[44:51],      decoder.field_157),
      Field("Restriction Notes",                       r[51:120],     decoder.field_163),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.21A.2 Enroute Airways Restriction Note Restriction Continuation Records
  def cont_note_restriction(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[7:11],       decoder.field_008),
      Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
      Field("Restriction Type",                        r[15:17],      decoder.field_201),
      Field("Continuation Record No",                  r[17],         decoder.field_016),
      Field("Application Type",                        r[18],         decoder.field_091),
      Field("Restriction Notes",                       r[51:120],     decoder.field_163),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.21B.1 Enroute Airways Restriction Seasonal Closure Primary Records
  #
  # Note 1: The standard length for the Route Identifier is
  # five characters. Some users envisage the need for
  # a six-character field. This reserved column will
  # permit this usage.
  #
  def primary_seasonal_closure(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[6:11],       decoder.field_008),
      Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
      Field("Restriction Type",                        r[15:17],      decoder.field_201),
      Field("Continuation Record No",                  r[17],         decoder.field_016),
      Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
      Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
      Field("Start Fix Section Code",                  r[25:27],      decoder.field_004),
      Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
      Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
      Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
      Field("Start Date",                              r[37:44],      decoder.field_157),
      Field("End Date",                                r[44:51],      decoder.field_157),
      Field("Time Code",                               r[51],         decoder.field_131),
      Field("Time Indicator",                          r[52],         decoder.field_138),
      Field("Time of Operation",                       r[53:63],      decoder.field_195),
      Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
      Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
      Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
      Field("Cruise Table Ident",                      r[93:95],      decoder.field_134),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.21C.1 Enroute Airways Restriction Cruising Table Replacement Primary Records
  #
  # Note 1: The standard length for the Route Identifier is
  # five characters. Some users envisage the need for
  # a six-character field. This reserved column will
  # permit this usage.
  #
  def primary_cruise_table(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[6:11],       decoder.field_008),
      Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
      Field("Restriction Type",                        r[15:17],      decoder.field_201),
      Field("Continuation Record No",                  r[17],         decoder.field_016),
      Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
      Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
      Field("Start Fix Section Code",                  r[25:27],      decoder.field_004),
      Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
      Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
      Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
      Field("Start Date",                              r[37:44],      decoder.field_157),
      Field("End Date",                                r[44:51],      decoder.field_157),
      Field("Time Code",                               r[51],         decoder.field_131),
      Field("Time Indicator",                          r[52],         decoder.field_138),
      Field("Time of Operation",                       r[53:63],      decoder.field_195),
      Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
      Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
      Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
      Field("Cruise Table Ident",                      r[93:95],      decoder.field_134),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.21C.2 Enroute Airways Restriction Cruising Table Replacement Continuation Records
  def cont_cruise_table(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[6:11],       decoder.field_008),
      Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
      Field("Restriction Type",                        r[15:17],      decoder.field_201),
      Field("Continuation Record No",                  r[17],         decoder.field_016),
      Field("Application Type",                        r[18],         decoder.field_091),
      Field("Time Code",                               r[51],         decoder.field_131),
      Field("Time Indicator",                          r[52],         decoder.field_138),
      Field("Time of Operation",                       r[53:63],      decoder.field_195),
      Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
      Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
      Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
      Field("Cruise Table Ident",                      r[93:95],      decoder.field_134),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]