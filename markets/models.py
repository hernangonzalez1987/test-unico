from django.db import models


class Market(models.Model):

    class Region(models.TextChoices):
        EAST = 'Leste'
        WEST = 'Oeste'
        SOUTH = 'Sul'
        NORTH = 'Norte'

    longitude = models.FloatField(blank=True, default=None,null=True)
    latitude = models.FloatField(blank=True, default=None,null=True)
    setcens = models.FloatField(blank=True, default=None,null=True)
    areap = models.FloatField(blank=True, default=None,null=True)
    cod_dist = models.IntegerField(blank=True, default=None,null=True)
    district = models.TextField(blank=True, default=None,null=True)
    cod_sub_prefecture = models.TextField(blank=True, default=None,null=True)
    sub_prefecture = models.TextField(blank=True, default=None,null=True)
    region_5 = models.TextField(choices=Region.choices,blank=True, default=None,null=True)
    region_8 = models.TextField(blank=True, default=None,null=True)
    name = models.TextField(blank=True, default=None,null=True)
    registration_code = models.TextField(unique=True)
    address_street = models.TextField(blank=True, default=None,null=True)
    address_number = models.TextField(blank=True, default=None,null=True)
    address_city = models.TextField(blank=True, default=None,null=True)
    reference = models.TextField(blank=True, default=None,null=True)
