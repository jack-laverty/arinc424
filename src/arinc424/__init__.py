from termcolor import colored
from .record import Record


def parse(line):
    """
    Parse an ARINC-424 record and dump the
    contents to the console as plaintext.
    """
    r = Record()
    if r.read(line):
        r.decode()


def search(file, filters):
    """
    Parse an ARINC-424 file and find all the
    records that contain given substrings.
    """
    with open(file) as f:
        count = 0
        for line in f.readlines():
            r = Record()
            if r.read(line) is False:
                continue
            if isinstance(filters, str):
                if filters not in r.raw:
                    continue
            elif isinstance(filters, list):
                if all(map(r.raw.__contains__, filters)) is False:
                    continue
            print(r.raw)
            count = count + 1
        print(colored(f"Found {count} records that contain {filters}", 'green' if count else 'red'))
