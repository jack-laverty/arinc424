# ARINC-424

[![build](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml/badge.svg)](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml)


A python library for parsing and decoding ARINC-424, the international standard file format for aircraft navigation data.

## Requirements
* Python >= 3.10

## Installation

Install the latest release with:
```bash
pip install arinc424
```

or clone the repository and install the package [from local source](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree)
for an editable local version of the library.
```bash
cd /arinc424
python3 -m pip install -e .
```

## Getting Started

### Parsing a Record

```Python
# parse_example.py

import arinc424

arinc424.parse("SUSAP KSEAK1ASEA     110000119Y N47265700W122182910E019900429250SEA K11800018000CU00Y NAS    SEATTLE-TACOMA INTL           045698808")
```

```console
foo@bar:~$ python3 parse_example.py

+---------------------------------+----------------------------------+--------------------------------+
| Field                           | Value                              | Decoded                      |
+---------------------------------+----------------------------------+--------------------------------+
| Record Type                     | 'S'                              | Standard                       |
| Customer / Area Code            | 'USA'                            | United States of America       |
| Section Code                    | 'PA'                             | Airport Reference Point        |
| Airport ICAO Identifier         | 'KSEA'                           | KSEA                           |
| ICAO Code                       | 'K1'                             | K1                             |
| ATA/IATA Designator             | 'SEA'                            | SEA                            |
| Continuation Record No          | '1'                              | Primary Record (with Cont.)    |
| Speed Limit Altitude            | '10000'                          | 10000 ft                       |
| Longest Runway                  | '119'                            | 11900 ft                       |
| IFR Capability                  | 'Y'                              | Official                       |
| Longest Runway Surface Code     | ' '                              |                                |
| Airport Reference Pt. Latitude  | 'N47265700'                      | N47265700                      |
| Airport Reference Pt. Longitude | 'W122182910'                     | W122182910                     |
| Magnetic Variation              | 'E0199'                          | 199 E                          |
| Airport Elevation               | '00429'                          | 00429                          |
| Speed Limit                     | '250'                            | 250 knots (IAS)                |
| Recommended Navaid              | 'SEA '                           | SEA                            |
| ICAO Code (2)                   | 'K1'                             | K1                             |
| Transition Altitude             | '18000'                          | 18000 ft                       |
| Transition Level                | '18000'                          | 18000 ft                       |
| Public Military Indicator       | 'C'                              | Public / Civil                 |
| Time Zone                       | 'U00'                            | GMT +8:00                      |
| Daylight Indicator              | 'Y'                              | Yes                            |
| Magnetic/True Indicator         | ' '                              |                                |
| Datum Code                      | 'NAS'                            | NAS                            |
| Airport Name                    | 'SEATTLE-TACOMA INTL           ' | SEATTLE-TACOMA INTL            |
| File Record No                  | '04569'                          | 04569                          |
| Cycle Date                      | '8808'                           | 1988, Release 08               |
+---------------------------------+----------------------------------+--------------------------------+
```

### Parsing a File

This function calls arinc424.parse() for every line of a given file.

```Python
path = 'path/to/arinc424_file'
arinc424.read_file(path)
```

## The Record Class

The examples in the [Getting Started](#getting-started) section utilise the ```arinc424.parse()``` function. Under the hood this function is creating a Record object, populating the fields of the record object with data from the provided record, and then calling the ```decode()``` function. This can also be done manually.

### Reading a Record

```Python
import arinc424

record = arinc424.Record()
record.read("SUSAP KSEAK1ASEA     110000119Y N47265700W122182910E019900429250SEA K11800018000CU00Y NAS    SEATTLE-TACOMA INTL           045698808")
record.decode()
```

### Writing a Record to a File

In addition to printing to the console, **decode()** will return a string which can be written to a file.

```Python
f = open("output.txt", "w")

# writes the record as plaintext
f.write(record.decode())

# writes the record in JSON format
f.write(record.json())

```

### Helper Functions

```Python

# True if primary record, otherwise False
record.primary()

# True if record is primary record with at least one continuation record to follow, otherwise False
record.hasCont()

#NOTE: both of these functions will return False if the record object has not been initialised with ARINC-424 data

```
