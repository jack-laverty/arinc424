from collections import defaultdict

def parse_section(line):

    def def_value():
        return "<UNKNOWN>"
      
    section, subsection = '',''
    sect = defaultdict(def_value)
    sub = defaultdict(def_value)

    sect['A'] = 'MORA'
    sect['D'] = 'Navaid'
    sect['E'] = 'Enroute'
    sect['H'] = 'Heliport'
    sect['P'] = 'Airport'
    sect['R'] = 'Company Routes'
    sect['T'] = 'Tables'
    sect['U'] = 'Airspace'

    if line[4] == 'A':
        sub['A'] = 'Grid MORA'
    elif line[4] == 'D':
        sub[' '] = 'VHF Navaid'
        sub['D'] = 'NDB Navaid'
    elif line[4] == 'E':
        sub['A'] = 'Waypoints'
        sub['M'] = 'Airway Markers'
        sub['P'] = 'Holding Patterns'
        sub['R'] = 'Airways and Routes'
        sub['T'] = 'Preferred Routes'
        sub['U'] = 'Airway Restrictions'
        sub['V'] = 'Communications'
    elif line[4] == 'H':
        sub['A'] = 'Pads'
        sub['C'] = 'Terminal Waypoints'
        sub['D'] = 'SIDs'
        sub['E'] = 'STARs'
        sub['F'] = 'Approach Procedures'
        sub['K'] = 'TAA'
        sub['S'] = 'MSA'
        sub['V'] = 'Communications'
    elif line[4] == 'P':
        sub['A'] = 'Reference Points'
        sub['B'] = 'Gates'
        sub['C'] = 'Terminal Waypoints'
        sub['D'] = 'SIDs'
        sub['E'] = 'STARs'
        sub['F'] = 'Approach Procedures'
        sub['G'] = 'Runways'
        sub['I'] = 'Localizer/Glideslope'
        sub['K'] = 'TAA'
        sub['L'] = 'MLS'
        sub['M'] = 'Localizer Marker'
        sub['N'] = 'Terminal NDB'
        sub['P'] = 'Path Point'
        sub['R'] = 'Flt Planning ARR/DEP'
        sub['S'] = 'MSA'
        sub['T'] = 'GLS Station'
        sub['V'] = 'Communications'
    elif line[4] == 'R':
        sub[' '] = 'Company Routes'
        sub['A'] = 'Alternate Records'
    elif line[4] == 'T':
        sub['C'] = 'Crusing Tables'
        sub['G'] = 'Geographical Reference'
        sub['N'] = 'RNAV Name Table'
    elif line[4] == 'U':
        sub['C'] = 'Controller Airspace'
        sub['F'] = 'FIR/UIR'
        sub['R'] = 'Restrictive Airspace'

    section = sect[line[4]]
    subsection = sub[line[5]]
    return section, subsection