from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.6 Enroute Airways Records (ER)
class EnrouteAirways():

  cont_idx = 38
  app_idx = 39
  continuations = ['A', 'P', 'Q']
  name = 'Enroute Airways'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'A':
        return self.read_cont(line)
      case 'P':
        return self.read_flight_plan0(line)
      case 'Q':
        return self.read_flight_plan1(line)
      case _:
        raise ValueError('Unknown Application Type')

  # 4.1.6.1 Enroute Airways Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[13:18],      decoder.field_008),
      Field("Sequence Number",                         r[25:29],      decoder.field_012),
      Field("Fix Identifier",                          r[29:34],      decoder.field_013),
      Field("ICAO Code",                               r[34:36],      decoder.field_014),
      Field("Section Code (2)",                        r[36:38],      decoder.field_004),
      Field("Continuation Record No",                  r[38],         decoder.field_016),
      Field("Waypoint Desc Code",                      r[39:43],      decoder.field_017),
      Field("Boundary Code",                           r[43],         decoder.field_018),
      Field("Route Type",                              r[44],         decoder.field_007),
      Field("Level",                                   r[45],         decoder.field_019),
      Field("Direction Restriction",                   r[46],         decoder.field_115),
      Field("Cruise Table Indicator",                  r[47:49],      decoder.field_134),
      Field("EU Indicator",                            r[49],         decoder.field_164),
      Field("Recommended NAVAID",                      r[50:54],      decoder.field_023),
      Field("ICAO Code (2)",                           r[54:56],      decoder.field_014),
      Field("RNP",                                     r[56:59],      decoder.field_211),
      Field("Theta",                                   r[62:66],      decoder.field_024),
      Field("Rho",                                     r[66:70],      decoder.field_025),
      Field("Outbound Magnetic Course",                r[70:74],      decoder.field_026),
      Field("Route Distance From",                     r[74:78],      decoder.field_027),
      Field("Inbound Magnetic Course",                 r[78:82],      decoder.field_028),
      Field("Minimum Altitude",                        r[83:88],      decoder.field_030),
      Field("Minimum Altitude (2)",                    r[88:93],      decoder.field_030),
      Field("Maximum Altitude",                        r[93:98],      decoder.field_127),
      Field("Fix Radius Transition Indicator",         r[98:101],     decoder.field_254),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.6.2 Enroute Airways Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[13:18],      decoder.field_008),
      Field("Sequence Number",                         r[25:29],      decoder.field_012),
      Field("Fix Identifier",                          r[29:34],      decoder.field_013),
      Field("ICAO Code",                               r[34:36],      decoder.field_014),
      Field("Section Code (2)",                        r[36:38],      decoder.field_004),
      Field("Continuation Record No",                  r[38],         decoder.field_016),
      Field("Application Type",                        r[39],         decoder.field_091),
      Field("Notes",                                   r[40:109],     decoder.field_061),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.6.3 Enroute Airways Flight Planning Continuation Records
  def read_flight_plan0(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[13:18],      decoder.field_008),
      Field("Sequence Number",                         r[25:29],      decoder.field_012),
      Field("Fix Identifier",                          r[29:34],      decoder.field_013),
      Field("ICAO Code",                               r[34:36],      decoder.field_014),
      Field("Section Code (2)",                        r[36:38],      decoder.field_004),
      Field("Continuation Record No",                  r[38],         decoder.field_016),
      Field("Application Type",                        r[39],         decoder.field_091),
      Field("Start/End Indicator",                     r[40],         decoder.field_152),
      Field("Start/End Date",                          r[41:52],      decoder.field_153),
      Field("Restr. Air ICAO Code",                    r[66:68],      decoder.field_014),
      Field("Restr. Air Type",                         r[68],         decoder.field_128),
      Field("Restr. Air Designation",                  r[69:79],      decoder.field_129),
      Field("Restr. Air Multiple Code",                r[79],         decoder.field_130),
      Field("Restr. Air ICAO Code (2)",                r[80:82],      decoder.field_014),
      Field("Restr. Air Type (2)",                     r[82],         decoder.field_012),
      Field("Restr. Air Designation (2)",              r[83:93],      decoder.field_129),
      Field("Restr. Air Multiple Code (2)",            r[93],         decoder.field_130),
      Field("Restr. Air ICAO Code (3)",                r[94:96],      decoder.field_014),
      Field("Restr. Air Type (3)",                     r[96],         decoder.field_012),
      Field("Restr. Air Designation (3)",              r[97:107],     decoder.field_129),
      Field("Restr. Air Multiple Code (3)",            r[107],        decoder.field_130),
      Field("Restr. Air ICAO Code (4)",                r[108:110],    decoder.field_014),
      Field("Restr. Air Type (4)",                     r[110],        decoder.field_012),
      Field("Restr. Air Designation (4)",              r[111:121],    decoder.field_129),
      Field("Restr. Air Link Continuation",            r[122],        decoder.field_174),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.6.4 Enroute Airways Flight Planning Continuation Records
  def read_flight_plan1(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4:6],        decoder.field_004),
      Field("Route Identifier",                        r[13:18],      decoder.field_008),
      Field("Sequence Number",                         r[25:29],      decoder.field_012),
      Field("Fix Identifier",                          r[29:34],      decoder.field_013),
      Field("ICAO Code",                               r[34:36],      decoder.field_014),
      Field("Section Code (2)",                        r[36:38],      decoder.field_004),
      Field("Continuation Record No",                  r[38],         decoder.field_016),
      Field("Waypoint Desc Code",                      r[39:43],      decoder.field_017),
      Field("Boundary Code",                           r[43],         decoder.field_018),
      Field("Route Type",                              r[44],         decoder.field_007),
      Field("Level",                                   r[45],         decoder.field_019),
      Field("Direction Restriction",                   r[46],         decoder.field_115),
      Field("Cruise Table Indicator",                  r[47:49],      decoder.field_134),
      Field("EU Indicator",                            r[49],         decoder.field_164),
      Field("Recommended NAVAID",                      r[50:54],      decoder.field_023),
      Field("ICAO Code (2)",                           r[54:56],      decoder.field_014),
      Field("RNP",                                     r[56:59],      decoder.field_211),
      Field("Theta",                                   r[62:66],      decoder.field_024),
      Field("Rho",                                     r[66:70],      decoder.field_025),
      Field("Outbound Magnetic Course",                r[70:74],      decoder.field_026),
      Field("Route Distance From",                     r[74:78],      decoder.field_027),
      Field("Inbound Magnetic Course",                 r[78:82],      decoder.field_028),
      Field("Minimum Altitude",                        r[83:88],      decoder.field_030),
      Field("Minimum Altitude (2)",                    r[88:93],      decoder.field_030),
      Field("Maximum Altitude",                        r[93:98],      decoder.field_127),
      Field("Fix Radius Transition Indicator",         r[98:101],     decoder.field_254),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]