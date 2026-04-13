from arinc424.decoder import Field
import arinc424.decoder as decoder



# 4.1.2  VHF NAVAID Record (D) 
 
# The VHF  NAVAID  file  contains  details  of  all  VOR,  
# VOR/DME, VORTAC, DME and TACAN stations within 
# the  geographical  area  of  interest.  For  VOR  and  TACAN  
# stations  having  the  same  identifier  but  different  operating  
# frequencies,  the  TACAN  is  available  and  the  VOR  is  
# suppressed unless the VOR is required to support Sections 
# 3.2.3.3,  3.2.3.4,  3.2.4.4,  3.2.4.5,  3.2.4.6,  3.2.4.11,  3.2.5,  
# 3.2.9,  3.3.5,  3.3.6,  3.3.7  or  3.3.8.  In  such  cases  the  VOR  
# is available and the TACAN is suppressed
class VHFNavaid():

  cont_idx = 21
  app_idx = 22
  continuations = ['A', 'L', 'P', 'S']
  name = 'VHF Navaid'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'A':
        return self.read_cont(line)
      case 'L':
        return self.read_lim(line)
      case 'P':
        return self.read_flight_plan0(line)
      case 'S':
        return self.read_sim(line)
      case _:
        return []

  # 4.1.2.1  VHF NAVAID Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                 r[0],          decoder.field_002),
      Field("Customer / Area Code",        r[1:4],        decoder.field_003),
      Field("Section Code",                r[4:6],        decoder.field_004),
      Field("Airport ICAO Identifier",     r[6:10],       decoder.field_006),
      Field("ICAO Code",                   r[10:12],      decoder.field_014),
      Field("VOR Identifier",              r[13:17],      decoder.field_033),
      Field("ICAO Code (2)",               r[19:21],      decoder.field_014),
      Field("Continuation Record No",      r[21],         decoder.field_016),
      Field("Frequency",                   r[22:27],      decoder.field_034),
      Field("Class",                       r[27:29],      decoder.field_035),
      Field("VOR Latitude",                r[32:41],      decoder.field_036),
      Field("VOR Longitude",               r[41:51],      decoder.field_037),
      Field("DME Ident",                   r[51:55],      decoder.field_038),
      Field("DME Latitude",                r[55:64],      decoder.field_036),
      Field("DME Longitude",               r[64:74],      decoder.field_037),
      Field("Station Declination",         r[74:79],      decoder.field_066),
      Field("DME Elevation",               r[79:84],      decoder.field_040),
      Field("Figure of Merit",             r[84],         decoder.field_149),
      Field("ILS/DME Bias",                r[85:87],      decoder.field_090),
      Field("Frequency Protection",        r[87:90],      decoder.field_150),
      Field("Datum Code",                  r[90:93],      decoder.field_197),
      Field("VOR Name",                    r[93:123],     decoder.field_071),
      Field("File Record No",              r[123:128],    decoder.field_031),
      Field("Cycle Date",                  r[128:132],    decoder.field_032)
    ]

  # 4.1.2.2  VHF NAVAID Continuation Records 
  def read_cont(self, r):
    return [
      Field("Record Type",                 r[0],          decoder.field_002),
      Field("Customer / Area Code",        r[1:4],        decoder.field_003),
      Field("Section Code",                r[4:6],        decoder.field_004),
      Field("Airport ICAO Identifier",     r[6:10],       decoder.field_006),
      Field("ICAO Code",                   r[10:12],      decoder.field_014),
      Field("VOR Identifier",              r[13:17],      decoder.field_033),
      Field("ICAO Code (2)",               r[19:21],      decoder.field_014),
      Field("Continuation Record No",      r[21],         decoder.field_016),
      Field("Application Type",            r[22],         decoder.field_091),
      Field("Notes",                       r[23:92],      decoder.field_061),
      Field("File Record No",              r[123:128],    decoder.field_031),
      Field("Cycle Date",                  r[128:132],    decoder.field_032),
    ]

  # 4.1.2.3  VHF NAVAID Simulation Continuation Records
  def read_sim(self, r):
    return [
      Field("Record Type",                 r[0],          decoder.field_002),
      Field("Customer / Area Code",        r[1:4],        decoder.field_003),
      Field("Section Code",                r[4:6],        decoder.field_004),
      Field("Airport ICAO Identifier",     r[6:10],       decoder.field_006),
      Field("ICAO Code",                   r[10:12],      decoder.field_014),
      Field("VOR Identifier",              r[13:17],      decoder.field_033),
      Field("ICAO Code (2)",               r[19:21],      decoder.field_014),
      Field("Continuation Record No",      r[21],         decoder.field_016),
      Field("Application Type",            r[22],         decoder.field_091),
      Field("Facility Characteristics",    r[27:32],      decoder.field_093),
      Field("Magnetic Variation",          r[74:79],      decoder.field_039),
      Field("Facility Elevation",          r[79:84],      decoder.field_092),
      Field("File Record No",              r[123:128],    decoder.field_031),
      Field("Cycle Date",                  r[128:132],    decoder.field_032)
    ]

  # 4.1.2.4  VHF NAVAID Flight Planning Continuation Records
  def read_flight_plan0(self, r):
    return [
      Field("Record Type",                 r[0],          decoder.field_002),
      Field("Customer / Area Code",        r[1:4],        decoder.field_003),
      Field("Section Code",                r[4:6],        decoder.field_004),
      Field("Airport ICAO Identifier",     r[6:10],       decoder.field_006),
      Field("ICAO Code",                   r[10:12],      decoder.field_014),
      Field("VOR Identifier",              r[13:17],      decoder.field_033),
      Field("ICAO Code (2)",               r[19:21],      decoder.field_014),
      Field("Continuation Record No",      r[21],         decoder.field_016),
      Field("Application Type",            r[22],         decoder.field_091),
      Field("FIR Identifier",              r[23:27],      decoder.field_116),
      Field("UIR Identifier",              r[28:31],      decoder.field_116),
      Field("Start/End Indicator",         r[32],         decoder.field_152),
      Field("Start/End Date",              r[32:43],      decoder.field_153),
      Field("File Record No",              r[123:128],    decoder.field_031),
      Field("Cycle Date",                  r[128:132],    decoder.field_032)
    ]

  # 4.1.2.5  VHF NAVAID Flight Planning Continuation Records
  def read_flight_plan1(self, r):
    return [
      Field("Record Type",                 r[0],          decoder.field_002),
      Field("Customer / Area Code",        r[1:4],        decoder.field_003),
      Field("Section Code",                r[4:6],        decoder.field_004),
      Field("Airport ICAO Identifier",     r[6:10],       decoder.field_006),
      Field("ICAO Code",                   r[10:12],      decoder.field_014),
      Field("VOR Identifier",              r[13:17],      decoder.field_033),
      Field("ICAO Code (2)",               r[19:21],      decoder.field_014),
      Field("Continuation Record No",      r[21],         decoder.field_016),
      Field("Frequency",                   r[22:27],      decoder.field_034),
      Field("Class",                       r[27:29],      decoder.field_035),
      Field("VOR Latitude",                r[32:41],      decoder.field_036),
      Field("VOR Longitude",               r[41:51],      decoder.field_037),
      Field("DME Ident",                   r[51:55],      decoder.field_038),
      Field("DME Latitude",                r[55:64],      decoder.field_036),
      Field("DME Longitude",               r[64:74],      decoder.field_037),
      Field("Station Declination",         r[74:79],      decoder.field_066),
      Field("DME Elevation",               r[79:84],      decoder.field_040),
      Field("Figure of Merit",             r[84],         decoder.field_149),
      Field("ILS/DME Bias",                r[85:87],      decoder.field_090),
      Field("Frequency Protection",        r[87:90],      decoder.field_150),
      Field("Datum Code",                  r[90:93],      decoder.field_197),
      Field("VOR Name",                    r[93:123],     decoder.field_071),
      Field("File Record No",              r[123:128],    decoder.field_031),
      Field("Cycle Date",                  r[128:132],    decoder.field_032)
    ]

  # 4.1.2.6 VHF NAVAID Limitation  Continuation Record
  def read_lim(self, r):
    return [
      Field("Record Type",                 r[0],          decoder.field_002),
      Field("Customer / Area Code",        r[1:4],        decoder.field_003),
      Field("Section Code",                r[4:6],        decoder.field_004),
      Field("Airport ICAO Identifier",     r[6:10],       decoder.field_006),
      Field("ICAO Code",                   r[10:12],      decoder.field_014),
      Field("VOR Identifier",              r[13:17],      decoder.field_033),
      Field("ICAO Code (2)",               r[19:21],      decoder.field_014),
      Field("Continuation Record No",      r[21],         decoder.field_016),
      Field("Application Type",            r[22],         decoder.field_091),
      Field("Navaid Limitation Code",      r[23],         decoder.field_205),
      Field("Component Affected Indicator", r[24],        decoder.field_206),
      Field("Sequence Number",             r[25:27],      decoder.field_012),
      Field("Sector From/Sector To",       r[27:29],      decoder.field_207),
      Field("Distance Description",        r[29],         decoder.field_187),
      Field("Distance Limitation",         r[30:36],      decoder.field_208),
      Field("Altitude Description",        r[36],         decoder.field_029),
      Field("Altitude Limitation",         r[37:43],      decoder.field_029),
      Field("Sector From/Sector To (2)",   r[43:45],      decoder.field_207),
      Field("Distance Description (2)",    r[45],         decoder.field_187),
      Field("Distance Limitation (2)",     r[46:52],      decoder.field_208),
      Field("Altitude Description (2)",    r[52],         decoder.field_029),
      Field("Altitude Limitation (2)",     r[53:59],      decoder.field_209),
      Field("Sector From/Sector To (3)",   r[59:61],      decoder.field_207),
      Field("Distance Description (3)",    r[61],         decoder.field_187),
      Field("Distance Limitation (3)",     r[62:68],      decoder.field_208),
      Field("Altitude Description (3)",    r[68],         decoder.field_029),
      Field("Altitude Limitation (3)",     r[69:75],      decoder.field_209),
      Field("Sector From/Sector To (4)",   r[75:77],      decoder.field_207),
      Field("Distance Description (4)",    r[77],         decoder.field_187),
      Field("Distance Limitation (4)",     r[79:84],      decoder.field_208),
      Field("Altitude Description (4)",    r[84],         decoder.field_029),
      Field("Altitude Limitation (4)",     r[85:91],      decoder.field_209),
      Field("Sector From/Sector To (5)",   r[91:93],      decoder.field_207),
      Field("Distance Description (5)",    r[93],         decoder.field_187),
      Field("Distance Limitation (5)",     r[94:100],     decoder.field_208),
      Field("Altitude Description (5)",    r[101],        decoder.field_029),
      Field("Altitude Limitation (5)",     r[101:107],    decoder.field_209),
      Field("Sequence End Indicator",      r[107],        decoder.field_210),
      Field("File Record No",              r[123:128],    decoder.field_031),
      Field("Cycle Date",                  r[128:132],    decoder.field_032)
    ]