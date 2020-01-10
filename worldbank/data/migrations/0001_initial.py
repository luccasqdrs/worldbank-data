# Generated by Django 3.0.2 on 2020-01-10 15:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('income', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=500)),
                ('organization', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SP_POP_TOTL', models.FloatField()),
                ('NY_GDP_MKTP_CD', models.FloatField()),
                ('EN_ATM_CO2E_PC', models.FloatField()),
                ('SP_DYN_LE00_IN', models.FloatField()),
                ('TX_VAL_TECH_MF_ZS', models.FloatField()),
                ('IP_PAT_NRES', models.FloatField()),
                ('IP_PAT_RESD', models.FloatField()),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(1960)])),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Country', verbose_name='stat_country')),
            ],
        ),
    ]
