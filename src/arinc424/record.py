import arinc424.decoder as decoder
from collections import defaultdict
from arinc424.decoder import Field
from prettytable import PrettyTable


class Record():

    def __init__(self):
        self.code = ''
        self.raw = ''
        self.fields = []

    def validate(self, line):
        line = line.strip()
        if line.startswith(('S', 'T')) is False:
            # print("Error Parsing: record doesn't start with record type")
            return False
        if len(line) != 132:
            # print("Error Parsing: record not 132 characters in length")
            return False
        if line[-9:].isnumeric() is False:
            # print("Error Parsing: record doesn't end in file record and cycle date")
            return False
        return True

    def read(self, line) -> bool:

        def def_val():
            return False

        records = defaultdict(def_val)
        records['AS'] = MORA()
        records['D '] = VHFNavaid()
        records['DB'] = NDBNavaid()
        records['EA'] = Waypoint(True)
        records['EM'] = AirwaysMarker()
        records['EP'] = Holding()
        records['ER'] = Airway()
        records['ET'] = PreferredRoute()
        records['EU'] = AirwayRestricted()
        records['EV'] = EnrouteComms()
        records['HA'] = Heliport()
        records['HC'] = HeliportTerminalWaypoint()
        records['HD'] = SIDSTARApp()
        records['HE'] = SIDSTARApp()
        records['HF'] = SIDSTARApp()
        records['HK'] = TAA(True)
        records['HS'] = MSA(True)
        records['HV'] = HeliportComms()
        records['PA'] = Airport()
        records['PB'] = AirportGate()
        records['PC'] = Waypoint(False)
        records['PD'] = SIDSTARApp()
        records['PE'] = SIDSTARApp()
        records['PF'] = SIDSTARApp()
        records['PG'] = Runway()
        records['PI'] = LocalizerGlideslope()
        records['PK'] = TAA()
        records['PL'] = MLS()
        records['PM'] = LocalizerMarker()
        records['PN'] = NDBNavaid()  # terminal
        records['PP'] = PathPoint()
        records['PR'] = FlightPlanning()
        records['PS'] = MSA(False)
        records['PT'] = GLS()
        records['PV'] = AirportCommunication()
        records['R '] = CompanyRoute()
        records['RA'] = AlternateRecord()
        records['TC'] = CruisingTables()
        records['TG'] = GeoReferenceTable()
        # records['TN'] = RNAV Name Table (OBSELETE)
        records['UC'] = ControlledAirspace()
        records['UF'] = FIR_UIR()
        records['UR'] = RestrictiveAirspace()

        if self.validate(line) is False:
            return False

        self.raw = line.strip()
        x1, x2 = line[4:6], line[4] + line[12]
        if x1 in records.keys():
            self.code = x1
        elif x2 in records.keys():
            self.code = x2
        else:
            return False

        self.fields = records[self.code].read(line)
        if not self.fields:
            return False

        return True

    def decode(self, format=None):
        table = PrettyTable(field_names=['Field', 'Value', 'Decoded'])
        table.align = 'l'
        for field in self.fields:
            table.add_row([field.name, "'{}'".format(field.value), field.decode(self)])
        match format:
            case None:
                print(table)
                return table.get_string()
            case 'json':
                print(table.get_json_string())
                return table.get_json_string()
            case _:
                print(f'Error: Invalid Output Format "{format}"')


# 4.1.5 Holding Pattern Records (EP)
class Holding():

    cont_idx = 38
    app_idx = 39

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
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


# 4.1.6 Enroute Airways Records (ER)
class Airway():

    cont_idx = 38
    app_idx = 39

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
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


# 4.1.7 Airport Records (PA)
class Airport():

    cont_idx = 21
    app_idx = 22

    def read(self, line) -> list:
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
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


# 4.1.8 Airport Gate Records (PB)
class AirportGate():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
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
# This file contains company tailored route information
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


# 4.1.13 Localizer Marker Records
class LocalizerMarker():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print(line)
                    # raise ValueError("Unsupported Localizer Marker record", line[self.app_idx])

    # 4.1.13.1
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport Identifier",                  r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Localizer Identifier",                r[13:17],      decoder.field_044),
            Field("Marker Type",                         r[17:20],      decoder.field_099),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Locator Frequency",                   r[22:27],      decoder.field_034),
            Field("Runway Identifier",                   r[27:32],      decoder.field_046),
            Field("Marker Latitude",                     r[32:41],      decoder.field_036),
            Field("Marker Longitude",                    r[41:51],      decoder.field_037),
            Field("Minor Axis Bearing",                  r[51:55],      decoder.field_100),
            Field("Locator Latitude",                    r[55:64],      decoder.field_036),
            Field("Locator Longitude",                   r[64:74],      decoder.field_037),
            Field("Localizer Class",                     r[74:79],      decoder.field_035),
            Field("Localizer Facility Characteristics",  r[79:83],      decoder.field_093),
            Field("Localizer Identifier (2)",            r[84:88],      decoder.field_033),
            Field("Magnetic Variation",                  r[90:95],      decoder.field_039),
            Field("Facility Elevation",                  r[97:102],     decoder.field_092),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.13.2
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport Identifier",                  r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Localizer Identifier",                r[13:17],      decoder.field_044),
            Field("Marker Type",                         r[17:20],      decoder.field_099),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.14 Airport Communications Records (PV)
class AirportCommunication():

    cont_idx = 25
    app_idx = 26

    def read(self, r) -> list:
        if int(r[self.cont_idx]) < 2:
            return self.read_primary(r)
        else:
            match r[self.app_idx]:
                case 'N':
                    return self.read_cont_narr(r)
                # TODO find a data set that has these continuation records to verify
                # case 'T':
                #     return self.read_time(r)
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
        return (
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
        )

    # 4.1.14.3 Airport Additional Continuation Records
    def read_time(self, r):
        return (
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
        )


