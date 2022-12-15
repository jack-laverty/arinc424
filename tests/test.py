from arinc424 import arinc424

if __name__ == "__main__":
    # with open('./input/navigation_data.pc') as f:
    #     tool = arinc424.Arinc424Tool()
        # for line in f.readlines():
        #     pass
            # record = tool.read(line)
            # record.dump()

    line = 'SSPAD        AA    NZ111480VDU  S37001670E174484910    S37001630E174484940E0200000292     WGEAUCKLAND                      187401707'
    tool = arinc424.Arinc424Tool()
    record = tool.read(line)
    record.dump()
