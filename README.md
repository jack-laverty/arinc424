# ARINC-424

[![build](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml/badge.svg)](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml)

An open-source tool for parsing and decoding ARINC-424, the international standard file format for aircraft navigation data.

## Installation

* Python 3.11 or greater
* Clone the repository
* Install the package [from local source](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree)

This library is still under development. One day it will be good enough to distribute through a package manager. That day is not today.

## Getting Started

### Importing the library
```Python
import arinc424.record as a424
```

### Reading a record
Create a record object. Use the **read()** method to read an ARINC-424 record in string format.

```Python
record = a424.Record()
record.read(line)
```

### Viewing a record
After [reading a record](#reading-a-record), **dump()** will print the record to the console.

```Python
record.dump()
```

```console
foo@bar:~$ python3 test.py

Record Type               : S
Customer / Area Code      : FOO
Airport ICAO Identifier   : BAR
.
.
.
and so on
```

### Writing a record to a file

```Python
f = open("output.txt", "w")

# writes the fields as they are
f.write(record.dump())

# writes the record in single-line JSON format
f.write(record.json())
```

### Decoding a record
Similar to **dump()**, but each value in the key-value pair is decoded to be human readable without referencing the ARINC-424 spec.
```Python
record.decode()
```

## Details

### Record Module
When an ARINC-424 record is read, the result is stored in a **Record** object.

**Record** objects hold information about that record, such as what *type* of record it is, what *fields* the record contains, and what values are in those fields.

### Output Formats

**Record** objects can output the data they hold. The data can be output in a several formats.

* decoded - the most human readable format
* JSON (single line) - useful for importing the records to a database
* raw data - the unmodified string from which the record object was created

### Supported Versions
* ARINC-424-18

