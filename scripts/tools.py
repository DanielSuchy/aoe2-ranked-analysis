import requests

def use_api(datatype, matchtype, game="aoe2de", start=None, count=None):
    root = "https://aoe2.net/api/" + datatype
    
    if datatype == "leaderboard":
        api_url = (root  + "?game=" + game + 
                    "&leaderboard_id=" + str(matchtype) +
                    "&start=" + str(start) +
                    "&count=" + str(count)
                   )
        
    response = requests.get(api_url)
    data_in_json = response.json()
    return data_in_json

use_api(datatype="leaderboard", matchtype=3, start=1, count=2)
    