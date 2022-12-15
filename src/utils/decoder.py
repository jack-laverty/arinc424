from collections import defaultdict

class Decoder():

    def init(self):
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