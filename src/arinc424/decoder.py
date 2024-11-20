from collections import defaultdict
import io
import string


class Field():

  def __init__(self, name, value, decode_fn):
    self.name = name
    self.value = value
    self.decode_fn = decode_fn

  def decode(self, record):
    return self.decode_fn(self.value, record)


# This file decodes fields within records based on
# Chapter 5 - Field Definitions

def def_val():
  return "<UNKNOWN>"


# 5.2 Record Type
def field_002(value, record):
  if value == 'S':
    return 'Standard'
  elif value == 'T':
    return 'Tailored'
  else:
    raise ValueError("Invalid Record Type", value)


# 5.3 Customer / Area Code
def field_003(value, record):
  match value:
    case 'USA':
      return 'United States of America'
    case 'AFR':
      return 'Africa'
    case 'CAN':
      return 'Canada'
    case 'EEU':
      return 'Eastern Europe and Asia'
    case 'EUR':
      return 'Europe'
    case 'LAM':
      return 'Latin America'
    case 'MES':
      return 'Middle East'
    case 'PAC':
      return 'Pacific'
    case 'SAM':
      return 'Southern America'
    case 'SPA':
      return 'South Pacific'
    case _:
      return '<UNKNOWN>'


# 5.4 & 5.5 Section Code & Subsection Code
def field_004(value, record):
  if (value.strip() == ''):
    return value
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
  return sections[value]


# 5.6 Airport/Heliport Identifier (ARPT/HELI IDENT)
def field_006(value, record):
  return value


# 5.7 Route Type
def field_007(value, record):
  d = defaultdict(def_val)
  if record.ident == 'ER':
    # Enroute Airway Records (ER)
    d['A'] = 'Airline Airway (Tailored Data)'
    d['C'] = 'Control'
    d['D'] = 'Direct Route'
    d['H'] = 'Helicopter Airways'
    d['O'] = 'Officially Designated Airways'
    d['R'] = 'RNAV Airways'
    d['S'] = 'Undesignated ATS Route'
  elif record.ident == 'ET':
    # Preferred Route Records (ET)
    d['C'] = 'North American Routes for North Atlantic Traffic Common Portion'
    d['D'] = 'Preferential Routes'
    d['J'] = 'Pacific Oceanic Transition Routes (PACOTS)'
    d['M'] = 'RNAV Airways'
    d['N'] = 'Undesignated ATS Route'
  elif record.ident == 'PD' or record.ident == 'HD':
    # Airport SID (PD) and Heliport SID (HD) Records
    d['0'] = 'Engine Out SID'
    d['1'] = 'SID Runway Transition'
    d['2'] = 'SID or SID Common Route'
    d['3'] = 'SID Enroute Transition'
    d['4'] = 'RNAV SID Runway Transition'
    d['5'] = 'RNAV SID or SID Common Route'
    d['6'] = 'RNAV SID Enroute Transition'
    d['F'] = 'FMS SID Runway Transition'
    d['M'] = 'FMS SID or SID Common Route'
    d['S'] = 'FMS SID Enroute Transition'
    d['R'] = 'RNP SID Runway Transition'
    d['N'] = 'RNP SID or SID Common Route'
    d['P'] = 'RNP SID Enroute Transition'
    d['T'] = 'Vector SID Runway Transition'
    d['V'] = 'Vector SID Enroute Transition'
  elif record.ident == 'PE' or record.ident == 'HE':
    # Airport STAR (PE) and Heliport STAR (HE) Records
    d['1'] = 'STAR Enroute Transition'
    d['2'] = 'STAR or STAR Common Route'
    d['3'] = 'STAR Runway Transition'
    d['4'] = 'RNAV STAR Enroute Transition'
    d['5'] = 'RNAV STAR or STAR Common Route'
    d['6'] = 'RNAV STAR Runway Transition'
    d['7'] = 'Profile Descent Enroute Transition'
    d['8'] = 'Profile Descent Common Route'
    d['9'] = 'Profile Descent Runway Transition'
    d['F'] = 'FMS STAR Enroute Transition'
    d['M'] = 'FMS STAR or STAR Common Route'
    d['S'] = 'FMS STAR Runway Transition'
    d['R'] = 'RNP STAR Enroute Transition'
    d['N'] = 'RNP STAR or STAR Common Route'
    d['P'] = 'RNP STAR Runway Transition'
  elif record.ident == 'PF' or record.ident == 'HF':
    # Airport Approach (PF) and Heliport Approach (HF) Records
    d['A'] = 'Approach Transition'
    d['B'] = 'Localizer/Backcourse Approach'
    d['D'] = 'VORDME Approach'
    d['F'] = 'Flight Management System (FMS) Approach'
    d['G'] = 'Instrument Guidance System (IGS) Approach'
    d['H'] = 'Area Navigation (RNAV) Approach with Required Navigation Performance (RNP) Approach'
    d['I'] = 'Instrument Landing System (ILS) Approach'
    d['J'] = 'GNSS Landing System (GLS) Approach'
    d['L'] = 'Localizer Only (LOC) Approach'
    d['M'] = 'Microwave Landing System (MLS) Approach'
    d['N'] = 'Non-Directional Beacon (NDB) Approach'
    d['P'] = 'Global Position System (GPS) Approach'
    d['Q'] = 'Non-Directional Beacon + DME (NDB+DME) Approach'
    d['R'] = 'Area Navigation (RNAV) Approach (Note 1)'
    d['S'] = 'VOR Approach using VORDME/VORTAC'
    d['T'] = 'TACAN Approach'
    d['U'] = 'Simplified Directional Facility (SDF) Approach'
    d['V'] = 'VOR Approach'
    d['W'] = 'Microwave Landing System (MLS), Type A Approach'
    d['X'] = 'Localizer Directional Aid (LDA) Approach'
    d['Y'] = 'Microwave Landing System (MLS), Type B and C Approach'
    d['Z'] = 'Missed Approach'
  return d[value] if d[value] != "bad value" else value + " - BAD VALUE"


# 5.8 Route Identifier (ROUTE IDENT)
def field_008(value, record):
  if value.strip().isalnum():
    return value
  else:
    raise ValueError("Route Identifier not alphanumeric", value)


# 5.9 SID/STAR Route Identifier (SID/STAR IDENT)
def field_009(value, record):
  if value.strip().isalnum():
    return value


# 5.10 Approach Route Identifier (APPROACH IDENT)
def field_010(value, record):
  return f"Approach: {value[0]}, Runway: {value[1:4]}"