# 4.1.15 Airways Marker Records (EM)
class AirwaysMarker():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    # 4.1.15.1 Airways Marker Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("Marker Identifier",                   r[13:17],      decoder.field_110),
            Field("ICAO Code",                           r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Marker Code",                         r[22:26],      decoder.field_111),
            Field("Marker Shape",                        r[27],         decoder.field_112),
            Field("Marker Power",                        r[28],         decoder.field_113),
            Field("Marker Latitude",                     r[32:41],      decoder.field_036),
            Field("Marker Longitude",                    r[41:51],      decoder.field_037),
            Field("Minor Axis",                          r[51:55],      decoder.field_100),
            Field("Magnetic Variation",                  r[74:79],      decoder.field_039),
            Field("Facility Elevation",                  r[79:84],      decoder.field_092),
            Field("Datum Code",                          r[84:87],      decoder.field_197),
            Field("Marker Name",                         r[93:123],     decoder.field_071),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.15.2 Airways Marker Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("Marker Identifier",                   r[13:17],      decoder.field_110),
            Field("ICAO Code",                           r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.16 Cruising Tables Records (TC)
class CruisingTables():

    def read(self, line):
        return self.read_primary(line)

    # 4.1.16.1 Cruising Table Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Cruise Table Identifier",                 r[6:8],        decoder.field_134),
            Field("Sequence Number",                         r[8],          decoder.field_012),
            Field("Course From",                             r[28:32],      decoder.field_135),
            Field("Course To",                               r[32:36],      decoder.field_135),
            Field("Mag/True",                                r[36],         decoder.field_165),
            Field("Cruise Level From",                       r[39:44],      decoder.field_136),
            Field("Vertical Separation",                     r[44:49],      decoder.field_137),
            Field("Cruise Level To ",                        r[49:54],      decoder.field_136),
            Field("Cruise Level From (2)",                   r[54:59],      decoder.field_136),
            Field("Vertical Separation (2)",                 r[59:64],      decoder.field_137),
            Field("Cruise Level To (2)",                     r[64:69],      decoder.field_136),
            Field("Cruise Level From (3)",                   r[69:74],      decoder.field_136),
            Field("Vertical Separation (3)",                 r[74:79],      decoder.field_137),
            Field("Cruise Level To (3)",                     r[79:84],      decoder.field_136),
            Field("Cruise Level From (4)",                   r[84:89],      decoder.field_136),
            Field("Vertical Separation (4)",                 r[89:94],      decoder.field_137),
            Field("Cruise Level To (4)",                     r[94:99],      decoder.field_136),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]


# 4.1.17 FIR/UIR Records (UF)
class FIR_UIR():

    cont_idx = 19
    app_idx = 20

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    # 4.1.17.1 FIR/UIR Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/UIR Identifier",                  r[6:10],       decoder.field_116),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("FIR/UIR Indicator",                   r[14],         decoder.field_117),
            Field("Sequence Number",                     r[15:19],      decoder.field_012),
            Field("Continuation Record No",              r[19],         decoder.field_016),
            Field("Adjacent FIR Identifier",             r[20:24],      decoder.field_116),
            Field("Adjacent UIR Identifier",             r[24:28],      decoder.field_116),
            Field("Reporting Units Speed",               r[28],         decoder.field_122),
            Field("Reporting Units Altitude",            r[29],         decoder.field_123),
            Field("Entry Report",                        r[30],         decoder.field_124),
            Field("Boundary Via",                        r[32:34],      decoder.field_118),
            Field("FIR/UIR Latitude",                    r[34:43],      decoder.field_036),
            Field("FIR/UIR Longitude",                   r[43:53],      decoder.field_037),
            Field("Arc Origin Latitude",                 r[53:62],      decoder.field_036),
            Field("Arc Origin Longitude",                r[62:72],      decoder.field_037),
            Field("Arc Distance",                        r[72:76],      decoder.field_119),
            Field("Arc Bearing",                         r[76:80],      decoder.field_120),
            Field("FIR Upper Limit",                     r[80:85],      decoder.field_121),
            Field("UIR Lower Limit",                     r[85:90],      decoder.field_121),
            Field("UIR Upper Limit",                     r[90:95],      decoder.field_121),
            Field("Cruise Table Ind",                    r[95:97],      decoder.field_134),
            Field("FIR/UIR Name",                        r[98:123],     decoder.field_125),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.17.2 FIR/UIR Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/UIR Identifier",                  r[6:10],       decoder.field_116),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("FIR/UIR Indicator",                   r[14],         decoder.field_117),
            Field("Sequence Number",                     r[15:19],      decoder.field_012),
            Field("Continuation Record No",              r[19],         decoder.field_016),
            Field("Application Type",                    r[20],         decoder.field_091),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.18 Restrictive Airspace Records (UR)
class RestrictiveAirspace():

    cont_idx = 24
    app_idx = 25

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'T':
                    return self.read_time(line)
                case 'P':
                    return self.read_flight0(line)
                case 'C':
                    return self.read_callsign(line)
                case _:
                    return []

    # 4.1.18.1 Restrictive Airspace Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("ICAO Code",                           r[6:8],        decoder.field_014),
            Field("Restrictive Type",                    r[8],          decoder.field_128),
            Field("Restrictive Airspace Designation",    r[9:19],       decoder.field_129),
            Field("Multiple Code",                       r[19],         decoder.field_130),
            Field("Sequence Number",                     r[20:24],      decoder.field_012),
            Field("Continuation Record No",              r[24],         decoder.field_016),
            Field("Level",                               r[25],         decoder.field_019),
            Field("Time Code",                           r[26],         decoder.field_131),
            Field("NOTAM",                               r[27],         decoder.field_132),
            Field("Boundary Via",                        r[30:32],      decoder.field_118),
            Field("Latitude",                            r[32:41],      decoder.field_036),
            Field("Longitude",                           r[41:51],      decoder.field_037),
            Field("Arc Origin Latitude",                 r[51:60],      decoder.field_036),
            Field("Arc Origin Longitude",                r[60:70],      decoder.field_037),
            Field("Arc Distance",                        r[70:74],      decoder.field_119),
            Field("Arc Bearing",                         r[74:78],      decoder.field_120),
            Field("Lower Limit",                         r[82:86],      decoder.field_121),
            Field("Unit Indicator",                      r[86],         decoder.field_133),
            Field("Upper Limit",                         r[87:92],      decoder.field_121),
            Field("Unit Indicator (2)",                  r[92],         decoder.field_133),
            Field("Restrictive Airspace Name",           r[93:123],     decoder.field_126),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.18.2 Restrictive Airspace Continuation Records
    def read_time(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("ICAO Code",                           r[6:8],        decoder.field_014),
            Field("Restrictive Type",                    r[8],          decoder.field_128),
            Field("Restrictive Airspace Designation",    r[9:19],       decoder.field_129),
            Field("Multiple Code",                       r[19],         decoder.field_130),
            Field("Sequence Number",                     r[20:24],      decoder.field_012),
            Field("Continuation Record No",              r[24],         decoder.field_016),
            Field("Application Type",                    r[25],         decoder.field_091),
            Field("Time Code",                           r[26],         decoder.field_131),
            Field("NOTAM",                               r[27],         decoder.field_132),
            Field("Time Indicator",                      r[27],         decoder.field_138),
            Field("Time of Operations",                  r[29:39],      decoder.field_195),
            Field("Time of Operations (2)",              r[39:49],      decoder.field_195),
            Field("Time of Operations (3)",              r[49:59],      decoder.field_195),
            Field("Time of Operations (4)",              r[59:69],      decoder.field_195),
            Field("Time of Operations (5)",              r[69:79],      decoder.field_195),
            Field("Time of Operations (6)",              r[79:89],      decoder.field_195),
            Field("Time of Operations (7)",              r[89:99],      decoder.field_195),
            Field("Controlling Agency",                  r[99:123],     decoder.field_140),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.18.3 Restrictive Airspace Flight Planning Continuation Record
    def read_flight0(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("ICAO Code",                           r[6:8],        decoder.field_014),
            Field("Restrictive Type",                    r[8],          decoder.field_128),
            Field("Restrictive Airspace Designation",    r[9:19],       decoder.field_129),
            Field("Multiple Code",                       r[19],         decoder.field_130),
            Field("Sequence Number",                     r[20:24],      decoder.field_012),
            Field("Continuation Record No",              r[24],         decoder.field_016),
            Field("Application Type",                    r[25],         decoder.field_091),
            Field("Start/End Indicator",                 r[29],         decoder.field_152),
            Field("Start/End Date",                      r[30:41],      decoder.field_153),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # TODO the spec doesn't show any restrictive airspace callsign continuation records
    # yet several data sets have them... are they from an old spec?
    # ?? Restrictive Airspace Call Sign Continuation Record
    def read_callsign(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("ICAO Code",                           r[6:8],        decoder.field_014),
            Field("Restrictive Type",                    r[8],          decoder.field_128),
            Field("Restrictive Airspace Designation",    r[9:19],       decoder.field_129),
            Field("Multiple Code",                       r[19],         decoder.field_130),
            Field("Sequence Number",                     r[20:24],      decoder.field_012),
            Field("Continuation Record No",              r[24],         decoder.field_016),
            Field("Application Type",                    r[25],         decoder.field_091),
            Field("Time Code",                           r[26],         decoder.field_131),
            Field("NOTAM",                               r[27],         decoder.field_132),
            Field("Time Indicator",                      r[27],         decoder.field_138),
            Field("Time of Operations",                  r[29:39],      decoder.field_195),
            Field("Time of Operations (2)",              r[39:49],      decoder.field_195),
            Field("Time of Operations (3)",              r[49:59],      decoder.field_195),
            Field("Time of Operations (4)",              r[59:69],      decoder.field_195),
            Field("Time of Operations (5)",              r[69:79],      decoder.field_195),
            Field("Time of Operations (6)",              r[79:89],      decoder.field_195),
            Field("Time of Operations (7)",              r[89:99],      decoder.field_195),
            Field("Controlling Agency",                  r[99:123],     decoder.field_140),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.21 Enroute Airways Restriction Records (EU)
class AirwayRestricted():

    def read(self, line):

        if int(line[17]) < 2:
            match line[15:17]:
                case 'AE':
                    return self.primary_altitude_exclude(line)
                case 'TC':
                    return self.primary_cruise_table(line)
                case 'SC':
                    return self.primary_seasonal_closure(line)
                case 'NR':
                    return self.primary_note_restriction(line)
                case _:
                    raise ValueError("Unknown Restricted Airway Type")
        else:
            match line[15:17]:
                case 'AE':
                    return self.cont_altitude_exclude(line)
                case 'TC':
                    return self.cont_cruise_table(line)
                case 'NR':
                    return self.cont_note_restriction(line)
                case _:
                    raise ValueError("Unknown Restricted Airway Type")

    # 4.1.21.1 Enroute Airways Restriction Altitude Exclusion Primary Records
    #
    # Note 1: The standard length for the Route Identifier is
    # five characters. Some users envisage the need for
    # a six-character field. This reserved column will
    # permit this usage.
    #
    def primary_altitude_exclude(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Route Identifier",                        r[6:11],       decoder.field_008),
            Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
            Field("Restriction Type",                        r[15:17],      decoder.field_201),
            Field("Continuation Record No",                  r[17],         decoder.field_016),
            Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
            Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
            Field("Start Fix Section Code",                  r[25:27],      decoder.field_004),
            Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
            Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
            Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
            Field("Start Date",                              r[37:44],      decoder.field_157),
            Field("End Date",                                r[44:51],      decoder.field_157),
            Field("Time Code",                               r[51],         decoder.field_131),
            Field("Time Indicator",                          r[52],         decoder.field_138),
            Field("Time of Operation",                       r[53:63],      decoder.field_195),
            Field("Time of Operation",                       r[63:73],      decoder.field_195),
            Field("Time of Operation",                       r[73:83],      decoder.field_195),
            Field("Time of Operation",                       r[83:93],      decoder.field_195),
            Field("Exclusion Indicator",                     r[93],         decoder.field_202),
            Field("Units of Altitude",                       r[94],         decoder.field_160),
            Field("Restriction Altitude",                    r[95:98],      decoder.field_161),
            Field("Block Indicator",                         r[98],         decoder.field_203),
            Field("Restriction Altitude",                    r[99:102],     decoder.field_161),
            Field("Block Indicator",                         r[102],        decoder.field_203),
            Field("Restriction Altitude",                    r[103:106],    decoder.field_161),
            Field("Block Indicator",                         r[106],        decoder.field_203),
            Field("Restriction Altitude",                    r[107:110],    decoder.field_161),
            Field("Block Indicator",                         r[110],        decoder.field_203),
            Field("Restriction Altitude",                    r[111:114],    decoder.field_161),
            Field("Block Indicator",                         r[114],        decoder.field_203),
            Field("Restriction Altitude",                    r[115:118],    decoder.field_161),
            Field("Block Indicator",                         r[118],        decoder.field_203),
            Field("Restriction Altitude",                    r[119:122],    decoder.field_161),
            Field("Block Indicator",                         r[122],        decoder.field_203),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]

    def cont_altitude_exclude(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Route Identifier",                        r[6:11],       decoder.field_008),
            Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
            Field("Restriction Type",                        r[15:17],      decoder.field_201),
            Field("Continuation Record No",                  r[17],         decoder.field_016),
            Field("Application Type",                        r[18],         decoder.field_091),
            Field("Time Code",                               r[51],         decoder.field_131),
            Field("Time Indicator",                          r[52],         decoder.field_138),
            Field("Time of Operation",                       r[53:63],      decoder.field_195),
            Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
            Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
            Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
            Field("Exclusion Operator",                      r[93],         decoder.field_202),
            Field("Units of Altitude",                       r[94],         decoder.field_160),
            Field("Restriction Altitude",                    r[95:98],      decoder.field_161),
            Field("Block Indicator",                         r[98],         decoder.field_203),
            Field("Restriction Altitude (2)",                r[99:102],     decoder.field_161),
            Field("Block Indicator (2)",                     r[102],        decoder.field_203),
            Field("Restriction Altitude (3)",                r[103:106],    decoder.field_161),
            Field("Block Indicator (3)",                     r[106],        decoder.field_203),
            Field("Restriction Altitude (4)",                r[107:110],    decoder.field_161),
            Field("Block Indicator (4)",                     r[110],        decoder.field_203),
            Field("Restriction Altitude (5)",                r[111:114],    decoder.field_161),
            Field("Block Indicator (5)",                     r[114],        decoder.field_203),
            Field("Restriction Altitude (6)",                r[115:118],    decoder.field_161),
            Field("Block Indicator (6)",                     r[118],        decoder.field_203),
            Field("Restriction Altitude (7)",                r[119:122],    decoder.field_161),
            Field("Block Indicator (7)",                     r[122],        decoder.field_203),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]

    # 4.1.21A.1 Enroute Airways Restriction Note Restriction Primary Records
    #
    # Note 1: The standard length for the Route Identifier is
    # five characters. Some users envisage the need
    # for a six-character field. This reserved column
    # will permit this usage.
    #
    def primary_note_restriction(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Route Identifier",                        r[7:11],       decoder.field_008),
            Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
            Field("Restriction Type",                        r[15:17],      decoder.field_201),
            Field("Continuation Record No",                  r[17],         decoder.field_016),
            Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
            Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
            Field("Start Fix Section Code",                  r[25],         decoder.field_004),
            Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
            Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
            Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
            Field("Start Date",                              r[37:44],      decoder.field_157),
            Field("End Date",                                r[44:51],      decoder.field_157),
            Field("Restriction Notes",                       r[51:120],     decoder.field_163),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]

    # 4.1.21A.2 Enroute Airways Restriction Note Restriction Continuation Records
    def cont_note_restriction(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Route Identifier",                        r[7:11],       decoder.field_008),
            Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
            Field("Restriction Type",                        r[15:17],      decoder.field_201),
            Field("Continuation Record No",                  r[17],         decoder.field_016),
            Field("Application Type",                        r[18],         decoder.field_091),
            Field("Restriction Notes",                       r[51:120],     decoder.field_163),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]

    # 4.1.21B.1 Enroute Airways Restriction Seasonal Closure Primary Records
    #
    # Note 1: The standard length for the Route Identifier is
    # five characters. Some users envisage the need for
    # a six-character field. This reserved column will
    # permit this usage.
    #
    def primary_seasonal_closure(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Route Identifier",                        r[6:11],       decoder.field_008),
            Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
            Field("Restriction Type",                        r[15:17],      decoder.field_201),
            Field("Continuation Record No",                  r[17],         decoder.field_016),
            Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
            Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
            Field("Start Fix Section Code",                  r[25:27],      decoder.field_004),
            Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
            Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
            Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
            Field("Start Date",                              r[37:44],      decoder.field_157),
            Field("End Date",                                r[44:51],      decoder.field_157),
            Field("Time Code",                               r[51],         decoder.field_131),
            Field("Time Indicator",                          r[52],         decoder.field_138),
            Field("Time of Operation",                       r[53:63],      decoder.field_195),
            Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
            Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
            Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
            Field("Cruise Table Ident",                      r[93:95],      decoder.field_134),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]

    # 4.1.21C.1 Enroute Airways Restriction Cruising Table Replacement Primary Records
    #
    # Note 1: The standard length for the Route Identifier is
    # five characters. Some users envisage the need for
    # a six-character field. This reserved column will
    # permit this usage.
    #
    def primary_cruise_table(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Route Identifier",                        r[6:11],       decoder.field_008),
            Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
            Field("Restriction Type",                        r[15:17],      decoder.field_201),
            Field("Continuation Record No",                  r[17],         decoder.field_016),
            Field("Start Fix Identifier",                    r[18:23],      decoder.field_013),
            Field("Start Fix ICAO Code",                     r[23:25],      decoder.field_014),
            Field("Start Fix Section Code",                  r[25:27],      decoder.field_004),
            Field("End Fix Identifier",                      r[27:32],      decoder.field_013),
            Field("End Fix ICAO Code",                       r[32:34],      decoder.field_014),
            Field("End Fix Section Code",                    r[34:36],      decoder.field_004),
            Field("Start Date",                              r[37:44],      decoder.field_157),
            Field("End Date",                                r[44:51],      decoder.field_157),
            Field("Time Code",                               r[51],         decoder.field_131),
            Field("Time Indicator",                          r[52],         decoder.field_138),
            Field("Time of Operation",                       r[53:63],      decoder.field_195),
            Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
            Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
            Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
            Field("Cruise Table Ident",                      r[93:95],      decoder.field_134),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]

    # 4.1.21C.2 Enroute Airways Restriction Cruising Table Replacement Continuation Records
    def cont_cruise_table(self, r):
        return [
            Field("Record Type",                             r[0],          decoder.field_002),
            Field("Customer / Area Code",                    r[1:4],        decoder.field_003),
            Field("Section Code",                            r[4:6],        decoder.field_004),
            Field("Route Identifier",                        r[6:11],       decoder.field_008),
            Field("Restriction Identifier",                  r[12:15],      decoder.field_154),
            Field("Restriction Type",                        r[15:17],      decoder.field_201),
            Field("Continuation Record No",                  r[17],         decoder.field_016),
            Field("Application Type",                        r[18],         decoder.field_091),
            Field("Time Code",                               r[51],         decoder.field_131),
            Field("Time Indicator",                          r[52],         decoder.field_138),
            Field("Time of Operation",                       r[53:63],      decoder.field_195),
            Field("Time of Operation (2)",                   r[63:73],      decoder.field_195),
            Field("Time of Operation (3)",                   r[73:83],      decoder.field_195),
            Field("Time of Operation (4)",                   r[83:93],      decoder.field_195),
            Field("Cruise Table Ident",                      r[93:95],      decoder.field_134),
            Field("File Record No",                          r[123:128],    decoder.field_031),
            Field("Cycle Date",                              r[128:132],    decoder.field_032)
        ]


# 4.1.22 Airport and Heliport MLS (Azimuth, Elevation
# and Back Azimuth) Records
class MLS():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    return []

    # 4.1.22.1 Airport and Heliport MLS Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport Identifier",                  r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("MLS Identifier",                      r[13:17],      decoder.field_044),
            Field("MLS Category",                        r[17],         decoder.field_080),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Channel",                             r[22:25],      decoder.field_166),
            Field("Runway Identifier",                   r[27:32],      decoder.field_046),
            Field("Azimuth Latitude",                    r[32:41],      decoder.field_036),
            Field("Azimuth Longitude",                   r[41:51],      decoder.field_037),
            Field("Azimuth Bearing",                     r[51:55],      decoder.field_167),
            Field("Elevation Latitude",                  r[55:64],      decoder.field_036),
            Field("Elevation Longitude",                 r[64:74],      decoder.field_037),
            Field("Azimuth Position",                    r[74:78],      decoder.field_048),
            Field("Azimuth Position Reference",          r[78],         decoder.field_049),
            Field("Elevation Position",                  r[79:83],      decoder.field_050),
            Field("Azimuth Proportional Angle Right",    r[83:86],      decoder.field_168),
            Field("Azimuth Proportional Angle Left",     r[86:89],      decoder.field_168),
            Field("Azimuth Coverage Right",              r[89:92],      decoder.field_172),
            Field("Azimuth Coverage Left",               r[92:95],      decoder.field_172),
            Field("Elevation Angle Span",                r[95:98],      decoder.field_169),
            Field("Magnetic Variation",                  r[98:103],     decoder.field_039),
            Field("EL Elevation",                        r[103:108],    decoder.field_074),
            Field("Nominal Elevation Angle",             r[108:112],    decoder.field_173),
            Field("Minimum Glide Path Angle",            r[112:115],    decoder.field_052),
            Field("Supporting Facility Identifier",      r[115:119],    decoder.field_033),
            Field("Supporting Facility ICAO Code",       r[119:121],    decoder.field_014),
            Field("Supporting Facility Section",         r[121:123],    decoder.field_004),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.22.2 Airport and Heliport MLS Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport Identifier",                  r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("MLS Identifier",                      r[13:17],      decoder.field_044),
            Field("MLS Category",                        r[17],         decoder.field_080),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("Facility Characteristics",            r[27:32],      decoder.field_093),
            Field("Back Azimuth Latitude",               r[32:41],      decoder.field_036),
            Field("Back Azimuth Longitude",              r[41:51],      decoder.field_037),
            Field("Back Azimuth Bearing",                r[51:55],      decoder.field_167),
            Field("MLS Datum Point Latitude",            r[55:64],      decoder.field_036),
            Field("MLS Datum Point Longitude",           r[64:74],      decoder.field_037),
            Field("Back Azimuth Position",               r[74:78],      decoder.field_048),
            Field("Back Azimuth Position Reference",     r[78],         decoder.field_049),
            Field("Back Azimuth Proportional Angle Right", r[83:86],    decoder.field_168),
            Field("Back Azimuth Proportional Angle Left", r[86:89],     decoder.field_168),
            Field("Back Azimuth Coverage Right",         r[89:92],      decoder.field_172),
            Field("Back Azimuth Coverage Left",          r[92:95],      decoder.field_172),
            Field("Back Azimuth True Bearing",           r[95:98],      decoder.field_094),
            Field("Back Azimuth Bearing Source",         r[100],        decoder.field_095),
            Field("Azimuth True Bearing",                r[101:106],    decoder.field_094),
            Field("Azimuth Bearing Source",              r[106],        decoder.field_095),
            Field("Glide Path Height at Landing Threshold", r[107:109], decoder.field_067),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.23 Enroute Communications Records (EV)
class EnrouteComms():

    cont_idx = 55
    app_idx = 56

    def read(self, r):
        if int(r[self.cont_idx]) < 2:
            return self.read_primary(r)
        else:
            match r[self.app_idx]:
                case ' ':
                    return self.read_cont(r)
                case 'T':
                    return self.read_timeop(r)
                case _:
                    raise ValueError('{}\n{}\n{}'.format("Unknown Application",
                                                         r[self.app_idx], r))

    # 4.1.23.1 Enroute Communications Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/RDO Ident",                       r[6:10],       decoder.field_190),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("Indicator",                           r[14],         decoder.field_117),
            Field("Remote Name",                         r[18:43],      decoder.field_189),
            Field("Communications Type",                 r[43:46],      decoder.field_101),
            Field("Comm Frequency",                      r[46:53],      decoder.field_103),
            Field("Guard/Transmit",                      r[53],         decoder.field_182),
            Field("Frequency Units",                     r[54],         decoder.field_104),
            Field("Continuation Record No",              r[55],         decoder.field_016),
            Field("Service Indicator",                   r[56:59],      decoder.field_106),
            Field("Radar Service",                       r[59],         decoder.field_102),
            Field("Modulation",                          r[60],         decoder.field_198),
            Field("Signal Emission",                     r[61],         decoder.field_199),
            Field("Latitude",                            r[62:71],      decoder.field_036),
            Field("Longitude",                           r[71:81],      decoder.field_037),
            Field("Magnetic Variation",                  r[81:86],      decoder.field_039),
            Field("Facility Elevation",                  r[86:91],      decoder.field_092),
            Field("H24 Indicator",                       r[91],         decoder.field_181),
            Field("Altitude Description",                r[92],         decoder.field_029),
            Field("Communication Altitude",              r[93:98],      decoder.field_184),
            Field("Communication Altitude (2)",          r[98:103],     decoder.field_184),
            Field("Remote Facility",                     r[103:107],    decoder.field_200),
            Field("ICAO Code",                           r[107:109],    decoder.field_014),
            Field("Section Code (2)",                    r[109:111],    decoder.field_004),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.23.2 Enroute Communications Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/RDO Ident",                       r[6:10],       decoder.field_190),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("Indicator",                           r[14],         decoder.field_117),
            Field("Remote Name",                         r[18:43],      decoder.field_189),
            Field("Communications Type",                 r[43:46],      decoder.field_101),
            Field("Comm Frequency",                      r[46:53],      decoder.field_103),
            Field("Guard/Transmit",                      r[53],         decoder.field_182),
            Field("Frequency Units",                     r[54],         decoder.field_104),
            Field("Continuation Record No",              r[55],         decoder.field_016),
            Field("Application Type",                    r[56],         decoder.field_091),
            Field("Time Code",                           r[57],         decoder.field_131),
            Field("NOTAM",                               r[58],         decoder.field_132),
            Field("Time Indicator",                      r[59],         decoder.field_138),
            Field("Time of Operation",                   r[60:70],      decoder.field_195),
            Field("Call Sign",                           r[93:123],     decoder.field_105),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.23.3 Enroute Communications Continuation Records
    def read_timeop(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/RDO Ident",                       r[6:10],       decoder.field_190),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("Indicator",                           r[14],         decoder.field_117),
            Field("Remote Name",                         r[18:43],      decoder.field_189),
            Field("Communications Type",                 r[43:46],      decoder.field_101),
            Field("Comm Frequency",                      r[46:53],      decoder.field_103),
            Field("Guard/Transmit",                      r[53],         decoder.field_182),
            Field("Frequency Units",                     r[54],         decoder.field_104),
            Field("Continuation Record No",              r[55],         decoder.field_016),
            Field("Application Type",                    r[56],         decoder.field_091),
            Field("Time of Operation",                   r[60:70],      decoder.field_195),
            Field("Time of Operation (2)",               r[70:80],      decoder.field_195),
            Field("Time of Operation (3)",               r[80:90],      decoder.field_195),
            Field("Time of Operation (4)",               r[90:100],     decoder.field_195),
            Field("Time of Operation (5)",               r[100:110],    decoder.field_195),
            Field("Time of Operation (6)",               r[110:120],    decoder.field_195),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.24 Preferred Routes Records (ET)
class PreferredRoute():

    cont_idx = 38
    app_idx = 39

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
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


# 4.1.25 Controlled Airspace Records (UC)
#
# The Controlled Airspace Record file contains a
# sequential listing of vertical and lateral limits of all types
# and classifications of Controlled Airspace. It includes
# Controlled Airspace associated with Airports and
# Heliports.
#
class ControlledAirspace():

    cont_idx = 24
    app_idx = 25

    def read(self, r) -> list:
        if int(r[self.cont_idx]) < 2:
            return self.read_primary(r)
        else:
            match r[self.app_idx]:
                case 'A':
                    return self.read_cont(r)
                case _:
                    return []

    # 4.1.25.1 Controlled Airspace Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("ICAO Code",                           r[6:8],        decoder.field_014),
            Field("Airspace Type",                       r[9],          decoder.field_213),
            Field("Airspace Center",                     r[9:14],       decoder.field_214),
            Field("Section Code (2)",                    r[14:16],      decoder.field_004),
            Field("Airspace Classification",             r[16],         decoder.field_215),
            Field("Multiple Code",                       r[19],         decoder.field_130),
            Field("Sequence Number",                     r[20:24],      decoder.field_012),
            Field("Continuation Record No",              r[24],         decoder.field_016),
            Field("Level",                               r[25],         decoder.field_019),
            Field("Time Code",                           r[26],         decoder.field_131),
            Field("NOTAM",                               r[27],         decoder.field_132),
            Field("Boundary Via",                        r[30:32],      decoder.field_118),
            Field("Latitude",                            r[32:41],      decoder.field_036),
            Field("Longitude",                           r[41:51],      decoder.field_037),
            Field("Arc Origin Latitude",                 r[51:60],      decoder.field_036),
            Field("Arc Origin Longitude",                r[60:70],      decoder.field_037),
            Field("Arc Distance",                        r[70:74],      decoder.field_119),
            Field("Arc Bearing",                         r[74:78],      decoder.field_120),
            Field("RNP",                                 r[78:81],      decoder.field_211),
            Field("Lower Limit",                         r[81:86],      decoder.field_121),
            Field("Unit Indicator",                      r[86],         decoder.field_133),
            Field("Upper Limit",                         r[87:92],      decoder.field_121),
            Field("Unit Indicator (2)",                  r[92],         decoder.field_133),
            Field("Controlled Airspace Name",            r[93:123],     decoder.field_216),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.25.2 Controlled Airspace Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("ICAO Code",                           r[6:8],        decoder.field_014),
            Field("Airspace Type",                       r[9],          decoder.field_213),
            Field("Airspace Center",                     r[9:14],       decoder.field_214),
            Field("Section Code (2)",                    r[14:16],      decoder.field_004),
            Field("Airspace Classification",             r[16],         decoder.field_215),
            Field("Multiple Code",                       r[19],         decoder.field_130),
            Field("Sequence Number",                     r[20:24],      decoder.field_012),
            Field("Continuation Record No",              r[24],         decoder.field_016),
            Field("Application Type",                    r[25],         decoder.field_091),
            Field("Time Code",                           r[26],         decoder.field_131),
            Field("NOTAM",                               r[27],         decoder.field_132),
            Field("Time Indicator",                      r[28],         decoder.field_138),
            Field("Time of Operations",                  r[29:39],      decoder.field_195),
            Field("Time of Operations (2)",              r[39:49],      decoder.field_195),
            Field("Time of Operations (3)",              r[49:59],      decoder.field_195),
            Field("Time of Operations (4)",              r[59:69],      decoder.field_195),
            Field("Time of Operations (5)",              r[69:79],      decoder.field_195),
            Field("Time of Operations (6)",              r[79:89],      decoder.field_195),
            Field("Time of Operations (7)",              r[89:99],      decoder.field_195),
            Field("Controlling Agency",                  r[99:123],     decoder.field_140),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.26 Geographical Reference Table Records (TG)
#
# The Geographical Reference Table file contains information
# that permits the cross referencing of otherwise undefined
# geographical entities and Route Identifiers in the Preferred
# Route file. The contents are not standardized and may vary
# from data supplier to data supplier. The contents of such a
# file can only be used in conjunction with the Preferred
# Route file of the same database in which the file is
# presented.
#
class GeoReferenceTable():

    cont_idx = 38
    app_idx = 39

    def read(self, r) -> list:
        if int(r[self.cont_idx]) < 2:
            return self.read_primary(r)
        else:
            match r[self.app_idx]:
                case 'A':
                    return self.read_cont(r)
                case _:
                    return []

    # 4.1.26.1 Geographical Reference Table Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                        r[0],           decoder.field_002),
            Field("Customer / Area Code",               r[1:4],         decoder.field_003),
            Field("Section Code",                       r[4:6],         decoder.field_004),
            Field("Geographical Ref Table ID",          r[6:8],         decoder.field_218),
            Field("Sequence Number",                    r[8],           decoder.field_012),
            Field("Geographical Entity",                r[9:38],        decoder.field_219),
            Field("Continuation Record No",             r[38],          decoder.field_016),
            Field("Preferred Route Ident",              r[40:50],       decoder.field_008),
            Field("Preferred Route Use Ind",            r[50:52],       decoder.field_220),
            Field("Preferred Route Ident (2)",          r[52:62],       decoder.field_008),
            Field("Preferred Route Use Ind (2)",        r[62:64],       decoder.field_220),
            Field("Preferred Route Ident (3)",          r[64:74],       decoder.field_008),
            Field("Preferred Route Use Ind (3)",        r[74:76],       decoder.field_220),
            Field("Preferred Route Ident (4)",          r[76:86],       decoder.field_008),
            Field("Preferred Route Use Ind (4)",        r[86:88],       decoder.field_220),
            Field("Preferred Route Ident (4)",          r[88:98],       decoder.field_008),
            Field("Preferred Route Use Ind (4)",        r[98:100],      decoder.field_220),
            Field("Preferred Route Ident (5)",          r[100:110],     decoder.field_008),
            Field("Preferred Route Use Ind (5)",        r[110:112],     decoder.field_220),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.26.2 Geographical Reference Table Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                        r[0],           decoder.field_002),
            Field("Customer / Area Code",               r[1:4],         decoder.field_003),
            Field("Section Code",                       r[4:6],         decoder.field_004),
            Field("Geographical Ref Table ID",          r[6:8],         decoder.field_218),
            Field("Sequence Number",                    r[8],           decoder.field_012),
            Field("Geographical Entity",                r[9:38],        decoder.field_219),
            Field("Continuation Record No",             r[38],          decoder.field_016),
            Field("Application Type",                   r[39],          decoder.field_091),
            Field("File Record No",                     r[123:128],     decoder.field_031),
            Field("Cycle Date",                         r[128:132],     decoder.field_032)
        ]


# 4.1.27 Flight Planning Arrival/Departure Data Records (PR)
class FlightPlanning():

    cont_idx = 69
    app_idx = 70

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'T':
                    return self.read_timeop(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    # 4.1.27.1 Flight Planning Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                     r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_009),
            Field("Procedure Type",                         r[19],          decoder.field_230),
            Field("Runway Transition Identifier",           r[20:25],       decoder.field_011),
            Field("Runway Transition Fix",                  r[25:30],       decoder.field_013),
            Field("ICAO Code (2)",                          r[30:32],       decoder.field_014),
            Field("Section Code (2)",                       r[32:34],       decoder.field_004),
            Field("Runway Transition Along Track Dist",     r[34:37],       decoder.field_231),
            Field("Common Segment Transition Fix",          r[37:42],       decoder.field_013),
            Field("ICAO Code (3)",                          r[42:44],       decoder.field_014),
            Field("Section Code (3)",                       r[44:46],       decoder.field_004),
            Field("Common Segment Along Track Dist",        r[46:49],       decoder.field_231),
            Field("Enroute Transition Identifier",          r[49:54],       decoder.field_011),
            Field("Enroute Transition Fix",                 r[54:59],       decoder.field_013),
            Field("ICAO Code (4)",                          r[59:61],       decoder.field_014),
            Field("Section Code (4)",                       r[61:63],       decoder.field_004),
            Field("Enroute Transition Along Track Dist",    r[63:66],       decoder.field_231),
            Field("Sequence Number",                        r[66:69],       decoder.field_012),
            Field("Continuation Number",                    r[69],          decoder.field_016),
            Field("Number of Engines",                      r[70:74],       decoder.field_232),
            Field("Turboprop/Jet Indicator",                r[74],          decoder.field_233),
            Field("RNAV Flag",                              r[75],          decoder.field_234),
            Field("ATC Weight Category",                    r[76],          decoder.field_235),
            Field("ATC Identifier",                         r[77:84],       decoder.field_236),
            Field("Time Code",                              r[84],          decoder.field_131),
            Field("Procedure Description",                  r[85:100],      decoder.field_237),
            Field("Leg Type Code",                          r[100:102],     decoder.field_238),
            Field("Reporting Code",                         r[102],         decoder.field_239),
            Field("Initial Departure Magnetic Course",      r[103:107],     decoder.field_026),
            Field("Altitude Description",                   r[107],         decoder.field_029),
            Field("Altitude",                               r[108:111],     decoder.field_240),
            Field("Altitude (2)",                           r[111:114],     decoder.field_240),
            Field("Speed Limit",                            r[114:117],     decoder.field_072),
            Field("Initial Cruise Table",                   r[117:119],     decoder.field_134),
            Field("Speed Limit Description",                r[119],         decoder.field_261),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]

    # 4.1.27.2 Flight Planning Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                     r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_009),
            Field("Procedure Type",                         r[19],          decoder.field_230),
            Field("Runway Transition Identifier",           r[20:25],       decoder.field_011),
            Field("Runway Transition Fix",                  r[25:30],       decoder.field_013),
            Field("ICAO Code (2)",                          r[30:32],       decoder.field_014),
            Field("Section Code (2)",                       r[32:34],       decoder.field_004),
            Field("Runway Transition Along Track Dist",     r[34:37],       decoder.field_231),
            Field("Common Segment Transition Fix",          r[37:42],       decoder.field_013),
            Field("ICAO Code (3)",                          r[42:44],       decoder.field_014),
            Field("Section Code (3)",                       r[44:46],       decoder.field_004),
            Field("Common Segment Along Track Dist",        r[46:49],       decoder.field_231),
            Field("Enroute Transition Identifier",          r[49:54],       decoder.field_011),
            Field("Enroute Transition Fix",                 r[54:59],       decoder.field_013),
            Field("ICAO Code (4)",                          r[59:61],       decoder.field_014),
            Field("Section Code (4)",                       r[61:63],       decoder.field_004),
            Field("Enroute Transition Along Track Dist",    r[63:66],       decoder.field_231),
            Field("Sequence Number",                        r[66:69],       decoder.field_012),
            Field("Continuation Number",                    r[69],          decoder.field_016),
            Field("Application Type",                       r[70],          decoder.field_091),
            Field("Intermediate Fix Identifier",            r[71:76],       decoder.field_013),
            Field("ICAO Code (5)",                          r[76:78],       decoder.field_014),
            Field("Section Code (5)",                       r[91:93],       decoder.field_004),
            Field("Intermediate Distance",                  r[106:109],     decoder.field_231),
            Field("Fix Related Transition Code",            r[109],         decoder.field_241),
            Field("Intermediate Fix Identifier",            r[110:115],     decoder.field_013),
            Field("ICAO Code (6)",                          r[115:117],     decoder.field_014),
            Field("Section Code (6)",                       r[118],         decoder.field_004),
            Field("Intermediate Distance",                  r[119:122],     decoder.field_231),
            Field("Fix Related Transition Code",            r[122],         decoder.field_241),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]

    # 4.1.27.3 Flight Planning Continuation Records
    def read_timeop(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                     r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_009),
            Field("Procedure Type",                         r[19],          decoder.field_230),
            Field("Runway Transition Identifier",           r[20:25],       decoder.field_011),
            Field("Runway Transition Fix",                  r[25:30],       decoder.field_013),
            Field("ICAO Code (2)",                          r[30:32],       decoder.field_014),
            Field("Section Code (2)",                       r[32:34],       decoder.field_004),
            Field("Runway Transition Along Track Dist",     r[34:37],       decoder.field_231),
            Field("Common Segment Transition Fix",          r[37:42],       decoder.field_013),
            Field("ICAO Code (3)",                          r[42:44],       decoder.field_014),
            Field("Section Code (3)",                       r[44:46],       decoder.field_004),
            Field("Common Segment Along Track Dist",        r[46:49],       decoder.field_231),
            Field("Enroute Transition Identifier",          r[49:54],       decoder.field_011),
            Field("Enroute Transition Fix",                 r[54:59],       decoder.field_013),
            Field("ICAO Code (4)",                          r[59:61],       decoder.field_014),
            Field("Section Code (4)",                       r[61:63],       decoder.field_004),
            Field("Enroute Transition Along Track Dist",    r[63:66],       decoder.field_231),
            Field("Sequence Number",                        r[66:69],       decoder.field_012),
            Field("Continuation Number",                    r[69],          decoder.field_016),
            Field("Application Type",                       r[70],          decoder.field_091),
            Field("Time Code",                              r[71],          decoder.field_131),
            Field("Time Indicator",                         r[72],          decoder.field_138),
            Field("Time of Operation",                      r[73:83],       decoder.field_195),
            Field("Time of Operation (1)",                  r[83:93],       decoder.field_195),
            Field("Time of Operation (2)",                  r[93:103],      decoder.field_195),
            Field("Time of Operation (3)",                  r[103:113],     decoder.field_195),
            Field("Time of Operation (4)",                  r[113:123],     decoder.field_195),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]


# 4.1.29 GLS Record (PT)
class GLS():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    # 4.1.29.1 GLS Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport and Heliport Identifier",     r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("GLS Ref Path Identifier",             r[13:17],      decoder.field_044),
            Field("GLS Category",                        r[17],         decoder.field_080),
            Field("Continuation Record No",              r[18:21],      decoder.field_016),
            Field("GLS Channel",                         r[22:27],      decoder.field_244),
            Field("Runway Identifier",                   r[27:32],      decoder.field_046),
            Field("GLS Approach Bearing",                r[51:55],      decoder.field_047),
            Field("Station Latitude",                    r[55:64],      decoder.field_036),
            Field("Station Longitude",                   r[64:74],      decoder.field_037),
            Field("GLS Station Ident",                   r[74:78],      decoder.field_243),
            Field("Service Volume Radius",               r[83:85],      decoder.field_245),
            Field("TDMA Slots",                          r[85:87],      decoder.field_246),
            Field("GLS Approach Slope",                  r[87:90],      decoder.field_052),
            Field("Magnetic Variation",                  r[90:95],      decoder.field_039),
            Field("Station Elevation",                   r[97:102],     decoder.field_074),
            Field("Datum Code",                          r[102:105],    decoder.field_197),
            Field("Station Type",                        r[105:108],    decoder.field_247),
            Field("Station Elevation WGS",               r[110:115],    decoder.field_248),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.1.29.2 GLS Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Airport and Heliport Identifier",     r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("GLS Ref Path Identifier",             r[13:17],      decoder.field_044),
            Field("GLS Category",                        r[17],         decoder.field_080),
            Field("Continuation Record No",              r[18:21],      decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


# 4.1.30 Alternate Record (RA)
class AlternateRecord():

    # 4.1.30.1 Alternate Primary Records
    def read(self, r):
        return [
            Field("Record Type",                            r[0],          decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],        decoder.field_003),
            Field("Section Code",                           r[4:6],        decoder.field_004),
            Field("Alternate Related Airport to Fix",       r[6:11],       decoder.field_075),
            Field("Alternate Related ICAO Code",            r[11:13],      decoder.field_014),
            Field("Alternate Section",                      r[13:15],      decoder.field_004),
            Field("Alternate Record Type",                  r[15:17],      decoder.field_250),
            Field("Distance to Alternate",                  r[19:22],      decoder.field_251),
            Field("Alternate Type",                         r[22],         decoder.field_252),
            Field("Primary Alternate Identifier",           r[23:33],      decoder.field_253),
            Field("Distance to Alternate (2)",              r[35:38],      decoder.field_251),
            Field("Alternate Type (2)",                     r[38],         decoder.field_252),
            Field("Additional Alternate Identifier One",    r[39:49],      decoder.field_253),
            Field("Distance to Alternate (3)",              r[51:54],      decoder.field_251),
            Field("Alternate Type (3)",                     r[54],         decoder.field_252),
            Field("Additional Alternate Identifier Two",    r[55:65],      decoder.field_253),
            Field("Distance to Alternate (3)",              r[67:70],      decoder.field_251),
            Field("Alternate Type (3)",                     r[70],         decoder.field_252),
            Field("Additional Alternate Identifier (3))",   r[71:81],      decoder.field_253),
            Field("Distance to Alternate (4)",              r[83:86],      decoder.field_251),
            Field("Alternate Type (4)",                     r[86],         decoder.field_252),
            Field("Additional Alternate Identifier (4)",    r[87:97],      decoder.field_253),
            Field("Distance to Alternate (5)",              r[99:102],     decoder.field_251),
            Field("Alternate Type (5)",                     r[102],        decoder.field_252),
            Field("Additional Alternate Identifier (5)",    r[103:113],    decoder.field_253),
            Field("File Record No",                         r[123:128],    decoder.field_031),
            Field("Cycle Date",                             r[128:132],    decoder.field_032)
        ]


# 4.1.31 Airport TAA (PK)
class TAA():

    cont_idx = 38
    app_idx = 39

    def __init__(self, heliport=False):
        self.heliport = heliport
        if self.heliport is False:
            self.id_name = "Airport Identifier"
        else:
            self.id_name = "Heliport Identifier"

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    # 4.1.31.1 Airport TAA Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                        r[0],           decoder.field_002),
            Field("Customer / Area Code",               r[1:4],         decoder.field_003),
            Field("Section Code",                       r[4]+r[12],     decoder.field_004),
            Field(self.id_name,                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                          r[10:12],       decoder.field_014),
            Field("Approach Identifier",                r[13:19],       decoder.field_010),
            Field("TAA Sector Identifier",              r[19],          decoder.field_272),
            Field("TAA Procedure Turn",                 r[20:24],       decoder.field_271),
            Field("TAA IAF Waypoint",                   r[29:34],       decoder.field_273),
            Field("ICAO Code (2)",                      r[10:12],       decoder.field_014),
            Field("Section Code (2)",                   r[36:38],       decoder.field_004),
            Field("Continuation Record No",             r[38],          decoder.field_016),
            Field("Mag/True Indicator",                 r[40],          decoder.field_165),
            Field("Sector Radius",                      r[41:45],       decoder.field_274),
            Field("Sector Bearing",                     r[45:51],       decoder.field_146),
            Field("Sector Minimum Altitude",            r[51:54],       decoder.field_147),
            Field("Sector Radius (2)",                  r[54:58],       decoder.field_274),
            Field("Sector Bearing (2)",                 r[58:64],       decoder.field_146),
            Field("Sector Minimum Altitude (2)",        r[64:67],       decoder.field_147),
            Field("Sector Radius (3)",                  r[67:71],       decoder.field_274),
            Field("Sector Bearing (3)",                 r[71:77],       decoder.field_146),
            Field("Sector Minimum Altitude (3)",        r[77:80],       decoder.field_147),
            Field("Sector Radius (4)",                  r[80:84],       decoder.field_274),
            Field("Sector Bearing (4)",                 r[84:90],       decoder.field_146),
            Field("Sector Minimum Altitude (4)",        r[90:93],       decoder.field_147),
            Field("Sector Radius (5)",                  r[93:97],       decoder.field_274),
            Field("Sector Bearing (5)",                 r[97:103],      decoder.field_146),
            Field("Sector Minimum Altitude (5)",        r[103:106],     decoder.field_147),
            Field("Sector Radius (6)",                  r[106:110],     decoder.field_274),
            Field("Sector Bearing (6)",                 r[110:116],     decoder.field_146),
            Field("Sector Minimum Altitude (6)",        r[116:119],     decoder.field_147),
            Field("File Record No",                     r[123:128],     decoder.field_031),
            Field("Cycle Date",                         r[128:132],     decoder.field_032)
        ]

    # 4.1.31.2 Airport Terminal Arrival Altitude Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                        r[0],           decoder.field_002),
            Field("Customer / Area Code",               r[1:4],         decoder.field_003),
            Field("Section Code",                       r[4]+r[12],     decoder.field_004),
            Field(self.id_name,                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                          r[10:12],       decoder.field_014),
            Field("Approach Identifier",                r[13:19],       decoder.field_010),
            Field("TAA Sector Identifier",              r[19],          decoder.field_272),
            Field("TAA Procedure Turn",                 r[20:24],       decoder.field_271),
            Field("TAA IAF Waypoint",                   r[29:34],       decoder.field_273),
            Field("ICAO Code (2)",                      r[10:12],       decoder.field_014),
            Field("Section Code (2)",                   r[36:38],       decoder.field_004),
            Field("Continuation Record No",             r[38],          decoder.field_016),
            Field("Application Notes",                  r[39],          decoder.field_091),
            Field("Notes",                              r[50:109],      decoder.field_061),
            Field("File Record No",                     r[123:128],     decoder.field_031),
            Field("Cycle Date",                         r[128:132],     decoder.field_032)
        ]


