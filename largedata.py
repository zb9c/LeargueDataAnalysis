import json
import xlsxwriter
import io
import requests
#For unicode shit
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

#Need to find a way to change champion id to actual champion name (https://pastebin.com/raw/JPp5gBkT)

#---COMPLETE---Need to download all data files from Riot and process them all into the spreadsheet(currently only 1 of 10)
#https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches{1-10}.json

#To create items to be added to the spreadshsheet (ie. gameId, playerName, etc.)
#Create array that the data will be stored in
#Go into the loop that is going through all the games, and for each game, append the data to its corrosponding array
#Youll then have to append the new array to the data array
#Then add the correct column heading to the array and to the lines that are appending the data to the spreadsheet

#Call with 1-10 to return LARGE json element with 100 games

champs = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json").json()
    
    
def downloadGame(number):
    url = 'https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches' + str(number) + '.json'
    response = requests.get(url)
    response.encoding = 'latin1'
    games = response.json()
    
    #Cleanes all games by removing unnecessary details
    for i in range(len(games['matches'])):
        del games['matches'][i]['mapId']
        del games['matches'][i]['gameMode']
        del games['matches'][i]['queueId']
        del games['matches'][i]['gameVersion']
        del games['matches'][i]['gameCreation']
        del games['matches'][i]['gameDuration']
        del games['matches'][i]['seasonId']
        
        for y in range(10):
            del games['matches'][i]['participants'][y]['timeline']
            del games['matches'][i]['participantIdentities'][y]['player']['profileIcon']
            del games['matches'][i]['participantIdentities'][y]['player']['platformId']
            del games['matches'][i]['participantIdentities'][y]['player']['matchHistoryUri']
            del games['matches'][i]['participantIdentities'][y]['player']['currentPlatformId']
    
    return games

def champion(number):
    championNumber = 0
    if championNumber =! number:
        for r in range(len(the)):
            championNumber = champions['data'][r][]
    
data = []
matchIds = []
playerNames = []
championPlayed = []
outcome = []
deaths = []
kills = []
wardsPlaced = []
wardsKilled = []
playerTier = []
teamDragons = []
teamBarons = []
minionsKilled = []

'''
#Open Games1.json and load as matchData
with io.open('Games1.json', encoding = 'latin-1') as data_file:
        matchData = json.load(data_file)

#Clean the Data        
for x in range(100):
    del matchData['matches'][x]['mapId']
    del matchData['matches'][x]['gameMode']
    del matchData['matches'][x]['queueId']
    del matchData['matches'][x]['gameVersion']
    del matchData['matches'][x]['gameCreation']
    del matchData['matches'][x]['gameDuration']
    del matchData['matches'][x]['seasonId']
    print x
    for y in range(10):
        del matchData['matches'][x]['participants'][y]['timeline']
        #del matchData['matches'][x]['participants'][y]['runes']
        del matchData['matches'][x]['participants'][y]['masteries']
        del matchData['matches'][x]['participantIdentities'][y]['player']['profileIcon']
        del matchData['matches'][x]['participantIdentities'][y]['player']['platformId']
        del matchData['matches'][x]['participantIdentities'][y]['player']['matchHistoryUri']
        del matchData['matches'][x]['participantIdentities'][y]['player']['currentPlatformId']

#Save Data as cleanData.json
with io.open('cleanData.json', 'w', encoding='latin-1') as outfile:
    str_ = json.dumps(matchData,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

#Open new cleanData.json as current working file as matches  
with io.open('cleanData.json', encoding = 'latin-1') as data_file:
    matches = json.load(data_file)

#Append data to its corrosponding array
for x in range(100):
    #Above loop goes through every match, bottom loop goes through each player, respectively
    for y in range(10):
        playerNames.append(matches['matches'][x]['participantIdentities'][y]['player']['summonerName'])
        championPlayed.append(matches['matches'][x]['participants'][y]['championId'])
        playerTier.append(matches['matches'][x]['participants'][y]['highestAchievedSeasonTier'])
        deaths.append(matches['matches'][x]['participants'][y]['stats']['deaths'])
        wardsPlaced.append(matches['matches'][x]['participants'][y]['stats']['wardsPlaced'])
        wardsKilled.append(matches['matches'][x]['participants'][y]['stats']['wardsKilled'])
        kills.append(matches['matches'][x]['participants'][y]['stats']['kills'])
        matchIds.append(matches['matches'][x]['gameId'])
        minionsKilled.append(matches['matches'][x]['participants'][y]['stats']['totalMinionsKilled'])
        
        #Find out if the player won/lost and append it to the array
        winner = matches['matches'][x]['participants'][y]['stats']['win']
        if winner == True:
            outcome.append("Win")
        else:
            outcome.append("Loss")
        
        #Find out which team the player was on, and how many barons/dragons the team got    
        playerTeam = matches['matches'][x]['participants'][y]['teamId']
        if playerTeam == 100:
            playerTeam = 0
        else:
            playerTeam = 1
        teamDragons.append(matches['matches'][x]['teams'][playerTeam]['dragonKills'])
        teamBarons.append(matches['matches'][x]['teams'][playerTeam]['baronKills'])
'''

