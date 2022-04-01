from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    land_area = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Continent(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveBigIntegerField()
    land_area = models.PositiveIntegerField(null=True)
    countries = models.ManyToManyField(Country, through='TransContinental')

    def __str__(self):
        return self.name


class TransContinental(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    main_continent = models.BooleanField(default=True)

    def __str__(self):
        continent_str = str(self.continent)
        if self.main_continent:
            continent_str += ' (Main)'
        return continent_str


class City(models.Model):
    name = models.CharField(max_length=200)
    population = models.PositiveIntegerField()
    is_country_capital = models.BooleanField(default=False)
    special_note = models.CharField(max_length=100, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_country_capital:
            return f"{self.name} ({self.special_note})"
        else:
            return self.name

