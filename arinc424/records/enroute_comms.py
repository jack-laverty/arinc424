
class EnrouteComms():

    cont_idx = 55
    app_idx = 56

    def read(self, r):
        if int(r[self.cont_idx]) < 2:
            return self.read_primary(r)
        else:
            match r[self.app_idx]:
                case 'A':
                    return self.read_cont(r)
                case 'T':
                    return self.read_timeop(r)
                case _:
                    raise ValueError('{}\n{}\n{}'.format("Unknown Value",
                                                         r[self.app_idx], r))

    def read_primary(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4:6]),
            ("FIR/RDO Ident",                       r[6:10]),
            ("FIR/UIR Address",                     r[10:14]),
            ("Indicator",                           r[14]),
            ("Remote Name",                         r[18:43]),
            ("Communications Type",                 r[43:46]),
            ("Comm Frequency",                      r[46:53]),
            ("Guard/Transmit",                      r[53]),
            ("Frequency Units",                     r[54]),
            ("Continuation Record No",              r[55]),
            ("Service Indicator",                   r[56:59]),
            ("Radar Service",                       r[59]),
            ("Modulation",                          r[60]),
            ("Signal Emission",                     r[61]),
            ("Latitude",                            r[62:71]),
            ("Longitude",                           r[71:81]),
            ("Magnetic Variation",                  r[81:86]),
            ("Facility Elevation",                  r[86:91]),
            ("H24 Indicator",                       r[91]),
            ("Altitude Description",                r[92]),
            ("Communication Altitude",              r[93:98]),
            ("Communication Altitude",              r[98:103]),
            ("Remote Facility",                     r[103:107]),
            ("ICAO Code",                           r[107:109]),
            ("Section Code",                        r[109:111]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4:6]),
            ("FIR/RDO Ident",                       r[6:10]),
            ("FIR/UIR Address",                     r[10:14]),
            ("Indicator",                           r[14]),
            ("Remote Name",                         r[18:43]),
            ("Communications Type",                 r[43:46]),
            ("Comm Frequency",                      r[46:53]),
            ("Guard/Transmit",                      r[53]),
            ("Frequency Units",                     r[54]),
            ("Continuation Record No",              r[55]),
            ("Application Type",                    r[56]),
            ("Time Code",                           r[57]),
            ("NOTAM",                               r[58]),
            ("Time Indicator",                      r[59]),
            ("Time of Operation",                   r[60:70]),
            ("Call Sign",                           r[93:123]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]

    def read_timeop(self, r):
        return [
            ("Record Type",                         r[0]),
            ("Customer / Area Code",                r[1:4]),
            ("Section Code",                        r[4:6]),
            ("FIR/RDO Ident",                       r[6:10]),
            ("FIR/UIR Address",                     r[10:14]),
            ("Indicator",                           r[14]),
            ("Remote Name",                         r[18:43]),
            ("Communications Type",                 r[43:46]),
            ("Comm Frequency",                      r[46:53]),
            ("Guard/Transmit",                      r[53]),
            ("Frequency Units",                     r[54]),
            ("Continuation Record No",              r[55]),
            ("Application Type",                    r[56]),
            ("Time of Operation",                   r[60:70]),
            ("Time of Operation",                   r[70:80]),
            ("Time of Operation",                   r[80:90]),
            ("Time of Operation",                   r[90:100]),
            ("Time of Operation",                   r[100:110]),
            ("Time of Operation",                   r[110:120]),
            ("File Record No",                      r[123:128]),
            ("Cycle Date",                          r[128:132])
        ]
