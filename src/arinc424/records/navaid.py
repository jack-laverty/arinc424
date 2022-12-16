
class VHFNavaid():
    def read_fields(section, r):
        fields = {}
        fields["Record Type"] = r[0]
        fields["Customer / Area Code"] = r[1:4]
        fields["Airport ICAO Identifier"] = r[6:10]
        fields["ICAO Code"] = r[10:12]
        fields["VOR Identifier"] = r[13:17]
        fields["ICAO Code (2)"] = r[19:21]
        fields["Section Code"] = section.code[0]
        fields["Subsection Code"] = section.code[1]
        fields["Continuation Records Number"] = r[21]
        fields["Frequency"] = r[22:27]
        fields["Class"] = r[27:32]
        fields["VOR Latitude"] = r[32:41]
        fields["VOR Longitude"] = r[41:51]
        fields["DME Ident"] = r[51:55]
        fields["DME Latitude"] = r[55:64]
        fields["DME Longitude"] = r[64:74]
        fields["Station Declination"] = r[74:79]
        fields["DME Elevation"] = r[79:84]
        fields["Figure of Merit"] = r[84]
        fields["ILS/DME Bias"] = r[85:87]
        fields["Frequency Protection"] = r[87:90]
        fields["Datum Code"] = r[90:93]
        fields["VOR Name"] = r[93:123]
        fields["File Record No"] = r[123:128]
        fields["Cycle Date"] = r[128:132]
        return fields


class VHFNavaidCont():
    def read_fields(section, r):
        fields = {}
        fields["Record Type"] = r[0]
        fields["Customer / Area Code"] = r[1:4]
        fields["Airport ICAO Identifier"] = r[6:10]
        fields["ICAO Code"] = r[10:12]
        fields["VOR Identifier"] = r[13:17]
        fields["ICAO Code (2)"] = r[19:21]
        fields["Section Code"] = section.code[0]
        fields["Subsection Code"] = section.code[1]
        fields["Continuation Records Number"] = r[21]
        fields["Application Type"] = r[22]
        fields["Notes"] = r[23:92]
        fields["Reserved (Expansion)"] = r[92:123]
        fields["File Record No"] = r[123:128]
        fields["Cycle Date"] = r[128:132]
        return fields


class VHFNavaidSimCont():
    def read_fields(section, r):
        fields = {}
        fields["Record Type"] = r[0]
        fields["Customer / Area Code"] = r[1:4]
        fields["Airport ICAO Identifier"] = r[6:10]
        fields["ICAO Code"] = r[10:12]
        fields["VOR Identifier"] = r[13:17]
        fields["ICAO Code (2)"] = r[19:21]
        fields["Section Code"] = section.code[0]
        fields["Subsection Code"] = section.code[1]
        fields["Continuation Records Number"] = r[21]
        fields["Application Type"] = r[22]
        fields["Facility Characteristics"] = r[27:32]
        fields["Reserved (Spacing)"] = r[32:74]
        fields["File Record No"] = r[123:128]
        fields["Cycle Date"] = r[128:132]
        return fields


# This Continuation Record is used to indicate the FIR and
# UIR within which the VHF NAVAID defined in the
# Primary Record is located and the Start/End validity
# dates/times of the Primary Record.
class VHFNavaidFlightPlanningCont0():
    def read_fields(section, r):
        fields = {}
        fields["Record Type"] = r[0]
        fields["Customer / Area Code"] = r[1:4]
        fields["Airport ICAO Identifier"] = r[6:10]
        fields["ICAO Code"] = r[10:12]
        fields["VOR Identifier"] = r[13:17]
        fields["ICAO Code (2)"] = r[19:21]
        fields["Section Code"] = section.code[0]
        fields["Subsection Code"] = section.code[1]
        fields["Continuation Records Number"] = r[21]
        fields["Application Type"] = r[22]
        fields["FIR Identifier"] = r[23:27]
        fields["UIR Identifier"] = r[28:31]
        fields["Start/End Indicator"] = r[32]
        fields["Start/End Date"] = r[32:43]
        fields["Reserved (Expansion)"] = r[43:123]
        fields["File Record No"] = r[123:128]
        fields["Cycle Date"] = r[128:132]
        return fields


# This Continuation Record is used to indicate the fields of
# the Primary Record that are changed. Used in conjunction
# with VHFNavaidFlightPlanningCont0.
class VHFNavaidFlightPlanningCont1():
    def read_fields(section, r):
        fields = {}
        fields["Record Type"] = r[0]
        fields["Customer / Area Code"] = r[1:4]
        fields["Airport ICAO Identifier"] = r[6:10]
        fields["ICAO Code"] = r[10:12]
        fields["VOR Identifier"] = r[13:17]
        fields["ICAO Code (2)"] = r[19:21]
        fields["Section Code"] = section.code[0]
        fields["Subsection Code"] = section.code[1]
        fields["Continuation Records Number"] = r[21]
        fields["Application Type"] = r[22]
        fields["Frequency"] = r[22:27]
        fields["Class"] = r[27:32]
        fields["VOR Latitude"] = r[32:41]
        fields["VOR Longitude"] = r[41:51]
        fields["DME Ident"] = r[51:55]
        fields["DME Latitude"] = r[55:64]
        fields["DME Longitude"] = r[64:74]
        fields["Station Declination"] = r[74:79]
        fields["DME Elevation"] = r[79:84]
        fields["Figure of Merit"] = r[84]
        fields["ILS/DME Bias"] = r[85:87]
        fields["Frequency Protection"] = r[87:90]
        fields["Datum Code"] = r[90:93]
        fields["VOR Name"] = r[93:123]
        fields["File Record No"] = r[123:128]
        fields["Cycle Date"] = r[128:132]
        return fields


class VHFNavaidLimitationCont():
    def read_fields(section, r):
        fields = {}
        fields["Record Type"] = r[0]
        fields["Customer / Area Code"] = r[1:4]
        fields["Airport ICAO Identifier"] = r[6:10]
        fields["ICAO Code"] = r[10:12]
        fields["VOR Identifier"] = r[13:17]
        fields["ICAO Code (2)"] = r[19:21]
        fields["Section Code"] = section.code[0]
        fields["Subsection Code"] = section.code[1]
        fields["Continuation Records Number"] = r[21]
        fields["Application Type"] = r[22]
        fields["FIR Identifier"] = r[23:27]
        fields["UIR Identifier"] = r[28:31]
        fields["Start/End Indicator"] = r[32]
        fields["Start/End Date"] = r[32:43]
        fields["Reserved (Expansion)"] = r[43:123]
        fields["File Record No"] = r[123:128]
        fields["Cycle Date"] = r[128:132]
        return fields
