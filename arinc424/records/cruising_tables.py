
class CruisingTables():

    def read(self, line):
        return self.read_primary(line)

    def read_primary(self, r):
        return [
            ("Record Type",                             r[0]),
            ("Section Code",                            r[4:6]),
            ("Cruising Table Identifier",               r[6:8]),
            ("Sequence Number",                         r[8]),
            ("Course From",                             r[28:32]),
            ("Course To",                               r[32:36]),
            ("Mag/True",                                r[36]),
            ("Cruise Level From",                       r[39:44]),
            ("Vertical Separation",                     r[44:49]),
            ("Cruise Level To",                         r[49:54]),
            ("Cruise Level From",                       r[54:59]),
            ("Vertical Separation",                     r[59:64]),
            ("Cruise Level To",                         r[64:69]),
            ("Cruise Level From",                       r[69:74]),
            ("Vertical Separation",                     r[74:79]),
            ("Cruise Level To",                         r[79:84]),
            ("Cruise Level From",                       r[84:89]),
            ("Vertical Separation",                     r[89:94]),
            ("Cruise Level To",                         r[94:99]),
            ("File Record No",                          r[123:128]),
            ("Cycle Date",                              r[128:132]),
        ]
