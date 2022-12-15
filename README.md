# ARINC 424 Tool
An open-source tool for parsing and decoding ARINC-424, the international standard file format for aircraft navigation data.

## Getting Started
* Clone the repository
* Install the dependencies

### Dependencies
* Python3
* PyMongo (Optional)
    * https://pymongo.readthedocs.io/en/stable/installation.html

## Usage

### Reading a record
Include the module, instantiate an object, and provide the read() function with an ARINC-424 record in string format. If the string is a valid ARINC-424 record, the **read()** function returns a [Record](#record-class)

### Printing a record
After creating a record object, **[obj].print()** can be called to print a record.

### Writing a record to a file
After creating a record object, **[obj].write(f)** can be called append the record output to a file. As with printing a record, the record can be written to a file in any of the output formats.

## Details

### Record Class
When an ARINC-424 record is read, the result is stored in a **Record**.

**Record** objects hold information about that record, such as what *type* of record it is, what *fields* the record contains, and what values are in those fields.


### Output Formats
**Record** objects can output the data they hold. The data can be output in a several formats.

* decoded - the most human readable format
* JSON (single line) - useful for importing the records to a database
* raw data - the unmodified string from which the record object was created

### Supported Versions
* ARINC-424-18

