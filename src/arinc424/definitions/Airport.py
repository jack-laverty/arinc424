from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.7 Airport Records (PA)
class Airport():

  cont_idx = 21
  app_idx = 22
  continuations = ['A', 'P', 'Q']
  name = 'Airport'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match line[self.app_idx]:
      case 'A':
        return self.read_cont(line)
      case 'P':
        return self.read_flight0(line)
      case 'Q':
        return self.read_flight1(line)
      case _:
        return []

  # 4.1.7.1 Airport Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4]+r[12],    decoder.field_004),
      Field("Airport ICAO Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                               r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                     r[13:16],      decoder.field_107),
      Field("Continuation Record No",                  r[21],         decoder.field_016),
      Field("Speed Limit Altitude",                    r[22:27],      decoder.field_073),
      Field("Longest Runway",                          r[27:30],      decoder.field_054),
      Field("IFR Capability",                          r[30],         decoder.field_108),
      Field("Longest Runway Surface Code",             r[31],         decoder.field_249),
      Field("Airport Reference Pt. Latitude",          r[32:41],      decoder.field_036),
      Field("Airport Reference Pt. Longitude",         r[41:51],      decoder.field_037),
      Field("Magnetic Variation",                      r[51:56],      decoder.field_039),
      Field("Airport Elevation",                       r[56:61],      decoder.field_055),
      Field("Speed Limit",                             r[61:64],      decoder.field_072),
      Field("Recommended Navaid",                      r[64:68],      decoder.field_023),
      Field("ICAO Code (2)",                           r[68:70],      decoder.field_014),
      Field("Transition Altitude",                     r[70:75],      decoder.field_053),
      Field("Transition Level",                        r[75:80],      decoder.field_053),
      Field("Public Military Indicator",               r[80],         decoder.field_177),
      Field("Time Zone",                               r[81:84],      decoder.field_178),
      Field("Daylight Indicator",                      r[84],         decoder.field_179),
      Field("Magnetic/True Indicator",                 r[85],         decoder.field_165),
      Field("Datum Code",                              r[86:89],      decoder.field_197),
      Field("Airport Name",                            r[93:123],     decoder.field_071),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.7.2 Airport Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4]+r[12],    decoder.field_004),
      Field("Airport ICAO Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                               r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                     r[13:16],      decoder.field_107),
      Field("Continuation Record No",                  r[21],         decoder.field_016),
      Field("Application Type",                        r[22],         decoder.field_091),
      Field("Notes",                                   r[23:92],      decoder.field_061),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.7.3 Airport Flight Planning Continuation Records
  #
  # This Continuation Record is used to indicate the FIR and UIR within which the Airport define in the Primary
  # Record resides in and the Start/End validity dates/times of the Primary Record and provide an indication if the
  # Airport defined in the Primary Record is associated with Controlled Airspace.
  #
  def read_flight0(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                     r[6:10],       decoder.field_006),
      Field("ICAO Code",                               r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                     r[13:16],      decoder.field_107),
      Field("Continuation Record No",                  r[21],         decoder.field_016),
      Field("Application Type",                        r[22],         decoder.field_091),
      Field("FIR Identifier",                          r[23:27],      decoder.field_116),
      Field("UIR Identifier",                          r[27:31],      decoder.field_116),
      Field("Start/End Indicator",                     r[31],         decoder.field_152),
      Field("Start/End Date/Time",                     r[32:43],      decoder.field_153),
      Field("Controlled A/S Indicator",                r[66],         decoder.field_217),
      Field("Controlled A/S Airport Ident",            r[67:71],      decoder.field_006),
      Field("Controlled A/S Airport ICAO",             r[71:73],      decoder.field_014),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]

  # 4.1.7.4 Airport Flight Planning Continuation Records
  #
  # This Continuation Record is used to indicate the fields on
  # the Primary Record that have changed, used in conjunction
  # with Section 4.1.7.3.
  #
  # Note: Flight Planning continuation records are designed
  # to carry off-cycle updates to the primary record,
  # and cannot carry an Application Type column.
  #
  def read_flight1(self, r):
    return [
      Field("Record Type",                             r[0],          decoder.field_002),
      Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
      Field("Section Code",                            r[4]+r[12],    decoder.field_004),
      Field("Airport ICAO Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                               r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                     r[13:16],      decoder.field_107),
      Field("Continuation Record No",                  r[21],         decoder.field_016),
      Field("Speed Limit Altitude",                    r[22:27],      decoder.field_073),
      Field("Longest Runway",                          r[27:30],      decoder.field_054),
      Field("IFR Capability",                          r[30],         decoder.field_108),
      Field("Longest Runway Surface Code",             r[31],         decoder.field_249),
      Field("Airport Reference Pt. Latitude",          r[32:41],      decoder.field_036),
      Field("Airport Reference Pt. Longitude",         r[41:51],      decoder.field_037),
      Field("Magnetic Variation",                      r[51:56],      decoder.field_039),
      Field("Airport Elevation",                       r[56:61],      decoder.field_055),
      Field("Speed Limit",                             r[61:64],      decoder.field_072),
      Field("Recommended Navaid",                      r[64:68],      decoder.field_023),
      Field("ICAO Code (2)",                           r[68:70],      decoder.field_014),
      Field("Transition Altitude",                     r[70:75],      decoder.field_053),
      Field("Transition Level",                        r[75:80],      decoder.field_053),
      Field("Public Military Indicator",               r[80],         decoder.field_177),
      Field("Time Zone",                               r[81:84],      decoder.field_178),
      Field("Daylight Indicator",                      r[84],         decoder.field_179),
      Field("Magnetic/True Indicator",                 r[85],         decoder.field_165),
      Field("Datum Code",                              r[86:89],      decoder.field_197),
      Field("Airport Name",                            r[93:123],     decoder.field_071),
      Field("File Record No",                          r[123:128],    decoder.field_031),
      Field("Cycle Date",                              r[128:132],    decoder.field_032)
    ]