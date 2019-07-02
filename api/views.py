from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Summoner
from riotwatcher import RiotWatcher, ApiError
from .helpers.ApiConnector import ApiConnector
from .helpers.PlayerBehavior import PlayerBehavior
from .helpers.PlayerData import *

# Create your views here.
def get_stream_widget(request, region, summoner_name):
    connector  = ApiConnector(region, 'RGAPI-b83d62d1-979d-49de-900d-6c17f8cabc52')
    behavior_helper = PlayerBehavior()

    rank_to_number = {
        'I':'1',
        'II':'2',
        'III':'3',
        'IV':'4',
    }

    summoner = connector.get_summoner_by_name(summoner_name)
    league = connector.get_league_by_account_id(summoner['id'])

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
        #'kda': connector.get_kda(summoner)
        }
    return render(request, 'widget.html', context={'summoner_info':summoner_info,})