class Heliport():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'P':
                    return self.read_flight0(line)
                case 'Q':
                    return self.read_flight1(line)
                case _:
                    raise ValueError('Unknown Application Type')

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


# 4.2.2 Heliport Terminal Waypoint Records (HC)
class HeliportTerminalWaypoint():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
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


# 4.2.5 Heliport Communications Records (HV)
class HeliportComms():

    cont_idx = 25
    app_idx = 26

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'T':
                    return self.read_timeop(line)
                case _:
                    raise ValueError('Unknown Application Type')

    # 4.2.5.1 Heliport Communications Primary Records
    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
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
            Field("Longitude",                           r[41:51],      decoder.field_036),
            Field("Magnetic Variation",                  r[51:56],      decoder.field_039),
            Field("Facility Elevation",                  r[56:61],      decoder.field_092),
            Field("H24 Indicator",                       r[61],         decoder.field_181),
            Field("Sectorization",                       r[62:68],      decoder.field_183),
            Field("Altitude Description",                r[68],         decoder.field_029),
            Field("Communication Altitude",              r[69:74],      decoder.field_184),
            Field("Communication Altitude (2)",          r[74:79],      decoder.field_184),
            Field("Sector Facility",                     r[79:83],      decoder.field_185),
            Field("ICAO Code (2)",                       r[83:85],      decoder.field_014),
            Field("Section Code (2)",                    r[85:87],      decoder.field_004),
            Field("Distance Description",                r[87],         decoder.field_187),
            Field("Communications Distance",             r[88:90],      decoder.field_188),
            Field("Remote Facility",                     r[90:94],      decoder.field_200),
            Field("ICAO Code (3)",                       r[94:96],      decoder.field_014),
            Field("Section Code (3)",                    r[96:98],      decoder.field_004),
            Field("Call Sign",                           r[98:123],     decoder.field_105),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    # 4.2.5.2 Heliport Communications Continuation Records
    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
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

    # 4.2.5.3 Heliport Communications Continuation Records
    def read_timeop(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field("Heliport Identifier",                 r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Communications Type",                 r[13:16],      decoder.field_101),
            Field("Communications Freq",                 r[16:23],      decoder.field_103),
            Field("Guard/Transmit",                      r[23],         decoder.field_182),
            Field("Frequency Units",                     r[24],         decoder.field_104),
            Field("Continuation Record No",              r[25],         decoder.field_016),
            Field("Application Type",                    r[26],         decoder.field_091),
            Field("Time Code",                           r[27],         decoder.field_131),
            Field("NOTAM",                               r[28],         decoder.field_132),
            Field("Time Indicator",                      r[29],         decoder.field_138),
            Field("Time of Operation",                   r[30:40],      decoder.field_195),
            Field("Time of Operation (2)",               r[40:50],      decoder.field_195),
            Field("Time of Operation (3)",               r[50:60],      decoder.field_195),
            Field("Time of Operation (4)",               r[60:70],      decoder.field_195),
            Field("Time of Operation (5)",               r[70:80],      decoder.field_195),
            Field("Time of Operation (6)",               r[80:90],      decoder.field_195),
            Field("Time of Operation (7)",               r[90:100],     decoder.field_195),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


class LocalizerGlideslope():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'S':
                    return self.read_sim(line)
                case _:
                    raise ValueError("Unsupported Localizer/Glideslope record")
                    # return self.read_flight1(line)

    def read_primary(self, r):
        return [
            Field("Record Type",                                r[0],          decoder.field_002),
            Field("Customer / Area Code",                       r[1:4],        decoder.field_003),
            Field("Section Code",                               r[4]+r[12],    decoder.field_004),
            Field("Airport Identifier",                         r[6:10],       decoder.field_006),
            Field("ICAO Code",                                  r[10:12],      decoder.field_014),
            Field("Localizer Identifier",                       r[13:17],      decoder.field_044),
            Field("ILS Category",                               r[17],         decoder.field_080),
            Field("Continuation Record No",                     r[21],         decoder.field_016),
            Field("Localizer Frequency",                        r[22:27],      decoder.field_045),
            Field("Runway Identifier",                          r[27:32],      decoder.field_046),
            Field("Localizer Latitude",                         r[32:41],      decoder.field_036),
            Field("Localizer Longitude",                        r[41:51],      decoder.field_037),
            Field("Localizer Bearing",                          r[51:55],      decoder.field_047),
            Field("Glide Slope Latitude",                       r[55:64],      decoder.field_036),
            Field("Glide Slope Longitude",                      r[64:74],      decoder.field_037),
            Field("Localizer Position",                         r[74:78],      decoder.field_048),
            Field("Localizer Position Reference",               r[78],         decoder.field_049),
            Field("Glide Slope Position",                       r[79:83],      decoder.field_050),
            Field("Localizer Width",                            r[83:87],      decoder.field_051),
            Field("Glide Slope Angle",                          r[87:90],      decoder.field_052),
            Field("Station Declination",                        r[90:95],      decoder.field_066),
            Field("Glide Slope Height at Landing Threshold",    r[95:97],      decoder.field_067),
            Field("Glide Slope Elevation",                      r[97:102],     decoder.field_074),
            Field("Supporting Facility ID Note 1",              r[102:106],    decoder.field_033),
            Field("Supporting Facility ICAO Code Note 1",       r[106:108],    decoder.field_014),
            Field("Supporting Facility Section Code Note 1",    r[108:110],    decoder.field_004),
            Field("File Record No",                             r[123:128],    decoder.field_031),
            Field("Cycle Date",                                 r[128:132],    decoder.field_032)
        ]

    def read_cont(self, r):
        return [
            Field("Record Type",                                r[0],           decoder.field_002),
            Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
            Field("Section Code",                               r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                                  r[10:12],       decoder.field_014),
            Field("Localizer Identifier",                       r[13:17],       decoder.field_044),
            Field("ILS Category",                               r[17],          decoder.field_080),
            Field("Continuation Record No",                     r[21],          decoder.field_016),
            Field("Notes",                                      r[23:92],       decoder.field_061),
            Field("File Record No",                             r[123:128],     decoder.field_031),
            Field("Cycle Date",                                 r[128:132],     decoder.field_032)
        ]

    def read_sim(self, r):
        return [
            Field("Record Type",                                r[0],           decoder.field_002),
            Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
            Field("Section Code",                               r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                                  r[10:12],       decoder.field_014),
            Field("Localizer Identifier",                       r[13:17],       decoder.field_044),
            Field("ILS Category",                               r[17],          decoder.field_080),
            Field("Continuation Record No",                     r[21],          decoder.field_016),
            Field("Application Type",                           r[22],          decoder.field_091),

            Field("Facility Characteristics",                   r[27:32],       decoder.field_093),
            Field("Localizer True Bearing",                     r[51:56],       decoder.field_094),
            Field("Localizer Bearing Source",                   r[56],          decoder.field_095),
            Field("Glide Slope Beam Width",                     r[87:90],       decoder.field_096),
            Field("Approach Route Ident",                       r[90:96],       decoder.field_010),
            Field("Approach Route Ident (2)",                   r[96:102],      decoder.field_010),
            Field("Approach Route Ident (3)",                   r[102:108],     decoder.field_010),
            Field("Approach Route Ident (4)",                   r[108:114],     decoder.field_010),
            Field("Approach Route Ident (5)",                   r[114:120],     decoder.field_010),
            Field("File Record No",                             r[123:128],     decoder.field_031),
            Field("Cycle Date",                                 r[128:132],     decoder.field_032),
        ]

    # def read_flight1(self, r):
    #     return [
    #         Field("Record Type",                                r[0],           decoder.field_000),
    #         Field("Customer / Area Code",                       r[1:4],         decoder.field_000),
    #         Field("Section Code",                               r[4]+r[12],     decoder.field_000),
    #         Field("Airport Identifier",                         r[6:10],        decoder.field_000),
    #         Field("ICAO Code",                                  r[10:12],       decoder.field_000),
    #         Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_000),
    #         Field("Route Type",                                 r[19],          decoder.field_000),
    #         Field("Transition Identifier",                      r[20:25],       decoder.field_000),
    #         Field("Sequence Number",                            r[26:29],       decoder.field_000),
    #         Field("Fix Identifier",                             r[29:34],       decoder.field_000),
    #         Field("ICAO Code (2)",                              r[34:36],       decoder.field_000),
    #         Field("Section Code (2)",                           r[36:38],       decoder.field_000),
    #         Field("Continuation Record No",                     r[38],          decoder.field_000),
    #         Field("Application Type",                           r[39],          decoder.field_000),
    #         Field("Start/End Indicator",                        r[40],          decoder.field_000),
    #         Field("Start/End Date",                             r[41:45],       decoder.field_000),
    #         Field("Leg Distance",                               r[74:78],       decoder.field_000),
    #         Field("File Record No",                             r[123:128],     decoder.field_000),
    #         Field("Cycle Date",                                 r[128:132],     decoder.field_000)
    #     ]


class MORA():

    def read(self, line):
        return self.read_primary(line)

    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("Starting Latitude",                   r[13:16],      decoder.field_141),
            Field("Starting Longitude",                  r[16:20],      decoder.field_142),
            Field("MORA",                                r[30:33],      decoder.field_143),
            Field("MORA (2)",                            r[33:36],      decoder.field_143),
            Field("MORA (3)",                            r[36:39],      decoder.field_143),
            Field("MORA (4)",                            r[39:42],      decoder.field_143),
            Field("MORA (5)",                            r[42:45],      decoder.field_143),
            Field("MORA (6)",                            r[45:48],      decoder.field_143),
            Field("MORA (7)",                            r[48:51],      decoder.field_143),
            Field("MORA (8)",                            r[51:54],      decoder.field_143),
            Field("MORA (9)",                            r[54:57],      decoder.field_143),
            Field("MORA (10)",                           r[57:60],      decoder.field_143),
            Field("MORA (11)",                           r[60:63],      decoder.field_143),
            Field("MORA (12)",                           r[63:66],      decoder.field_143),
            Field("MORA (13)",                           r[66:69],      decoder.field_143),
            Field("MORA (14)",                           r[69:72],      decoder.field_143),
            Field("MORA (15)",                           r[72:75],      decoder.field_143),
            Field("MORA (16)",                           r[75:78],      decoder.field_143),
            Field("MORA (17)",                           r[78:81],      decoder.field_143),
            Field("MORA (18)",                           r[81:84],      decoder.field_143),
            Field("MORA (19)",                           r[84:87],      decoder.field_143),
            Field("MORA (21)",                           r[87:90],      decoder.field_143),
            Field("MORA (22)",                           r[90:93],      decoder.field_143),
            Field("MORA (23)",                           r[93:96],      decoder.field_143),
            Field("MORA (24)",                           r[96:99],      decoder.field_143),
            Field("MORA (25)",                           r[99:102],     decoder.field_143),
            Field("MORA (26)",                           r[102:105],    decoder.field_143),
            Field("MORA (27)",                           r[105:108],    decoder.field_143),
            Field("MORA (28)",                           r[108:111],    decoder.field_143),
            Field("MORA (29)",                           r[111:114],    decoder.field_143),
            Field("MORA (30)",                           r[114:117],    decoder.field_143),
            Field("MORA (31)",                           r[117:120],    decoder.field_143),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


class MSA():

    cont_idx = 38
    app_idx = 39

    def __init__(self, heliport) -> None:
        self.heliport = heliport
        if self.heliport is False:
            self.id_name = "Airport Identifier"
        else:
            self.id_name = "Heliport Identifier"

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    raise ValueError("Unsupported MLS record")

    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field(self.id_name,                          r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("MSA Center",                          r[13:17],      decoder.field_144),
            Field("ICAO Code (2)",                       r[18:20],      decoder.field_014),
            Field("Section Code (2)",                    r[20:22],      decoder.field_004),
            Field("Multiple Code",                       r[22],         decoder.field_130),
            Field("Continuation Record No",              r[38],         decoder.field_016),
            Field("Sector Bearing",                      r[42:48],      decoder.field_146),
            Field("Sector Altitude",                     r[48:51],      decoder.field_147),
            Field("Sector Radius",                       r[51:53],      decoder.field_145),
            Field("Sector Bearing (2)",                  r[53:59],      decoder.field_146),
            Field("Sector Altitude (2)",                 r[59:62],      decoder.field_147),
            Field("Sector Radius (2)",                   r[62:64],      decoder.field_145),
            Field("Sector Bearing (3)",                  r[64:70],      decoder.field_146),
            Field("Sector Altitude (3)",                 r[70:73],      decoder.field_147),
            Field("Sector Radius (3)",                   r[73:75],      decoder.field_145),
            Field("Sector Bearing (4)",                  r[75:81],      decoder.field_146),
            Field("Sector Altitude (4)",                 r[81:84],      decoder.field_147),
            Field("Sector Radius (4)",                   r[84:86],      decoder.field_145),
            Field("Sector Bearing (5)",                  r[86:92],      decoder.field_146),
            Field("Sector Altitude (5)",                 r[92:95],      decoder.field_147),
            Field("Sector Radius (5)",                   r[95:97],      decoder.field_145),
            Field("Sector Bearing (6)",                  r[97:103],     decoder.field_146),
            Field("Sector Altitude (6)",                 r[103:106],    decoder.field_147),
            Field("Sector Radius (6)",                   r[106:108],    decoder.field_145),
            Field("Sector Bearing (7)",                  r[108:114],    decoder.field_146),
            Field("Sector Altitude (7)",                 r[114:117],    decoder.field_147),
            Field("Sector Radius (7)",                   r[117:119],    decoder.field_145),
            Field("Magnetic/True Bearing",               r[119],        decoder.field_165),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4]+r[12],    decoder.field_004),
            Field(self.id_name,                          r[6:10],       decoder.field_006),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("MSA Center",                          r[13:17],      decoder.field_144),
            Field("ICAO Code (2)",                       r[18:20],      decoder.field_014),
            Field("Section Code (2)",                    r[20:22],      decoder.field_004),
            Field("Multiple Code",                       r[22],         decoder.field_130),
            Field("Continuation Record No",              r[38],         decoder.field_016),
            Field("Application Type",                    r[39],         decoder.field_091),
            Field("Notes",                               r[40:109],     decoder.field_061),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]


