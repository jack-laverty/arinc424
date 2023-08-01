#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
python -m unittest discover -s $BASEDIR -p 'test_reads.py'
