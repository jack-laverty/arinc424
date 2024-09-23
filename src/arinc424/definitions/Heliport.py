from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.2.1  Heliport Records (HA)
class Heliport():

  cont_idx = 21
  app_idx = 22
  continuations = ['A', 'P', 'Q']
  name = 'Heliport'

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
      case 'Q':
        return self.read_flight1(line)
      case _:
        return []

  # 4.2.1.1  Heliport Primary Records 
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                 r[13:16],      decoder.field_107),
      Field("PAD Identifier",                      r[16:21],      decoder.field_180),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Speed Limit Altitude",                r[22:27],      decoder.field_073),
      Field("Datum Code",                          r[27:30],      decoder.field_197),
      Field("IFR Indicator",                       r[30],         decoder.field_108),
      Field("Latitude",                            r[32:41],      decoder.field_036),
      Field("Longitude",                           r[41:51],      decoder.field_037),
      Field("Magnetic Variation",                  r[51:56],      decoder.field_039),
      Field("Heliport Elevation",                  r[56:61],      decoder.field_055),
      Field("Speed Limit",                         r[61:64],      decoder.field_072),
      Field("Recommended VHF Navaid",              r[64:68],      decoder.field_023),
      Field("ICAO Code (2)",                       r[68:70],      decoder.field_014),
      Field("Transition Altitude",                 r[70:75],      decoder.field_053),
      Field("Transition Level",                    r[75:80],      decoder.field_053),
      Field("Public Military Indicator",           r[80],         decoder.field_177),
      Field("Time Zone",                           r[81:84],      decoder.field_178),
      Field("Daylight Indicator",                  r[84],         decoder.field_179),
      Field("Pad Dimensions",                      r[85:91],      decoder.field_176),
      Field("Magnetic/True Indicator",             r[91],         decoder.field_165),
      Field("Heliport Name",                       r[93:123],     decoder.field_071),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.2.1.2  Heliport Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                 r[13:16],      decoder.field_107),
      Field("PAD Identifier",                      r[16:21],      decoder.field_180),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("Notes",                               r[23:92],      decoder.field_061),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.2.1.3  Heliport Flight Planning Continuation Records 
  def read_flight0(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                 r[13:16],      decoder.field_107),
      Field("PAD Identifier",                      r[16:21],      decoder.field_180),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("FIR Identifier",                      r[23:27],      decoder.field_116),
      Field("UIR Identifier",                      r[27:31],      decoder.field_116),
      Field("Start/End Indicator",                 r[31],         decoder.field_152),
      Field("Start/End Date/Time",                 r[32:43],      decoder.field_153),
      Field("Controlled A/S Indicator",            r[66],         decoder.field_217),
      Field("Controlled A/S Airport Indentifier",  r[67:71],      decoder.field_006),
      Field("Controlled A/S Airport ICAO",         r[71:73],      decoder.field_014),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.2.1.4  Heliport Flight Planning Continuation Records
  def read_flight1(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("ATA/IATA Designator",                 r[13:16],      decoder.field_107),
      Field("PAD Identifier",                      r[16:21],      decoder.field_180),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Type",                    r[22],         decoder.field_091),
      Field("Notes",                               r[23:92],      decoder.field_061),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]