class NDBNavaid():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'P':
                    return self.read_flight_plan0(line)
                case 'Q':
                    return self.read_flight_plan1(line)
                case 'S':
                    return self.read_sim(line)
                case _:
                    raise ValueError('Unknown NDB MAVAID Application Type')

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


class VHFNavaid():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'L':
                    return self.read_lim(line)
                case 'P':
                    return self.read_flight_plan0(line)
                case 'S':
                    return self.read_sim(line)
                case _:
                    return self.read_flight_plan1(line)

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


class PathPoint():

    cont_idx = 26
    app_idx = 27

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'E':
                    return self.read_ext(line)
                case _:
                    raise ValueError("bad path point", line[self.app_idx])

    def read_primary(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                     r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("Approach Procedure Ident",               r[13:19],       decoder.field_010),
            Field("Runway or Helipad Ident",                r[19:24],       decoder.field_046),  # TODO or 180
            Field("Operation Type",                         r[24:26],       decoder.field_223),
            Field("Continuation Record No",                 r[26],          decoder.field_016),
            Field("Route Identifier",                       r[27],          decoder.field_224),
            Field("SBAS Service Provider Ident",            r[28:30],       decoder.field_255),
            Field("Reference Path Data Selector",           r[30:32],       decoder.field_256),
            Field("Reference Path Identifier",              r[32:36],       decoder.field_257),
            Field("Approach Performance Designator",        r[36],          decoder.field_258),
            Field("Landing Threshold Point Latitude",       r[37:48],       decoder.field_267),
            Field("Landing Threshold Point Longitude",      r[48:60],       decoder.field_268),
            Field("(LTP) Ellipsoid Height",                 r[60:66],       decoder.field_225),
            Field("Glide Path Angle",                       r[66:70],       decoder.field_226),
            Field("Flight Path Alignment Point Latitude",   r[70:81],       decoder.field_267),
            Field("Flight Path Alignment Point Longitude",  r[81:93],       decoder.field_268),
            Field("Course Width at Threshold Note 4",       r[93:98],       decoder.field_228),
            Field("Length Offset",                          r[98:102],      decoder.field_259),
            Field("Path Point TCH",                         r[102:108],     decoder.field_265),
            Field("TCH Units Indicator",                    r[108],         decoder.field_266),
            Field("HAL",                                    r[109:112],     decoder.field_263),
            Field("VAL",                                    r[112:115],     decoder.field_264),
            Field("SBAS FAS Data CRC Remainder",            r[115:123],     decoder.field_229),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]

    def read_ext(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                     r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("Approach Procedure Ident",               r[13:19],       decoder.field_010),
            Field("Runway or Helipad Ident",                r[19:24],       decoder.field_046),  # TODO or 180
            Field("Operation Type",                         r[24:26],       decoder.field_223),
            Field("Continuation Record No",                 r[26],          decoder.field_016),
            Field("Application Type",                       r[27],          decoder.field_091),
            Field("(FPAP) Ellipsoid Height",                r[28:34],       decoder.field_225),
            Field("(FPAP) Orthometric Height",              r[34:40],       decoder.field_227),
            Field("(LTP) Orthometric Height",               r[40:46],       decoder.field_227),
            Field("Approach Type Identifier",               r[46:56],       decoder.field_262),
            Field("GNSS Channel Number",                    r[56:61],       decoder.field_244),
            Field("Helicopter Procedure Course",            r[71:123],      decoder.field_269),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]