# 5.11 Transition Identifier (TRANS IDENT)
def field_011(value, record):
  return value


# 5.12 Sequence Number (SEQ NR)
def field_012(value, record):
  match len(value.strip()):
    case 1:
      return f'MSA Table, TAA Table, Cruise Table - Sequence No. {value}'
    case 2:
      return f'VHF Navaid Limitation Continuation Records - Sequence No. {value}'
    case 3:
      return f'SID/STAR/Approach and Company Routes - Sequence No. {value}'
    case 4:
      return f'Enroute Airways, Preferred Routes, FIR/UIR, and Restrictive Airspace - Sequence No. {value}'
    case _:
      return value

# 5.13 Fix Identifier (FIX IDENT)
def field_013(value, record):
  return value


# 5.14 ICAO Code (ICAO CODE)
def field_014(value, record):
  return value


# 5.16 Continuation Record Number (CONT NR)
def field_016(value, record):
  match value:
    case '0':
      return 'Primary Record'
    case '1':
      return 'Primary Record (with Cont.)'
    case _:
      return str(value) + ' - Continuation'


# 5.17 Waypoint Description Code (DESC CODE)
def field_017(value: str, record):
  s = io.StringIO()
  match value[0]:
    case 'A':
      s.write('Airport as Waypoint\n')
    case 'E':
      s.write('Essential Waypoint\n')
    case 'F':
      s.write('Off Airway Waypoint\n')
    case 'G':
      s.write('Runway/Helipad as Waypoint\n')
    case 'H':
      s.write('Heliport as Waypoint\n')
    case 'N':
      s.write('NDB Navaid as Waypoint\n')
    case 'P':
      s.write('Phantom Waypoint\n')
    case 'R':
      s.write('Non-Essential Waypoint\n')
    case 'T':
      s.write('Transition Essential Waypoint\n')
    case 'V':
      s.write('VHF Navaid as Waypoint\n')

  match value[1]:
    case 'B':
      s.write('Flyover Waypoint: End of SID/STAR Route Type, APCH Transition or Final Approach\n')
    case 'E':
      s.write('End of Enroute Airway or Terminal Procedure Route Type\n')
    case 'U':
      s.write('Uncharted Airway Intersection\n')
    case 'Y':
      s.write('Fly-Over Waypoint\n')

  match value[2]:
    case 'A':
      s.write('Unnamed Stepdown Fix After Final Approach Fix\n')
    case 'B':
      s.write('Unnamed Stepdown Fix Before Final Approach Fix\n')
    case 'C':
      s.write('ATC Compulsory Waypoint\n')
    case 'G':
      s.write('Oceanic Gateway Waypoint\n')
    case 'M':
      s.write('First Leg of Missed Approach Procedure\n')
    case 'P':
      s.write('Path Point Fix\n')
    case 'R':
      s.write('Fix used for turning final approach\n')
    case 'S':
      s.write('Named Stepdown Fix\n')

  match value[3]:
    case 'A':
      s.write('Initial Approach Fix\n')
    case 'B':
      s.write('Intermediate Approach Fix\n')
    case 'C':
      s.write('Initial Approach Fix with Holding\n')
    case 'D':
      s.write('Initial Approach Fix with Final Approach Course Fix\n')
    case 'E':
      s.write('Final End Point Fix\n')
    case 'F':
      s.write('Published Final Approach Fix or Database Final Approach Fix\n')
    case 'H':
      s.write('Holding Fix\n')
    case 'I':
      s.write('Final Approach Course Fix\n')
    case 'M':
      s.write('Published Missed Approach Point Fix\n')

  return s.getvalue().strip()


# 5.18 Boundary Code (BDY CODE)
def field_018(value, record):
  return value


# 5.19 Level (LEVEL)
def field_019(value, record):
  return value


# 5.20 Turn Direction (TURN DIR)
def field_020(value, record):
  if value == 'R':
    return 'Right'
  elif value == 'L':
    return 'Left'
  # TODO check this
  elif value == 'E' or value == ' ':
    return 'Either'
  else:
    raise ValueError("Invalid Turn Direction:", value)


# 5.21 Path and Termination (PATH TERM)
LegTypeDesc = defaultdict(def_val)
LegTypeDesc['IF'] = 'Initial Fix or IF Leg.'
LegTypeDesc['TF'] = 'Track to a Fix or TF Leg.'
LegTypeDesc['CF'] = 'Course to a Fix or CF Leg.'
LegTypeDesc['DF'] = 'Direct to a Fix or DF Leg.'
LegTypeDesc['FA'] = 'Fix to an Altitude or FA Leg.'
LegTypeDesc['FC'] = 'Track from a Fix for a Distance or FC Leg.'
LegTypeDesc['FD'] = 'Track from a Fix to a DME Distance or FD Leg.'
LegTypeDesc['FM'] = 'From a Fix to a Manual termination or FM Leg.'
LegTypeDesc['CA'] = 'Course to an Altitude or CA Leg.'
LegTypeDesc['CD'] = 'Course to a DME Distance or CD Leg.'
LegTypeDesc['CI'] = 'Course to an Intercept or CI Leg.'
LegTypeDesc['CR'] = 'Course to a Radial termination or CR Leg.'
LegTypeDesc['RF'] = 'Constant Radius Arc or RF Leg.'
LegTypeDesc['AF'] = 'Arc to a Fix or AF Leg.'
LegTypeDesc['VA'] = 'Heading to an Altitude termination or VA Leg.'
LegTypeDesc['VD'] = 'Heading to a DME Distance termination or VD Leg.'
LegTypeDesc['VI'] = 'Heading to an Intercept or VI Leg.'
LegTypeDesc['VM'] = 'Heading to a Manual termination or VM Leg.'
LegTypeDesc['VR'] = 'Heading to a Radial termination or VR Leg.'
LegTypeDesc['PI'] = '045/180 Procedure Turn or PI Leg.'
LegTypeDesc['HA'] = 'Holding pattern (Altitude Termination)'
LegTypeDesc['HF'] = 'Holding pattern (Single circuit terminating at the fix)'
LegTypeDesc['HM'] = 'Holding pattern (Manual Termination)'

def field_021(value: str, record):
  value = value.strip()
  if len(value) == 0:
    return value

  if not value.isalpha():
    raise ValueError("Invalid Path and Termination:", value)

  return LegTypeDesc[value]


# 5.22 Turn Direction Valid (TDV)
def field_022(value, record):
  value = value.strip()
  if len(value) > 0:
    if value.isalpha() is False:
      raise ValueError("Invalid Turn Direction Valid (TDV):", value)
  return value


