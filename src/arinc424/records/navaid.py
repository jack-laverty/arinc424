
class VHFNavaid():

    def find_type(self, line):
        if int(line[21]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return 'VHF Navaid Primary Record'
        else:
            # continuation record # 2 or greater = continuation record
            return 'VHF Navaid Continuation Record'

        # TODO: how do you determine what type of continuation record it is?
        # parse the rest of the record and try to line it up with one of the
        # continuation record structures? kind of annoying, no?

    def read_primary(self, r):
        fields = []
        fields.append(["Record Type",                   r[0]])
        fields.append(["Customer / Area Code",          r[1:4]])
        fields.append(["Section Code",                  r[4]])
        fields.append(["Subsection Code",               r[5]])
        fields.append(["Airport ICAO Identifier",       r[6:10]])
        fields.append(["ICAO Code",                     r[10:12]])
        fields.append(["VOR Identifier",                r[13:17]])
        fields.append(["ICAO Code (2)",                 r[19:21]])
        fields.append(["Continuation Records No",       r[21]])
        fields.append(["Frequency",                     r[22:27]])
        fields.append(["Class",                         r[27:32]])
        fields.append(["VOR Latitude",                  r[32:41]])
        fields.append(["VOR Longitude",                 r[41:51]])
        fields.append(["DME Ident",                     r[51:55]])
        fields.append(["DME Latitude",                  r[55:64]])
        fields.append(["DME Longitude",                 r[64:74]])
        fields.append(["Station Declination",           r[74:79]])
        fields.append(["DME Elevation",                 r[79:84]])
        fields.append(["Figure of Merit",               r[84]])
        fields.append(["ILS/DME Bias",                  r[85:87]])
        fields.append(["Frequency Protection",          r[87:90]])
        fields.append(["Datum Code",                    r[90:93]])
        fields.append(["VOR Name",                      r[93:123]])
        fields.append(["File Record No",                r[123:128]])
        fields.append(["Cycle Date",                    r[128:132]])
        return fields

    def read_cont(self, r):
        fields = []
        fields.append(["Record Type",                   r[0]])
        fields.append(["Customer / Area Code",          r[1:4]])
        fields.append(["Section Code",                  r[4]])
        fields.append(["Subsection Code",               r[5]])
        fields.append(["Airport ICAO Identifier",       r[6:10]])
        fields.append(["ICAO Code",                     r[10:12]])
        fields.append(["VOR Identifier",                r[13:17]])
        fields.append(["ICAO Code (2)",                 r[19:21]])
        fields.append(["Continuation Records No",       r[21]])
        fields.append(["Application Type",              r[22]])
        fields.append(["Notes",                         r[23:92]])
        fields.append(["Reserved (Expansion)",          r[92:123]])
        fields.append(["File Record No",                r[123:128]])
        fields.append(["Cycle Date",                    r[128:132]])
        return fields

    def read_sim(self, r):
        fields = []
        fields.append(["Record Type",                   r[0]])
        fields.append(["Customer / Area Code",          r[1:4]])
        fields.append(["Section Code",                  r[4]])
        fields.append(["Subsection Code",               r[5]])
        fields.append(["Airport ICAO Identifier",       r[6:10]])
        fields.append(["ICAO Code",                     r[10:12]])
        fields.append(["VOR Identifier",                r[13:17]])
        fields.append(["ICAO Code (2)",                 r[19:21]])
        fields.append(["Continuation Records No",       r[21]])
        fields.append(["Application Type",              r[22]])
        fields.append(["Facility Characteristics",      r[27:32]])
        fields.append(["Reserved (Spacing)",            r[32:74]])
        fields.append(["File Record No",                r[123:128]])
        fields.append(["Cycle Date",                    r[128:132]])
        return fields

    # This Continuation Record is used to indicate the FIR and
    # UIR within which the VHF NAVAID defined in the
    # Primary Record is located and the Start/End validity
    # dates/times of the Primary Record.
    def read_flight_plan0(self, section, r):
        fields = []
        fields.append(["Record Type",                   r[0]])
        fields.append(["Customer / Area Code",          r[1:4]])
        fields.append(["Section Code",                  r[4]])
        fields.append(["Subsection Code",               r[5]])
        fields.append(["Airport ICAO Identifier",       r[6:10]])
        fields.append(["ICAO Code",                     r[10:12]])
        fields.append(["VOR Identifier",                r[13:17]])
        fields.append(["ICAO Code (2)",                 r[19:21]])
        fields.append(["Continuation Records No",       r[21]])
        fields.append(["Application Type",              r[22]])
        fields.append(["FIR Identifier",                r[23:27]])
        fields.append(["UIR Identifier",                r[28:31]])
        fields.append(["Start/End Indicator",           r[32]])
        fields.append(["Start/End Date",                r[32:43]])
        fields.append(["Reserved (Expansion)",          r[43:123]])
        fields.append(["File Record No",                r[123:128]])
        fields.append(["Cycle Date",                    r[128:132]])
        return fields

    # This Continuation Record is used to indicate the fields of
    # the Primary Record that are changed. Used in conjunction
    # with flight_plan0.
    def read_flight_plan1(self, section, r):
        fields = {}
        fields.append(["Record Type",                   r[0]])
        fields.append(["Customer / Area Code",          r[1:4]])
        fields.append(["Section Code",                  r[4]])
        fields.append(["Subsection Code",               r[5]])
        fields.append(["Airport ICAO Identifier",       r[6:10]])
        fields.append(["ICAO Code",                     r[10:12]])
        fields.append(["VOR Identifier",                r[13:17]])
        fields.append(["ICAO Code (2)",                 r[19:21]])
        fields.append(["Continuation Records No",       r[21]])
        fields.append(["Application Type",              r[22]])
        fields.append(["Frequency",                     r[22:27]])
        fields.append(["Class",                         r[27:32]])
        fields.append(["VOR Latitude",                  r[32:41]])
        fields.append(["VOR Longitude",                 r[41:51]])
        fields.append(["DME Ident",                     r[51:55]])
        fields.append(["DME Latitude",                  r[55:64]])
        fields.append(["DME Longitude",                 r[64:74]])
        fields.append(["Station Declination",           r[74:79]])
        fields.append(["DME Elevation",                 r[79:84]])
        fields.append(["Figure of Merit",               r[84]])
        fields.append(["ILS/DME Bias",                  r[85:87]])
        fields.append(["Frequency Protection",          r[87:90]])
        fields.append(["Datum Code",                    r[90:93]])
        fields.append(["VOR Name",                      r[93:123]])
        fields.append(["File Record No",                r[123:128]])
        fields.append(["Cycle Date",                    r[128:132]])
        return fields   

    def read_lim(self, r):
        fields = []
        fields.append(["Record Type",                   r[0]])
        fields.append(["Customer / Area Code",          r[1:4]])
        fields.append(["Section Code",                  r[4]])
        fields.append(["Subsection Code",               r[5]])
        fields.append(["Airport ICAO Identifier",       r[6:10]])
        fields.append(["ICAO Code",                     r[10:12]])
        fields.append(["VOR Identifier",                r[13:17]])
        fields.append(["ICAO Code (2)",                 r[19:21]])
        fields.append(["Continuation Records No",       r[21]])
        fields.append(["Application Type",              r[22]])
        fields.append(["Navaid Limitation Code",        r[23]])
        fields.append(["Component Affected Indicator",  r[24]])
        fields.append(["Sequence Number",               r[25:27]])
        fields.append(["Sector From/Sector To",         r[27:29]])
        fields.append(["Distance Description",          r[29]])
        fields.append(["Distance Limiation",            r[30:36]])
        fields.append(["Altitude Description",          r[36]])
        fields.append(["Altitude Limiation",            r[37:43]])
        fields.append(["Sector From/Sector To",         r[43:45]])
        fields.append(["Distance Description",          r[45]])
        fields.append(["Distance Limiation",            r[46:52]])
        fields.append(["Altitude Description",          r[52]])
        fields.append(["Altitude Limiation",            r[53:59]])
        fields.append(["Sector From/Sector To",         r[59:61]])
        fields.append(["Distance Description",          r[61]])
        fields.append(["Distance Limiation",            r[62:68]])
        fields.append(["Altitude Description",          r[68]])
        fields.append(["Altitude Limiation",            r[69:75]])
        fields.append(["Sector From/Sector To",         r[75:77]])
        fields.append(["Distance Description",          r[77]])
        fields.append(["Distance Limiation",            r[79:84]])
        fields.append(["Altitude Description",          r[84]])
        fields.append(["Altitude Limiation",            r[85:91]])
        fields.append(["Sector From/Sector To",         r[91:93]])
        fields.append(["Distance Description",          r[93]])
        fields.append(["Distance Limiation",            r[94:100]])
        fields.append(["Altitude Description",          r[101]])
        fields.append(["Altitude Limiation",            r[101:107]])
        fields.append(["Sequence End Indicator",        r[107]])
        fields.append(["Blank (Spacing)",               r[108:123]])
        fields.append(["File Record No",                r[123:128]])
        fields.append(["Cycle Date",                    r[128:132]])
        return fields
