
class Gate():

    cont_idx = 21
    app_idx = 22

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
            ("Section Code",                        r[4]+r[12]),
            ("Airport ICAO Identifier",             r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Gate Identifier",                     r[13:18]),
            ("Continuation Record No",              r[21]),
            ("Gate Latitude",                       r[32:41]),
            ("Gate Longitude",                      r[41:51]),
            ("Name",                                r[98:123]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4]+r[12]),
            ("Airport ICAO Identifier",             r[6:10]),
            ("ICAO Code",                           r[10:12]),
            ("Gate Identifier",                     r[13:18]),
            ("Continuation Record No",              r[21]),
            ("Notes",                               r[23:92]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]
