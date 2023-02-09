from collections import defaultdict


def freq(val):
    if (val.isnumeric()):
        return "{:.2f}".format(float(val)/100)
    else:
        return val


def cycle(val):
    x = val[:2]
    return '{}, {}'.format("19" + x if int(x) > 50 else "20" + x,
                           val[2:])


def altitude(val):
    return val.lstrip('0') + " ft" if val.isnumeric() else '<Blank>'


def dme_el(val):
    return altitude(val)


def gps(val):
    x = len(val)
    if val.strip() == '':
        return '<Blank>'
    else:
        return "{:03} {:02} {:02} {:02} {}".format(
            int(val[1:x-6]),
            int(val[x-6:x-4]),
            int(val[x-4:x-2]),
            int(val[x-2:x]),
            val[0]
        )


def text(val):
    return val.strip() if val.strip() != '' else '<Blank>'


def def_val():
    return "<Unsupported Decoding>"


def facility(val):
    facility = defaultdict(def_val)
    facility['V'] = 'VOR'
    facility[' '] = ''
    facility['D'] = 'DME'
    facility['T'] = 'TACAN'
    facility['M'] = 'MIL TACAN'
    facility['I'] = 'ILS/DME or ILS/TACAN'
    facility['N'] = 'MLS/DME/N'
    facility['P'] = 'MLS/DME/P'
    return ' '.join([facility[val[0]], facility[val[1]]]).strip()


def power(val):
    power = defaultdict(def_val)
    power['T'] = 'Terminal'
    power['L'] = 'Low Altitude'
    power['H'] = 'High Altitude'
    power['U'] = 'Undefined'
    power['C'] = 'ILS/TACAN'
    return str(power[val])


def info(val):
    info = defaultdict(def_val)
    info['D'] = 'Biased ILS/DME or ILS/TACAN'
    info['A'] = 'Automatic Transcribed Weather Broadcast'
    info['B'] = 'Scheduled Weather Broadcast'
    info['W'] = 'No Voice on Frequency'
    info[' '] = 'Voice on Frequency'
    return str(info[val])


def colloc(val):
    collocation = defaultdict(def_val)
    collocation[' '] = 'Collocated Navaids'
    collocation['N'] = 'Non-Collocated Navaids'
    return str(collocation[val])


def waypoint(val):
    match val[0]:
        case 'C':
            return "Combined Named Intersection\
 and RNAV"
        case 'I':
            return 'Unnamed, Charted Intersection'
        case 'N':
            return 'NDB Navaid as Waypoint' + val[1:]
        case 'R':
            return 'Named Intersection'
        case 'U':
            return 'Uncharted Airway Intersection'
        case 'V':
            return 'VFR Waypoint'
        case 'W':
            return 'RNAV Waypoint'

    match val[1]:
        case 'A':
            return 'Final Approach Fix'
        case 'B':
            return 'Initial and Final Approach Fix'
        case 'C':
            return 'Final Approach Course Fix'
        case 'D':
            return 'Intermediate Approach Fix'
        case 'E':
            return 'Off-Route intersection in the\
FAA National Reference System'
        case 'F':
            return 'Off-Route Intersection'
        case 'I':
            return 'Initial Approach Fix'
        case 'K':
            return 'Final Approach Course Fix at\
Initial Approach Fix'
        case 'L':
            return 'Final Approach Course Fix at\
Intermediate Approach Fix'
        case 'M':
            return 'Missed Approach Fix'
        case 'N':
            return 'Initial Approach Fix and Missed\
Approach Fix'
        case 'O':
            return 'Oceanic Entry/Exit Waypoint'
        case 'P':
            return 'Pitch and Catch Point in the FAA\
High Altitude Redesign'
        case 'S':
            return 'AACAA and SUA Waypoints in\
the FAA High Altitude Redesign'
        case 'U':
            return 'FIR/UIR or Controlled Airspace\
Intersection'
        case 'V':
            return 'Latitude/Longitude Intersection,\
Full Degree of Latitude'
        case 'W':
            return 'Latitude/Longitude Intersection,\
Half Degree of Latitude'
        case _:
            return "Unknown Waypoint Type"


