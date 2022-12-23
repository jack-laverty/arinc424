from collections import defaultdict

sections = defaultdict(None)
sections['AA'] = 'Grid MORA'
sections['D '] = 'VHF Navaid'
sections['DB'] = 'NDB Navaid'
sections['EA'] = 'Waypoint'
sections['EM'] = 'Airways Marker'
sections['EP'] = 'Holding Patterns'
sections['ER'] = 'Airways and Routes'
sections['ET'] = 'Preferred Routes'
sections['EU'] = 'Airway Restrictions'
sections['EV'] = 'Communications'
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
sections['TC'] = 'Crusing Table'
sections['TG'] = 'Geographical Reference'
sections['TN'] = 'RNAV Name Table'
sections['UC'] = 'Controller Airspace'
sections['UF'] = 'Airspace FIR/UIR'
sections['UR'] = 'Restrictive Airspace'


def freq(val):
    if (val.isnumeric()):
        return "{:.2f}".format(float(val)/100)
    else:
        return val


def cycle(val):
    s = ''
    if int(val[:2]) > 50:
        s += ("19" + val[:2])
    else:
        s += ("20" + val[:2])
    s += ', ' + (val[2:])
    return s


def dme_el(val):
    if val.strip() == '':
        return '<Blank>'
    else:
        return val.lstrip('0') + " ft"


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


# frequency protection
# ILS/DME bias
# station declination
# continuation
def text(val):
    return val.strip() if val.strip() != '' else '<Blank>'


def def_val():
    return "<Unsupported>"


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
