# -*- coding: utf-8 -*-

import sys
import json

import pandas as pd

def main(fpath, d_fpath):
    df = pd.read_csv(fpath)
    content = []
    for idx, row in df.iterrows():
        obj = {}
        for k,v in row.iteritems():
            obj[k] = v
        content.append(obj)

    with open(d_fpath, "w") as fd:
        fd.write(json.dumps(content))

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: csv_to_json.py $csv_file $json_file")
        sys.exit(1)

    main(*sys.argv[1:])

