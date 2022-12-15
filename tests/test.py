import arinc424.record as a424

if __name__ == "__main__":
    line = 'SSPAD        AA    NZ111480VDU  S37001670E174484910    S37001630E174484940E0200000292     WGEAUCKLAND                      187401707'
    record = a424.Record()
    record.read(line)
    record.dump()
