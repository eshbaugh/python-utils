#!/usr/bin/env python3

import pandas as pd

in_file = './data/USAspending-data-catalog.json'
out_file = './data/USAspending-data-catalog.csv'

print( 'Coverting ', in_file, ' to ', out_file )

df = pd.read_json (in_file)
df.to_csv (out_file, index = None)
