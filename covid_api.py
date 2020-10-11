import csv
import bottle
from pathlib import Path
from copy import deepcopy
from json import dumps, loads
from collections import defaultdict
from bottle import request, response
from bottle import post, get, put, delete


app = application = bottle.default_app()


#======================================================================#
# Schemas/DataTypes
#======================================================================#


@get('/schemas')
def schemas():
    """Get schemas"""
    out = []
    with open('source_info_table.tsv', 'r', encoding='utf-8') as f:
        for item in csv.DictReader(f, delimiter='\t'):
            out.append(item)
    return dumps(out)


@get('/datatypes')
def datatypes():
    """Get datatypes"""
    out = []
    with open('datatypes_table.tsv', 'r', encoding='utf-8') as f:
        for item in csv.DictReader(f, delimiter='\t'):
            out.append(item)
    return dumps(out)


#======================================================================#
# GeoJSON Data
#======================================================================#


GEOJSON_TEMPLATE = {
  "type": "FeatureCollection",
  "features": []
}


class POINT_GEOJSON:
    DATA = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    PATH = Path('geojson/point')

    for path in PATH.iterdir():
        with open(path, 'r', encoding='utf-8') as f:
            geojson = loads(f.read())

        for feature in geojson['features']:
            properties = feature['properties']
            DATA[properties['region_schema']][properties['region_parent']][properties['region_child']].append(feature)


class POLY_GEOJSON:
    DATA = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    PATH = Path('geojson/poly')

    for path in PATH.iterdir():
        with open(path, 'r', encoding='utf-8') as f:
            geojson = loads(f.read())

        for feature in geojson['features']:
            properties = feature['properties']
            DATA[properties['region_schema']][properties['region_parent']][properties['region_child']].append(feature)


@get('/geojson_point_data')
def geojson_point_data(schema, region_parent=None, region_child=None):
    """Get GeoJSON"""
    if region_child is not None:
        # Get just for a single region child
        geojson_out = deepcopy(GEOJSON_TEMPLATE)
        geojson_out['features'].extend(POINT_GEOJSON.DATA[schema][region_parent][region_child])
    elif region_parent is not None:
        # Get all region children for a given region parent
        geojson_out = deepcopy(GEOJSON_TEMPLATE)
        [geojson_out['features'].extend(i) for i in POINT_GEOJSON.DATA[schema][region_parent]]
    else:
        # Get all region parents/children for a given schema
        geojson_out = deepcopy(GEOJSON_TEMPLATE)
        for region_parent in POINT_GEOJSON.DATA[schema]:
            for region_child in POINT_GEOJSON.DATA[schema][region_parent]:
                geojson_out['features'].extend(POINT_GEOJSON.DATA[schema][region_parent][region_child])

    return dumps(geojson_out)


@get('/geojson_poly_data')
def geojson_poly_data(schema, region_parent=None, region_child=None):
    """Get GeoJSON"""
    if region_child is not None:
        # Get just for a single region child
        geojson_out = deepcopy(GEOJSON_TEMPLATE)
        geojson_out['features'].extend(POLY_GEOJSON.DATA[schema][region_parent][region_child])
    elif region_parent is not None:
        # Get all region children for a given region parent
        geojson_out = deepcopy(GEOJSON_TEMPLATE)
        [geojson_out['features'].extend(i) for i in POLY_GEOJSON.DATA[schema][region_parent]]
    else:
        # Get all region parents/children for a given schema
        geojson_out = deepcopy(GEOJSON_TEMPLATE)
        for region_parent in POLY_GEOJSON.DATA[schema]:
            for region_child in POLY_GEOJSON.DATA[schema][region_parent]:
                geojson_out['features'].extend(POLY_GEOJSON.DATA[schema][region_parent][region_child])

    return dumps(geojson_out)


#======================================================================#
# Case Data
#======================================================================#


class CASE_DATA:
    PATH = Path('casedata')


def case_data_sources():
    pass


@get('/case_datatypes')
def case_datatypes(schema):
    """Get possible case datatypes"""
    pass


@get('/case_data')
def case_data(schema, region_parent=None, region_child=None):
    """Get case data"""
    if region_child is not None:
        pass
    elif region_parent is not None:
        pass
    else:
        pass


if __name__ == '__main__':
    bottle.run(host='127.0.0.1', port=8000)
