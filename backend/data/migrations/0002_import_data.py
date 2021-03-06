# Generated by Django 3.0.2 on 2020-01-09 10:56
import pandas as pd
import requests

from django.db import migrations

import zipfile
import io

from data.settings import INDICATORS_LIST


def extract_zip(file_obj):
    buffer = io.BytesIO()
    buffer.write(file_obj)
    input_zip = zipfile.ZipFile(buffer)
    return {name: input_zip.read(name) for name in input_zip.namelist()}


def download_data(ind_list):
    df_indicator = pd.DataFrame()
    df_stat = pd.DataFrame()
    hasCountry = False

    for ind in ind_list:
        res = requests.get(f'http://api.worldbank.org/v2/en/indicator/{ind}?downloadformat=csv')
        for name, file in extract_zip(res.content).items():
            if 'Metadata' in name:
                df = pd.read_csv(io.StringIO(file.decode('utf-8')))
                if 'Indicator' in name:
                    df_indicator = pd.concat([df_indicator, df])
                elif not hasCountry:
                    df_country = df
                    hasCountry = True
            else:
                df = pd.read_csv(io.StringIO(file.decode('utf-8')), skiprows=4)
                df_stat = pd.concat([df_stat, df])

    return df_country, df_indicator, df_stat


def import_data(apps, schema_editor):
    Country = apps.get_model('data', 'Country')
    Indicator = apps.get_model('data', 'Indicator')
    Stat = apps.get_model('data', 'Stat')

    df_c, df_i, df_s = download_data(INDICATORS_LIST)

    df_s = df_s.loc[df_s['Country Code'].isin(df_c['Country Code'].to_list())]

    ids = ['Country Code', 'Indicator Code']
    values = list(map(str, range(1960, 2020)))

    df_s = df_s.drop(['Country Name', 'Indicator Name'], axis=1)
    df_s = pd.melt(df_s, id_vars=ids, value_vars=values, var_name='Year', value_name='Value')
    df_s = df_s.pivot_table('Value', ['Year', 'Country Code'], 'Indicator Code').reset_index()
    df_s = df_s.fillna(0)

    records = df_c.to_dict('records')
    instances = [Country(
        name=record['TableName'],
        code=record['Country Code'],
        region=record['Region'],
        income=record['IncomeGroup']
    ) for record in records]

    Country.objects.bulk_create(instances)

    records = df_i.to_dict('records')
    instances = [Indicator(
        name=record['INDICATOR_NAME'],
        code=record['INDICATOR_CODE'],
        note=record['SOURCE_NOTE'],
        organization=record['SOURCE_ORGANIZATION']
    ) for record in records]

    Indicator.objects.bulk_create(instances)
    records = df_s.to_dict('records')
    instances = [Stat(
        country=Country.objects.get(code=record['Country Code']),
        year=record['Year'],
        **{ind.replace('.','_'): record[str(ind)] for ind in INDICATORS_LIST}
    ) for record in records]

    Stat.objects.bulk_create(instances)


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
