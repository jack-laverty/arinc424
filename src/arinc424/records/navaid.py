
def read_fields(section, r):
    fields = {}
    fields["Record Type"]                  = r[0]
    fields["Customer / Area Code"]         = r[1:4]
    fields["Airport ICAO Identifier"]      = r[6:10]
    fields["ICAO Code"]                    = r[10:12]
    fields["ICAO Code (2)"]                = r[19:21]
    fields["Cycle Date"]                   = r[128:132]
    fields["Section Code"]                 = section.code[0]
    fields["Subsection Code"]              = section.code[1]
    fields["File Record No"]               = r[123:128]
    fields["VOR Identifier"]               = r[13:17]
    fields["Continuation Records Number"]  = r[21]

    if int(fields["Continuation Records Number"]) < 2:
        fields["Frequency"]                = r[22:27]
        fields["Class"]                    = r[27:32]
        fields["VOR Latitude"]             = r[32:41]
        fields["VOR Longitude"]            = r[41:51]
        fields["DME Ident"]                = r[51:55]
        fields["DME Latitude"]             = r[55:64]
        fields["DME Longitude"]            = r[64:74]
        fields["Station Declination"]      = r[74:79]
        fields["DME Elevation"]            = r[79:84]
        fields["Figure of Merit"]          = r[84]
        fields["ILS/DME Bias"]             = r[85:87]
        fields["Frequency Protection"]     = r[87:90]
        fields["Datum Code"]               = r[90:93]
        fields["VOR Name"]                 = r[93:123]
    else:
        fields["Application Type"]         = r[22]
        fields["Notes"]                    = r[23:92]
        fields["Reserved (Expansion)"]     = r[92:123]
    
    return fields