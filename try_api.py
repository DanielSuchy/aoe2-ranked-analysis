import requests

#try to access the leaderboard
#leaderboard_id = 3 means 1v1 games, teamgames are 4
#start = starting rank, count = how many players
api_url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=1"
response = requests.get(api_url)
print(response.json())

#access ranking of a single player, based on profile id
api_url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&profile_id=254415"
response = requests.get(api_url)
print(response.json())

#access ranking of a single player, based on name
api_url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&search=SalzZ_classicpro"
response = requests.get(api_url)
print(response.json())

#search for players by name, seems to return all names that contain 'pl'
api_url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&search=pl&count=3"
response = requests.get(api_url)
print(response.json())

#extract names of top 3 players whose name contains 'pl'
leaderboard = response.json()["leaderboard"] #leaderboard entry contains 'player profile'
names = [i["name"] for i in leaderboard]
print(names)

#request 5 past matches of a player by id
api_url = "https://aoe2.net/api/player/matches?game=aoe2de&profile_id=254415&count=5"
response = requests.get(api_url)
print(response.json())

#1v1s or teamgames?
player_count = [i["num_players"] for i in response.json()]
print(player_count)

#ranked or lobby?
match_names = [i["name"] for i in response.json()]
print(match_names)

#search by player name is not possible in API, id <--> name association needs to be made first
api_url = "https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&search=SalzZ_classicpro"
response = requests.get(api_url)
profile_id = response.json()["leaderboard"][0]["profile_id"]

api_url = ("https://aoe2.net/api/player/matches?game=aoe2de&profile_id=" + 
            str(profile_id) + 
            "&count=1")
response = requests.get(api_url)
print(response.json())

#ranking history - get ELO development over last 5 matches
api_url = "https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&profile_id=254415&count=5"
response = requests.get(api_url)
elos = [i["rating"] for i in response.json()]
print(elos)

#
api_url = "https://aoe2.net/api/match?match_id=159419942"
response = requests.get(api_url)
print(response.json())
