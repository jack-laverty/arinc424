from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.25 Controlled Airspace Records (UC)
#
# The Controlled Airspace Record file contains a
# sequential listing of vertical and lateral limits of all types
# and classifications of Controlled Airspace. It includes
# Controlled Airspace associated with Airports and
# Heliports.
#
class ControlledAirspace():

  cont_idx = 24
  app_idx = 25
  continuations = ['A']
  name = 'Controlled Airspace'

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

  # 4.1.25.1 Controlled Airspace Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("ICAO Code",                           r[6:8],        decoder.field_014),
      Field("Airspace Type",                       r[9],          decoder.field_213),
      Field("Airspace Center",                     r[9:14],       decoder.field_214),
      Field("Section Code (2)",                    r[14:16],      decoder.field_004),
      Field("Airspace Classification",             r[16],         decoder.field_215),
      Field("Multiple Code",                       r[19],         decoder.field_130),
      Field("Sequence Number",                     r[20:24],      decoder.field_012),
      Field("Continuation Record No",              r[24],         decoder.field_016),
      Field("Level",                               r[25],         decoder.field_019),
      Field("Time Code",                           r[26],         decoder.field_131),
      Field("NOTAM",                               r[27],         decoder.field_132),
      Field("Boundary Via",                        r[30:32],      decoder.field_118),
      Field("Latitude",                            r[32:41],      decoder.field_036),
      Field("Longitude",                           r[41:51],      decoder.field_037),
      Field("Arc Origin Latitude",                 r[51:60],      decoder.field_036),
      Field("Arc Origin Longitude",                r[60:70],      decoder.field_037),
      Field("Arc Distance",                        r[70:74],      decoder.field_119),
      Field("Arc Bearing",                         r[74:78],      decoder.field_120),
      Field("RNP",                                 r[78:81],      decoder.field_211),
      Field("Lower Limit",                         r[81:86],      decoder.field_121),
      Field("Unit Indicator",                      r[86],         decoder.field_133),
      Field("Upper Limit",                         r[87:92],      decoder.field_121),
      Field("Unit Indicator (2)",                  r[92],         decoder.field_133),
      Field("Controlled Airspace Name",            r[93:123],     decoder.field_216),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.25.2 Controlled Airspace Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("ICAO Code",                           r[6:8],        decoder.field_014),
      Field("Airspace Type",                       r[9],          decoder.field_213),
      Field("Airspace Center",                     r[9:14],       decoder.field_214),
      Field("Section Code (2)",                    r[14:16],      decoder.field_004),
      Field("Airspace Classification",             r[16],         decoder.field_215),
      Field("Multiple Code",                       r[19],         decoder.field_130),
      Field("Sequence Number",                     r[20:24],      decoder.field_012),
      Field("Continuation Record No",              r[24],         decoder.field_016),
      Field("Application Type",                    r[25],         decoder.field_091),
      Field("Time Code",                           r[26],         decoder.field_131),
      Field("NOTAM",                               r[27],         decoder.field_132),
      Field("Time Indicator",                      r[28],         decoder.field_138),
      Field("Time of Operations",                  r[29:39],      decoder.field_195),
      Field("Time of Operations (2)",              r[39:49],      decoder.field_195),
      Field("Time of Operations (3)",              r[49:59],      decoder.field_195),
      Field("Time of Operations (4)",              r[59:69],      decoder.field_195),
      Field("Time of Operations (5)",              r[69:79],      decoder.field_195),
      Field("Time of Operations (6)",              r[79:89],      decoder.field_195),
      Field("Time of Operations (7)",              r[89:99],      decoder.field_195),
      Field("Controlling Agency",                  r[99:123],     decoder.field_140),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]
