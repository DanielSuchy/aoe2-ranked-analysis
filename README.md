# aoe2-ranked-analysis
 Analyzing data from aoe2.net

task one: analyze elo ratings of new players

new players are defined as:
have played their last ranked 1v1 placement game within the last 90 days before 11.09.2022
only play 1v1s (no teamgames etc)
were still active within 30 days before 11.09.2022
have played less than 50 games in total

questions:
What is average elo rating after the ten placement games?
How many wins/losses are there?
When do they win their first game? After/before placement games?
What is their elo after three months?

overview of the scripts:
get_players - downloads a leaderboard of all players
get_rating_history - downloads ratings of players likely to be new (to save time)
get_matchtype_experience - assigns match type experience to players likely to be new (to save time)
get_subset_players - filters out players that are actually new (needs rating history and matchtype experience)

findings:
there are 1815 players that match the above criteria
their mean ELO after the first placement games is 909
on average they win 3.89 of their placement games
the average player then went on to play 21 games, but went down to 875 ELO
82 percent of players won at least one of their placement games
More games played lead to higher variation in the data
30% of these players reach the ELO of over 1000 after the placement games
	