# 5.23 Recommended NAVAID (RECD NAV)
def field_023(value, record):
  value = value.strip()
  if len(value) > 0:
    if value.isalnum() is False or len(value) > 4:
      raise ValueError("Invalid Recommended NAVAID (RECD NAV):", value)
  return value


# 5.24 Theta (THETA)
def field_024(value, record):
  value = value.strip()
  if len(value) > 0:
    if value.isalnum() is False or len(value) > 4:
      raise ValueError("Invalid Theta:", value)
  return value


# 5.25 Rho (RHO)
def field_025(value, record):
  value = value.strip()
  if len(value) > 0:
    if value.isalnum() is False or len(value) > 4:
      raise ValueError("Invalid Rho:", value)
  return value


# 5.26 Outbound Magnetic Course (OB MAG CRS)
def field_026(value, record):
  value = value.strip()

  # Validate the value
  if len(value) == 0:
    return value

  if value.isalnum() is False or len(value) > 4:
    raise ValueError('Invalid Outbound Magnetic Course', value)

  # Handle the 'T' in the tenths position for degrees true
  if value.endswith('T'):
    return value
  else:
    return "{:.1f}".format(float(value) / 10)


# 5.27 Route Distance From, Holding Distance/Time (RTE DIST FROM, HOLD DIST/TIME)
def field_027(value, record):
  value = value.strip()

  if len(value) > 0:
    if value[0] == 'T':
      return "{:.1f} min".format(float(value[1:]) / 10)
    else:
      return "{:.1f} nm".format(float(value) / 10)

  return value


# 5.28 Inbound Magnetic Course (IB MAG CRS)
def field_028(value, record):
  return value


