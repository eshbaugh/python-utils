#!/usr/bin/env python3

import pandas as pd
import json

in_file = './data/USAspending-data-catalog.json'
out_file = './data/USAspending-data-catalog.csv'

print( 'Coverting ', in_file, ' to ', out_file )

# Read the input file 
with open(in_file) as data_file:
    data = json.load(data_file)

# Convert the data into a Data Frame with the dataset content as rows
df = pd.json_normalize( data, 'dataset')


# Output the CSV file
df.to_csv (out_file, index = True, header = True)
