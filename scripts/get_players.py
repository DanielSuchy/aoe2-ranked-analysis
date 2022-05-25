#download the 1v1 ranked leaderboard from aoe2.net
import requests
import pandas as pd

path = '../data/players.csv'
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
relevant_data = data_in_json["leaderboard"]

#save the result as csv
df = pd.DataFrame(relevant_data)
df.to_csv(path, index=False)