# 5.29 Altitude Description (ALT DESC)
def field_029(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.30 Altitude/Minimum Altitude
def field_030(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.31 File Record Number (FRN)
def field_031(value, record):
  return value


# 5.32 Cycle Date (CYCLE)
def field_032(value, record):
  year = "19" + value[:2] if int(value[:2]) > 50 else "20" + value[:2]
  return '{}, Release {}'.format(year, value[2:])


# 5.33 VOR/NDB Identifier (VOR IDENT/NDB IDENT)
def field_033(value, record):
  return value


# 5.34 VOR/NDB Frequency (VOR/NDB FREQ)
def field_034(value, record):
  value = value.strip()
  if len(value) > 0:
    if value.isnumeric() is False:
      print(f'Unsupported VOR/NDB Frequency: "{value}"')
      print(f'from record type "{record.ident}": "{record.raw}"')
      exit()
    else:
      return "{:.2f}".format(float(value)/100)
  return value


# 5.35 NAVAID Class (CLASS)
def field_035(value, record):
  # elif facility.contains(field):
  #   d = defaultdict(def_val)
  #   d['V'] = 'VOR'
  #   d[' '] = ''
  #   d['D'] = 'DME'
  #   d['T'] = 'TACAN'
  #   d['M'] = 'MIL TACAN'
  #   d['I'] = 'ILS/DME or ILS/TACAN'
  #   d['N'] = 'MLS/DME/N'
  #   d['P'] = 'MLS/DME/P'
  #   return ' '.join([d[val[0]], d[val[1]]]).strip()
  # elif power.contains(field):
  #   d = defaultdict(def_val)
  #   d['T'] = 'Terminal'
  #   d['L'] = 'Low Altitude'
  #   d['H'] = 'High Altitude'
  #   d['U'] = 'Undefined'
  #   d['C'] = 'ILS/TACAN'
  #   return str(d[val])
  # elif field == "Class Info":
  #   d = defaultdict(def_val)
  #   d['D'] = 'Biased ILS/DME or ILS/TACAN'
  #   d['A'] = 'Automatic Transcribed Weather Broadcast'
  #   d['B'] = 'Scheduled Weather Broadcast'
  #   d['W'] = 'No Voice on Frequency'
  #   d[' '] = 'Voice on Frequency'
  #   return str(d[val])
  # elif colloc.contains(field):
  #   collocation[' '] = 'Collocated Navaids'
  #   collocation['N'] = 'Non-Collocated Navaids'
  return value


# 5.36 Latitude (LATITUDE)
def field_036(value, record):
  return value


# 5.37 Longitude (LONGITUDE)
def field_037(value, record):
  return value


# 5.38 DME Identifier (DME IDENT)
def field_038(value, record):
  return value


# 5.39 Magnetic Variation (MAG VAR, D MAG VAR)
def field_039(value, record):
  return value if value.strip() == '' else "{:03} {}".format(int(value[1:]), value[0])


# 5.40 DME Elevation (DME ELEV)
def field_040(value, record):
  return value


# 5.41 Region Code (REGN CODE)
def field_041(value, record):
  return value


# 5.42 Waypoint Type (TYPE)
def field_042(value, record):
  match value[0]:
    case 'C':
      return "Combined Named Intersection and RNAV"
    case 'I':
      return 'Unnamed, Charted Intersection'
    case 'N':
      return 'NDB Navaid as Waypoint' + value[1:]
    case 'R':
      return 'Named Intersection'
    case 'U':
      return 'Uncharted Airway Intersection'
    case 'V':
      return 'VFR Waypoint'
    case 'W':
      return 'RNAV Waypoint'
  match value[1]:
    case 'A':
      return 'Final Approach Fix'
    case 'B':
      return 'Initial and Final Approach Fix'
    case 'C':
      return 'Final Approach Course Fix'
    case 'D':
      return 'Intermediate Approach Fix'
    case 'E':
      return 'Off-Route intersection in FAA National Reference System'
    case 'F':
      return 'Off-Route Intersection'
    case 'I':
      return 'Initial Approach Fix'
    case 'K':
      return 'Final Approach Course Fix at Initial Approach Fix'
    case 'L':
      return 'Final Approach Course Fix at Intermediate Approach Fix'
    case 'M':
      return 'Missed Approach Fix'
    case 'N':
      return 'Initial Approach Fix and Missed Approach Fix'
    case 'O':
      return 'Oceanic Entry/Exit Waypoint'
    case 'P':
      return 'Pitch and Catch Point in the FAA High Altitude Redesign'
    case 'S':
      return 'AACAA and SUA Waypoints in the FAA High Altitude Redesign'
    case 'U':
      return 'FIR/UIR or Controlled Airspace Intersection'
    case 'V':
      return 'Latitude/Longitude Intersection, Full Degree of Latitude'
    case 'W':
      return 'Latitude/Longitude Intersection, Half Degree of Latitude'
    case _:
      return "Unknown Waypoint Type"


# 5.43 Waypoint Name/Description (NAME/DESC)
def field_043(value, record):
  return value.strip()


# 5.44 Localizer/MLS/GLS Identifier (LOC, MLS, GLS IDENT)
def field_044(value, record):
  return value


# 5.45 Localizer Frequency (FREQ)
def field_045(value, record):
  if (value.isnumeric()):
    return "{:.2f}".format(float(value)/100)
  else:
    return "BAD VALUE"


# 5.46 Runway Identifier (RUNWAY ID)
def field_046(value, record):
  return value


# 5.47 Localizer Bearing (LOC BRG)
def field_047(value, record):
  return value


# 5.48 Localizer Position (LOC FR RW END Azimuth/Back Azimuth Position (AZ/BAZ FR RWEND)
def field_048(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.49 Localizer/Azimuth Position Reference (@, +, -)
def field_049(value, record):
  match value:
    case '@':
      return 'Beyond stop end of runway'
    case '+':
      return 'Ahead of approach end of runway'
    case '-':
      return 'To the side of runway'
    case _:
      return value
      # raise ValueError(f'Invalid Localizer Position Reference "{value}"')


# 5.50 Glide Slope Position (GS FR RW THRES) Elevation Position (EL FR RW THRES)
def field_050(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.51 Localizer Width (LOC WIDTH)
def field_051(value, record):
  return value


# 5.52 Glide Slope Angle (GS ANGLE) Minimum Elevation Angle (MIN ELEV ANGLE)
def field_052(value, record):
  return value


# 5.53 Transition Altitude/Level (TRANS ALTITUDE/LEVEL)
def field_053(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.54 Longest Runway (LONGEST RWY)
def field_054(value, record):
  if value.isnumeric():
    return value.lstrip('0')+"00" + " ft"
  else:
    return value


# 5.55 Airport/Heliport Elevation (ELEV)
def field_055(value, record):
  return value


# 5.56 Gate Identifier (GATE IDENT)
def field_056(value, record):
  return value


# 5.57 Runway Length (RUNWAY LENGTH)
def field_057(value, record):
  return value


# 5.58 Runway Magnetic Bearing (RWY BRG)
def field_058(value, record):
  return value


# 5.59 Runway Description (RUNWAY DESCRIPTION)
def field_059(value, record):
  return value


# 5.60 Name (NAME)
def field_060(value, record):
  return value


# 5.61 Notes (Continuation Records) (NOTES)
def field_061(value, record):
  return value


# 5.62 Inbound Holding Course (IB HOLD CRS)
def field_062(value, record):
  if (value.isnumeric()):
    return float(value)/10
  else:
    return "BAD VALUE"


# 5.63 Turn (TURN)
def field_063(value, record):
  return value


# 5.64 Leg Length (LEG LENGTH)
def field_064(value, record):
  return value


# 5.65 Leg Time (LEG TIME)
def field_065(value, record):
  if value.strip() == '':
    return

  try:
    return '{}m {}s'.format(int(value[0]), int(value[1])*6)
  except (ValueError, IndexError) as e:
    print(f'Error: Invalid value passed to format_time. Value: "{value}". Error: {str(e)}')
    return f'Invalid Value: "{value}"'


# 5.66 Station Declination (STN DEC)
def field_066(value, record):
  return value


# 5.67 Threshold Crossing Height (TCH)
def field_067(value, record):
  return value


# 5.68 Landing Threshold Elevation (LANDING THRES ELEV)
def field_068(value, record):
  return value


# 5.69 Threshold Displacement Distance (DSPLCD THR)
def field_069(value, record):
  return value


# 5.70 Vertical Angle (VERT ANGLE)
def field_070(value, record):
  return value


# 5.71 Name Field
def field_071(value, record):
  return value


# 5.72 Speed Limit (SPEED LIMIT)
def field_072(value, record):
  if value.isnumeric():
    return value + " knots (IAS)"
  elif value.strip() == '':
    return value
  else:
    raise ValueError('Invalid speed' + value)


# 5.73 Speed Limit Altitude
def field_073(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.74 Component Elevation (GS ELEV, EL ELEV, AZ ELEV, BAZ ELEV)
def field_074(value, record):
  return value


# 5.75 From/To - Airport/Fix
def field_075(value, record):
  return value


# 5.76 Company Route Ident
def field_076(value, record):
  return value


# 5.77 VIA Code
def field_077(value, record):
  return value


# 5.78 SID/STAR/App/AWY (S/S/A/AWY) SID/STAR/Awy (S/S/AWY)
def field_078(value, record):
  return value


# 5.79 Stopway
def field_079(value, record):
  return value


# 5.80 ILS/MLS/GLS Category (CAT)
def field_080(value, record):
  return value


# 5.81 ATC Indicator (ATC)
def field_081(value, record):
  return value


# 5.82 Waypoint Usage
def field_082(value, record):
  wp = ''
  if value[1] == 'B':
    wp = wp + 'HI and LO Altitude'
  elif value[1] == 'H':
    wp = wp + 'HI Altitude'
  elif value[1] == 'L':
    wp = wp + 'LO Altitude'
  elif value[1] == ' ':
    wp = wp + 'Terminal Use Only'
  elif value[0] == 'R':
    wp = wp + 'RNAV'
  else:
    raise ValueError(f"Invalid Waypoint Usage: '{value}'")
  return wp


# 5.83 To FIX
def field_083(value, record):
  return value


# 5.84 RUNWAY TRANS
def field_084(value, record):
  return value


# 5.85 ENRT TRANS
def field_085(value, record):
  return value


# 5.86 Cruise Altitude
def field_086(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.87 Terminal/Alternate Airport (TERM/ALT ARPT)
def field_087(value, record):
  return value


# 5.88 Alternate Distance (ALT DIST)
def field_088(value, record):
  return value


# 5.89 Cost Index
def field_089(value, record):
  return value


# 5.90 ILS/DME Bias
def field_090(value, record):
  return value


# 5.91 Continuation Record Application Type (APPL)
def field_091(value, record):
  match value:
    case 'A':
      return 'Standard ARINC Continuation containing notes or other formatted data'
    case 'B':
      return 'Combined Controlling Agency/Call Sign and formatted Time of Operation'
    case 'C':
      return 'Call Sign/Controlling Agency Continuation'
    case 'E':
      return 'Primary Record Extension'
    case 'L':
      return 'VHF Navaid Limitation Continuation'
    case 'N':
      return 'Sector Narrative Continuation'
    case 'T':
      return 'Time of Operations Continuation "formatted time data"'
    case 'U':
      return 'Time of Operations Continuation "Narrative time data"'
    case 'V':
      return 'Time of Operations Continuation, Start/End Date'
    case 'P':
      return 'Flight Planning Application Continuation'
    case 'Q':
      return 'Flight Planning Application Primary Data Continuation'
    case 'S':
      return 'Simulation Application Continuation'
    case 'W':
      return 'Airport or Heliport Procedure Data Continuation with SBAS use authorization information'
    case _:
      return 'Unknown Application Type: ' + str(value)


# 5.92 Elevation (FAC ELEV)
def field_092(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.93 Facility Characteristics (FAC CHAR)
def field_093(value, record):
  return value


# 5.94 True Bearing (TRUE BRG)
def field_094(value, record):
  return value


# 5.95 Government Source (SOURCE)
def field_095(value, record):
  return value


# 5.96 Glide Slope Beam Width (GS BEAM WIDTH)
def field_096(value, record):
  return value


# 5.97 Touchdown Zone Elevation (TDZE)
def field_097(value, record):
  return value


# 5.98 ‘TDZE Location (LOCATION)
def field_098(value, record):
  return value


# 5.99 Marker Type (MKR TYPE)
def field_099(value, record):
  return value


# 5.100 Minor Axis Bearing (MINOR AXIS TRUE BRG)
def field_100(value, record):
  return value


# 5.101 Communications Type (COMM TYPE)
def field_101(value, record):
  d = defaultdict(def_val)
  d['ACC'] = 'Area Control Center'
  d['ACP'] = 'Airlift Command Post'
  d['AIR'] = 'Air to Air'
  d['APP'] = 'Approach Control'
  d['ARR'] = 'Arrival Control'
  d['ASO'] = 'Automatic Surface Observing System (ASOS)'
  d['ATI'] = 'Automatic Terminal Info Service (ATIS)'
  d['AWI'] = 'Airport Weather Information Broadcast (AWIB)'
  d['AWO'] = 'Automatic Weather Observing Service (AWOS)'
  d['AWS'] = 'Aerodrome Weather Information Services (AWIS)'
  d['CLD'] = 'Clearance Delivery'
  d['CPT'] = 'Clearance, Pre-Taxi'
  d['CTA'] = 'Control Area (Terminal)'
  d['CTL'] = 'Control'
  d['DEP'] = 'Departure Control'
  d['DIR'] = 'Director (Approach Control Radar)'
  d['EFS'] = 'Enroute Flight Advisory Service (EFAS)'
  d['EMR'] = 'Emergency'
  d['FSS'] = 'Flight Service Station'
  d['GCO'] = 'Ground Comm Outlet'
  d['GND'] = 'Ground Control'
  d['GTE'] = 'Gate Control'
  d['HEL'] = 'Helicopter Frequency'
  d['INF'] = 'Information'
  d['MIL'] = 'Military Frequency'
  d['MUL'] = 'Multicom'
  d['OPS'] = 'Operations'
  d['PAL'] = 'Pilot Activated Lighting (Note 1)'
  d['RDO'] = 'Radio'
  d['RDR'] = 'Radar'
  d['RFS'] = 'Remote Flight Service Station (RFSS)'
  d['RMP'] = 'Ramp/Taxi Control'
  d['RSA'] = 'Airport Radar Service Area (ARSA)'
  d['TCA'] = 'Terminal Control Area'
  d['TMA'] = 'Terminal Control Area'
  d['TML'] = 'Terminal'
  d['TRS'] = 'Terminal Radar Service Area (TRSA)'
  d['TWE'] = 'Transcribe Weather Broadcast (TWEB)'
  d['TWR'] = 'Tower, Air Traffic Control'
  d['UAC'] = 'Upper Area Control'
  d['UNI'] = 'Unicom'
  d['VOL'] = 'Volmet'
  return d[value] if d[value] != "bad value" else value + "BAD VALUE"


# 5.102 Radar (RADAR)
def field_102(value, record):
  match value:
    case 'R':
      return 'Radar Capabilities'
    case 'N':
      return 'No Radar Capabilities'
    case _:
      return value


# 5.103 ‘Communications Frequency (COMM FREQ)
def field_103(value, record):
  if (value.isnumeric()):
    return "{:.2f}".format(float(value)/100)
  else:
    return "BAD VALUE"


# 5.104 Frequency Units (FREQ UNIT)
def field_104(value, record):
  d = defaultdict(def_val)
  d['H'] = 'High Frequency (3000 kHz - 30,000 kHz)'
  d['V'] = 'Very High Frequency (30,000 kHz - 200 MHz)'
  d['U'] = 'Ultra High Frequency (200 MHz - 3000 MHz)'
  d['C'] = 'Communication Channel for 8.33 kHz spacing'
  return d[value] if d[value] != "bad value" else value + "BAD VALUE"


# 5.105 Call Sign (CALL SIGN)
def field_105(value, record):
  return value


# 5.106 Service Indicator (SER IND)
def field_106(value, record):
  if (value.strip() == ''):
    return value
  sections = defaultdict(def_val)
  sections['A  '] = 'Airport Advisory Serivce (AAS)'
  sections['C  '] = 'Community Aerodrome Radio Station (CARS)'
  sections['D  '] = 'Departure Service (Other than Departure Control Unit)'
  sections['F  '] = 'Flight Information Serivce (FIS)'
  sections['I  '] = 'Initial Contact (IC)'
  sections['L  '] = 'Arrival Service (Other than Arrival Control Unit)'
  sections['P  '] = 'Pre-Departure Clearance (Data Link Service)'
  sections['S  '] = 'Aerodrome Flight Information Service (AFIS)'
  sections['T  '] = 'Terminal Area Control (Other than dedicated Terminal Control Unit)'
  sections[' A '] = 'Aerodrome Traffic Frequency (ATF)'
  sections[' C '] = 'Common Traffic Advisory Frequency (CTAF)'
  sections[' M '] = 'Mandatory Frequency (MF) '
  sections[' R '] = 'Air/Air'
  sections[' S '] = 'Secondary Frequency'
  sections['  A'] = 'Air/Ground'
  sections['  D'] = 'VHF Direction Finding Service (VDF)'
  sections['  G'] = 'Remote Communications Air to Ground (RCAG)'
  sections['  L'] = 'Language other than English'
  sections['  M'] = 'Military Use Frequency'
  sections['  P'] = 'Pilot Controlled Light (PCL)'
  sections['  R'] = 'Remote Communications Outlet (RCO)'
  return sections[value]


# 5.107 ATAMIATA Designator (ATA/IATA)
def field_107(value, record):
  return value


# 5.108 IFR Capability (IFR)
def field_108(value, record):
  match value:
    case 'Y':
      return 'Official'
    case 'N':
      return 'Non-official'
    case _:
      raise ValueError('Invalid IFR Capability')


# 5.109 Runway Width (WIDTH)
def field_109(value, record):
  return value


# 5.110 Marker Ident (MARKER IDENT)
def field_110(value, record):
  return value


# 5.111 Marker Code (MARKER CODE)
def field_111(value, record):
  return value


# 5.112 Marker Shape (SHAPE)
def field_112(value, record):
  match value:
    case 'E':
      return 'Elliptical'
    case 'B':
      return 'Bone'
    case _:
      return value


# 5.113 High/Low (HIGH/LOW)
def field_113(value, record):
  match value:
    case 'H':
      return 'High Power (general use)'
    case 'L':
      return 'Low Power (low altitude use)'
    case _:
      return value


# 5.114 Duplicate Identifier (DUP IND)
def field_114(value, record):
  return value


# 5.115 Direction Restriction
def field_115(value, record):
  return value


# 5.116 FIR/UIR Identifier (FIR/UIR IDENT)
def field_116(value, record):
  return value


# 5.117 FIR/UIR Indicator (IND)
def field_117(value, record):
  if value == 'F':
    return 'FIR'
  elif value == 'U':
    return 'UIR'
  elif value == 'B':
    return 'Combined FIR/UIR'
  else:
    return value


# 5.118 Boundary Via (BDRY VIA)
def field_118(value, record):
  s = ''
  match value[0]:
    case 'C':
      s += 'Circle'
    case 'G':
      s += 'Great Circle'
    case 'H':
      s += 'Rhumb Line'
    case 'L':
      s += 'Counter Clockwise ARC'
    case 'R':
      s += 'Clockwise ARC'
    case _:
      print(f'Unsupported Boundary Via: "{value}"')
      return f'Unsupported Value: "{value}"'

  if value[1] == 'E':
    s += ', End of description, return to origin point'

  return s


# 5.119 Arc Distance (ARC DIST)
def field_119(value, record):
  return value


# 5.120 ‘Arc Bearing (ARC BRG)
def field_120(value, record):
  return value


# 5.121 Lower/Upper Limit
def field_121(value, record):
  return value


# 5.122 FIR/UIR ATC Reporting Units Speed (RUS)
def field_122(value, record):
  return value


# 5.123 FIR/UIR ATC Reporting Units Altitude (RUA)
def field_123(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.124 FIR/UIR Entry Report (ENTRY)
def field_124(value, record):
  return value


# 5.125 FIR/UIR Name
def field_125(value, record):
  return value


# 5.126 Restrictive Airspace Name
def field_126(value, record):
  return value


# 5.127 Maximum Altitude (MAX ALT)
def field_127(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.128 Restrictive Airspace Type (REST TYPE)
def field_128(value, record):
  return value


# 5.129 Restrictive Airspace Designation
def field_129(value, record):
  return value


# 5.130 Multiple Code (MULTI CD)
def field_130(value, record):
  return value


# 5.131 Time Code (TIME CD)
def field_131(value, record):
  return value


# 5.132 NOTAM
def field_132(value, record):
  return value


# 5.133 Unit Indicator (UNIT IND)
def field_133(value, record):
  return value


# 5.134 Cruise Table Identifier (CRSE TBL IDENT)
def field_134(value, record):
  return value


# 5.135 Course FROM/TO.
def field_135(value, record):
  if (value.isnumeric()):
    return float(value)/10
  else:
    return "BAD VALUE"


# 5.136 Cruise Level From/To
def field_136(value, record):
  return value


# 5.137 Vertical Separation
def field_137(value, record):
  return value


# 5.138 Time Indicator (TIME IND)
def field_138(value, record):
  return value


# 5.139 Intentionally Left Blank
def field_139(value, record):
  return value


# 5.140 Controlling Agency
def field_140(value, record):
  return value


# 5.141 Starting Latitude
def field_141(value, record):
  return value


# 5.142 Starting Longitude
def field_142(value, record):
  return value


# 5.143 Grid MORA,
def field_143(value, record):
  return value


# 5.144 Center Fix (CENTER FIX)
def field_144(value, record):
  return value


# 5.145 Radius Li
def field_145(value, record):
  return value


# 5.146 Sector Bearing (SEC BRG)
def field_146(value, record):
  return value


# 5.147 Sector Altitude (SEC ALT)
def field_147(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.148 Enroute Alternate Airport (EAA)
def field_148(value, record):
  return value


# 5.149 Figure of Merit (MERIT)
def field_149(value, record):
  return value


# 5.150 Frequency Protection Distance (FREQ PRD)
def field_150(value, record):
  return value


# 5.151 FIR/UIR Address (ADDRESS)
def field_151(value, record):
  return value


# 5.152 Start/End Indicator (S/E IND)
def field_152(value, record):
  return value


# 5.153 Start/End Date
def field_153(value, record):
  return value


# 5.154 Restriction Identifier (REST IDENT)
def field_154(value, record):
  return value


# 5.155 Intentionally Left Blank
def field_155(value, record):
  return value


# 5.156 Intentionally Left Blank
def field_156(value, record):
  return value


# 5.157 Airway Restriction Start/End Date (START/END DATE)
def field_157(value, record):
  return value


# 5.158 Intentionally Left Blank
def field_158(value, record):
  return value


# 5.159 Intentionally Left Blank
def field_159(value, record):
  return value


# 5.160 Units of Altitude (UNIT IND)
def field_160(value, record):
  return value


# 5.161 Restriction Altitude (REST ALT)
def field_161(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.162 Step Climb Indicator (STEP)
def field_162(value, record):
  return value


# 5.163 Restriction Notes
def field_163(value, record):
  return value


# 5.164 EU Indicator (EU IND)
def field_164(value, record):
  return value


# 5.165 Magnetic/True Indicator (M/T IND)
def field_165(value, record):
  if value == 'M':
    return 'Magnetic'
  elif value == 'T':
    return 'True'
  else:
    return value


# 5.166 Channel
def field_166(value, record):
  return value


# 5.167 MLS Azimuth Bearing (MLS AZ BRG) MLS Back Azimuth Bearing (MLS BAZ BRG)
def field_167(value, record):
  return value


# 5.168 Azimuth Proportional Angle Right/Left (AZ PRO RIGHT/LEFT)
# Back Azimuth Proportional Angle Right/Left (BAZ PRO RIGHT/LEFT)
def field_168(value, record):
  return value


# 5.169 Elevation Angle Span (EL ANGLE SPAN)
def field_169(value, record):
  return value


# 5.170 Decision Height (DH)
def field_170(value, record):
  return value


# 5.171 Minimum Descent Height (MDH)
def field_171(value, record):
  return value


# 5.172 Azimuth Coverage Sector Right/Left (AZ COV RIGHT/LEFT) Back Azimuth Coverage Sector Right/Left (BAZ COV RIGHT/LEFT)
def field_172(value, record):
  return value


# 5.173 Nominal Elevation Angle (NOM ELEV ANGLE)
def field_173(value, record):
  return value


# 5.174 Restrictive Airspace Link Continuation (LC)
def field_174(value, record):
  return value


# 5.175 Holding Speed (HOLD SPEED)
def field_175(value, record):
  return value


# 5.176 Pad Dimensions
def field_176(value, record):
  return value


# 5.177 Public/Military Indicator (PUB/MIL)
def field_177(value, record):
  match value:
    case 'C':
      return 'Public / Civil'
    case 'M':
      return 'Military'
    case 'P':
      return 'Private (not open to public)'
    case _:
      return f'Unsupported Value: "{value}"'


# 5.178 Time Zone
def field_178(value, record):
  if value[0].isalpha() and value[1:].isnumeric():
    x = string.ascii_uppercase.index(value[0]) - 12
    y = 'GMT +' + str(x) if x >= 0 else 'GMT -' + str(x)
    return y + ':' + str(value[1:])
  else:
    return f'Unsupported Value: "{value}"'


# 5.179 Daylight Time Indicator (DAY TIME)
def field_179(value, record):
  match value:
    case 'Y':
      return 'Yes'
    case 'N':
      return 'No'
    case _:
      return f'Unsupported Value: "{value}"'


# 5.180 Pad Identifier (PAD IDENT)
def field_180(value, record):
  return value


# 5.181 H24 Indicator (H24)
def field_181(value, record):
  d = defaultdict(def_val)
  d['Y'] = '24-Hour Availability'
  d['N'] = 'Part-time Availability'
  return d[value] if d[value] != "bad value" else value + "BAD VALUE"


# 5.182 Guard/Transmit (G/T)
def field_182(value, record):
  match value:
    case 'G':
      return "Guard (radio receives on this freq)"
    case 'T':
      return "Transmit (radio transmits on this freq)"
    case ' ':
      return "Guards and Transmits"
    case _:
      raise ValueError("bad guard/transmit")


# 5.183 Sectorization (SECTOR)
def field_183(value, record):
  return value


# 5.184 Communication Altitude (COMM ALTITUDE)
def field_184(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.185 Sector Facility (SEC FAC)
def field_185(value, record):
  return value


# 5.186 Narrative
def field_186(value, record):
  return value


# 5.187 Distance Description (DIST DESC)
def field_187(value, record):
  return value


# 5.188 Communications Distance (COMM DIST)
def field_188(value, record):
  return value


# 5.189 Remote Site Name
def field_189(value, record):
  return value


# 5.190 FIR/RDO Identifier (FIR/RDO)
def field_190(value, record):
  return value


# 5.191 Triad Stations (TRIAD STA)
def field_191(value, record):
  return value


# 5.192 Group Repetition Interval (GRI)
def field_192(value, record):
  return value


# 5.193 Additional Secondary Phase Factor (ASF)
def field_193(value, record):
  return value


# 5.194 Initial/Terminus Airport/Fix
def field_194(value, record):
  return value


# 5.195 Time of Operation
def field_195(value, record):
  return value


# 5.196 Name Format Indicator (NAME IND)
def field_196(value, record):
  match value[0]:
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
      return 'Published Name Fix, less than five letters'
    case 'R':
      return 'Published Name Fix, more than five letters'
    case 'T':
      return 'Airport/Rwy Related Fix (Note 2)'
    case 'U':
      return 'UIR Fix'
  match value[1]:
    case 'O':
      return 'Localizer Marker with officially published five - letter identifier'
    case 'M':
      return 'Localizer Marker without officially published five - letter identifier'
    case _:
      return 'Unknown Name Format Indicator'


# 5.197 Datum Code (DATUM)
def field_197(value, record):
  return value


# 5.198 Modulation (MODULN)
def field_198(value, record):
  d = defaultdict(def_val)
  d['A'] = 'Amplitude Modulated'
  d['F'] = 'Frequency Modulated'
  return d[value] if d[value] != "bad value" else value + "BAD VALUE"


# 5.199 Signal Emission (SIG EM)
def field_199(value, record):
  if value.strip() == '':
    return value
  d = defaultdict(def_val)
  d['3'] = 'Double Sideband (A3) '
  d['A'] = 'Single sideband, reduced carrier (A3A) '
  d['B'] = 'Two Independent sidebands (A3B)'
  d['H'] = 'Single sideband, full carrier (A3H) '
  d['J'] = 'Single sideband, suppressed carrier (A3J)'
  d['L'] = 'Lower (single) sideband, carrier unknown'
  d['U'] = 'Upper (single) sideband, carrier unknown'
  return d[value] if d[value] != "bad value" else value + "BAD VALUE"


# 5.200 Remote Facility (REM FAC)
def field_200(value, record):
  return value


# 5.201 Restriction Record Type (REST TYPE)
def field_201(value, record):
  return value


# 5.202 Exclusion Indicator (EXC IND)
def field_202(value, record):
  return value


# 5.203 Block Indicator (BLOCK IND)
def field_203(value, record):
  return value


# 5.204 ARC Radius (ARC RAD)
def field_204(value, record):
  return value


# 5.205 Navaid Limitation Code (NLC)
def field_205(value, record):
  return value


# 5.206 Component Affected Indicator (COMP AFFTD IND)
def field_206(value, record):
  return value


# 5.207 Sector From/Sector To (SECTR)
def field_207(value, record):
  return value


# 5.208 Distance Limitation (DIST LIMIT)
def field_208(value, record):
  return value


# 5.209 Altitude Limitation (ALT LIMIT)
def field_209(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.210 Sequence End Indicator (SEQ END)
def field_210(value, record):
  return value


# 5.211 Required Navigation Performance (RNP)
def field_211(value, record):
  return value


# 5.212 Runway Gradient (RWY GRAD)
def field_212(value, record):
  return value


# 5.213 Controlled Airspace Type (ARSP TYPE)
def field_213(value, record):
  return value


# 5.214 Controlled Airspace Center (ARSP CNTR)
def field_214(value, record):
  return value


# 5.215 Controlled Airspace Classification (ARSP CLASS)
def field_215(value, record):
  return value


# 5.216 Controlled Airspace Name (ARSP NAME)
def field_216(value, record):
  return value


# 5.217 Controlled Airspace Indicator (CTLD ARSP IND)
def field_217(value, record):
  return value


# 5.218 Geographical Reference Table Identifier (GEO REF TBL ID)
def field_218(value, record):
  return value


# 5.219 Geographical Entity (GEO ENT)
def field_219(value, record):
  return value


# 5.220 Preferred Route Use Indicator (ET IND)
def field_220(value, record):
  return value


# 5.221 Aircraft Use Group (ACFT USE GP)
def field_221(value, record):
  return value


# 5.222 GNSS/FMS Indicator (GNSS/FMS IND)
def field_222(value, record):
  return value


# 5.223 Operations Type (OPS TYPE)
def field_223(value, record):
  return value


# 5.224 Route Indicator (RTE IND)
def field_224(value, record):
  return value


# 5.225 Ellipsoidal Height
def field_225(value, record):
  return value


# 5.226 Glide Path Angle (GPA)
def field_226(value, record):
  return value


# 5.227 Orthometric Height (ORTH HGT)
def field_227(value, record):
  return value


# 5.228 Course Width at Threshold (CRSWDTH)
def field_228(value, record):
  return value


# 5.229 Final Approach Segment DATA CRC Remainder (FAS CRC)
def field_229(value, record):
  return value


# 5.230 Procedure Type (PROC TYPE)
def field_230(value, record):
  return value


# 5.231 Along Track Distance (ATD)
def field_231(value, record):
  return value


# 5.232 Number of Engines Restriction (NOE)
def field_232(value, record):
  return value


# 5.233 Turboprop/Jet Indicator (TURBO)
def field_233(value, record):
  return value


# 5.234 RNAV Flag (RNAV)
def field_234(value, record):
  return value


# 5.235 ATC Weight Category (ATC WC)
def field_235(value, record):
  return value


# 5.236 ATC Identifier (ATC ID)
def field_236(value, record):
  return value


# 5.237 Procedure Description (PROC DESC)
def field_237(value, record):
  return value


# 5.238 Leg Type Code (LTC)
def field_238(value, record):
  return value


# 5.239 Reporting Code (RPT)
def field_239(value, record):
  return value


# 5.240 Altitude (ALT)
def field_240(value, record):
  return value.lstrip('0') + " ft" if value.isnumeric() else value


# 5.241 Fix Related Transition Code (FRT Code)
def field_241(value, record):
  return value


# 5.242 Procedure Category (PRO CAT)
def field_242(value, record):
  return value


# 5.243 GLS Station Identifier
def field_243(value, record):
  return value


# 5.244 GLS Channel
def field_244(value, record):
  return value


# 5.245 Service Volume Radius
def field_245(value, record):
  return value


# 5.246 TDMA Slots
def field_246(value, record):
  return value


# 5.247 Station Type
def field_247(value, record):
  return value


# 5.248 Station Elevation WGS84
def field_248(value, record):
  return value


# 5.249 Longest Runway Surface Code (LRSC)
def field_249(value, record):
  return value


# 5.250 Alternate Record Type (ART)
def field_250(value, record):
  return value


# 5.251 Distance To Alternate (DTA)
def field_251(value, record):
  return value


# 5.252 Alternate Type (ALT TYPE)
def field_252(value, record):
  return value


# 5.253 Primary and Additional Alternate Identifier (ALT IDENT)
def field_253(value, record):
  return value


# 5.254 Fixed Radius Transition Indicator (FIXED RAD IND)
def field_254(value, record):
  return value


# 5.255 SBAS Service Provider Identifier (SBAS ID)
def field_255(value, record):
  return value


# 5.256 Reference Path Data Selector (REF PDS)
def field_256(value, record):
  return value


# 5.257 Reference Path Identifier (REF ID)
def field_257(value, record):
  return value


# 5.258 Approach Performance Designator (APD)
def field_258(value, record):
  return value


# 5.259 Length Offset (OFFSET)
def field_259(value, record):
  return value


# 5.260 Terminal Procedure Flight Planning Leg Distance (LEG DIST)
def field_260(value, record):
  return value


# 5.261 Speed Limit Description (SLD)
def field_261(value, record):
  return value


# 5.262 Approach Type Identifier (ATI)
def field_262(value, record):
  return value


# 5.263 HAL
def field_263(value, record):
  return value


# 5.264 VAL
def field_264(value, record):
  return value


# 5.265 Path Point TCH
def field_265(value, record):
  return value


# 5.266 TCH Units Indicator
def field_266(value, record):
  return value


# 5.267 High Precision Latitude (HPLAT)
def field_267(value, record):
  return value


# 5.268 High Precision Longitude (HPLONG)
def field_268(value, record):
  return value


# 5.269 Helicopter Procedure Course (HPC)
def field_269(value, record):
  if value.strip() != '': # this is allowed to be empty for non-heli records?
    return float(value)/10
  return value


# 5.270 TCH Value Indicator (TCHVI)
def field_270(value, record):
  match value:
    case 'I':
      return 'ILS or MLS Glideslope'
    case 'R':
      return 'RNAV Procedure'
    case 'V':
      return 'Visual Glideslope Indicator (VGSI)'
    case 'D':
      return 'Default Value (40 or 50 feet)'
    case ' ':   # this is apparently allowed to be empty, see ARINC SPECIFICATION 424 - Page 165
      return value
    case _:
      raise ValueError(f'Bad TCH Value Indicator: {value}')


# 5.271 Procedure Turn (PROC TURN)
def field_271(value, record):
  return value


# 5.272 TAA Sector Identifier
def field_272(value, record):
  return value


# 5.273 TAA IAF Waypoint
def field_273(value, record):
  return value


# 5.274 TAA Sector Radius
def field_274(value, record):
  return value


# 5.275 Level of Service Name (LSN)
def field_275(value, record):
  return value


# 5.276 ??
def field_276(value, record):
  return value