class Runway():

    cont_idx = 21
    app_idx = 22

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'S':
                    return self.read_sim(line)
                # case 'W':
                #     return self.read_cont(line)
                case _:
                    raise ValueError("bad runway")

    def read_primary(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport ICAO Identifier",                r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("Runway Identifier",                      r[13:18],       decoder.field_046),
            Field("Continuation Record No",                 r[21],          decoder.field_016),
            Field("Runway Length",                          r[22:27],       decoder.field_057),
            Field("Runway Magnetic Bearing",                r[27:31],       decoder.field_058),
            Field("Runway Latitude",                        r[32:41],       decoder.field_036),
            Field("Runway Longitude",                       r[41:51],       decoder.field_037),
            Field("Runway Gradient",                        r[51:56],       decoder.field_212),
            Field("(LTP) Ellipsoid Height",                 r[60:66],       decoder.field_225),
            Field("Landing Threshold Elevation",            r[66:71],       decoder.field_068),
            Field("Displaced Threshold Dist",               r[71:75],       decoder.field_069),
            Field("Threshold Crossing Height",              r[75:77],       decoder.field_067),
            Field("Runway Width",                           r[77:80],       decoder.field_109),
            Field("TCH Value Indicator",                    r[80],          decoder.field_109),
            Field("Localizer/MLS/GLS Ref Path Ident",       r[81:85],       decoder.field_044),
            Field("Localizer/MLS/GLS Category/Class",       r[85],          decoder.field_080),
            Field("Stopway",                                r[86:90],       decoder.field_079),
            Field("Localizer/MLS/GLS Ref Path Ident (2)",   r[90:94],       decoder.field_044),
            Field("Localizer/MLS/GLS Category/Class (2)",   r[94],          decoder.field_080),
            Field("Runway Description",                     r[101:123],     decoder.field_059),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]

    def read_cont(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport ICAO Identifier",                r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("Runway Identifier",                      r[13:18],       decoder.field_046),
            Field("Continuation Record No",                 r[21],          decoder.field_016),
            Field("Notes",                                  r[23:92],       decoder.field_061),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]

    def read_sim(self, r):
        return [
            Field("Record Type",                            r[0],           decoder.field_002),
            Field("Customer / Area Code",                   r[1:4],         decoder.field_003),
            Field("Section Code",                           r[4]+r[12],     decoder.field_004),
            Field("Airport ICAO Identifier",                r[6:10],        decoder.field_006),
            Field("ICAO Code",                              r[10:12],       decoder.field_014),
            Field("Runway Identifier",                      r[13:18],       decoder.field_046),
            Field("Continuation Record No",                 r[21],          decoder.field_016),
            Field("Application Type",                       r[22],          decoder.field_091),
            Field("Runway True Bearing",                    r[51:56],       decoder.field_094),
            Field("True Bearing Source",                    r[56],          decoder.field_095),
            Field("TDZE Location",                          r[65],          decoder.field_098),
            Field("Touchdown Zone Elevation",               r[66:71],       decoder.field_097),
            Field("File Record No",                         r[123:128],     decoder.field_031),
            Field("Cycle Date",                             r[128:132],     decoder.field_032)
        ]

    # def read_flight1(self, r):
    #     return [
    #         Field("Record Type",                            r[0],           decoder.field_000),
    #         Field("Customer / Area Code",                   r[1:4],         decoder.field_000),
    #         Field("Section Code",                           r[4]+r[12],     decoder.field_000),
    #         Field("Airport Identifier",                     r[6:10],        decoder.field_000),
    #         Field("ICAO Code",                              r[10:12],       decoder.field_000),
    #         Field("SID/STAR/Approach Identifier",           r[13:19],       decoder.field_000),
    #         Field("Route Type",                             r[19],          decoder.field_000),
    #         Field("Transition Identifier",                  r[20:25],       decoder.field_000),
    #         Field("Sequence Number",                        r[26:29],       decoder.field_000),
    #         Field("Fix Identifier",                         r[29:34],       decoder.field_000),
    #         Field("ICAO Code (2)",                          r[34:36],       decoder.field_000),
    #         Field("Section Code (2)",                       r[36:38],       decoder.field_000),
    #         Field("Continuation Record No",                 r[38],          decoder.field_000),
    #         Field("Application Type",                       r[39],          decoder.field_000),
    #         Field("Start/End Indicator",                    r[40],          decoder.field_000),
    #         Field("Start/End Date",                         r[41:45],       decoder.field_000),
    #         Field("Leg Distance",                           r[74:78],       decoder.field_000),
    #         Field("File Record No",                         r[123:128],     decoder.field_000),
    #         Field("Cycle Date",                             r[128:132],     decoder.field_000)
    #     ]


