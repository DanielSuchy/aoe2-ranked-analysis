import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

#load the data
players_path = '../data/latest/new_players.csv'
ratings_path = '../data/latest/candidate_players_ratinghistory.csv'
players = pd.read_csv(players_path, index_col='profile_id')
ratings = pd.read_csv(ratings_path, index_col='profile_id')

#select rankings only for relevant players
new_player_ids = players.index
ratings = ratings[ratings.index.isin(new_player_ids)]

#find out when each game was played
timestamps = ratings['timestamp'].tolist()
dates = [datetime.fromtimestamp(timestamp) for timestamp in timestamps]
ratings['date'] = dates

#get first game for every player
agg_ratings = ratings.groupby(['profile_id']).min()
first_games = ratings[ratings.timestamp.isin(agg_ratings.timestamp)]

#verify that these are indeed the first games
first_games = first_games[first_games.num_wins + first_games.num_losses == 10]
players = players[players.index.isin(first_games.index)]

#initial ELO of the players after placement games
first_games.rating.mean()
first_games.num_wins.mean()
first_games.num_losses.mean()

#ELO of the players at download date
players['games_played'] = players.wins + players.losses + players.drops #you loose ELO if you drop
players.games_played.mean()
players.rating.mean()

#how many players won at leat one placement game
won_a_game = first_games[first_games.num_wins>1]
len(won_a_game) / len(first_games)

#ELO distribution after the first game
elos = first_games.rating
elos.plot.hist(grid=False, bins=10, rwidth=0.9, color='#607c8e', range=(250, 1750))
plt.title('ELO after the placement games')
plt.xlabel('ELO')
plt.ylabel('Number of players')

#ELO distribution at the download date
elos = players.rating
elos.plot.hist(grid=False, bins=10, rwidth=0.9, color='#607c8e', range=(250, 1750))
plt.title('ELO at the download date')
plt.xlabel('ELO')
plt.ylabel('Number of players')

#Is there less variation after more games?
first_games.rating.std()
players.rating.std()

#how many players end up over 1000 ELO?
high_elo = first_games[first_games.rating > 1000]
len(high_elo) / len(first_games)
high_elo = players[players.rating > 1000]
len(high_elo) / len(first_games)

#when do players win their first game?
ratings['total_games'] = ratings.num_wins + ratings.num_losses #drops do not count here
first_games_won = ratings.loc[(ratings['num_wins'] == 1) & (ratings['total_games'] > 10)]
first_games_agg = first_games_won.groupby('profile_id').min()

#display the above
games = first_games_agg.total_games
games.plot.hist(grid=False, bins=10, rwidth=0.9, color='#607c8e', range=(10,50))