def nfi(val):

    match val[0]:
        case 'A':
            return 'Abeam Fix'
        case 'B':
            return 'Bearing and Distance Fix '
        case 'D':
            return 'Airport Name as Fix'
        case 'F':
            return 'FIR Fix'
        case 'H':
            return 'Phonetic Letter Name Fix'
        case 'I':
            return 'Airport Ident as Fix'
        case 'L':
            return 'Latitude/Longitude Fix '
        case 'M':
            return 'Multiple Word Name Fix'
        case 'N':
            return 'Navaid Ident as Fix'
        case 'P':
            return 'Published Five - Letter - Name - Fix'
        case 'Q':
            return 'Published Name Fix, less than five\
letters'
        case 'R':
            return 'Published Name Fix, more than five\
letters'
        case 'T':
            return 'Airport/Rwy Related Fix (Note 2)'
        case 'U':
            return 'UIR Fix'

    match val[1]:
        case 'O':
            return 'Localizer Marker with officially\
published five - letter identifier'
        case 'M':
            return 'Localizer Marker without officially\
published five - letter identifier'
        case _:
            return 'Unknown Name Format Indicator'


def section(val):
    sections = defaultdict(def_val)
    sections['AS'] = 'Grid MORA'
    sections['D '] = 'VHF Navaid'
    sections['DB'] = 'NDB Navaid'
    sections['EA'] = 'Waypoint'
    sections['EM'] = 'Airways Marker'
    sections['EP'] = 'Holding Pattern'
    sections['ER'] = 'Airways and Route'
    sections['ET'] = 'Preferred Route'
    sections['EU'] = 'Airway Restrictions'
    sections['EV'] = 'Enroute Communication'
    sections['HA'] = 'Heliport Pads'
    sections['HC'] = 'Heliport Terminal Waypoint'
    sections['HD'] = 'Heliport SIDs'
    sections['HE'] = 'Heliport STARs'
    sections['HF'] = 'Heliport Approach Procedure'
    sections['HK'] = 'Heliport TAA'
    sections['HS'] = 'Heliport MSA'
    sections['HV'] = 'Heliport Communication'
    sections['PA'] = 'Airport Reference Point'
    sections['PB'] = 'Airport Gates'
    sections['PC'] = 'Airport Terminal Waypoint'
    sections['PD'] = 'Airport SID'
    sections['PE'] = 'Airport STAR'
    sections['PF'] = 'Airport Approach Procedure'
    sections['PG'] = 'Airport Runway'
    sections['PI'] = 'Airport Localizer/Glideslope'
    sections['PK'] = 'Airport TAA'
    sections['PL'] = 'Airport MLS'
    sections['PM'] = 'Airport Localizer Marker'
    sections['PN'] = 'Airport Terminal'
    sections['PP'] = 'Airport Path'
    sections['PR'] = 'Airport Flt Planning ARR/DEP'
    sections['PS'] = 'Airport MSA'
    sections['PT'] = 'Airport GLS Station'
    sections['PV'] = 'Airport Communication'
    sections['R '] = 'Company Route'
    sections['RA'] = 'Alternate Record'
    sections['TC'] = 'Cruising Table'
    sections['TG'] = 'Geographical Reference'
    sections['TN'] = 'RNAV Name Table'
    sections['UC'] = 'Controller Airspace'
    sections['UF'] = 'Airspace FIR/UIR'
    sections['UR'] = 'Restrictive Airspace'
    return sections[val]


def record(val):
    if val == 'S':
        return 'Standard'
    elif val == 'T':
        return 'Tailored'
    else:
        return 'Error: invalid record type'


def cont(val):
    match val:
        case '0':
            return 'Primary Record'
        case '1':
            return 'Primary Record (with Cont.)'
        case _:
            return str(val) + ' - Continuation'


def app(val):
    match val:
        case 'A':
            return 'Standard ARINC Continuation containing\
notes or other formatted data'
        case 'B':
            return 'Combined Controlling Agency/Call Sign\
and formatted Time of Operation'
        case 'C':
            return 'Call Sign/Controlling Agency Continuation'
        case 'E':
            return 'Primary Record Extension'
        case 'L':
            return 'VHF Navaid Limitation Continuation'
        case 'N':
            return 'A Sector Narrative Continuation'
        case 'T':
            return 'A Time of Operations Continuation\
"formatted time data"'
        case 'U':
            return 'A Time of Operations Continuation\
"Narrative time data"'
        case 'V':
            return 'A Time of Operations Continuation,\
Start/End Date'
        case 'P':
            return 'A Flight Planning Application Continuation'
        case 'Q':
            return 'A Flight Planning Application Primary Data\
Continuation'
        case 'S':
            return 'Simulation Application Continuation'
        case 'W':
            return 'An Airport or Heliport Procedure Data\
Continuation with SBAS use authorization\
information'
        case _:
            return 'Unknown Application Type: ' + str(val)


def mk_shape(val):
    match val:
        case 'E':
            return 'Elliptical'
        case 'B':
            return 'Bone'
        case _:
            return val


