from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.3  NDB NAVAID Record (DB or PN)
class NDBNavaid():

  cont_idx = 21
  app_idx = 22
  continuations = ['A', 'P', 'Q', 'S']
  name = 'NDB Navaid'

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
      case 'S':
        return self.read_sim(line)
      case _:
        return []

  # 4.1.3.1  NDB NAVAID Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                     r[0],         decoder.field_002),
      Field("Customer / Area Code",            r[1:4],       decoder.field_003),
      Field("Section Code",                    r[4:6],       decoder.field_004),
      Field("Airport ICAO Identifier",         r[6:10],      decoder.field_006),
      Field("ICAO Code",                       r[10:12],     decoder.field_014),
      Field("NDB Identifier",                  r[13:17],     decoder.field_033),
      Field("ICAO Code (2)",                   r[19:21],     decoder.field_014),
      Field("Continuation Record No",          r[21],        decoder.field_016),
      Field("NDB Frequency",                   r[22:27],     decoder.field_034),
      Field("NDB Class",                       r[27:31],     decoder.field_035),
      Field("NDB Latitude",                    r[32:41],     decoder.field_036),
      Field("NDB Longitude",                   r[41:51],     decoder.field_037),
      Field("Magnetic Variation",              r[74:79],     decoder.field_039),
      Field("Datum Code",                      r[90:93],     decoder.field_197),
      Field("NDB Name",                        r[93:123],    decoder.field_071),
      Field("File Record No",                  r[123:128],   decoder.field_031),
      Field("Cycle Date",                      r[128:132],   decoder.field_032)
    ]

  # 4.1.3.2  NDB NAVAID Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                     r[0],         decoder.field_002),
      Field("Customer / Area Code",            r[1:4],       decoder.field_003),
      Field("Section Code",                    r[4:6],       decoder.field_004),
      Field("Airport ICAO Identifier",         r[6:10],      decoder.field_006),
      Field("ICAO Code",                       r[10:12],     decoder.field_014),
      Field("NDB Identifier",                  r[13:17],     decoder.field_033),
      Field("ICAO Code (2)",                   r[19:21],     decoder.field_014),
      Field("Continuation Record No",          r[21],        decoder.field_016),
      Field("Application Type",                r[22],        decoder.field_091),
      Field("Notes",                           r[23:92],     decoder.field_061),
      Field("File Record No",                  r[123:128],   decoder.field_031),
      Field("Cycle Date",                      r[128:132],   decoder.field_032)
    ]

  # 4.1.3.3  NDB NAVAID Simulation Continuation Record
  def read_sim(self, r):
    return [
      Field("Record Type",                     r[0],         decoder.field_002),
      Field("Customer / Area Code",            r[1:4],       decoder.field_003),
      Field("Section Code",                    r[4:6],       decoder.field_004),
      Field("Airport ICAO Identifier",         r[6:10],      decoder.field_006),
      Field("ICAO Code",                       r[10:12],     decoder.field_014),
      Field("NDB Identifier",                  r[13:17],     decoder.field_033),
      Field("ICAO Code (2)",                   r[19:21],     decoder.field_014),
      Field("Continuation Record No",          r[21],        decoder.field_016),
      Field("Application Type",                r[22],        decoder.field_091),
      Field("Facility Characteristics",        r[27:32],     decoder.field_093),
      Field("Facility Elevation",              r[79:84],     decoder.field_092),
      Field("File Record No",                  r[123:128],   decoder.field_031),
      Field("Cycle Date",                      r[128:132],   decoder.field_032),
    ]

  # 4.1.3.4 NDB NAVAID Flight Planning Continuation Records
  def read_flight_plan0(self, r):
    return [
      Field("Record Type",                     r[0],         decoder.field_002),
      Field("Customer / Area Code",            r[1:4],       decoder.field_003),
      Field("Section Code",                    r[4:6],       decoder.field_004),
      Field("Airport ICAO Identifier",         r[6:10],      decoder.field_006),
      Field("ICAO Code",                       r[10:12],     decoder.field_014),
      Field("NDB Identifier",                  r[13:17],     decoder.field_033),
      Field("ICAO Code (2)",                   r[19:21],     decoder.field_014),
      Field("Continuation Record No",          r[21],        decoder.field_016),
      Field("Application Type",                r[22],        decoder.field_091),
      Field("FIR Identifier",                  r[23:27],     decoder.field_116),
      Field("UIR Identifier",                  r[28:31],     decoder.field_116),
      Field("Start/End Indicator",             r[32],        decoder.field_152),
      Field("Start/End Date",                  r[32:43],     decoder.field_153),
      Field("File Record No",                  r[123:128],   decoder.field_031),
      Field("Cycle Date",                      r[128:132],   decoder.field_032)
    ]

  # 4.1.3.5  NDB NAVAID Flight Planning Continuation Records
  def read_flight_plan1(self, r):
    return [
      Field("Record Type",                     r[0],         decoder.field_002),
      Field("Customer / Area Code",            r[1:4],       decoder.field_003),
      Field("Section Code",                    r[4:6],       decoder.field_004),
      Field("Airport ICAO Identifier",         r[6:10],      decoder.field_006),
      Field("ICAO Code",                       r[10:12],     decoder.field_014),
      Field("NDB Identifier",                  r[13:17],     decoder.field_033),
      Field("ICAO Code (2)",                   r[19:21],     decoder.field_014),
      Field("Continuation Record No",          r[21],        decoder.field_016),
      Field("NDB Frequency",                   r[22:27],     decoder.field_034),
      Field("NDB Class",                       r[27:31],     decoder.field_035),
      Field("NDB Latitude",                    r[32:41],     decoder.field_036),
      Field("NDB Longitude",                   r[41:51],     decoder.field_037),
      Field("Magnetic Variation",              r[74:79],     decoder.field_039),
      Field("Datum Code",                      r[90:93],     decoder.field_197),
      Field("NDB Name",                        r[93:123],    decoder.field_071),
      Field("File Record No",                  r[123:128],   decoder.field_031),
      Field("Cycle Date",                      r[128:132],   decoder.field_032)
    ]