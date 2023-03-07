from collections import defaultdict
import string


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
    return "ERROR: bad value"


def def_fn():
    return text


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
    sections['HD'] = 'Heliport SID'
    sections['HE'] = 'Heliport STAR'
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
            return 'Sector Narrative Continuation'
        case 'T':
            return 'Time of Operations Continuation\
"formatted time data"'
        case 'U':
            return 'Time of Operations Continuation\
"Narrative time data"'
        case 'V':
            return 'Time of Operations Continuation,\
Start/End Date'
        case 'P':
            return 'Flight Planning Application Continuation'
        case 'Q':
            return 'Flight Planning Application Primary Data\
Continuation'
        case 'S':
            return 'Simulation Application Continuation'
        case 'W':
            return 'Airport or Heliport Procedure Data\
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


def ifr(val):
    match val:
        case 'Y':
            return 'Official'
        case 'N':
            return 'Non-official'
        case _:
            raise ValueError('Invalid IFR Capability')


def rwy(val):
    if val.isnumeric():
        return val.lstrip('0')+"00" + " ft"
    else:
        raise ValueError('Invalid runway length')


def mag(val):
    if val.strip() == '':
        return '<Blank>'
    else:
        return "{:03} {}".format(
            int(val[1:]),
            val[0]
        )


def speed(val):
    if val.isnumeric():
        return val + " knots (IAS)"
    else:
        raise ValueError('Invalid speed')


def mil(val):
    match val:
        case 'C':
            return 'Public / Civil'
        case 'M':
            return 'Military'
        case 'P':
            return 'Private (not open to public)'
        case _:
            raise ValueError('Invalid Pub/Mil')


def daylight(val):
    match val:
        case 'Y':
            return 'Yes'
        case 'N':
            return 'No'
        case _:
            raise ValueError('Invalid Daylight')


def time(val):
    if val[0].isalpha() and val[1:].isnumeric():
        x = string.ascii_uppercase.index(val[0]) - 12
        y = 'GMT +' + str(x) if x >= 0 else 'GMT -' + str(x)
        return y + ':' + str(val[1:])
    else:
        raise ValueError('Invalid Time Zone')


def area(key):
    match key:
        case 'USA':
            return 'USA - United States of America'
        case 'AFR':
            return 'AFR - Africa'
        case 'XYZ':
            # TODO: wat
            return 'XYZ - No Idea'
        case _:
            raise ValueError('Invalid Area')


def commtype(key):
    ct = defaultdict(def_val)
    ct['ACC'] = 'Area Control Center'
    ct['ACP'] = 'Airlift Command Post'
    ct['AIR'] = 'Air to Air'
    ct['APP'] = 'Approach Control'
    ct['ARR'] = 'Arrival Control'
    ct['ASO'] = 'Automatic Surface Observing System (ASOS)'
    ct['ATI'] = 'Automatic Terminal Info Service (ATIS)'
    ct['AWI'] = 'Airport Weather Information Broadcast (AWIB)'
    ct['AWO'] = 'Automatic Weather Observing Service (AWOS)'
    ct['AWS'] = 'Aerodrome Weather Information Services (AWIS)'
    ct['CLD'] = 'Clearance Delivery'
    ct['CPT'] = 'Clearance, Pre-Taxi'
    ct['CTA'] = 'Control Area (Terminal)'
    ct['CTL'] = 'Control'
    ct['DEP'] = 'Departure Control'
    ct['DIR'] = 'Director (Approach Control Radar)'
    ct['EFS'] = 'Enroute Flight Advisory Service (EFAS)'
    ct['EMR'] = 'Emeergency'
    ct['FSS'] = 'Flight Service Station'
    ct['GCO'] = 'Ground Comm Outlet'
    ct['GND'] = 'Ground Control'
    ct['GTE'] = 'Gate Control'
    ct['HEL'] = 'Helicopter Frequency'
    ct['INF'] = 'Information'
    ct['MIL'] = 'Military Frequency'
    ct['MUL'] = 'Multicom'
    ct['OPS'] = 'Operations'
    ct['PAL'] = 'Pilot Activated Lighting (Note 1)'
    ct['RDO'] = 'Radio'
    ct['RDR'] = 'Radar'
    ct['RFS'] = 'Remote Flight Service Station (RFSS)'
    ct['RMP'] = 'Ramp/Taxi Control'
    ct['RSA'] = 'Airport Radar Service Area (ARSA)'
    ct['TCA'] = 'Terminal Control Area'
    ct['TMA'] = 'Terminal Control Area'
    ct['TML'] = 'Terminal'
    ct['TRS'] = 'Terminal Radar Service Area (TRSA)'
    ct['TWE'] = 'Transcribe Weather Broadcast (TWEB)'
    ct['TWR'] = 'Tower, Air Traffic Control'
    ct['UAC'] = 'Upper Area Control'
    ct['UNI'] = 'Unicom'
    ct['VOL'] = 'Volmet'
    return ct[key] if ct[key] != "bad value" else key + " - BAD VALUE"


def frequnit(key):
    d = defaultdict(def_val)
    d['H'] = 'High Frequency (3000 kHz - 30,000 kHz)'
    d['V'] = 'Very High Frequency (30,000 kHz - 200 MHz)'
    d['U'] = 'Ultra High Frequency (200 MHz - 3000 MHz)'
    d['C'] = 'Communication Channel for 8.33 kHz spacing'
    return d[key] if d[key] != "bad value" else key + " - BAD VALUE"


def mod(key):
    d = defaultdict(def_val)
    d['A'] = 'Amplitude Modulated'
    d['F'] = 'Frequency Modulated'
    return d[key] if d[key] != "bad value" else key + " - BAD VALUE"


