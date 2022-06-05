import requests

def use_api(datatype, matchtype, game="aoe2de", start=None, count=None, profile_id=None):
    root = "https://aoe2.net/api/"
    
    if datatype == "leaderboard":
        api_url = (root  + datatype + "?game=" + game + 
                    "&leaderboard_id=" + str(matchtype) +
                    "&start=" + str(start) +
                    "&count=" + str(count)
                   )
    elif datatype == "ratinghistory":
        api_url = (root + "player/" + datatype + "?game=" + game +
                    "&leaderboard_id=" + str(matchtype) +
                    "&profile_id=" + str(profile_id) +
                    "&count=" + str(count)
                  )
        
    response = requests.get(api_url)
    data_in_json = response.json()
    return data_in_json
    