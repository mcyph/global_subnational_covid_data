# global_subnational_covid_data

Auto-generated subnational COVID-19 data from many sources 
using the covid_19_grab_au project, which is no longer only 
getting Australian data but from many countries around the 
world. As far as I know, it is the largest continually 
updated data source of its kind. The goal is to be able 
to convert this data into a common universal format, 
so as to be able to use it for comparative analysis and 
similar purposes.

This data is currently used for covid-19-au, a project 
started by Dr. Chunyang Chen and a group of volunteer students 
from Monash and other universities. The data can be viewed live 
at https://covid-19-au.com/world.

The data is obtained from original sources where possible. 
Some of the data also comes from aggregated sources like 
[John Hopkins University](https://github.com/CSSEGISandData/COVID-19), 
[Microsoft Bing](https://github.com/microsoft/Bing-COVID-19-Data) or the
[European Commission Joint Research Centre](https://data.humdata.org/dataset/europe-covid-19-subnational-cases).

GeoJSON data is also provided to allow for displaying this data.
For information on the licensing of each file, see also 
https://github.com/mcyph/covid_19_au_grab/tree/master/geojson_data/data.
Preliminary and has not been checked so will contain errors! 
I have started to validate sources against place names in the 
GeoJSON files, but it's a manual process which is very 
time-consuming. 
Should not be used for anything important, and is strictly 
for non-commercial or research purposes only.

If you use this data, please acknowledge the sources below, 
and cite that it was automatically aggregated using the 
[covid_19_au_grab project](https://github.com/mcyph/covid_19_au_grab) 
by Dave Morrissey.

## Datatypes

| Datatype ID | Description |
| --- | --- |
| new | Number of new cases for the day. Negative numbers may indicate figures have been revised downwards. |
| new_male | New male cases for the day. |
| new_female | New female cases for the day. |
| total | Total (cumulative) number of cases to this date, whether probable or confirmed. |
| total_male | Total (cumulative) male cases. |
| total_female | Total (cumulative) female cases. |
| confirmed | Confirmed cases by test. |
| probable | Cases considered likely to be COVID-19. |
| confirmed_new | New cases confirmed by tests for the day. |
| probable_new | New cases considered likely to be COVID-19 for the day. |
| status_deaths | Number of people who have passed away to date. |
| status_hospitalized | Number of people currently in hospital with COVID-19. |
| status_hospitalized_runningtotal | Number of people that have been in hospital with COVID-19 since the start of reporting. |
| status_icu | Number of people currently in intensive care. |
| status_icu_ventilators | Number of people currently in intensive care with mechanical ventilators. |
| status_icu_runningtotal | The total number of people who have ever been in ICU. |
| status_icu_ventilators_runningtotal | The total number of people who have ever been in ICU with mechanical ventilators.  |
| status_recovered | The total number of people who have recovered from COVID-19. |
| status_active | The current number of people who are considered to still have COVID-19. Definitions for this can vary widely around the world. |
| status_unknown | The total number of people who have contracted COVID-19 that are of unknown status. They may have recovered, still have the virus, or have passed away due to it. |
| status_deaths_new | The new number of people who have passed away for the day. |
| status_hospitalized_new | The new number people people who are currently hospitalized with COVID-19. |
| status_hospitalized_runningtotal_new | |
| status_icu_new | The number of people who are currently in ICU relative to the previous day. |
| status_icu_ventilators_new | The number of people who are currently in ICU with mechanical ventilators relative to the previous day. |
| status_icu_runningtotal_new | The number of people who have ever been in ICU relative to the previous day. |
| status_icu_ventilators_runningtotal_new | The number of people who have ever been in ICU with mechanical ventilators relative to the previous day. |
| status_recovered_new | The total number of people who have recovered from COVID-19 in the previous day. |
| status_active_new | The current number of people who are considered to still have COVID-19 relative to the previous day. |
| status_unknown_new | The total number of people who have contracted COVID-19 that are of unknown status relative to the previous day. |
| source_overseas | Overseas, counted separately |
| source_cruise_ship | Overseas, included in SOURCE_OVERSEAS |
| source_interstate | Local-transmission from interstate, counted separately |
| source_confirmed | Local-transmission from confirmed cases, counted separately |
| source_community | Local-unknown community transmission, counted separately |
| source_under_investigation | "other" |
| source_domestic | For in-country which may or may not be community transmission (New Zealand data) |
| tests_total | The total number of tests to date. |
| tests_negative | The total number of tests to date which have returned negative results. |
| tests_positive | The total number of tests to date which have returned positive results. |
| tests_new | The total number of new tests in the last day. |
| age_care_total | The total number of people who are in aged care who currently have contracted COVID-19 |
| age_care_male | The total number of males who are in aged care who currently have contracted COVID-19 |
| age_care_female | The total number of females who are in aged care who currently have contracted COVID-19 |
| age_care_new | |
| age_care_male_new | |
| age_care_female_new | |
| facebook_covid_symptoms | |
| facebook_flu_symptoms | |
| google_mobility_retail_recreation | |
| google_mobility_supermarket_pharmacy | |
| google_mobility_parks | |
| google_mobility_public_transport | |
| google_mobility_workplaces | |
| google_mobility_residential | |

## Schemas

Kinds of geographic schemas (mapping to the GeoJSON files):

| Schema ID | Description |
| --- | --- |
| admin_0 | Values for a country (equivalent to lowercased ISO 3166-1 alpha-2 codes) |
| admin_1 | Values for the whole state/territory/province (equivalent to lowercased ISO-3166-2 codes) |
| postcode | Australian Postcodes (NSW and Victoria) |
| lga | Local Government Area (Australia-wide) |
| hhs | Queensland, Australia |
| lhd | NSW, Australia Local Health Districts |
| ths | Tasmania, Australia Health Services |
| sa3 | SA3 for ACT, Australia |
| bd_district | Bangladesh districts |
| br_city | Brazilian Cities |
| co_municipality | Colombian Municipalities |
| de_ags | German AGS |
| fr_overseas_collectivity | French Overseas Collectivities |
| in_district | Indian Districts |
| it_province | Italian Provinces |
| jp_city | Japanese Cities |
| my_district | Malaysian Districts |
| nz_dhb | New Zealand District Health Board |
| th_district | Thailand Districts |
| uk_area | United Kingdom Area (a custom level above admin_1 for Northern Ireland, Wales, Scotland and Britain) |
| us_county | United States Counties |
| ps_province | Palestinian Provinces |
| cr_canton | Costa Rican Cantons |
| cu_municipality | Cuban Municipalities |
| ca_health_region | Canadian Health Regions |
| lk_district | Sri Lankan Districts |
| np_district | Nepal Districts |
| pt_municipality | Portuguese Municipalities |
| cz_okres | Czech Republic Okres |
| fi_health_district | Finnish Health Districts |
| tr_nuts1 | Turkey on NUTS 1 statistics level |
| de_kreis | Germany Kreis |
| lt_municipality | Lithuanian Municipalities |
| il_municipality | Israel Municipalities |
| hk_district | Hong Kong Districts |
| es_province | Spain Provinces |


Data sources come from the following URLs:

| source_id | source_url | source_desc |
| --- | --- | --- |
| af_humdata | https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit |  |
| au_act | https://www.covid19.act.gov.au |  |
| au_nsw | https://www.health.nsw.gov.au/Infectious/covid-19/Pages/default.aspx |  |
| au_nt | https://coronavirus.nt.gov.au |  |
| au_qld | https://www.qld.gov.au/health/conditions/health-alerts/coronavirus-covid-19 |  |
| au_sa | https://www.covid-19.sa.gov.au |  |
| au_vic | https://www.dhhs.vic.gov.au/coronavirus |  |
| au_wa | https://ww2.health.wa.gov.au/en/Articles/A_E/Coronavirus |  |
| bd_gov | https://iedcr.gov.bd/ |  |
| be_epistat | https://epistat.wiv-isp.be/covid/ |  |
| br_kaggle | https://www.kaggle.com/unanimad/corona-virus-brazil | CC0: Public Domain |
| bw_gov | https://covid19portal.gov.bw/ |  |
| ca_covid_19_canada | https://github.com/ishaberry/Covid19Canada |  |
| ch_open_swiss_data | https://github.com/openZH/covid_19 | Creative Commons Attribution 4.0 International |
| co_ocha_humdata | https://data.humdata.org/dataset/positive-cases-of-covid-19-in-colombia |  |
| cu_covid19cubadata | https://github.com/covid19cubadata/covid19cubadata.github.io/tree/master/data |  |
| cz_mzcr | https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19 |  |
| de_rki_dash | https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4/page/page_1/ |  |
| de_unofficial | https://github.com/jgehrcke/covid-19-germany-gae |  |
| es_datadista | https://github.com/datadista/datasets/ |  |
| es_iscii | https://cnecovid.isciii.es/covid19/ |  |
| et_ocha_humdata | https://data.humdata.org/dataset/ethiopia-coronavirus-covid-19-subnational-cases |  |
| eu_subnational | https://data.humdata.org/dataset/europe-covid-19-subnational-cases |  |
| fr_opencovid_fr | https://github.com/opencovid19-fr/data |  |
| fr_sante_publique | https://www.data.gouv.fr/fr/organizations/sante-publique-france/ |  |
| gb_uk_unofficial | https://github.com/tomwhite/covid-19-uk-data |  |
| gh_ghs | https://www.ghanahealthservice.org/covid19/ |  |
| gr_covid_19_greece | https://covid-19-greece.herokuapp.com |  |
| hk_dash | https://chp-dashboard.geodata.gov.hk/covid-19/en.html |  |
| hr_gov | https://www.koronavirus.hr/ |  |
| ht_hdx_humdata | https://data.humdata.org/dataset/haiti-covid-19-subnational-cases |  |
| id_kawalcovid19 | https://kawalcovid19.id/ |  |
| ie_open_data | https://data.gov.ie/dataset?q=covid&sort=score+desc%2C+metadata_created+desc |  |
| iq_hdx_humdata | https://data.humdata.org/dataset/iraq-coronavirus-covid-19-subnational-cases |  |
| iq_wikipedia | https://ar.wikipedia.org/wiki/%D8%AC%D8%A7%D8%A6%D8%AD%D8%A9_%D9%81%D9%8A%D8%B1%D9%88%D8%B3_%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7_%D9%81%D9%8A_%D8%A7%D9%84%D8%B9%D8%B1%D8%A7%D9%82_2020 |  |
| is_gov | https://www.covid.is/data |  |
| it_protezionecivile_covid19 | https://github.com/pcm-dpc/COVID-19 |  |
| jp_tokyo_city | https://www.metro.tokyo.lg.jp |  |
| kg_gov | https://covid.kg/ |  |
| kh_gov | https://covid19-map.cdcmoh.gov.kh/ |  |
| kr_kaggle_ds4c | https://www.kaggle.com/kimjihoo/coronavirusdataset |  |
| kz_gov | https://www.coronavirus2020.kz/kz |  |
| lk_arimacdev | https://github.com/arimacdev/covid19-srilankan-data |  |
| lt_dash | https://registrucentras.maps.arcgis.com/apps/opsdashboard/index.html#/becd01f2fade4149ba7a9e5baaddcd8d |  |
| lv_infogram | https://covid19.gov.lv/covid-19/covid-19-statistika/covid-19-izplatiba-latvija |  |
| ly_hdx_humdata | https://data.humdata.org/dataset/libya-coronavirus-covid-19-subnational-cases |  |
| ma_hespress | https://covid.hespress.com/ |  |
| mk_gov | https://koronavirus.gov.mk/vesti/218055 |  |
| mm_covidmyanmar | https://data.covidmyanmar.com | Dataset created by Dr.Nyein Chan Ko Ko (covidmyanmar.com) dr.nyeinchankoko@gmail.com |
| mw_moh | https://covid19.health.gov.mw/ |  |
| my_esri_dash | https://www.arcgis.com/apps/opsdashboard/index.html#/6520fd7121374686aa35578ffe2d2cb7 |  |
| my_unofficial_github | https://github.com/ynshung/covid-19-malaysia |  |
| ng_ncdc | https://covid19.ncdc.gov.ng/ |  |
| om_gov | https://covid19.moh.gov.om/ |  |
| ps_gov | https://www.corona.ps/details |  |
| pt_dash | https://covid19.min-saude.pt/ponto-de-situacao-atual-em-portugal/ |  |
| rs_gov | https://covid19.data.gov.rs |  |
| sa_gov | https://covid19.moh.gov.sa/ |  |
| sd_gov | https://covid19.sd/ |  |
| si_sledilnik | https://covid-19.sledilnik.org/sl/stats |  |
| sn_ocha_rowca_humdata | https://data.humdata.org/dataset/positive-cases-of-covid-19-in-senegal |  |
| so_ocha_somalia_humdata | https://data.humdata.org/dataset/somalia-coronavirus-covid-19-subnational-cases |  |
| tr_dash | https://cbskampus.maps.arcgis.com/apps/opsdashboard/index.html#/233c6c3e8a7144eb8153ca1636ea3f86 |  |
| tr_wikipedia | https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27de_COVID-19_pandemisi |  |
| tw_cdc | https://nidss.cdc.gov.tw/en/NIDSS_DiseaseMap.aspx?dc=1&dt=5&disease=19CoV |  |
| ve_ocha_venezuela_humdata | https://data.humdata.org/dataset/corona-virus-covid-19-cases-and-deaths-in-venezuela |  |
| ve_patria | https://covid19.patria.org.ve/estadisticas-venezuela/ |  |
| vn_moh | https://ncov.moh.gov.vn/ |  |
| world_eu_cdc | https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide |  |
| world_google_mobility | https://www.google.com/covid19/mobility/ |  |
| world_jhu_admin0 | https://github.com/CSSEGISandData/COVID-19 |  |
| world_jhu_admin1 | https://github.com/CSSEGISandData/COVID-19 |  |
| world_jhu_admin2 | https://github.com/CSSEGISandData/COVID-19 |  |
| world_owid | https://github.com/owid/covid-19-data |  |
| world_umd_covidmap | https://covidmap.umd.edu |  |
| ye_yemen_corona | http://yemen-corona.com/ |  |
| za_gov | https://sacoronavirus.co.za/ |  |

