# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=20)
    city_price = models.IntegerField()
    city_url = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'city'


class Route(models.Model):
    route_id = models.IntegerField(primary_key=True)
    route_city1 = models.ForeignKey(City, models.DO_NOTHING, db_column='route_city1')
    route_city2 = models.ForeignKey(City, models.DO_NOTHING, db_column='route_city2')
    route_distance = models.IntegerField()
    route_type = models.CharField(max_length=20)
    route_start = models.IntegerField()
    route_finish = models.IntegerField()
    route_fee = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'route'


class Scenery(models.Model):
    scenery_id = models.IntegerField(primary_key=True)
    scenery_city = models.ForeignKey(City, models.DO_NOTHING, db_column='scenery_city')
    scenery_name = models.CharField(max_length=20)
    scenery_url = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'scenery'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'user'
