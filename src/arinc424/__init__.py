from termcolor import colored
from .record import Record
from prettytable import PrettyTable
from collections import Counter
import os
from tqdm import tqdm


def parse(line, output=True):
  """
  Parse an ARINC-424 record and dump the
  contents to the console as plaintext.
  """
  r = Record()
  if r.read(line):
    r.decode(output)
    return True
  return False


def search(file, filters):
  """
  Search an ARINC-424 file and find all the
  records that contain given substrings.
  """
  with open(file) as f:
    count = 0
    r = Record()
    for line in f.readlines():
      r.reset()
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


def read_file(path, output=True):
    """
    Parse all ARINC-424 records within a file.
    """
    good, bad = 0, 0
    counts = Counter()
    with open(path) as f:
        lines = f.readlines()

    r = Record()
    with tqdm(total=len(lines), unit='rec', desc=os.path.basename(path)) as pbar:
        for line in lines:
            r.reset()
            if r.read(line):
                counts[r.definition.name] += 1
                if output:
                    r.decode(output)
                good += 1
            else:
                bad += 1
            pbar.update(1)
            pbar.set_postfix(good=good, bad=bad)

    table = PrettyTable(field_names=['Name', 'Count'])
    table.align = 'l'
    for name, count in sorted(counts.items(), key=lambda x: -x[1]):
        table.add_row([name, count])
    print(table)
    print(f'Total: {good} records ({bad} bad)')
