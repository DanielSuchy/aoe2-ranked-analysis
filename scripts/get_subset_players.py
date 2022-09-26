#find a subset of players relevant for the analysis
import pandas as pd
from datetime import datetime

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

#find out when each game was played
timestamps = ratings['timestamp'].tolist()
dates = [datetime.fromtimestamp(timestamp) for timestamp in timestamps]
ratings['date'] = dates

#how many days before download was it played?
download_date = datetime(2022, 9, 11)
days_ago = [(game_date - download_date).days * -1 for game_date in ratings['date']]
ratings['days_ago'] = days_ago

#which players played their first game less than 90 days ago?
agg_ratings = ratings.groupby(['profile_id']).max()
days_ago = agg_ratings['days_ago']
less_90_days_ago = days_ago[days_ago <= 90]

#select only players that fit the 90 day condition
new_players = players.join(less_90_days_ago, how='inner')
new_players_path = '../data/latest/new_players.csv'
new_players.to_csv(new_players_path)
    