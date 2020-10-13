from json import loads
from pathlib import Path
from collections import defaultdict


class POLY_GEOJSON:
    DATA = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    PATH = Path('geojson/poly')

    for path in PATH.iterdir():
        with open(path, 'r', encoding='utf-8') as f:
            geojson = loads(f.read())

        for feature in geojson['features']:
            properties = feature['properties']
            DATA[properties['region_schema']][properties['region_parent']][properties['region_child']].append(feature)
