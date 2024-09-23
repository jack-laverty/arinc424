from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.8 Airport Gate Records (PB)
class AirportGate():

  cont_idx = 21
  app_idx = 22
  continuations = ['A']
  name = 'Airport Gate'

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

  # 4.1.8.1 Airport Gate Primary Record
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport ICAO Identifier",             r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Gate Identifier",                     r[13:18],      decoder.field_056),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Gate Latitude",                       r[32:41],      decoder.field_036),
      Field("Gate Longitude",                      r[41:51],      decoder.field_037),
      Field("Name",                                r[98:123],     decoder.field_060),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.8.2 Airport Gate Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport ICAO Identifier",             r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Gate Identifier",                     r[13:18],      decoder.field_056),
      Field("Continuation Record No",              r[21],         decoder.field_016),
      Field("Application Notes",                   r[22],         decoder.field_091),
      Field("Notes",                               r[23:92],      decoder.field_061),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]


# 4.1.12 Company Route Records (R)
#
# This record contains company tailored route information
#
class CompanyRoute():

  # 4.1.12.1 Company Route Primary Records
  def read(self, r) -> list:
    return [
      Field("Record Type",                        r[0],           decoder.field_002),
      Field("Customer",                           r[1:4],         decoder.field_003),
      Field("Section Code",                       r[4:6],         decoder.field_004),
      Field("From Airport/Fix",                   r[6:11],        decoder.field_075),
      Field("ICAO Code",                          r[12:14],       decoder.field_014),
      Field("Airspace Center",                    r[9:14],        decoder.field_214),
      Field("Section Code (2)",                   r[14:16],       decoder.field_004),
      Field("To Airport/Fix",                     r[16:21],       decoder.field_075),
      Field("ICAO Code (2)",                      r[22:24],       decoder.field_014),
      Field("Section Code (3)",                   r[24:26],       decoder.field_004),
      Field("Company Route ID",                   r[26:36],       decoder.field_076),
      Field("Sequence Number",                    r[36:39],       decoder.field_012),
      Field("VIA",                                r[39:42],       decoder.field_077),
      Field("SID/STAR/App/Awy",                   r[42:48],       decoder.field_078),
      Field("Area Code",                          r[48:51],       decoder.field_003),
      Field("To Fix",                             r[51:57],       decoder.field_132),
      Field("ICAO Code",                          r[57:59],       decoder.field_118),
      Field("Section Code (4)",                   r[59],          decoder.field_036),
      Field("RUnway Trans",                       r[61:66],       decoder.field_037),
      Field("ENRT Trans",                         r[66:71],       decoder.field_036),
      Field("Cruise Altitude",                    r[72:77],       decoder.field_037),
      Field("Terminal/Alternate Airport",         r[77:81],       decoder.field_119),
      Field("ICAO Code",                          r[81:83],       decoder.field_120),
      Field("Alternate Distance",                 r[83:87],       decoder.field_211),
      Field("Cost Index",                         r[87:90],       decoder.field_121),
      Field("Enroute Alternate Airport",          r[90:94],       decoder.field_133),
      Field("File Record No",                     r[123:128],     decoder.field_031),
      Field("Cycle Date",                         r[128:132],     decoder.field_032)
    ]