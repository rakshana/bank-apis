from __future__ import unicode_literals

from django.db import models


class Banks(models.Model):
    name = models.CharField(max_length=49, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'banks'


class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank = models.ForeignKey(Banks, models.DO_NOTHING, blank=True, null=True)
    branch = models.CharField(max_length=74, blank=True, null=True)
    address = models.CharField(max_length=195, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
