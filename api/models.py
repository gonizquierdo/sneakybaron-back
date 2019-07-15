from django.db import models
from django.utils.crypto import get_random_string
import uuid
import os
import random, string

def generate_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Create your models here.
class Summoner(models.Model):

    REGIONS = [
        ('la1', 'LAN'),
        ('la2', 'LAS'),
        ('na', 'NA'),
        ('br1', 'BR'),
    ]

    summoner_name = models.CharField(max_length=255)
    region_value = models.CharField(max_length=3, choices=REGIONS)
    url = models.CharField(max_length=20, unique=True, default=generate_url)

    def __str__(self):
        return self.summoner_name

    def url_pretty(self):
        return 'https://api.sneakybaron.gg/api/widget/{}'.format(self.url)