class SIDSTARApp():

    cont_idx = 38
    app_idx = 39

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'E':
                    return self.read_ext(line)
                case 'P':
                    return self.read_flight0(line)
                case 'W':
                    return self.read_data(line)
                case _:
                    raise ValueError("bad SID/STAR/APP")

    def read_primary(self, r):
        return [
            Field("Record Type",                                r[0],           decoder.field_002),
            Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
            Field("Section Code",                               r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                                  r[10:12],       decoder.field_014),
            Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
            Field("Route Type",                                 r[19],          decoder.field_007),
            Field("Transition Identifier",                      r[20:25],       decoder.field_011),
            Field("Sequence Number",                            r[26:29],       decoder.field_012),
            Field("Fix Identifier",                             r[29:34],       decoder.field_013),
            Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
            Field("Section Code (2)",                           r[36:38],       decoder.field_004),
            Field("Continuation Record No",                     r[38],          decoder.field_016),
            Field("Waypoint Description Code",                  r[39:43],       decoder.field_017),
            Field("Turn Direction",                             r[43],          decoder.field_020),
            Field("RNP",                                        r[44:47],       decoder.field_211),
            Field("Path and Termination",                       r[47:49],       decoder.field_021),
            Field("Turn Direction Valid",                       r[49],          decoder.field_022),
            Field("Recommended Navaid",                         r[50:54],       decoder.field_023),
            Field("ICAO Code (3)",                              r[54:56],       decoder.field_014),
            Field("Arc Radius",                                 r[56:62],       decoder.field_204),
            Field("Theta",                                      r[62:66],       decoder.field_024),
            Field("Rho",                                        r[66:70],       decoder.field_025),
            Field("Magnetic Course",                            r[70:74],       decoder.field_026),
            Field("Route / Holding Distance or Time",           r[74:78],       decoder.field_027),
            Field("Recommended Navaid (2)",                     r[78:80],       decoder.field_004),
            Field("Altitude Description",                       r[82],          decoder.field_029),
            Field("ATC Indicator",                              r[83],          decoder.field_081),
            Field("Altitude",                                   r[84:89],       decoder.field_030),
            Field("Altitude (2)",                               r[89:94],       decoder.field_030),
            Field("Transition Altitude",                        r[94:99],       decoder.field_053),
            Field("Speed Limit",                                r[99:102],      decoder.field_072),
            Field("Vertical Angle",                             r[102:106],     decoder.field_070),
            Field("Center Fix or TAA Procedure Turn Indicator", r[106:111],     decoder.field_144),  # or 271
            Field("Multiple Code or TAA Sector Identifier",     r[111],         decoder.field_130),  # or 272
            Field("ICAO Code (4)",                              r[112:113],     decoder.field_014),
            Field("Section Code (3)",                           r[114:116],     decoder.field_004),
            Field("GNSS/FMS Indication",                        r[116],         decoder.field_222),
            Field("Speed Limit Description",                    r[117],         decoder.field_261),
            Field("Apch Route Qualifier 1",                     r[118],         decoder.field_007),
            Field("Apch Route Qualifier 2",                     r[119],         decoder.field_007),
            Field("File Record No",                             r[123:128],     decoder.field_031),
            Field("Cycle Date",                                 r[128:132],     decoder.field_032)
        ]

    def read_ext(self, r):
        return [
            Field("Record Type",                                r[0],           decoder.field_002),
            Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
            Field("Section Code",                               r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                                  r[10:12],       decoder.field_014),
            Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
            Field("Route Type",                                 r[19],          decoder.field_007),
            Field("Transition Identifier",                      r[20:25],       decoder.field_011),
            Field("Sequence Number",                            r[26:29],       decoder.field_012),
            Field("Fix Identifier",                             r[29:34],       decoder.field_013),
            Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
            Field("Section Code (2)",                           r[36:38],       decoder.field_004),
            Field("Continuation Record No",                     r[38],          decoder.field_016),
            Field("Application Type",                           r[39],          decoder.field_091),
            Field("CAT A Decision Height",                      r[40:44],       decoder.field_170),
            Field("CAT B Decision Height",                      r[44:48],       decoder.field_170),
            Field("CAT C Decision Height",                      r[48:52],       decoder.field_170),
            Field("CAT D Decision Height",                      r[52:56],       decoder.field_170),
            Field("CAT A Minimum Descent Altitude",             r[56:60],       decoder.field_171),
            Field("CAT B Minimum Descent Altitude",             r[60:64],       decoder.field_171),
            Field("CAT C Minimum Descent Altitude",             r[64:68],       decoder.field_171),
            Field("CAT D Minimum Descent Altitude",             r[68:72],       decoder.field_171),
            Field("Procedure TCH",                              r[72:75],       decoder.field_067),
            Field("Localizer Only Altitude Desc",               r[75],          decoder.field_029),
            Field("Localizer Only Altitude",                    r[76:81],       decoder.field_030),
            Field("Localizer Only Vertical Angle",              r[81:85],       decoder.field_070),
            Field("RNP",                                        r[89:92],       decoder.field_211),
            Field("Apch Route Qualifier 1",                     r[118],         decoder.field_007),
            Field("Apch Route Qualifier 2",                     r[119],         decoder.field_007),
            Field("File Record No",                             r[123:128],     decoder.field_031),
            Field("Cycle Date",                                 r[128:132],     decoder.field_032)
        ]

    def read_flight0(self, r):
        return [
            Field("Record Type",                                r[0],           decoder.field_002),
            Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
            Field("Section Code",                               r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                                  r[10:12],       decoder.field_014),
            Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
            Field("Route Type",                                 r[19],          decoder.field_007),
            Field("Transition Identifier",                      r[20:25],       decoder.field_011),
            Field("Sequence Number",                            r[26:29],       decoder.field_012),
            Field("Fix Identifier",                             r[29:34],       decoder.field_013),
            Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
            Field("Section Code (2)",                           r[36:38],       decoder.field_004),
            Field("Continuation Record No",                     r[38],          decoder.field_016),
            Field("Application Type",                           r[39],          decoder.field_091),
            Field("Start/End Indicator",                        r[40],          decoder.field_152),
            Field("Start/End Date",                             r[41:45],       decoder.field_153),
            Field("Leg Distance",                               r[74:78],       decoder.field_260),
            Field("File Record No",                             r[123:128],     decoder.field_031),
            Field("Cycle Date",                                 r[128:132],     decoder.field_032)
        ]

    def read_data(self, r):
        return [
            Field("Record Type",                                r[0],           decoder.field_002),
            Field("Customer / Area Code",                       r[1:4],         decoder.field_003),
            Field("Section Code",                               r[4]+r[12],     decoder.field_004),
            Field("Airport Identifier",                         r[6:10],        decoder.field_006),
            Field("ICAO Code",                                  r[10:12],       decoder.field_014),
            Field("SID/STAR/Approach Identifier",               r[13:19],       decoder.field_009),
            Field("Route Type",                                 r[19],          decoder.field_007),
            Field("Transition Identifier",                      r[20:25],       decoder.field_011),
            Field("Sequence Number",                            r[26:29],       decoder.field_012),
            Field("Fix Identifier",                             r[29:34],       decoder.field_013),
            Field("ICAO Code (2)",                              r[34:36],       decoder.field_014),
            Field("Section Code (2)",                           r[36:38],       decoder.field_004),
            Field("Continuation Record No",                     r[38],          decoder.field_016),
            Field("Application Type",                           r[39],          decoder.field_091),
            Field("FAS Block Provided",                         r[40],          decoder.field_276),
            Field("FAS Block Provided Level of Service Name",   r[41:51],       decoder.field_275),
            Field("LNAV/VNAV Authorized for SBAS",              r[51],          decoder.field_276),
            Field("LNAV/VNAV Level of Service Name",            r[52:62],       decoder.field_275),
            Field("LNAV Authorized for SBAS",                   r[62],          decoder.field_276),
            Field("LNAV Level of Service Name",                 r[63:73],       decoder.field_275),
            Field("Apch Route Qualifier 1",                     r[118],         decoder.field_007),
            Field("Apch Route Qualifier 2",                     r[119],         decoder.field_007),
            Field("File Record No",                             r[123:128],     decoder.field_031),
            Field("Cycle Date",                                 r[128:132],     decoder.field_032)
        ]


