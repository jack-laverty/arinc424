from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.24 Preferred Routes Records (ET)
# The Preferred Routes file contains details defining the  
# Preferred Routes, North America Routes for North Atlantic Traffic, the Traffic Orientation System, and the  
# similar predefined routings that do not meet the 
# requirements of the Enroute Airway Record. 
class PreferredRoute():

  cont_idx = 38
  app_idx = 39
  continuations = ['A', 'T']
  name = 'Preferred Route'

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

  # 4.1.24.1 Preferred Route Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                r[0],           decoder.field_002),
      Field("Customer / Area Code",       r[1:4],         decoder.field_003),
      Field("Section Code",               r[4:6],         decoder.field_004),
      Field("Route Identifier",           r[13:23],       decoder.field_008),
      Field("Preferred Route Use Ind",    r[23:25],       decoder.field_220),
      Field("Sequence Number",            r[25:29],       decoder.field_012),
      Field("Continuation Record No",     r[38],          decoder.field_016),
      Field("To Fix Identifier",          r[39:44],       decoder.field_083),
      Field("ICAO Code",                  r[44:46],       decoder.field_014),
      Field("Section Code (2)",           r[46:48],       decoder.field_004),
      Field("VIA Code",                   r[48:51],       decoder.field_077),
      Field("SID/STAR/AWY Ident",         r[51:57],       decoder.field_078),
      Field("AREA Code",                  r[57:60],       decoder.field_003),
      Field("Level",                      r[60],          decoder.field_019),
      Field("Route Type",                 r[61],          decoder.field_007),
      Field("Initial Airport/Fix",        r[62:67],       decoder.field_194),
      Field("ICAO Code",                  r[67:69],       decoder.field_014),
      Field("Section Code",               r[69:71],       decoder.field_004),
      Field("Terminus Airport/Fix",       r[71:76],       decoder.field_194),
      Field("ICAO Code",                  r[76:78],       decoder.field_014),
      Field("Section Code",               r[78:80],       decoder.field_004),
      Field("Minimum Altitude",           r[80:85],       decoder.field_030),
      Field("Maximum Altitude",           r[85:90],       decoder.field_127),
      Field("Time Code",                  r[90],          decoder.field_131),
      Field("Aircraft Use Group",         r[91:93],       decoder.field_221),
      Field("Direction Restriction",      r[93],          decoder.field_115),
      Field("Altitude Description",       r[94],          decoder.field_029),
      Field("Altitude One",               r[95:100],      decoder.field_030),
      Field("Altitude Two",               r[100:105],     decoder.field_030),
      Field("File Record No",             r[123:128],     decoder.field_031),
      Field("Cycle Date",                 r[128:132],     decoder.field_032)
    ]

  # 4.1.24.2 Preferred Route Continuation Records
  def read_timeop(self, r):
    return [
      Field("Record Type",                r[0],           decoder.field_002),
      Field("Customer / Area Code",       r[1:4],         decoder.field_003),
      Field("Section Code",               r[4:6],         decoder.field_004),
      Field("Route Identifier",           r[13:23],       decoder.field_008),
      Field("Preferred Route Use Ind",    r[23:25],       decoder.field_220),
      Field("Sequence Number",            r[25:29],       decoder.field_012),
      Field("Continuation Record No",     r[38],          decoder.field_016),
      Field("Application Type",           r[39],          decoder.field_091),
      Field("Time Code",                  r[40],          decoder.field_131),
      Field("Time Indicator",             r[41],          decoder.field_138),
      Field("Time of Operation",          r[42:52],       decoder.field_195),
      Field("Time of Operation (2)",      r[52:62],       decoder.field_195),
      Field("Time of Operation (3)",      r[62:72],       decoder.field_195),
      Field("Time of Operation (4)",      r[72:82],       decoder.field_195),
      Field("Time of Operation (5)",      r[82:92],       decoder.field_195),
      Field("Time of Operation (6)",      r[92:102],      decoder.field_195),
      Field("Time of Operation (7)",      r[102:112],     decoder.field_195),
      Field("File Record No",             r[123:128],     decoder.field_031),
      Field("Cycle Date",                 r[128:132],     decoder.field_032)
    ]

  # 4.1.24.3 Preferred Route Continuation Record
  def read_cont(self, r):
    return [
      Field("Record Type",                r[0],           decoder.field_002),
      Field("Customer / Area Code",       r[1:4],         decoder.field_003),
      Field("Section Code",               r[4:6],         decoder.field_004),
      Field("Route Identifier",           r[13:23],       decoder.field_008),
      Field("Preferred Route Use Ind",    r[23:25],       decoder.field_220),
      Field("Sequence Number",            r[25:29],       decoder.field_012),
      Field("Continuation Record No",     r[38],          decoder.field_016),
      Field("Application Type",           r[39],          decoder.field_091),
      Field("Notes",                      r[40:109],      decoder.field_061),
      Field("File Record No",             r[123:128],     decoder.field_031),
      Field("Cycle Date",                 r[128:132],     decoder.field_032)
    ]