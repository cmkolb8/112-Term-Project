#this file calculates the stats and stores them in a text file
#funciton taken from cmu notes https://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

#funciton taken from cmu notes https://www.cs.cmu.edu/~112/notes/notes-strings.html
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

highestScore = None
gamesPlayed = 0
winRate = None
wins = 0

def checkScore(mode, score):
    content = readFile("highScore.txt")
    part = content.split(': ')
    highScore = part[1]
    highestScoreStr = highScore[0]
    highestScore = int(highestScoreStr)
    games = part[2]
    gamesPlayedStr = games[0]
    gamesPlayed = int(gamesPlayedStr)
    rate = part[3]
    winRateStr = rate[0]
    winRate = int(winRateStr)
    winsStr = part[4]
    wins = int(winsStr)
    try: 
        if(highestScore == None or score < highestScore):
            highestScore = score
        else: 
            pass
        gamesPlayed = gamesPlayed + 1
        if(mode.myScore == 0):
            wins += 1
            winRate = int((wins / gamesPlayed) * 100)
        once = False
    except: 
        highestScore = score
        gamesPlayed = 1
        if(mode.myScore == 0):
            winRate = 100
            wins = 1
        else: 
            winRate = 0
            wins = 0
    once = False

    contentsToWrite = f'Highest score: {highestScore}\nGames Played: {gamesPlayed}\nWin Rate: {winRate} %\n Wins: {wins}'
    writeFile("highScore.txt", contentsToWrite)
