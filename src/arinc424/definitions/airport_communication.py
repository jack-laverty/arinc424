from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.14 Airport Communications Records (PV)
class AirportCommunication():

  cont_idx = 25
  app_idx = 26
  continuations = ['N']
  name = 'Airport Communications'

  def application_type(self, line):
    return line[self.app_idx]

  def read(self, line, primary) -> list:

    if primary:
      return self.read_primary(line)

    application = line[self.app_idx]
    match application:
      case 'N':
        return self.read_cont_narr(line)
      # TODO find a data set that has these continuation records to verify
      # case 'T':
      #     return self.read_time(line)
      case _:
        return []

  # 4.1.14.1 Airport Communications Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport Identifier",                  r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Communications Type",                 r[13:16],      decoder.field_101),
      Field("Communications Freq",                 r[16:23],      decoder.field_103),
      Field("Guard/Transmit",                      r[23],         decoder.field_182),
      Field("Frequency Units",                     r[24],         decoder.field_104),
      Field("Continuation Record No",              r[25],         decoder.field_016),
      Field("Service Indicator",                   r[26:29],      decoder.field_106),
      Field("Radar Service",                       r[29],         decoder.field_102),
      Field("Modulation",                          r[30],         decoder.field_198),
      Field("Signal Emission",                     r[31],         decoder.field_199),
      Field("Latitude",                            r[32:41],      decoder.field_036),
      Field("Longitude",                           r[41:51],      decoder.field_037),
      Field("Magnetic Variation",                  r[51:56],      decoder.field_039),
      Field("Facility Elevation",                  r[56:61],      decoder.field_092),
      Field("H24 Indicator",                       r[61],         decoder.field_181),
      Field("Sectorization",                       r[62:68],      decoder.field_183),
      Field("Altitude Description",                r[68],         decoder.field_029),
      Field("Communication Altitude",              r[69:74],      decoder.field_184),
      Field("Communication Altitude (2)",          r[74:79],      decoder.field_184),
      Field("Sector Facility",                     r[79:83],      decoder.field_185),
      Field("ICAO Code (2)",                       r[83:85],      decoder.field_014),
      Field("Section (2)",                         r[85:87],      decoder.field_004),
      Field("Distance Description",                r[87],         decoder.field_187),
      Field("Communications Distance",             r[88:90],      decoder.field_188),
      Field("Remote Facility",                     r[90:94],      decoder.field_200),
      Field("ICAO Code (3)",                       r[94:96],      decoder.field_014),
      Field("Section (3)",                         r[96:98],      decoder.field_004),
      Field("Call Sign",                           r[98:123],     decoder.field_105),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.14.2 Airport Communications Continuation Records
  def read_cont_narr(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4]+r[12],    decoder.field_004),
      Field("Airport Identifier",                  r[6:10],       decoder.field_006),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Communications Type",                 r[13:16],      decoder.field_101),
      Field("Communications Freq",                 r[16:23],      decoder.field_103),
      Field("Guard/Transmit",                      r[23],         decoder.field_182),
      Field("Frequency Units",                     r[24],         decoder.field_104),
      Field("Continuation Record No",              r[25],         decoder.field_016),
      Field("Application Type",                    r[26],         decoder.field_091),
      Field("Narrative",                           r[27:87],      decoder.field_186),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.14.3 Airport Additional Continuation Records
  def read_time(self, r):
    return [
      Field("Record Type",                        r[0],           decoder.field_002),
      Field("Customer / Area Code",               r[1:4],         decoder.field_003),
      Field("Section Code",                       r[4]+r[12],     decoder.field_004),
      Field("Airport Identifier",                 r[6:10],        decoder.field_006),
      Field("ICAO Code",                          r[10:12],       decoder.field_014),
      Field("Communications Type",                r[13:16],       decoder.field_101),
      Field("Communications Freq",                r[16:23],       decoder.field_103),
      Field("Guard/Transmit",                     r[23],          decoder.field_182),
      Field("Frequency Units",                    r[24],          decoder.field_104),
      Field("Continuation Record No",             r[25],          decoder.field_016),
      Field("Application Type",                   r[26],          decoder.field_091),
      Field("Time Code",                          r[27],          decoder.field_131),
      Field("NOTAM",                              r[28],          decoder.field_132),
      Field("Time Indicator",                     r[29],          decoder.field_138),
      Field("Time of Operaion",                   r[30:40],       decoder.field_195),
      Field("Time of Operaion (2)",               r[40:50],       decoder.field_195),
      Field("Time of Operaion (2)",               r[50:60],       decoder.field_195),
      Field("Time of Operaion (3)",               r[60:70],       decoder.field_195),
      Field("Time of Operaion (4)",               r[70:80],       decoder.field_195),
      Field("Time of Operaion (5)",               r[80:90],       decoder.field_195),
      Field("Time of Operaion (6)",               r[90:100],      decoder.field_195),
      Field("File Record No",                     r[123:128],     decoder.field_031),
      Field("Cycle Date",                         r[128:132],     decoder.field_032)
    ]