#Download and store games and 'matches element
for i in range(1,10):
    matches = downloadGame(i)
    for x in range(100):
    
    #Above loop goes through every match, bottom loop goes through each player, respectively
        for y in range(10):
            playerNames.append(matches['matches'][x]['participantIdentities'][y]['player']['summonerName'])
            
            
            championPlayed.append(matches['matches'][x]['participants'][y]['championId'])
            
            playerTier.append(matches['matches'][x]['participants'][y]['highestAchievedSeasonTier'])
            deaths.append(matches['matches'][x]['participants'][y]['stats']['deaths'])
            wardsPlaced.append(matches['matches'][x]['participants'][y]['stats']['wardsPlaced'])
            wardsKilled.append(matches['matches'][x]['participants'][y]['stats']['wardsKilled'])
            kills.append(matches['matches'][x]['participants'][y]['stats']['kills'])
            matchIds.append(matches['matches'][x]['gameId'])
            minionsKilled.append(matches['matches'][x]['participants'][y]['stats']['totalMinionsKilled'])
            
            #Find out if the player won/lost and append it to the array
            winner = matches['matches'][x]['participants'][y]['stats']['win']
            if winner == True:
                outcome.append("Win")
            else:
                outcome.append("Loss")
            
            #Find out which team the player was on, and how many barons/dragons the team got    
            playerTeam = matches['matches'][x]['participants'][y]['teamId']
            if playerTeam == 100:
                playerTeam = 0
            else:
                playerTeam = 1
            teamDragons.append(matches['matches'][x]['teams'][playerTeam]['dragonKills'])
            teamBarons.append(matches['matches'][x]['teams'][playerTeam]['baronKills'])

#Setup workbook called largedata and the worksheet well be writing to
workbook = xlsxwriter.Workbook('largeData.xlsx')
worksheet = workbook.add_worksheet()

#Creating the worksheet headings
worksheet.write('A1', 'Game Id')
worksheet.write('B1', 'Player Name')
worksheet.write('C1', 'Champion Played')
worksheet.write('D1', 'Outcome')
worksheet.write('E1', 'Deaths')
worksheet.write('F1', 'Kills')
worksheet.write('G1', 'Wards Killed')
worksheet.write('H1', 'Wards Placed')
worksheet.write('I1', 'Player Tier')
worksheet.write('J1', 'Team Dragons')
worksheet.write('K1', 'Team Barons')
worksheet.write('L1', 'Minions Killed')

#Append arrays to the data array
data.append(matchIds)
data.append(playerNames)
data.append(championPlayed)
data.append(outcome)
data.append(deaths)
data.append(kills)
data.append(wardsKilled)
data.append(wardsPlaced)
data.append(playerTier)
data.append(teamDragons)
data.append(teamBarons)
data.append(minionsKilled)

#Adding data to the corrosponding column
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])
worksheet.write_column('D2', data[3])
worksheet.write_column('E2', data[4])
worksheet.write_column('F2', data[5])
worksheet.write_column('G2', data[6])
worksheet.write_column('H2', data[7])
worksheet.write_column('I2', data[8])
worksheet.write_column('J2', data[9])
worksheet.write_column('K2', data[10])
worksheet.write_column('L2', data[11])

workbook.close()
