#download the 1v1 ranked leaderboard from aoe2.net
import pandas as pd
from tools import use_api

path = '../data/latest/players.csv'
datatype="leaderboard"
leaderboard_id = str(3) #download the 1v1 ranked leaderboard

#how many players are there?
player_data = use_api(datatype=datatype, matchtype=leaderboard_id, start=1, count=1)
player_count = player_data['total']

#write the header
columns = player_data["leaderboard"][0].keys()
columns = ','.join(columns) + '\n'
with open(path, "w") as f:
    f.write(columns)
    
#download the data
upto_rank = player_count
by = 10000; # API supports up to 10000 entries at the same time
counter = by #how many we have downloaded so far
while (counter <= upto_rank + by):
    start = counter - by + 1 # e.g. 1, 101, 201, 301...
    all_data = use_api(datatype=datatype, matchtype=leaderboard_id, start=start, count=by)
    relevant_data = all_data["leaderboard"]
    
    print("Downloading leaderborad rank", relevant_data[0]["rank"], "to", relevant_data[-1]["rank"])
    #save the result as csv
    df = pd.DataFrame(relevant_data)
    df.to_csv(path, index=False, mode='a', header=False)
    
    counter = counter + by;