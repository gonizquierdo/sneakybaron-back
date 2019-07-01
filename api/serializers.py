from rest_framework import serializers
from api.models import Summoner
class summonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summoner
        fields = '__all__'
