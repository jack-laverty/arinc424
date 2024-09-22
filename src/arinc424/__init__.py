from termcolor import colored
from .record import Record
import os


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


def read_file(path, output=True):
  """
  Parse all ARINC-424 records within a file.
  """
  with open(path) as f:
    for line in f.readlines():
      parse(line, output)


def read_folder(path):
  """
  Parse all ARINC-424 records for every file in a given folder.
  """
  for file in os.scandir(path):
    read_file(os.path.join(path, file.name))