def mk_power(val):
    match val:
        case 'H':
            return 'High Power (general use)'
        case 'L':
            return 'Low Power (low altitude use)'
        case _:
            return val


decode_fn = defaultdict(def_val)
decode_fn["Airport Elevation"] = text
decode_fn["Airport ICAO Identifier"] = text
decode_fn["Airport Name"] = text
decode_fn["Airport Reference Pt. Latitude"] = gps
decode_fn["Airport Reference Pt. Longitude"] = gps
decode_fn["Altitude Description"] = text
decode_fn["Altitude Limiation"] = text
decode_fn["Application Type"] = app
decode_fn["Arc Radius"] = text
decode_fn["ATA/IATA Designator"] = text
decode_fn["Blank (Spacing)"] = text
decode_fn["Boundary Code"] = text
decode_fn["Call Sign"] = text
decode_fn["Class Collocation"] = colloc
decode_fn["Class Facility"] = facility
decode_fn["Class Info"] = info
decode_fn["Class Power"] = power
decode_fn["Class"] = text
decode_fn["Communication Altitude"] = text
decode_fn["Communications Distance"] = text
decode_fn["Communications Freq"] = text
decode_fn["Communications Type"] = text
decode_fn["Component Affected Indicator"] = text
decode_fn["Continuation Record No"] = cont
decode_fn["Controlled A/S Airport ICAO"] = text
decode_fn["Controlled A/S Airport Indent"] = text
decode_fn["Controlled A/S Airport Indentifier"] = text
decode_fn["Controlled A/S Indicator"] = text
decode_fn["Course From"] = text
decode_fn["Course To"] = text
decode_fn["Cruise Level From"] = altitude
decode_fn["Cruise Level To"] = altitude
decode_fn["Cruise Table Indicator"] = text
decode_fn["Cruising Table Identifier"] = text
decode_fn["Customer / Area Code"] = text
decode_fn["Cycle Date"] = cycle
decode_fn["Datum Code"] = text
decode_fn["Daylight Indicator"] = text
decode_fn["Direction Restriction"] = text
decode_fn["Displaced Threshold Dist"] = text
decode_fn["Distance Description"] = text
decode_fn["Distance Limiation"] = text
decode_fn["DME Elevation"] = dme_el
decode_fn["DME Ident"] = text
decode_fn["DME Latitude"] = gps
decode_fn["DME Longitude"] = gps
decode_fn["Duplicate Identifier"] = text
decode_fn["Dynamic Mag. Variation"] = text
decode_fn["EU Indicator"] = text
decode_fn["Facility Characteristics"] = text
decode_fn["Facility Elevation"] = text
decode_fn["Figure of Merit"] = text
decode_fn["File Record No"] = text
decode_fn["FIR Identifier"] = text
decode_fn["Fix Identifier"] = text
decode_fn["Fix Radius Transition Indicator"] = text
decode_fn["Frequency Protection"] = freq
decode_fn["Frequency Units"] = text
decode_fn["Frequency"] = freq
decode_fn["Guard/Transmit"] = text
decode_fn["H24 Indicator"] = text
decode_fn["Heliport Elevation"] = text
decode_fn["Heliport Identifier"] = text
decode_fn["Heliport Name"] = text
decode_fn["Holding Speed"] = text
decode_fn["ICAO Code (2)"] = text
decode_fn["ICAO Code"] = nfi
decode_fn["IFR Capability"] = text
decode_fn["IFR Indicator"] = text
decode_fn["ILS/DME Bias"] = text
decode_fn["Inbound Holding Course"] = text
decode_fn["Inbound Magnetic Course"] = text
decode_fn["Landing Threshold Elevation"] = text
decode_fn["Latitude"] = gps
decode_fn["Leg Length"] = text
decode_fn["Leg Time"] = text
decode_fn["Level"] = text
decode_fn["Localizer/MLS/GLS Category/Class (2)"] = text
decode_fn["Localizer/MLS/GLS Category/Class"] = text
decode_fn["Localizer/MLS/GLS Ref Path Ident (2)"] = text
decode_fn["Localizer/MLS/GLS Ref Path Ident"] = text
decode_fn["Longest Runway Surface Code"] = text
decode_fn["Longest Runway"] = text
decode_fn["Longitude"] = gps
decode_fn["Mag/True"] = text
decode_fn["Magnetic Variation"] = text
decode_fn["Magnetic/True Indicator"] = text
decode_fn["Marker Code"] = text
decode_fn["Marker Identifier"] = text
decode_fn["Marker Latitude"] = gps
decode_fn["Marker Longitude"] = gps
decode_fn["Marker Name"] = text
decode_fn["Marker Power"] = mk_power
decode_fn["Marker Shape"] = mk_shape
decode_fn["Maximum Altitude"] = text
decode_fn["Minimum Altitude"] = text
decode_fn["Minor Axis"] = text
decode_fn["Modulation"] = text
decode_fn["MORA"] = text
decode_fn["Name Format Indicator"] = nfi
decode_fn["Name"] = text
decode_fn["Narrative"] = text
decode_fn["Navaid Limitation Code"] = text
decode_fn["NDB Class Collocation"] = colloc
decode_fn["NDB Class Facility"] = facility
decode_fn["NDB Class Info"] = info
decode_fn["NDB Class Power"] = power
decode_fn["NDB Frequency"] = freq
decode_fn["NDB Identifier"] = text
decode_fn["NDB Latitude"] = gps
decode_fn["NDB Longitude"] = gps
decode_fn["NDB Name"] = text
decode_fn["NOTAM"] = text
decode_fn["Notes"] = text
decode_fn["Outbound Magnetic Course"] = text
decode_fn["Pad Dimensions"] = text
decode_fn["PAD Identifier"] = text
decode_fn["Public Military Indicator"] = text
decode_fn["Radar Service"] = text
decode_fn["Recommended NAVAID"] = text
decode_fn["Recommended VHF Navaid"] = text
decode_fn["Record Type"] = record
decode_fn["Region Code"] = text
decode_fn["Remote Facility"] = text
decode_fn["Reserved (Expansion)"] = text
decode_fn["Reserved (Spacing)"] = text
decode_fn["Restr. Air Designation"] = text
decode_fn["Restr. Air ICAO Code"] = text
decode_fn["Restr. Air Link Continuation"] = app
decode_fn["Restr. Air Multiple Code"] = text
decode_fn["Restr. Air Type"] = text
decode_fn["Restriction Identifier"] = text
decode_fn["Restriction Type"] = text
decode_fn["Rho"] = text
decode_fn["RNP"] = text
decode_fn["Route Distance From"] = text
decode_fn["Route Identifier"] = text
decode_fn["Route Type"] = waypoint
decode_fn["Runway Description"] = text
decode_fn["Runway Gradient"] = text
decode_fn["Runway Identifier"] = text
decode_fn["Runway Latitude"] = gps
decode_fn["Runway Length"] = text
decode_fn["Runway Longitude"] = gps
decode_fn["Runway Magnetic Bearing"] = text
decode_fn["Runway True Bearing"] = text
decode_fn["Runway Width"] = text
decode_fn["Section Code"] = section
decode_fn["Sector Facility"] = text
decode_fn["Sector From/Sector To"] = text
decode_fn["Sectorization"] = text
decode_fn["Sequence End Indicator"] = text
decode_fn["Sequence Number"] = text
decode_fn["Service Indicator"] = text
decode_fn["Signal Emission"] = text
decode_fn["Speed Limit Altitude"] = text
decode_fn["Speed Limit"] = text
decode_fn["Start Fix ICAO Code"] = text
decode_fn["Start Fix Identifier"] = text
decode_fn["Start Fix Section Code"] = text
decode_fn["Starting Latitude"] = text
decode_fn["Starting Longitude"] = text
decode_fn["Start/End Date"] = text
decode_fn["Start/End Date/Time"] = text
decode_fn["Start/End Indicator"] = text
decode_fn["Station Declination"] = text
decode_fn["Stopway"] = text
decode_fn["Subsection Code"] = text
decode_fn["TCH Value Indicator"] = text
decode_fn["TDZE Location"] = text
decode_fn["Theta"] = text
decode_fn["Threshold Crossing Height"] = text
decode_fn["Time Code"] = text
decode_fn["Time Indicator"] = text
decode_fn["Time of Operation"] = text
decode_fn["Time Zone"] = text
decode_fn["Touchdown Zone Elevation"] = text
decode_fn["Transition Altitude"] = text
decode_fn["Transition Level"] = text
decode_fn["True Bearing Source"] = text
decode_fn["Turn Direction"] = text
decode_fn["UIR Identifier"] = text
decode_fn["Vertical Separation"] = altitude
decode_fn["VOR Identifier"] = text
decode_fn["VOR Latitude"] = gps
decode_fn["VOR Longitude"] = gps
decode_fn["VOR Name"] = text
decode_fn["Waypoint Desc Code"] = text
decode_fn["Waypoint Identifier"] = text
decode_fn["Waypoint Latitude"] = gps
decode_fn["Waypoint Longitude"] = gps
decode_fn["Waypoint Name / Desc"] = text
decode_fn["Waypoint Type"] = waypoint
decode_fn["Waypoint Usage"] = text
