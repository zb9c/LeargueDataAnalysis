import requests
import json
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
import xlsxwriter
import time

def getID(sumName):
    URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + sumName + "?api_key=" + APIKey
    response = requests.get(URL).json()
    ids = response['accountId']
    ids = str(ids)
    return ids
def getMatches(id):
    url = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + id + "?champion=16" + "&api_key=" + APIKey  #Used to get Soraka Games
    #url = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + id + "?api_key=" + APIKey
    response = requests.get(url).json()
    return response
def matchInfo(matchID):
    url = "https://na1.api.riotgames.com/lol/match/v3/matches/" + matchID + "?api_key=" + APIKey
    response = requests.get(url).json()
    #print url
    return response

APIKey = "RGAPI-735c8023-0382-41c9-89e5-a608e910533f"
gameIds = []
Wins = []
dragons = []
wardsPurchased = []

who = 'CheekyBastard'
matches = getMatches(str(getID(who)))

#'clean' out matches array before saving it
for x in range(len(matches["matches"])):
    
    gameIds.append(matches["matches"][x]["gameId"])
    
    del matches["matches"][x]["queue"]
    del matches["matches"][x]["season"]
    del matches["matches"][x]["role"]
    del matches["matches"][x]["timestamp"]
    del matches["matches"][x]["lane"]
    del matches["matches"][x]["platformId"]
    
#Save matches as WHO.json using the matches 
with io.open( who + '.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(matches,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=True)
    outfile.write(to_unicode(str_))

#Saves all matches as 0-99.json after cleaning them
for x in range(len(matches["matches"])):
    time.sleep(2)
    
    #Pulls the data from Riot API
    match = matchInfo(str(gameIds[x]))
    
    #Clean data pulled from RiotAPI
    del match['platformId']
    del match['gameCreation']
    del match['gameDuration']
    del match['gameType']
    del match['gameVersion']
    del match['seasonId']
    
    
    
    
    #Saves response as json file
    with io.open(str(x) + who + '.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(match,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

#Using that json we need to create a csv file that saves all that data
