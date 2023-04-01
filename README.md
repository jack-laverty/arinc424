# ARINC-424

[![build](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml/badge.svg)](https://github.com/jack-laverty/arinc424/actions/workflows/build.yml)


A python library for parsing and decoding ARINC-424, the international standard file format for aircraft navigation data.

## Installation

* Python 3.10 or greater
* Clone the repository
* Install the package [from local source](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree) (no official package released until the work is finished to some degree)

## Getting Started

### Importing the library
```Python
import arinc424.record as a424
```

### Reading a record
Create a record object. Use the **read()** method to read an ARINC-424 record in string format.

```Python
record = a424.Record()
result = record.read(line)
```

### Viewing a record
After [reading a record](#reading-a-record), **dump()** will print the record to the console.

```Python
# example1.py
if result == a424.ERR_NONE:
    record.dump()
```

```console
foo@bar:~$ python3 example1.py

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
# example2.py
if result == a424.ERR_NONE:
    record.decode()
```

```console
foo@bar:~$ python3 example2.py

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

## Command Line Interface

* search
  * field, substring etc
* filter
* read and dump/decode

## Contribution

More examples of ARINC-424 records will always be useful. The small set of examples kept in ```/data``` are limited, despite
being critical for testing. Feel free to add more examples to the ```/data``` folder, or send them to me directly. Thanks!
