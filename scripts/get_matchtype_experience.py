#find out, if players play 1v1s, teamgames, or both and save the result
from tools import use_api, get_new_players

#according to aoe2.net API documentation
#exclude deathmatch gamemode, bc. it was removed from ranked queue
unranked=0
standard_1v1=3
standard_team=4
empwars_1v1=13
empwars_team=14

players_path = '../data/latest/candidate_players.csv'
players_data = get_new_players(players_path)
player_ids = players_data['profile_id']

for i, player_id in enumerate(player_ids):
    print("Getting matchtype experience, player:", i + 1, "out of:", len(player_ids))
    
    #continue processing where it last finnished
    processed = players_data.loc[players_data['profile_id'] == int(player_id), 'plays_unranked']
    if processed.isna().bool() == False:
        continue
    
    plays_unranked = bool(use_api(datatype='ratinghistory', matchtype=unranked, profile_id=player_id, count=1))
    plays_1v1 = bool(use_api(datatype='ratinghistory', matchtype=standard_1v1, profile_id=player_id, count=1))
    plays_teamgames = bool(use_api(datatype='ratinghistory', matchtype=standard_team, profile_id=player_id, count=1))
    plays_empwars = bool(use_api(datatype='ratinghistory', matchtype=empwars_1v1, profile_id=player_id, count=1))
    plays_team_empwars = bool(use_api(datatype='ratinghistory', matchtype=empwars_team, profile_id=player_id, count=1))
    
    players_data.loc[players_data['profile_id'] == int(player_id), 'plays_unranked'] = plays_unranked;
    players_data.loc[players_data['profile_id'] == int(player_id), 'plays_1v1s'] = plays_1v1;
    players_data.loc[players_data['profile_id'] == int(player_id), 'plays_teamgames'] = plays_teamgames;
    players_data.loc[players_data['profile_id'] == int(player_id), 'plays_empwars'] = plays_empwars;
    players_data.loc[players_data['profile_id'] == int(player_id), 'plays_team_empwars'] = plays_team_empwars;
    
#save the data
players_data.to_csv('../data/latest/candidate_players.csv', index=False)
