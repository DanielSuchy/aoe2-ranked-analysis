#download the 1v1 ranked leaderboard from aoe2.net
import requests
import json

game = "aoe2de" #ignore the HD version
leaderbleaderboard_id = str(3) #download the 1v1 ranked leaderboard
start = str(1) #start at the highest rated player
count = str(100) # download top 100 players

api_url = ("https://aoe2.net/api/leaderboard?" +
            "game=" + game +
            "&leaderboard_id=" + leaderbleaderboard_id +
            "&start=" + start +
            "&count=" + count
          )

response = requests.get(api_url)
data_in_json = response.json()

#save the result as json
with open('./data/json/top_players.json', 'w') as outfile:
    json.dump(data_in_json, outfile, indent = 4) #indent = 4 makes the file human-readable