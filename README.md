# ARINC 424 Parser
An open-source parser for ARINC-424, the international standard file format for aircraft navigation data.

## Overview
The parser is provided input files in ARINC-424-18 format. Each record is read from the input file and written to an output file in JSON format. The output file(s) are located in the output folder. JSON is more human readable and a better intermediary format for importing the navigation data into a modern database.

Records that are partially complete, or of the wrong format, will be flagged and omitted from the program output.


## Getting Started
* Clone the repository
* Install the dependencies

## Dependencies
* Python3
* PyMongo (Optional)
    * https://pymongo.readthedocs.io/en/stable/installation.html

## Supported Versions
* ARINC-424-18
