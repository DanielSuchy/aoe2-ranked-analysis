#download the 1v1 ranked leaderboard from aoe2.net
import requests
import pandas as pd

path = '../data/players.csv'
game = "aoe2de" #ignore the HD version
leaderbleaderboard_id = str(3) #download the 1v1 ranked leaderboard

#how many players are there?
api_url = ("https://aoe2.net/api/leaderboard?" +
            "game=" + game +
            "&leaderboard_id=" + leaderbleaderboard_id +
            "&start=" + str(1) + #query any single player, api also returns total count
            "&count=" + str(1)
          )

response = requests.get(api_url)
player_count = response.json()['total']

#write the header
api_url = ("https://aoe2.net/api/leaderboard?" +
            "game=" + game +
            "&leaderboard_id=" + leaderbleaderboard_id +
            "&start=" + str(1) +
            "&count=" + str(1)
          )

response = requests.get(api_url)
data_in_json = response.json()
columns = data_in_json["leaderboard"][0].keys()
columns = ','.join(columns) + '\n'

with open(path, "w") as f:
    f.write(columns)
    
#download the data
upto_rank = player_count
by = 10000; # API supports up to 10000 entries at the same time
counter = by #how many we have downloaded so far
while (counter <= upto_rank + by):
    start = counter - by + 1 # e.g. 1, 101, 201, 301...
    api_url = ("https://aoe2.net/api/leaderboard?" +
                "game=" + game +
                "&leaderboard_id=" + leaderbleaderboard_id +
                "&start=" + str(start) +
                "&count=" + str(by)
              )
    
    response = requests.get(api_url)
    data_in_json = response.json()
    relevant_data = data_in_json["leaderboard"]
    
    print("Downloading player rank", relevant_data[0]["rank"], "to", relevant_data[-1]["rank"])
    #save the result as csv
    df = pd.DataFrame(relevant_data)
    df.to_csv(path, index=False, mode='a', header=False)
    
    counter = counter + by;