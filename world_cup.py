import requests
import json

match_day = input('Sisesta mängupäeva number: ')

request_header = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2Mzg0NjI2MWY5YzMyYjNmNjMxMzA4NjkiLCJpYXQiOjE2Njk2MjAzMjIsImV4cCI6MTY2OTcwNjcyMn0.HfNA6DoSuU3bt7Fxg2GYI66fprND5wkp8003aSaflV4",
    "Content-Type": "application/json"
}

response = requests.get("http://api.cup2022.ir/api/v1/bymatch/" + match_day, headers=request_header)
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)

matches = response.json()

for match in matches['data']:
    if match['time_elapsed'] != 'notstarted':
        print(match['home_team_en'], '-', match['away_team_en'])
        print(str(match['home_score']) + ':' + str(match['away_score']))

        if match['home_score']:
            print(match['home_team_en'], 'väravalööjad:')
            print(', '.join(match['home_scorers'][0].split(',')))
            
        if match['away_score']:
            print(match['away_team_en'], 'väravalööjad:')
            print(', '.join(match['away_scorers'][0].split(',')))