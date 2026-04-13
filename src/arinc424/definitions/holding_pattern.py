from arinc424.decoder import Field
import arinc424.decoder as decoder


# 4.1.5 Holding Pattern Records (EP)
class HoldingPattern():

  cont_idx = 38
  app_idx = 39
  continuations = ['A']
  name = 'Holding Pattern'

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

  # 4.1.5.1 Holding Pattern Primary Records
  #
  # Note1: In Enroute Fix Holding Pattern records, the code
  # of “ENRT” is used in the Region Code field and
  # the ICAO Code field is blank. In Terminal Fix
  # Holding Records, the Region Code field contains
  # the identifier of the Airport or Heliport with
  # which the holding is associated. The ICAO Code
  # field will not be blank. This information will
  # uniquely identify the Terminal NDB, Airport
  # Terminal Waypoint or Heliport Terminal
  # Waypoint.
  #
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("Region Code",                         r[6:10],       decoder.field_041),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Duplicate Identifier",                r[27:29],      decoder.field_114),
      Field("Fix Identifier",                      r[29:34],      decoder.field_013),
      Field("ICAO Code (2)",                       r[34:36],      decoder.field_014),
      Field("Section Code (2)",                    r[36:38],      decoder.field_004),
      Field("Continuation Record No",              r[38],         decoder.field_016),
      Field("Inbound Holding Course",              r[39:43],      decoder.field_062),
      Field("Turn Direction",                      r[43],         decoder.field_063),
      Field("Leg Length",                          r[44:47],      decoder.field_064),
      Field("Leg Time",                            r[47:49],      decoder.field_065),
      Field("Minimum Altitude",                    r[49:54],      decoder.field_030),
      Field("Maximum Altitude",                    r[54:59],      decoder.field_127),
      Field("Holding Speed",                       r[59:62],      decoder.field_175),
      Field("RNP",                                 r[62:65],      decoder.field_211),
      Field("Arc Radius",                          r[65:71],      decoder.field_204),
      Field("Name",                                r[98:123],     decoder.field_060),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]

  # 4.1.5.2 Holding Pattern Continuation Records
  def read_cont(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Customer / Area Code",                r[1:4],        decoder.field_003),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("Region Code",                         r[6:10],       decoder.field_041),
      Field("ICAO Code",                           r[10:12],      decoder.field_014),
      Field("Duplicate Identifier",                r[27:29],      decoder.field_114),
      Field("Fix Identifier",                      r[29:34],      decoder.field_013),
      Field("ICAO Code (2)",                       r[34:36],      decoder.field_014),
      Field("Section Code (2)",                    r[36:38],      decoder.field_004),
      Field("Continuation Record No",              r[38],         decoder.field_016),
      Field("Application Type",                    r[40],         decoder.field_091),
      Field("Notes",                               r[40:109],     decoder.field_061),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]