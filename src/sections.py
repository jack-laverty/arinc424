from collections import defaultdict

class Section:

    section = ''

    def read(self, line):
        self.section += line[4]
        if self.section == 'D':
            self.section += line[5]
        elif self.section == 'P':
            self.section += line[12]
        elif self.section == 'E':
            self.section += line[5]

    def decode(self):
        def def_value():
            return "UNKNOWN: " + "'" + self.section + "'"
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
        return sections[self.section]
    
    def is_airport(self):
        return self.section[0] == 'P'
    
    def is_navaid(self):
        return self.section[0] == 'D'

    def is_enroute(self):
        return self.section[0] == 'E'