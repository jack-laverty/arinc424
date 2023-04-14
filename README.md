# ARINC-424

[![build](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml/badge.svg)](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml)


A python library for parsing and decoding ARINC-424, the international standard file format for aircraft navigation data.

## Requirements
* Python >= 3.10

## Installation

```bash
pip install arinc424
```

## Getting Started

### Reading a record
Create a record object. Use the **read()** method to read an ARINC-424 record in string format.

```Python
import arinc424.record as arinc424

record = arinc424.Record()
record.read(line)
```

### Viewing a record
After [reading a record](#reading-a-record), **dump()** will print the record to the console.

```Python
record.dump()
```

```console
foo@bar:~$ python3 dump_example.py

Record Type               : S
Customer / Area Code      : USA
Section Code              : ER
.
.
.
Cycle Date                : 8704
```

### Decoding a record
Similar to **dump()**, but each value in the key-value pair is decoded to be human readable without referencing the ARINC-424 spec.
```Python
record.decode()
```

```console
foo@bar:~$ python3 decode_example.py

Record Type               : Standard Record
Customer / Area Code      : United States of America
Section Code              : Airways and Routes
.
.
.
Cycle Date                : 1987, April
```

### Writing a record to a file

In addition to printing to the console, **dump()** and **decode()** will return strings which can
be written to files.

* decoded - the most human readable format
* JSON (single line) - useful for importing the records to a database
* raw data - the unmodified string from which the record object was created

```Python
f = open("output.txt", "w")

# writes the fields as they are
f.write(record.dump())

# writes the record in single-line JSON format
f.write(record.json())
```
