
class ControlledAirspace():

    cont_idx = 24
    app_idx = 25

    def read(self, r):
        if int(r[self.cont_idx]) < 2:
            return self.read_primary(r)
        else:
            match r[self.app_idx]:
                case 'A':
                    return self.read_cont(r)
                case _:
                    raise ValueError('Unknown Application Type')

    def read_primary(self, r):
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":                        r[4:6],
            "ICAO Code":                           r[6:8],
            "Airspace Type":                       r[9],
            "Airspace Center":                     r[9:14],
            "Section Code (2)":                    r[14:16],
            "Airspace Classification":             r[16],
            "Multiple Code":                       r[19],
            "Sequence Number":                     r[20:24],
            "Continuation Record No":              r[24],
            "Level":                               r[25],
            "Time Code":                           r[26],
            "NOTAM":                               r[27],
            "Boundary Via":                        r[30:32],
            "Latitude":                            r[32:41],
            "Longitude":                           r[41:51],
            "Arc Origin Latitude":                 r[51:60],
            "Arc Origin Longitude":                r[60:70],
            "Arc Distance":                        r[70:74],
            "Arc Bearing":                         r[74:78],
            "RNP":                                 r[78:81],
            "Lower Limit":                         r[81:86],
            "Unit Indicator":                      r[86],
            "Upper Limit":                         r[87:92],
            "Unit Indicator (2)":                  r[92],
            "Controlled Airspace Name":            r[93:123],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }

    def read_cont(self, r):
        # standard ARINC continuation containing notes or other
        # formatted data
        return {
            "Record Type":                         r[0],
            "Customer / Area Code":                r[1:4],
            "Section Code":                        r[4:6],
            "ICAO Code":                           r[6:8],
            "Airspace Type":                       r[9],
            "Airspace Center":                     r[9:14],
            "Section Code (2)":                    r[14:16],
            "Airspace Classification":             r[16],
            "Multiple Code":                       r[19],
            "Sequence Number":                     r[20:24],
            "Continuation Record No":              r[24],
            "Application Type":                    r[25],
            "Time Code":                           r[26],
            "NOTAM":                               r[27],
            "Time Indicator":                      r[28],
            "Time of Operations":                  r[29:39],
            "Time of Operations (2)":              r[39:49],
            "Time of Operations (3)":              r[49:59],
            "Time of Operations (4)":              r[59:69],
            "Time of Operations (5)":              r[69:79],
            "Time of Operations (6)":              r[79:89],
            "Time of Operations (7)":              r[89:99],
            "Controlling Agency":                  r[99:123],
            "File Record No":                      r[123:128],
            "Cycle Date":                          r[128:132]
        }
