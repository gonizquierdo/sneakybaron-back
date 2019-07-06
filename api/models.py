from django.db import models
from django.utils.crypto import get_random_string
import uuid
import os
from base64 import standard_b64encode


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
    url = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.summoner_name

    def save(self, *args, **kwargs):
        self.url = standard_b64encode(os.urandom(14)).decode('utf-8')
        super().save(*args, **kwargs)
