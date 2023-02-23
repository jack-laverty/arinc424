
class Holding():

    cont_idx = 38
    app_idx = 39

    def read(self, line):
        if int(line[self.cont_idx]) < 2:
            return self.read_primary(line)
        else:
            match line[self.app_idx]:
                case 'A':
                    return self.read_cont(line)
                case _:
                    print("Unsupported Application Type")
                    return []

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4:6]),
            ("Region Code",                         r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Duplicate Identifier",                r[27:29]),
            ("Fix Identifier",                      r[29:34]),
            ("ICAO Code",                           r[34:36]),
            ("Section Code",                        r[36:38]),
            ("Continuation Record No",              r[38]),
            ("Inbound Holding Course",              r[39:43]),
            ("Turn Direction",                      r[43]),
            ("Leg Length",                          r[44:47]),
            ("Leg Time",                            r[47:49]),
            ("Minimum Altitude",                    r[49:54]),
            ("Maximum Altitude",                    r[54:59]),
            ("Holding Speed",                       r[59:62]),
            ("RNP",                                 r[62:65]),
            ("Arc Radius",                          r[65:71]),
            ("Name",                                r[98:123]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132]),
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4:6]),
            ("Region Code",                         r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Duplicate Identifier",                r[27:29]),
            ("Fix Identifier",                      r[29:34]),
            ("ICAO Code",                           r[34:36]),
            ("Section Code",                        r[36:38]),
            ("Continuation Record No",              r[38]),
            ("Application Type",                    r[40]),
            ("Notes",                               r[40:109]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132]),
        ]
