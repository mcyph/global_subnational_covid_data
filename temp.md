## API

A basic API server which uses Bottle is also provided.

It serves on port 8000 (a demonstration can be found at endpoint https://langlynx.ddns.net:8000/)
and has the following methods:

* `/source_ids`

    * Description: Get possible source IDs, e.g. "world_jhu" for the John Hopkins data etc.

    * Parameters: (no additional parameters)

    * Examples:

        * Request: `/source_ids`
        * Response:

            > [{"source_id": "af_humdata",
              "source_url": "https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit",
            "source_desc": ""}, ...]

* `/datatypes`

    * Description: Get all possible datatypes (the same as the table in this `README.md` document below)

    * Parameters: (no additional parameters)

    * Examples:

        * Request: `/datatypes`
        * Response:

            > [{"datatype_id": "new", "desc": "Number of new cases for the day. Negative numbers may indicate figures have been revised downwards."}, ...]

* `/geojson_point_data`

    * Description: Get the GeoJSON (geographic point or polygon) data for a given
      administrative area. The latest covid-19 case data is added to the properties
      where available.

    * Parameters: schema, region_child, region_parent, source_id

    * Examples:

        * Request: `/geojson_point_data?schema=admin_0&region_parent=&region_child=au&datatype=total`
        * Response:

            > {"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [133.4955, -24.805500000000002]}, "properties": {"region_schema": "admin_0", "region_parent": "", "region_child": "au", "area": 1133.4680009999997, "bounding_box": [113.385, -38.896, 153.606, -10.715], "point": [133.4955, -24.805500000000002], "labels": {"long": "Australia", "ciawf": "Australia", "sort": "Australia", "alt": null, "len": 9, "ar": "أستراليا", "bn": "অস্ট্রেলিয়া", "de": "Australien", "en": "Australia", "es": "Australia", "fr": "Australie", "el": "Αυστραλία", "hi": "ऑस्ट्रेलिया", "hu": "Ausztrália", "id": "Australia", "it": "Australia", "ja": "オーストラリア", "ko": "오스트레일리아", "nl": "Australië", "pl": "Australia", "pt": "Austrália", "ru": "Австралия", "sv": "Australien", "tr": "Avustralya", "vi": "Úc", "zh": "澳大利亚"}, "population": 25364307, "google_mobility_retail_recreation": -16, "google_mobility_retail_recreation_updated": "09-10-2020", "google_mobility_retail_recreation_source_id": "google_mobility", "google_mobility_residential": 8, "google_mobility_residential_updated": "09-10-2020", "google_mobility_residential_source_id": "google_mobility", "google_mobility_parks": -9, "google_mobility_parks_updated": "09-10-2020", "google_mobility_parks_source_id": "google_mobility", "google_mobility_workplaces": -19, "google_mobility_workplaces_updated": "09-10-2020", "google_mobility_workplaces_source_id": "google_mobility", "google_mobility_supermarket_pharmacy": 1, "google_mobility_supermarket_pharmacy_updated": "09-10-2020", "google_mobility_supermarket_pharmacy_source_id": "google_mobility", "google_mobility_public_transport": -42, "google_mobility_public_transport_updated": "09-10-2020", "google_mobility_public_transport_source_id": "google_mobility", "facebook_flu_symptoms": 1116, "facebook_flu_symptoms_updated": "10-10-2020", "facebook_flu_symptoms_source_id": "umd_covidmap", "facebook_covid_symptoms": 1107, "facebook_covid_symptoms_updated": "10-10-2020", "facebook_covid_symptoms_source_id": "umd_covidmap", "tests_total": 8008111, "tests_total_updated": "11-10-2020", "tests_total_source_id": "owid", "tests_new": 42837, "tests_new_updated": "08-10-2020", "tests_new_source_id": "owid", "status_deaths": 898, "status_deaths_updated": "12-10-2020", "status_deaths_source_id": "eu_cdc", "total": 27264, "total_updated": "12-10-2020", "total_source_id": "eu_cdc", "status_deaths_new": 1, "status_deaths_new_updated": "12-10-2020", "status_deaths_new_source_id": "eu_cdc", "status_active": 1368, "status_active_updated": "11-10-2020", "status_active_source_id": "bing", "status_recovered_new": 170, "status_recovered_new_updated": "11-10-2020", "status_recovered_new_source_id": "bing", "new": 20, "new_updated": "12-10-2020", "new_source_id": "eu_cdc", "status_active_new": -151, "status_active_new_updated": "11-10-2020", "status_active_new_source_id": "bing", "status_recovered": 24998, "status_recovered_updated": "11-10-2020", "status_recovered_source_id": "bing"}}, ...]}

* `/geojson_poly_data`

    Description: The same parameters as `/geojson_point_data`, but will output the
    borders of each administrative area rather than just the central points in them.

* `/case_data_sources`

    * Description: Get the possible data sources for a given schema.

    * Parameters: schema

    * Examples:

        * Request: `/case_data_sources?schema=admin_1`
        * Response:

            >

* `/case_datatypes`

    * Description: Get the possible datatypes for a given schema.

    * Parameters: schema

    * Examples:

        * Request: `/case_datatypes?schema=admin_1`
        * Response:

            >

* `/case_data_time_series`

    * Description: Get all case figures collected to date as time series data.

    * Parameters:

    * Examples:

        Get country-level (schema `admin_0`) totals for Australia (`au`)
        (note countries don't have a `region_parent`):
        * Request: `/case_data_time_series?schema=admin_0&region_parent=&region_child=au&datatype=total`
        * Response:

            > {"bing": {"total": [["25-01-2020", 4], ...}, ...}

        Get for a specific `datatype` (`status_active`) and `region_child` (`monash`):
        * Request: `/case_data_time_series?schema=lga&datatype=status_active&region_parent=au-vic&region_child=monash`
        * Response:

            > {"dhhs_csv": {"status_active": [["29-08-2020", 48], ...}}

        Get all `datatype`s by a specific `region_child` (`monash`):
        * Request: `/case_data_time_series?schema=lga&region_parent=au-vic&region_child=monash`
        * Response:

            > {"google_mobility": {"google_mobility_retail_recreation": [["15-02-2020", 8], ...], ...}, ...}

* `/latest_case_data`

    * Description: Get only the latest case figures.

    * Parameters:

    * Examples:

        * Request: `/`
        * Response:

            >
