#download the 1v1 ranked rating history for new players
#doing so for all players takes too much time for now
import pandas as pd
from datetime import datetime, timedelta
from tools import use_api

def substract_30_days():
    today = datetime.now()
    month_ago = today - timedelta(30) # within the last 30 days
    return datetime.timestamp(month_ago) 

#the goal here is to get players likely to be new, to shorten dwnld time
def get_new_players(leaderboard):
    month_ago = substract_30_days()    
    players = pd.read_csv(leaderboard)
    players = players[players.games < 50] # more likely to be new
    players = players[players.highest_rating<1500] # less likely to be smurfs
    players = players[players.last_match_time > month_ago] # are recently active
    
    return players
    
leaderboard = '../data/players.csv'
path = '../data/ratinghistory.csv'
datatype="ratinghistory"
leaderboard_id = str(3) #download the 1v1 ranked leaderboard

new_players = get_new_players(leaderboard)

for i, profile_id in enumerate(new_players.profile_id):    
    print('player', i + 1, 'out of', len(new_players))
    matches = use_api(datatype=datatype, matchtype=leaderboard_id, profile_id=profile_id, count=40)
    for match in matches:
        match['profile_id'] = profile_id

    df = pd.DataFrame(matches)
    
    if (i == 0): # write the header
        df.to_csv(path, index=False, mode='w', header=True)
    else: # do not repeat the header
        df.to_csv(path, index=False, mode='a', header=False)