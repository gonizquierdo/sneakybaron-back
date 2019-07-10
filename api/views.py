from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from .models import Summoner
from riotwatcher import RiotWatcher, ApiError
from .helpers.ApiConnector import ApiConnector
from .helpers.PlayerBehavior import PlayerBehavior
from .helpers.PlayerData import *
import json
import urllib

# Create your views here.
def get_stream_widget(request, code):
    summoner = get_object_or_404(Summoner, url=code)

    region = summoner.region_value
    summoner_name = summoner.summoner_name

    connector  = ApiConnector(region, 'RGAPI-f2369e90-c15e-4f5e-8478-7ebcbd745741')
    behavior_helper = PlayerBehavior()

    rank_to_number = {
        'I':'1',
        'II':'2',
        'III':'3',
        'IV':'4',
    }

    summoner_obj = connector.get_summoner_by_name(summoner_name)
    league = connector.get_league_by_account_id(summoner_obj['id'])

    total_games = league['wins'] + league['losses']
    win_rate = round(league['wins']*100/total_games)

    #TODO: Traer la matchlist de la base o de la api dependiendo si existe. INEFICIENTE. para implementar kda
    #matchlist =  connector.get_last_games_by_account_id(summoner['accountId'], 5)
    #stats = behavior_helper.get_stats_for_matchlist(connector, summoner, matchlist)

    summoner_info = {
        'tier':league['tier'].lower(),
        'rank':league['rank'],
        'rank_number':rank_to_number[league['rank']],
        'league_points':league['leaguePoints'],
        'wins':league['wins'],
        'losses':league['losses'],
        'win_rate': win_rate,
        'wins': league['wins'],
        'losses': league['losses'],
        'hot_streak': league['hotStreak'],
        }

    if 'miniSeries' in league:
        summoner_info['mini_series'] = league['miniSeries']['progress']
    else:
        summoner_info['mini_series'] = False

    return render(request, 'widget.html', context={'summoner_info':summoner_info,})

def get_patch_info(request, patch, language):
    with urllib.request.urlopen("https://sneaky-static-data.s3.us-east-2.amazonaws.com/parches/{}/{}.json".format(language, patch)) as patch_file:
        patch_json = json.loads(patch_file.read())
        return JsonResponse(patch_json)