def h24(key):
    d = defaultdict(def_val)
    d['Y'] = '24-Hour Availability'
    d['N'] = 'Part-time Availability'
    return d[key] if d[key] != "bad value" else key + " - BAD VALUE"


def cruise_ident(key):
    if key == 'AA':
        return 'ICAO Standard Cruise Table'
    elif key == 'AO':
        return 'Exception to ICAO Cruise Table'
    elif key.isalpha() and key[1] == key[0]:
        return 'Modified Cruise Table'
    elif key.isalpha() and key[1] == 'O':
        return 'Exception to Modified Cruise Table'
    else:
        print(key)
        raise ValueError("Invalid Cruise Table Ident")


def magtrue(key):
    if key == 'M':
        return 'Magnetic'
    elif key == 'T':
        return 'True'
    else:
        raise ValueError("Invalid Mag/True Indicator")


def course(val):
    return float(val)/10


def turn(key):
    if key == 'R':
        return 'Right'
    elif key == 'L':
        return 'Left'
    else:
        raise ValueError("Invalid Turn Direction")


def legtime(val):
    return '{}m {}s'.format(int(val[0]), int(val[1])*6)


def wpusage(key):
    if key == ' B':
        return 'HI and LO Altitude'
    elif key == ' H':
        return 'HI Altitude'
    elif key == ' L':
        return 'LO Altitude'
    elif key == '  ':
        return 'Terminal Use Only'
    elif key == 'R ':
        return 'RNAV'
    else:
        raise ValueError("Invalid Waypoint Usage")


def boundary(key):
    if key == 'C ':
        return 'Circle'
    elif key == 'G ':
        return 'Great Circle'
    elif key == 'H ':
        return 'Rhumb Line'
    elif key == 'L ':
        return 'Counter Clockwise ARC'
    elif key == 'R ':
        return 'Clockwise ARC'
    elif key == ' E':
        return 'End of description, return to origin point'
    else:
        raise ValueError("Invalid Boundary Via")


def firuir(key):
    if key == 'F':
        return 'FIR'
    elif key == 'U ':
        return 'UIR'
    elif key == 'B':
        return 'Combined FIR/UIR'
    else:
        raise ValueError("Invalid FIR/UIR Indicator")


decode_fn = defaultdict(def_fn)
decode_fn["Airport Elevation"] = altitude
decode_fn["Airport Reference Pt. Latitude"] = gps
decode_fn["Airport Reference Pt. Longitude"] = gps
decode_fn["Application Type"] = app
decode_fn["Boundary Via"] = boundary
decode_fn["Course To"] = course
decode_fn["Course From"] = course
decode_fn["Class Collocation"] = colloc
decode_fn["Class Facility"] = facility
decode_fn["Class Info"] = info
decode_fn["Class Power"] = power
decode_fn["Communications Freq"] = freq
decode_fn["Communications Type"] = commtype
decode_fn["Continuation Record No"] = cont
# decode_fn["Cruise Table Identifier"] = cruise_ident
decode_fn["Cruise Level From"] = altitude
decode_fn["Cruise Level To"] = altitude
decode_fn["Customer / Area Code"] = area
decode_fn["Cycle Date"] = cycle
decode_fn["Daylight Indicator"] = daylight
decode_fn["DME Elevation"] = altitude
decode_fn["DME Latitude"] = gps
decode_fn["DME Longitude"] = gps
decode_fn["Facility Elevation"] = altitude
decode_fn["FIR/UIR Indicator"] = firuir
decode_fn["FIR/UIR Latitude"] = gps
decode_fn["FIR/UIR Longitude"] = gps
decode_fn["Frequency"] = freq
decode_fn["Frequency Protection"] = freq
decode_fn["Frequency Units"] = frequnit
decode_fn["H24 Indicator"] = h24
decode_fn["IFR Capability"] = ifr
decode_fn["Inbound Holding Course"] = course
decode_fn["Latitude"] = gps
decode_fn["Leg Time"] = legtime
decode_fn["Longest Runway"] = rwy
decode_fn["Longitude"] = gps
decode_fn["Magnetic Variation"] = mag
decode_fn["Mag/True"] = magtrue
decode_fn["Marker Latitude"] = gps
decode_fn["Marker Longitude"] = gps
decode_fn["Marker Power"] = mk_power
decode_fn["Marker Shape"] = mk_shape
decode_fn["Modulation"] = mod
decode_fn["Name Format Indicator"] = nfi
decode_fn["NDB Class Collocation"] = colloc
decode_fn["NDB Class Facility"] = facility
decode_fn["NDB Class Info"] = info
decode_fn["NDB Class Power"] = power
decode_fn["NDB Frequency"] = freq
decode_fn["NDB Latitude"] = gps
decode_fn["NDB Longitude"] = gps
decode_fn["Public Military Indicator"] = mil
decode_fn["Record Type"] = record
decode_fn["Restr. Air Link Continuation"] = app
decode_fn["Runway Latitude"] = gps
decode_fn["Runway Longitude"] = gps
decode_fn["Section Code"] = section
decode_fn["Speed Limit"] = speed
decode_fn["Speed Limit Altitude"] = altitude
decode_fn["Time Zone"] = time
decode_fn["Transition Altitude"] = altitude
decode_fn["Transition Level"] = altitude
decode_fn["Turn Direction"] = turn
decode_fn["Vertical Separation"] = altitude
decode_fn["VOR Latitude"] = text
decode_fn["VOR Longitude"] = text
decode_fn["Waypoint Latitude"] = gps
decode_fn["Waypoint Longitude"] = gps
decode_fn["Waypoint Type"] = waypoint
decode_fn["Waypoint Usage"] = wpusage
