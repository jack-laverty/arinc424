from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.2.2 Heliport Terminal Waypoint Records (HC)
class HeliportTerminalWaypoint():

  cont_idx = 21
  app_idx = 22
  continuations = ['A', 'P']
  name = 'Heliport Terminal Waypoint'

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
        return self.read_flight0(line)
      case _:
        # TODO: sketchy
        return self.read_flight1(line)

  # 4.2.2.1 Heliport Terminal Waypoint Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
      Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Waypoint Type",                       r[26:29],      decoder.field_042),
      Field("Waypoint Usage",                      r[29:31],      decoder.field_082),
      Field("Waypoint Latitude",                   r[32:41],      decoder.field_036),
      Field("Waypoint Longitude",                  r[41:51],      decoder.field_037),
      Field("Dynamic Magnetic Variation",          r[74:79],      decoder.field_039),
      Field("Datum Code",                          r[84:87],      decoder.field_197),
      Field("Name Format Indicator",               r[95:98],      decoder.field_196),
      Field("Waypoint Name/Description",           r[98:123],     decoder.field_043),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.2.2.2 Heliport Terminal Waypoint Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
      Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("Notes",                               r[23:92],      decoder.field_061),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.2.2.3 Heliport Terminal Waypoint Flight Planning Continuation Records
  def read_flight0(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
      Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("FIR Identifier",                      r[23:27],      decoder.field_116),
      Field("UIR Identifier",                      r[27:31],      decoder.field_116),
      Field("Start/End Indicator",                 r[31],         decoder.field_152),
      Field("Start/End Date",                      r[32:43],      decoder.field_153),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.2.2.4 Heliport Terminal Waypoint Flight Planning Continuation Records
  def read_flight1(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
      Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Waypoint Type",                       r[26:29],      decoder.field_042),
      Field("Waypoint Usage",                      r[29:31],      decoder.field_082),
      Field("Waypoint Latitude",                   r[32:41],      decoder.field_036),
      Field("Waypoint Longitude",                  r[41:51],      decoder.field_037),
      Field("Dynamic Magnetic Variation",          r[74:79],      decoder.field_039),
      Field("Datum Code",                          r[84:87],      decoder.field_197),
      Field("Name Format Indicator",               r[95:98],      decoder.field_196),
      Field("Waypoint Name/Description",           r[98:123],     decoder.field_043),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]