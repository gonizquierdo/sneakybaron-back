import requests
from riotwatcher import RiotWatcher

class ApiConnector():

    def __init__(self, region, api_key):
        self._region = region
        self._watcher = RiotWatcher(api_key)

    # ------ Summoner related functions ------
    def get_summoner_by_name(self, summoner_name):
        summoner = self._watcher.summoner.by_name(self._region, summoner_name)
        return summoner

    def get_league_by_account_id(self, id):
        league = self._watcher.league.by_summoner(self._region, id)
        return league[0]

    def get_last_games_by_account_id(self,account_id, n_games=50):
        begin_index = 0

        if n_games < 100:
            return self._watcher.match.matchlist_by_account(self._region, account_id, end_index=n_games)['matches']
        else:
            print("MAX 100 GAMES.")

    def get_last_games_by_account_id_for_lane(self, account_id, lane, n_games=50):
        begin_index = 0
        if n_games < 100:

            matchlist =  self._watcher.match.matchlist_by_account(self._region, account_id, end_index=n_games)
            matches = []
            for game in matchlist['matches']:
                if game['lane'] == lane:
                    matches.append(game)
            return matches
        else:
            print("MAX 100 GAMES.")

    def get_summoner_league_and_division(self,summoner_id):
        res = self._watcher.league.positions_by_summoner(self._region, summoner_id)
        print(res)
        if res:
            for queue in res:
                if queue['queueType'] == 'RANKED_SOLO_5x5':
                    tier = queue['tier']
                    rank = queue['rank']
            return tier, rank
        else:
            return ["UNRANKED", "-"]

    # ------ Matches related functions ------
    def get_match_by_game_id(self,game_id):

        game = self._watcher.match.by_id(self._region, game_id)
        return game

    def get_active_game_by_summoner_id(self,summoner_id):
        return self._watcher.spectator.by_summoner(self._region, summoner_id)

    def get_timeline_by_game_id(self, game_id):
        timeline = self._watcher.match.timeline_by_match(self._region, game_id)
        return timeline
