import pandas as pd

#load the data
players_path = '../data/latest/new_players.csv'
ratings_path = '../data/latest/candidate_players_ratinghistory.csv'
players = pd.read_csv(players_path, index_col='profile_id')
ratings = pd.read_csv(ratings_path, index_col='profile_id')

new_player_ids = players.index
new_player_ratings = ratings[ratings.index.isin(new_player_ids)]