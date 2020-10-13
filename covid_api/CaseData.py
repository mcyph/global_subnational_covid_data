import csv
from pathlib import Path
from collections import defaultdict


def _reverse_date(date):
    return '-'.join(date.split('-')[::-1])


class CASE_DATA:
    # schema ->
    #   region_parent ->
    #   region_child ->
    #   (source_id, datatype, age_range) ->
    #   [['dd-mm-yyyy', value] ...]
    PATH = Path('casedata')

    DATA = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    SOURCES_BY_SCHEMA = defaultdict(set)
    DATATYPES_BY_SCHEMA = defaultdict(set)

    for country_code_dir in PATH.iterdir():
        for source_id_dir in country_code_dir.iterdir():
            for csv_for_datatype_path in source_id_dir.iterdir():
                source_id = source_id_dir.name
                datatype = csv_for_datatype_path.name.replace('.csv', '')

                with open(csv_for_datatype_path, 'r', encoding='utf-8') as f:
                    for item_dict in csv.DictReader(f):
                        # region_schema,region_parent,region_child,agerange,2020-03-22,...
                        region_schema = item_dict['region_schema']
                        region_parent = item_dict['region_parent']
                        region_child = item_dict['region_child']
                        agerange = item_dict['agerange']

                        values = []
                        for date_key in list(item_dict.keys())[4:]:
                            if not item_dict[date_key]:
                                continue
                            values.append([
                                _reverse_date(date_key),
                                int(item_dict[date_key])
                            ])

                        DATA[region_schema][region_parent][region_child][source_id, datatype, agerange] = values
                        SOURCES_BY_SCHEMA[region_schema].add(source_id)
                        DATATYPES_BY_SCHEMA[region_schema].add(datatype)

    @staticmethod
    def get_time_series(schema,
                        datatype=None,
                        source_id=None,
                        region_parent=None,
                        region_child=None,
                        age_breakdowns=False):

        if age_breakdowns:
            if region_child is not None:
                out = {}
                for (i_source_id, i_datatype, i_agerange), values in CASE_DATA.DATA[schema][region_parent][region_child].items():
                    if source_id and i_source_id != source_id:
                        continue
                    elif datatype and i_datatype != datatype:
                        continue
                    elif not i_agerange:
                        continue
                    out.setdefault(i_source_id, {}).setdefault(i_datatype, {})[i_agerange] = values
            elif region_parent is not None:
                out = {}
                for region_child in CASE_DATA.DATA[schema][region_parent]:
                    for (i_source_id, i_datatype, i_agerange), values in CASE_DATA.DATA[schema][region_parent][region_child].items():
                        if source_id and i_source_id != source_id:
                            continue
                        elif datatype and i_datatype != datatype:
                            continue
                        elif not i_agerange:
                            continue
                        out.setdefault(i_source_id, {}).setdefault(i_datatype, {}).setdefault(region_child, {})[i_agerange] = values
            else:
                out = {}
                for region_parent in CASE_DATA.DATA[schema]:
                    for region_child in CASE_DATA.DATA[schema][region_parent]:
                        for (i_source_id, i_datatype, i_agerange), values in CASE_DATA.DATA[schema][region_parent][region_child].items():
                            if source_id and i_source_id != source_id:
                                continue
                            elif datatype and i_datatype != datatype:
                                continue
                            elif not i_agerange:
                                continue
                            out.setdefault(i_source_id, {}).setdefault(i_datatype, {}).setdefault(region_parent, {}).setdefault(region_child, {})[i_agerange] = values
        else:
            if region_child is not None:
                out = {}
                for (i_source_id, i_datatype, i_agerange), values in CASE_DATA.DATA[schema][region_parent][region_child].items():
                    if source_id and i_source_id != source_id:
                        continue
                    elif datatype and i_datatype != datatype:
                        continue
                    elif i_agerange:
                        continue
                    out.setdefault(i_source_id, {})[i_datatype] = values
            elif region_parent is not None:
                out = {}
                for region_child in CASE_DATA.DATA[schema][region_parent]:
                    for (i_source_id, i_datatype, i_agerange), values in CASE_DATA.DATA[schema][region_parent][region_child].items():
                        if source_id and i_source_id != source_id:
                            continue
                        elif datatype and i_datatype != datatype:
                            continue
                        elif i_agerange:
                            continue
                        out.setdefault(i_source_id, {}).setdefault(i_datatype, {})[region_child] = values
            else:
                out = {}
                for region_parent in CASE_DATA.DATA[schema]:
                    for region_child in CASE_DATA.DATA[schema][region_parent]:
                        for (i_source_id, i_datatype, i_agerange), values in CASE_DATA.DATA[schema][region_parent][region_child].items():
                            if source_id and i_source_id != source_id:
                                continue
                            elif datatype and i_datatype != datatype:
                                continue
                            elif i_agerange:
                                continue
                            out.setdefault(i_source_id, {}).setdefault(i_datatype, {}).setdefault(region_parent, {})[region_child] = values

        return out

    @staticmethod
    def get_latest_case_data(schema,
                             datatype=None,
                             source_id=None,
                             region_parent=None,
                             region_child=None,
                             age_breakdowns=False):

        out = CASE_DATA.get_time_series(schema, datatype, source_id, region_parent, region_child, age_breakdowns)

        def recurse_keys(obj):
            for key, value in list(obj.items()):
                if isinstance(value, dict):
                    recurse_keys(value)
                elif isinstance(value, (list, tuple)):
                    date, value = value[-1]
                    obj[key] = {'date': date, 'value': value}
                else:
                    raise Exception(value)

        recurse_keys(out)
        return out

    @staticmethod
    def get_latest_case_data_singlesource(schema,
                                          datatype=None,
                                          source_id=None,
                                          region_parent=None,
                                          region_child=None):

        out = {}
        data = CASE_DATA.get_latest_case_data(schema, datatype, source_id, region_parent, region_child,
                                              age_breakdowns=False)

        if region_child is not None:
            for source_id, datatype_dict in data.items():
                for datatype, value_dict in datatype_dict.items():
                    value_dict['date'] = _reverse_date(value_dict['date'])
                    value_dict['source_id'] = source_id
                    out.setdefault((datatype, region_parent, region_child), value_dict)

                    if value_dict['date'] > out[datatype, region_parent, region_child]['date']:
                        out[datatype, region_parent, region_child] = value_dict
        elif region_parent is not None:
            for source_id, datatype_dict in data.items():
                for datatype, region_parent_dict in datatype_dict.items():
                    for region_parent, value_dict in region_parent_dict.items():
                        value_dict['date'] = _reverse_date(value_dict['date'])
                        value_dict['source_id'] = source_id
                        out.setdefault((datatype, region_parent, region_child), value_dict)

                        if value_dict['date'] > out[datatype, region_parent, region_child]['date']:
                            out[datatype, region_parent, region_child] = value_dict
        else:
            for source_id, datatype_dict in data.items():
                for datatype, region_parent_dict in datatype_dict.items():
                    for region_parent, region_child_dict in region_parent_dict.items():
                        for region_child, value_dict in region_child_dict.items():
                            value_dict['date'] = _reverse_date(value_dict['date'])
                            value_dict['source_id'] = source_id
                            out.setdefault((datatype, region_parent, region_child), value_dict)

                            if value_dict['date'] > out[datatype, region_parent, region_child]['date']:
                                out[datatype, region_parent, region_child] = value_dict

        r = {}
        for (datatype, region_parent, region_child), value_dict in out.items():
            r.setdefault((region_parent, region_child), {}).update({
                f'{datatype}': value_dict['value'],
                f'{datatype}_updated': _reverse_date(value_dict['date']),
                f'{datatype}_source_id': value_dict['source_id']
            })
        return r
