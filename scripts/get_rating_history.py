#download the 1v1 ranked rating history for relatively new players
#doing so for all players takes too much time for now
import pandas as pd
from tools import use_api, get_new_players
    
leaderboard = '../data/latest/players.csv'
path = '../data/latest/candidate_players_ratinghistory.csv'
datatype="ratinghistory"
leaderboard_id = str(3) #download the 1v1 ranked leaderboard

new_players = get_new_players(leaderboard) # played less than month ago, have less than 50 games

for i, profile_id in enumerate(new_players.profile_id):    
    print('player', i + 1, 'out of', len(new_players))
    matches = use_api(datatype=datatype, matchtype=leaderboard_id, profile_id=profile_id, count=60)
    for match in matches:
        match['profile_id'] = profile_id

    df = pd.DataFrame(matches)
    
    if (i == 0): # write the header
        df.to_csv(path, index=False, mode='w', header=True)
    else: # do not repeat the header
        df.to_csv(path, index=False, mode='a', header=False)