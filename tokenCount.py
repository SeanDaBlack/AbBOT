import csv

def getToken():
    with open("tokenCount.csv","r") as f:
        file = list(csv.reader(f))
        return(int(file[0][0]))

def addToken():
    currentToken = getToken()
    with open("tokenCount.csv","w") as f:
        file = csv.writer(f)
        file.writerow([currentToken + 1])

def resetToken():
    with open("tokenCount.csv","w") as f:
        file = csv.writer(f)
        file.writerow([0])
 