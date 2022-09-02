import requests
import pandas as pd
from datetime import datetime, timedelta

def use_api(datatype, matchtype, game="aoe2de", start=None, count=None, profile_id=None):
    root = "https://aoe2.net/api/"
    
    if datatype == "leaderboard":
        api_url = (root  + datatype + "?game=" + game + 
                    "&leaderboard_id=" + str(matchtype) +
                    "&start=" + str(start) +
                    "&count=" + str(count)
                   )
    elif datatype == "ratinghistory":
        api_url = (root + "player/" + datatype + "?game=" + game +
                    "&leaderboard_id=" + str(matchtype) +
                    "&profile_id=" + str(profile_id) +
                    "&count=" + str(count)
                  )
        
    response = requests.get(api_url)
    data_in_json = response.json()
    return data_in_json

def substract_30_days():
    today = datetime.now()
    month_ago = today - timedelta(30) # within the last 30 days
    return datetime.timestamp(month_ago) 

#the goal here is to get players likely to be new, to shorten dwnld time
def get_new_players(leaderboard):
    month_ago = substract_30_days()    
    players = pd.read_csv(leaderboard)
    players = players[players.games < 50] # more likely to be new
    #players = players[players.highest_rating<1500] # less likely to be smurfs
    players = players[players.last_match_time > month_ago] # are recently active
    
    return players
    