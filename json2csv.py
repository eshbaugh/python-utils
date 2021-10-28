#!/usr/bin/env python3

import pandas as pd
import json

in_file = './data/USAspending-data-catalog.json'
out_file = './data/USAspending-data-catalog.csv'

print( 'Coverting ', in_file, ' to ', out_file )

# Read the input file into a Data Frame


with open(in_file) as data_file:
    data = json.load(data_file)

df = pd.json_normalize( data, 'dataset')
#df = pd.read_json (in_file)

print( df )

df.to_csv (out_file, index = True, header = True)
