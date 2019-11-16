
table = {}
def createTeam(team):
    table[team] = {
            "MP": 0,
            "P": 0,
            "W": 0,
            "D": 0,
            "L": 0
        }
    return table[team]

def updateTable(teamA, teamB, result):
    teamA["MP"]+=1
    teamB["MP"]+=1
    if result == 'win':
        teamA["W"]+=1
        teamA["P"]+=3
        teamB["L"]+=1
    elif result == 'loss':
        teamB["W"]+=1
        teamB["P"]+=3
        teamA["L"]+=1
    else:
        teamA["D"]+=1
        teamA["P"]+=1
        teamB["D"]+=1
        teamB["P"]+=1

def tally(rows):
    result = ["Team                           | MP |  W |  D |  L |  P"]
    if len(rows) == 0:
        return result
    games=[row.split(";") for row in rows]
    for game in games:
        teamA = table[game[0]] if game[0] in table else createTeam(game[0])
        teamB = table[game[1]] if game[1] in table else createTeam(game[1])
        updateTable(teamA, teamB, game[2])
    
    sortednames=sorted(table.keys(), key=lambda x:x.lower())
    sortednames.sort(key=lambda x: table[x]["P"], reverse=True)
    for key in sortednames:
        team = table[key]
        sheet = f"|  {team['MP']} |  {team['W']} |  {team['D']} |  {team['L']} |  {team['P']}"
        spaces = 31 - len(key)
        for i in range(spaces):
            key+=" "
        result.append(key + sheet)
    table.clear()
    return result

