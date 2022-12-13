from collections import defaultdict
import sections
import json

AIRPORT_RECORD                          = 'PA'
AIRPORT_COMMUNICATIONS_RECORD           = 'PV'
AIRPORT_STAR_RECORD                     = 'PE'
AIRPORT_APPROACH_RECORD                 = 'PF'
AIRPORT_RUNWAY_RECORD                   = 'PG'
AIRPORT_MSA_RECORD                      = 'PS'
AIRPORT_WAYPOINT_RECORD                 = 'PC'
AIRPORT_SID_RECORD                      = 'PD'
AIRPORT_LOCALIZER_GLIDESLOPE_RECORD     = 'PI'
AIRPORT_ILS_MARKER                      = 'PM'

class Airport:

    record = {}
    def __init__(self):
        return

    def parse_record(self, r, section):
        self.record["Record Type"]                      = r[0]
        self.record["Customer / Area Code"]             = r[1:4]
        self.record["Airport ICAO Identifier"]          = r[6:10]
        self.record["ICAO Code"]                        = r[10:12]
        self.record["Cycle Date"]                       = r[128:132]
        self.record["Section Code"], self.record["Subsection Code"] = section.section[0], section.section[1]

        if section.section == AIRPORT_RECORD:
            self.record["Continuation Records Number"]          = r[21]
            if int(self.record["Continuation Records Number"]) < 2:
                self.record["ATA/IATA Designator"]              = r[13:16]
                self.record["Speed Limit Altitude"]             = r[22:27]
                self.record["Longest Runway"]                   = r[27:30]
                self.record["IFR Capability"]                   = r[30]
                self.record["Longest Runway Surface Code"]      = r[31]
                self.record["Airport Reference Pt. Latitude"]   = r[32:41]
                self.record["Airport Reference Pt. Longitude"]  = r[41:51]
                self.record["Magnetic Variation"]               = r[51:56]
                self.record["Airport Elevation"]                = r[56:61]
                self.record["Speed Limit"]                      = r[61:64]
                self.record["Recommended Navaid"]               = r[64:68]
                self.record["ICAO Code 2"]                      = r[68:70]
                self.record["Transitions Altitude"]             = r[70:75]
                self.record["Transition Level"]                 = r[75:80]
                self.record["Public/Military Indicator"]        = r[80]
                self.record["Time Zone"]                        = r[81:84]
                self.record["Daylight Indicator"]               = r[84]
                self.record["Magnetic/True Indicator"]          = r[85]
                self.record["Datum Code"]                       = r[86:89]
                self.record["Reserved (Expansion)"]             = r[16:18] if r[16:18].strip() != '' else '<Blank>' 
                self.record["Reserved (Expansion) 2"]           = r[89:93] if r[89:93].strip() != '' else '<Blank>' 
                self.record["Airport Name"]                     = r[93:123]
                self.record["File Record No"]                   = r[123:128]
            else:
                self.record["VOR Identifier"]                   = r[13:17]
                self.record["ICAO Code"]                        = r[19:21]
                self.record["Application Type"]                 = r[22]
                self.record["Notes"]                            = r[23:92]
                self.record["Reserved (Expansion)"]             = r[92:123] if r[92:123].strip() != '' else '<Blank>' 
                self.record["File Record No"]                   = r[123:128]
        elif section.section == AIRPORT_COMMUNICATIONS_RECORD:
            self.record["Continuation Records Number"]          = r[25]
            if int(self.record["Continuation Records Number"]) < 2:
                self.record["Communications Type"]              = r[13:16]
                self.record["Communications Frequency"]         = r[16:23]
                self.record["Guard/Transmit"]                   = r[23]
                self.record["Frequency Units"]                  = r[24]
                self.record["Service Indicator"]                = r[26:29]
                self.record["Radar Service"]                    = r[29]
                self.record["Modulation"]                       = r[30]
                self.record["Signal Emission"]                  = r[31]
                self.record["Latitude"]                         = r[32:41]
                self.record["Longitude"]                        = r[41:51]
                self.record["Magnetic Variation"]               = r[51:56]
                self.record["Facility Elevation"]               = r[56:61]
                self.record["H24 Indicator"]                    = r[62]
                self.record["Sectorization"]                    = r[62:68]
                self.record["Altitude Description"]             = r[69]
                self.record["Communication Altitude"]           = r[69:74]
                self.record["Communication Altitude (2)"]       = r[74:79]
                self.record["Sector Facility"]                  = r[79:83]
                self.record["ICAO Code (2)"]                    = r[83:85]
                self.record["Section Code (2)"]                 = r[85]
                self.record["Subsection Code (2)"]              = r[86]
                self.record["Distance Description"]             = r[87]
                self.record["Communications Distance"]          = r[88:90]
                self.record["Remote Facility"]                  = r[90:94]
                self.record["ICAO Code (3)"]                    = r[94:96]
                self.record["Section Code (3)"]                 = r[96]
                self.record["Subsection Code (3)"]              = r[97]
                self.record["Call Sign"]                        = r[98:123]
                self.record["File Record No"]                   = r[123:128]
            else:
                self.record["Application Type"]                 = r[26]
                self.record["Narrative"]                        = r[27:87]
                self.record["Reserved (Expansion)"]             = r[87:123] if r[87:123].strip() != '' else '<Blank>' 
                self.record["File Record No"]                   = r[123:128]
        elif section.section == AIRPORT_STAR_RECORD:
                pass
        elif section.section == AIRPORT_APPROACH_RECORD:
                pass
        elif section.section == AIRPORT_RUNWAY_RECORD:
                pass
        elif section.section == AIRPORT_MSA_RECORD:
                pass
        elif section.section == AIRPORT_LOCALIZER_GLIDESLOPE_RECORD:
                pass
        elif section.section == AIRPORT_WAYPOINT_RECORD:
                pass
        elif section.section == AIRPORT_SID_RECORD:
                pass
        elif section.section == AIRPORT_ILS_MARKER:
                pass
        else:
            print("Unsupported Airport Record", section.section)

    def dump(self):
        for k, v in self.record.items():
            print("{:<26}: {}".format(k, v))

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record, sort_keys=True, indent=4, separators=(',', ': '))