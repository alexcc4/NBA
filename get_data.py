__author__ = 'alex'
#-*- encoding: utf-8 -*-

import urllib
import json
import requests
from arrow import now

BASE_URL = 'http://stats.nba.com/stats/leaderstiles'
QUERY_PARAM = {
    "Season": "2014-15",
    "SeasonType": "Regular Season",
    "LeagueID": "00",
    "Stat": "PTS",
    "PlayerOrTeam": "Player",
    "GameScope": "Season",
    "PlayerScope": "All Players"
}
stat_array = ['PTS', 'REB', 'AST', 'STL', 'FG_PCT', 'FT_PCT', 'FG3_PCT', 'BLK']
data_obj = {
    "time": now().timestamp * 1000
}

#TODO add player image url


def fetch_players():
    """ get data from nba site"""
    for stat in stat_array:
        QUERY_PARAM['Stat'] = stat
        res = requests.get('?'.join([BASE_URL, urllib.urlencode(QUERY_PARAM)]))
        result = json.loads(res.text)
        current_ranking = result['resultSet'][0]
        record = {
            "name": stat,
            "detail": []
        }
        for row in current_ranking['rowSet']:
            record['detail'].append(dict(zip(current_ranking['headers'], row)))
        # print record

if __name__ == '__main__':
    fetch_players()