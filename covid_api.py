import csv
import bottle
from copy import deepcopy
from json import dumps as _dumps
from bottle import request, response, get

from covid_api.CaseData import CASE_DATA
from covid_api.PointGeoJSON import POINT_GEOJSON
from covid_api.PolyGeoJSON import POLY_GEOJSON


app = application = bottle.default_app()


def dumps(obj):
    response.content_type = 'application/json'
    return _dumps(obj, ensure_ascii=False)


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


@get('/geojson_point_data')
def geojson_point_data():
    """Get GeoJSON"""
    schema = request.query.schema
    region_child = request.query.get('region_child')
    region_parent = request.query.get('region_parent')
    source_id = request.query.get('source_id', None)

    # Get most recent figures, choosing the most recently
    # updated if source_id isn't explicitly specified
    case_data = CASE_DATA.get_latest_case_data_singlesource(schema, None, source_id,
                                                            region_parent, region_child, age_breakdowns=False)

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

    for feature in geojson_out['features']:
        properties = feature['properties']
        key = properties['region_parent'], properties['region_child']  # FIXME!
        if key in case_data:
            case_data_dict = case_data[key]
            properties.update(case_data_dict)

    return dumps(geojson_out)


@get('/geojson_poly_data')
def geojson_poly_data():
    """Get GeoJSON"""
    schema = request.query.schema
    region_child = request.query.get('region_child')
    region_parent = request.query.get('region_parent')
    source_id = request.query.get('source_id', None)

    # Get most recent figures, choosing the most recently
    # updated if source_id isn't explicitly specified
    case_data = CASE_DATA.get_latest_case_data_singlesource(schema, None, source_id,
                                                            region_parent, region_child, age_breakdowns=False)

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

    for feature in geojson_out['features']:
        properties = feature['properties']
        key = properties['region_parent'], properties['region_child']  # FIXME!
        if key in case_data:
            case_data_dict = case_data[key]
            properties.update(case_data_dict)

    return dumps(geojson_out)


#======================================================================#
# Case Data
#======================================================================#


@get('/case_data_sources')
def case_data_sources():
    """Get possible case data sources by schema"""
    schema = request.query.schema
    return dumps(CASE_DATA.SOURCES_BY_SCHEMA[schema])


@get('/case_datatypes')
def case_datatypes():
    """Get possible case datatypes by schema"""
    schema = request.query.schema
    return dumps(CASE_DATA.DATATYPES_BY_SCHEMA[schema])


@get('/case_data_time_series')
def case_data_time_series():
    """Get case data time series"""
    schema = request.query.schema
    datatype = request.query.get('datatype', None)
    source_id = request.query.get('source_id', None)

    region_parent = request.query.get('region_parent')
    region_child = request.query.get('region_child')
    age_breakdowns = request.query.get('age_breakdowns', False)

    out = CASE_DATA.get_time_series(schema, datatype, source_id, region_parent, region_child, age_breakdowns)
    return dumps(out)


@get('/latest_case_data')
def latest_case_data():
    """Get the latest case data only"""
    schema = request.query.schema
    datatype = request.query.get('datatype', None)
    source_id = request.query.get('source_id', None)

    region_parent = request.query.get('region_parent')
    region_child = request.query.get('region_child')
    age_breakdowns = request.query.get('age_breakdowns', False)

    out = CASE_DATA.get_latest_case_data(schema, datatype, source_id, region_parent, region_child, age_breakdowns)
    return dumps(out)


if __name__ == '__main__':
    bottle.run(host='127.0.0.1', port=8000)
