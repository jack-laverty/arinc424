import records.airport as airport
import records.navaid as navaid
import utils.sections
import utils.record

class Arinc424Tool():
    
    def __init__(self):
        return
    
    def read(self, line):

        record = utils.record.Record()

        if line.startswith('S' or 'T') == False:
            return None

        section = utils.sections.Section()
        section.read(line)

        if section.is_navaid():
            record.fields = navaid.read_fields(section, line)
        elif section.is_airport():
            record.fields = airport.read_fields(section, line)
        
        return record
    
    def write(self):
        pass
        # dir = os.path.join("..", "output")
        # if not os.path.exists(dir):
        #     os.mkdir(dir)
        # out_file = "output"
        # w = open(dir + "\\" + out_file + ".json", 'w')