class Waypoint():

    cont_idx = 21
    app_idx = 22

    def __init__(self, enrt) -> None:
        self.enrt = enrt

    def read(self, line) -> list:
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case 'P':
                    return self.read_flight_plan0(line)
                case 'Q':
                    return self.read_flight_plan1(line)
                case _:
                    raise ValueError("bad waypoint record")

    def read_primary(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Waypoint Type",                       r[26:29],      decoder.field_042),
            Field("Waypoint Usage",                      r[29:31],      decoder.field_082),
            Field("Waypoint Latitude",                   r[32:41],      decoder.field_036),
            Field("Waypoint Longitude",                  r[41:51],      decoder.field_037),
            Field("Dynamic Mag. Variation",              r[74:79],      decoder.field_039),
            Field("Datum Code",                          r[84:87],      decoder.field_197),
            Field("Name Format Indicator",               r[95:98],      decoder.field_196),
            Field("Waypoint Name / Desc",                r[98:123],     decoder.field_043),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_cont(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Application Type",                    r[22],         decoder.field_091),
            Field("Notes",                               r[23:123],     decoder.field_061),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_flight_plan0(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
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

    def read_flight_plan1(self, r) -> list:
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",
                  r[4:6] if self.enrt is True else r[4]+r[12],          decoder.field_004),
            Field("Region Code",                         r[6:10],       decoder.field_041),
            Field("ICAO Code",                           r[10:12],      decoder.field_014),
            Field("Waypoint Identifier",                 r[13:18],      decoder.field_013),
            Field("ICAO Code (2)",                       r[19:21],      decoder.field_014),
            Field("Continuation Record No",              r[21],         decoder.field_016),
            Field("Waypoint Type",                       r[26:29],      decoder.field_042),
            Field("Waypoint Usage",                      r[29:31],      decoder.field_082),
            Field("Waypoint Latitude",                   r[32:41],      decoder.field_036),
            Field("Waypoint Longitude",                  r[41:51],      decoder.field_037),
            Field("Dynamic Mag. Variation",              r[74:79],      decoder.field_039),
            Field("Datum Code",                          r[84:87],      decoder.field_197),
            Field("Name Format Indicator",               r[95:98],      decoder.field_196),
            Field("Waypoint Name / Desc",                r[98:123],     decoder.field_043),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]
