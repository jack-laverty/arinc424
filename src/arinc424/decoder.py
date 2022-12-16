from collections import defaultdict

class Decoder():

    def init(self):
        def def_value():
            return "UNKNOWN SECTION"
            exit()
        sections = defaultdict(def_value)
        sections['AA'] = 'Grid MORA'
        sections['D '] = 'VHF Navaid'
        sections['DD'] = 'NDB Navaid'
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
        return

    def freq(self, val):
        return float(val)/100

    def continuation(self, val):
        return int(val)

    def record_type(self, val):
        if val == 'S':
            return 'Standard'
        elif val == 'T':
            return 'Tailored'
        else:
            return 'Error: invalid record type'
    
    def cycle_date(self, val):
        s = ''
        s += "Revision Year" + int("20" + val[:2]) + '\n'
        s += "Release Cycle" + int(val[2:])
        return s

    def dme_elevation(self, val):
        if val.strip() == '':
            return '<Blank>'
        else:
            return val.lstrip('0') + " ft"

    def gps(self, val):
        x = len(val)
        if val.strip() == '':
            return '<Blank>'
        else:
            return ' '.join([val[1:x-6], val[x-6:x-4], val[x-4:x-2], val[x-2:x], val[0]])
    
    # frequency protection
    # ILS/DME bias
    # station declination
    def generic_text(self, val):
        return val.strip() if val.strip() != '' else '<Blank>'

    def navaid_class(self, val):
        def def_value():
            return "<UNKNOWN>"
        facility = defaultdict(def_value)
        power = defaultdict(def_value)
        info = defaultdict(def_value)
        collocation = defaultdict(def_value)
        facility['V']       = 'VOR'
        facility[' ']       = ''
        facility['D']       = 'DME'
        facility['T']       = 'TACAN'
        facility['M']       = 'MIL TACAN'
        facility['I']       = 'ILS/DME or ILS/TACAN'
        facility['N']       = 'MLS/DME/N'
        facility['P']       = 'MLS/DME/P'
        power['T']          = 'Terminal'
        power['L']          = 'Low Altitude'
        power['H']          = 'High Altitude'
        power['U']          = 'Undefined'
        power['C']          = 'ILS/TACAN'
        info['D']           = 'Biased ILS/DME or ILS/TACAN'
        info['A']           = 'Automatic Transcribed Weather Broadcast'
        info['B']           = 'Scheduled Weather Broadcast'
        info['W']           = 'No Voice on Frequency'
        info[' ']           = 'Voice on Frequency'
        collocation[' ']    = 'Collocated Navaids'
        collocation['N']    = 'Non-Collocated Navaids'

        return {
                "Facility":     facility[val[0]] + facility[val[1]],
                "Power":        power[val[2]],
                "Info":         info[val[3]],
                "Collocation":  collocation[val[4]],
        }
    
    def section(self, val):
        return sections[val]