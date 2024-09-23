from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.27 Flight Planning Arrival/Departure Data Records (PR)
class FlightPlanning():

  cont_idx = 69
  app_idx = 70
  continuations = ['A', 'T']
  name = 'Flight Planning Arrival/Departure'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'A':
        return self.read_cont(line)
      case 'T':
        return self.read_timeop(line)
      case _:
        return []

  # 4.1.27.1 Flight Planning Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                            r[0],           decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
      Field("Section Code",                           r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                     r[6:10],        decoder.field_006),
      Field("ICAO Code",                              r[10:12],       decoder.field_014),
      Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_009),
      Field("Procedure Type",                         r[19],          decoder.field_230),
      Field("Runway Transition Identifier",           r[20:25],       decoder.field_011),
      Field("Runway Transition Fix",                  r[25:30],       decoder.field_013),
      Field("ICAO Code (2)",                          r[30:32],       decoder.field_014),
      Field("Section Code (2)",                       r[32:34],       decoder.field_004),
      Field("Runway Transition Along Track Dist",     r[34:37],       decoder.field_231),
      Field("Common Segment Transition Fix",          r[37:42],       decoder.field_013),
      Field("ICAO Code (3)",                          r[42:44],       decoder.field_014),
      Field("Section Code (3)",                       r[44:46],       decoder.field_004),
      Field("Common Segment Along Track Dist",        r[46:49],       decoder.field_231),
      Field("Enroute Transition Identifier",          r[49:54],       decoder.field_011),
      Field("Enroute Transition Fix",                 r[54:59],       decoder.field_013),
      Field("ICAO Code (4)",                          r[59:61],       decoder.field_014),
      Field("Section Code (4)",                       r[61:63],       decoder.field_004),
      Field("Enroute Transition Along Track Dist",    r[63:66],       decoder.field_231),
      Field("Sequence Number",                        r[66:69],       decoder.field_012),
      Field("Continuation Number",                    r[69],          decoder.field_016),
      Field("Number of Engines",                      r[70:74],       decoder.field_232),
      Field("Turboprop/Jet Indicator",                r[74],          decoder.field_233),
      Field("RNAV Flag",                              r[75],          decoder.field_234),
      Field("ATC Weight Category",                    r[76],          decoder.field_235),
      Field("ATC Identifier",                         r[77:84],       decoder.field_236),
      Field("Time Code",                              r[84],          decoder.field_131),
      Field("Procedure Description",                  r[85:100],      decoder.field_237),
      Field("Leg Type Code",                          r[100:102],     decoder.field_238),
      Field("Reporting Code",                         r[102],         decoder.field_239),
      Field("Initial Departure Magnetic Course",      r[103:107],     decoder.field_026),
      Field("Altitude Description",                   r[107],         decoder.field_029),
      Field("Altitude",                               r[108:111],     decoder.field_240),
      Field("Altitude (2)",                           r[111:114],     decoder.field_240),
      Field("Speed Limit",                            r[114:117],     decoder.field_072),
      Field("Initial Cruise Table",                   r[117:119],     decoder.field_134),
      Field("Speed Limit Description",                r[119],         decoder.field_261),
      Field("File Record No",                         r[123:128],     decoder.field_031),
      Field("Cycle Date",                             r[128:132],     decoder.field_032)
    ]

  # 4.1.27.2 Flight Planning Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                            r[0],           decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
      Field("Section Code",                           r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                     r[6:10],        decoder.field_006),
      Field("ICAO Code",                              r[10:12],       decoder.field_014),
      Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_009),
      Field("Procedure Type",                         r[19],          decoder.field_230),
      Field("Runway Transition Identifier",           r[20:25],       decoder.field_011),
      Field("Runway Transition Fix",                  r[25:30],       decoder.field_013),
      Field("ICAO Code (2)",                          r[30:32],       decoder.field_014),
      Field("Section Code (2)",                       r[32:34],       decoder.field_004),
      Field("Runway Transition Along Track Dist",     r[34:37],       decoder.field_231),
      Field("Common Segment Transition Fix",          r[37:42],       decoder.field_013),
      Field("ICAO Code (3)",                          r[42:44],       decoder.field_014),
      Field("Section Code (3)",                       r[44:46],       decoder.field_004),
      Field("Common Segment Along Track Dist",        r[46:49],       decoder.field_231),
      Field("Enroute Transition Identifier",          r[49:54],       decoder.field_011),
      Field("Enroute Transition Fix",                 r[54:59],       decoder.field_013),
      Field("ICAO Code (4)",                          r[59:61],       decoder.field_014),
      Field("Section Code (4)",                       r[61:63],       decoder.field_004),
      Field("Enroute Transition Along Track Dist",    r[63:66],       decoder.field_231),
      Field("Sequence Number",                        r[66:69],       decoder.field_012),
      Field("Continuation Number",                    r[69],          decoder.field_016),
      Field("Application Type",                       r[70],          decoder.field_091),
      Field("Intermediate Fix Identifier",            r[71:76],       decoder.field_013),
      Field("ICAO Code (5)",                          r[76:78],       decoder.field_014),
      Field("Section Code (5)",                       r[91:93],       decoder.field_004),
      Field("Intermediate Distance",                  r[106:109],     decoder.field_231),
      Field("Fix Related Transition Code",            r[109],         decoder.field_241),
      Field("Intermediate Fix Identifier",            r[110:115],     decoder.field_013),
      Field("ICAO Code (6)",                          r[115:117],     decoder.field_014),
      Field("Section Code (6)",                       r[118],         decoder.field_004),
      Field("Intermediate Distance",                  r[119:122],     decoder.field_231),
      Field("Fix Related Transition Code",            r[122],         decoder.field_241),
      Field("File Record No",                         r[123:128],     decoder.field_031),
      Field("Cycle Date",                             r[128:132],     decoder.field_032)
    ]

  # 4.1.27.3 Flight Planning Continuation Records
  def read_timeop(self, r):
    return [
      Field("Record Type",                            r[0],           decoder.field_002),
      Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
      Field("Section Code",                           r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                     r[6:10],        decoder.field_006),
      Field("ICAO Code",                              r[10:12],       decoder.field_014),
      Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_009),
      Field("Procedure Type",                         r[19],          decoder.field_230),
      Field("Runway Transition Identifier",           r[20:25],       decoder.field_011),
      Field("Runway Transition Fix",                  r[25:30],       decoder.field_013),
      Field("ICAO Code (2)",                          r[30:32],       decoder.field_014),
      Field("Section Code (2)",                       r[32:34],       decoder.field_004),
      Field("Runway Transition Along Track Dist",     r[34:37],       decoder.field_231),
      Field("Common Segment Transition Fix",          r[37:42],       decoder.field_013),
      Field("ICAO Code (3)",                          r[42:44],       decoder.field_014),
      Field("Section Code (3)",                       r[44:46],       decoder.field_004),
      Field("Common Segment Along Track Dist",        r[46:49],       decoder.field_231),
      Field("Enroute Transition Identifier",          r[49:54],       decoder.field_011),
      Field("Enroute Transition Fix",                 r[54:59],       decoder.field_013),
      Field("ICAO Code (4)",                          r[59:61],       decoder.field_014),
      Field("Section Code (4)",                       r[61:63],       decoder.field_004),
      Field("Enroute Transition Along Track Dist",    r[63:66],       decoder.field_231),
      Field("Sequence Number",                        r[66:69],       decoder.field_012),
      Field("Continuation Number",                    r[69],          decoder.field_016),
      Field("Application Type",                       r[70],          decoder.field_091),
      Field("Time Code",                              r[71],          decoder.field_131),
      Field("Time Indicator",                         r[72],          decoder.field_138),
      Field("Time of Operation",                      r[73:83],       decoder.field_195),
      Field("Time of Operation (1)",                  r[83:93],       decoder.field_195),
      Field("Time of Operation (2)",                  r[93:103],      decoder.field_195),
      Field("Time of Operation (3)",                  r[103:113],     decoder.field_195),
      Field("Time of Operation (4)",                  r[113:123],     decoder.field_195),
      Field("File Record No",                         r[123:128],     decoder.field_031),
      Field("Cycle Date",                             r[128:132],     decoder.field_032)
    ]