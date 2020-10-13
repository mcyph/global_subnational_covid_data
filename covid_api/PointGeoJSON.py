from json import loads
from pathlib import Path
from collections import defaultdict


class POINT_GEOJSON:
    DATA = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    PATH = Path('geojson/point')

    for path in PATH.iterdir():
        with open(path, 'r', encoding='utf-8') as f:
            geojson = loads(f.read())

        for feature in geojson['features']:
            properties = feature['properties']
            DATA[properties['region_schema']][properties['region_parent']][properties['region_child']].append(feature)
