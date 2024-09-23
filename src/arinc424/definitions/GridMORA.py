from arinc424.decoder import Field
import arinc424.decoder as decoder

# 4.1.19  Grid MORA Records (AS) 
 
# The Grid MORA (Minimum Off Rate Altitude) file 
# contains a table of Minimum Off Route Altitudes. 
class GridMORA():

  def read(self, line, primary):
    return self.read_primary(line)

  # 4.1.19.1  Grid MORA Primary Records
  def read_primary(self, r):
    return [
      Field("Record Type",                         r[0],          decoder.field_002),
      Field("Section Code",                        r[4:6],        decoder.field_004),
      Field("Starting Latitude",                   r[13:16],      decoder.field_141),
      Field("Starting Longitude",                  r[16:20],      decoder.field_142),
      Field("MORA",                                r[30:33],      decoder.field_143),
      Field("MORA (2)",                            r[33:36],      decoder.field_143),
      Field("MORA (3)",                            r[36:39],      decoder.field_143),
      Field("MORA (4)",                            r[39:42],      decoder.field_143),
      Field("MORA (5)",                            r[42:45],      decoder.field_143),
      Field("MORA (6)",                            r[45:48],      decoder.field_143),
      Field("MORA (7)",                            r[48:51],      decoder.field_143),
      Field("MORA (8)",                            r[51:54],      decoder.field_143),
      Field("MORA (9)",                            r[54:57],      decoder.field_143),
      Field("MORA (10)",                           r[57:60],      decoder.field_143),
      Field("MORA (11)",                           r[60:63],      decoder.field_143),
      Field("MORA (12)",                           r[63:66],      decoder.field_143),
      Field("MORA (13)",                           r[66:69],      decoder.field_143),
      Field("MORA (14)",                           r[69:72],      decoder.field_143),
      Field("MORA (15)",                           r[72:75],      decoder.field_143),
      Field("MORA (16)",                           r[75:78],      decoder.field_143),
      Field("MORA (17)",                           r[78:81],      decoder.field_143),
      Field("MORA (18)",                           r[81:84],      decoder.field_143),
      Field("MORA (19)",                           r[84:87],      decoder.field_143),
      Field("MORA (21)",                           r[87:90],      decoder.field_143),
      Field("MORA (22)",                           r[90:93],      decoder.field_143),
      Field("MORA (23)",                           r[93:96],      decoder.field_143),
      Field("MORA (24)",                           r[96:99],      decoder.field_143),
      Field("MORA (25)",                           r[99:102],     decoder.field_143),
      Field("MORA (26)",                           r[102:105],    decoder.field_143),
      Field("MORA (27)",                           r[105:108],    decoder.field_143),
      Field("MORA (28)",                           r[108:111],    decoder.field_143),
      Field("MORA (29)",                           r[111:114],    decoder.field_143),
      Field("MORA (30)",                           r[114:117],    decoder.field_143),
      Field("MORA (31)",                           r[117:120],    decoder.field_143),
      Field("File Record No",                      r[123:128],    decoder.field_031),
      Field("Cycle Date",                          r[128:132],    decoder.field_032)
    ]