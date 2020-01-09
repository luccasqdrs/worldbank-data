from django.db import models


class Country(models.Model):
    code = models.CharField(max_length=4, unique=True, primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    income = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)


class Indicator(models.Model):
    code = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    note = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)


class Stat(models.Model):
    country = models.ForeignKey(Country, verbose_name="stat_country", on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, verbose_name="stat_indicator", on_delete=models.CASCADE)
    for i in range(1960, 2020):
        vars()[f"year_{i}"] = models.CharField(max_length=500)