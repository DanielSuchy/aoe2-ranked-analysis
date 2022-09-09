#find a subset of players relevant for the analysis
import pandas as pd
from datetime import datetime
from tools import substract_n_days

#load the data
players_path = '../data/latest/candidate_players.csv'
ratings_path = '../data/latest/candidate_players_ratinghistory.csv'
players = pd.read_csv(players_path, index_col='profile_id')
ratings = pd.read_csv(ratings_path)

#consider players who only play 1v1s
players = players[~players['plays_1v1s'].isnull()]
players = players[players['plays_teamgames'] == False]
players = players[players['plays_empwars'] == False]
players = players[players['plays_team_empwars'] == False]

#find out which games were played less the 3 months ago
three_months_ago = substract_n_days(90) #substract 90 days
ratings['three_months_ago'] = ratings.timestamp < three_months_ago
timestamps = ratings['timestamp'].tolist()
dates = [datetime.fromtimestamp(timestamp) for timestamp in timestamps]
ratings['dates'] = dates

#use only players who played their first game less than three months ago
profile_ids = players.index
for profile_id in profile_ids:
    player_matches = ratings[ratings['profile_id'] == profile_id]
    first_game_i = player_matches.timestamp.idxmin()
    first_game = player_matches.loc[first_game_i]
    if first_game.three_months_ago == False:
        #i = players[players.profile_id == profile_id].index
        players = players.drop(index=profile_id)
        
relevant_players_path = '../data/latest/new_players.csv'
players.to_csv(relevant_players_path)
    