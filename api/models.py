from django.db import models

# Create your models here.
class Summoner(models.Model):
  summoner_name = models.CharField(max_length=255)
  email = models.EmailField()
  main_champion = models.CharField(max_length=255)
  region_value = models.CharField(max_length=3)
  league_value = models.CharField(max_length=20)
  division_value = models.IntegerField()
