from collections import defaultdict

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

def read_fields(section, r):
    fields = {}
    fields["Record Type"]                       = r[0]
    fields["Customer / Area Code"]              = r[1:4]
    fields["Airport ICAO Identifier"]           = r[6:10]
    fields["ICAO Code"]                         = r[10:12]
    fields["Cycle Date"]                        = r[128:132]
    fields["Section Code"]                      = section.code[0]
    fields["SSubsection Code"]                  = section.code[1]

    if section.code == AIRPORT_RECORD:
        fields["Continuation Records Number"]          = r[21]
        if int(fields["Continuation Records Number"]) < 2:
            fields["ATA/IATA Designator"]              = r[13:16]
            fields["Speed Limit Altitude"]             = r[22:27]
            fields["Longest Runway"]                   = r[27:30]
            fields["IFR Capability"]                   = r[30]
            fields["Longest Runway Surface Code"]      = r[31]
            fields["Airport Reference Pt. Latitude"]   = r[32:41]
            fields["Airport Reference Pt. Longitude"]  = r[41:51]
            fields["Magnetic Variation"]               = r[51:56]
            fields["Airport Elevation"]                = r[56:61]
            fields["Speed Limit"]                      = r[61:64]
            fields["Recommended Navaid"]               = r[64:68]
            fields["ICAO Code 2"]                      = r[68:70]
            fields["Transitions Altitude"]             = r[70:75]
            fields["Transition Level"]                 = r[75:80]
            fields["Public/Military Indicator"]        = r[80]
            fields["Time Zone"]                        = r[81:84]
            fields["Daylight Indicator"]               = r[84]
            fields["Magnetic/True Indicator"]          = r[85]
            fields["Datum Code"]                       = r[86:89]
            fields["Reserved (Expansion)"]             = r[16:18]
            fields["Reserved (Expansion) 2"]           = r[89:93]
            fields["Airport Name"]                     = r[93:123]
            fields["File Record No"]                   = r[123:128]
        else:
            fields["VOR Identifier"]                   = r[13:17]
            fields["ICAO Code"]                        = r[19:21]
            fields["Application Type"]                 = r[22]
            fields["Notes"]                            = r[23:92]
            fields["Reserved (Expansion)"]             = r[92:123]
            fields["File Record No"]                   = r[123:128]
    elif section.code == AIRPORT_COMMUNICATIONS_RECORD:
        fields["Continuation Records Number"]          = r[25]
        if int(fields["Continuation Records Number"]) < 2:
            fields["Communications Type"]              = r[13:16]
            fields["Communications Frequency"]         = r[16:23]
            fields["Guard/Transmit"]                   = r[23]
            fields["Frequency Units"]                  = r[24]
            fields["Service Indicator"]                = r[26:29]
            fields["Radar Service"]                    = r[29]
            fields["Modulation"]                       = r[30]
            fields["Signal Emission"]                  = r[31]
            fields["Latitude"]                         = r[32:41]
            fields["Longitude"]                        = r[41:51]
            fields["Magnetic Variation"]               = r[51:56]
            fields["Facility Elevation"]               = r[56:61]
            fields["H24 Indicator"]                    = r[62]
            fields["Sectorization"]                    = r[62:68]
            fields["Altitude Description"]             = r[69]
            fields["Communication Altitude"]           = r[69:74]
            fields["Communication Altitude (2)"]       = r[74:79]
            fields["Sector Facility"]                  = r[79:83]
            fields["ICAO Code (2)"]                    = r[83:85]
            fields["Section Code (2)"]                 = r[85]
            fields["Subsection Code (2)"]              = r[86]
            fields["Distance Description"]             = r[87]
            fields["Communications Distance"]          = r[88:90]
            fields["Remote Facility"]                  = r[90:94]
            fields["ICAO Code (3)"]                    = r[94:96]
            fields["Section Code (3)"]                 = r[96]
            fields["Subsection Code (3)"]              = r[97]
            fields["Call Sign"]                        = r[98:123]
            fields["File Record No"]                   = r[123:128]
        else:
            fields["Application Type"]                 = r[26]
            fields["Narrative"]                        = r[27:87]
            fields["Reserved (Expansion)"]             = r[87:123] if r[87:123].strip() != '' else '<Blank>' 
            fields["File Record No"]                   = r[123:128]
    elif section.code == AIRPORT_STAR_RECORD:
            pass
    elif section.code == AIRPORT_APPROACH_RECORD:
            pass
    elif section.code == AIRPORT_RUNWAY_RECORD:
            pass
    elif section.code == AIRPORT_MSA_RECORD:
            pass
    elif section.code == AIRPORT_LOCALIZER_GLIDESLOPE_RECORD:
            pass
    elif section.code == AIRPORT_WAYPOINT_RECORD:
            pass
    elif section.code == AIRPORT_SID_RECORD:
            pass
    elif section.code == AIRPORT_ILS_MARKER:
            pass
    else:
        print("Unsupported Airport Record", section.code)
        