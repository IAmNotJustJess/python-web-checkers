
class Controller:
    def __init__(self):
        self.gamestate = "waiting"
        self.currentTurn = "red"
        self.materialsRed = 12
        self.materialsBlack = 12

gamecontroller = Controller()

checkers = [
    ["b", " ", "b", " ", "b", " ", "b", " "],
    [" ", "b", " ", "b", " ", "b", " ", "b"],
    ["b", " ", "b", " ", "b", " ", "b", " "],
    [" ", "n", " ", "n", " ", "n", " ", "n"],
    ["n", " ", "n", " ", "n", " ", "n", " "],
    [" ", "r", " ", "r", " ", "r", " ", "r"],
    ["r", " ", "r", " ", "r", " ", "r", " "],
    [" ", "r", " ", "r", " ", "r", " ", "r"]
       ]

def checkAvailability(x, y, x2, y2, t):
    print(checkers)
    if x < 0 or x > 7 or y < 0 or y > 7 or x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
        return 0
    if t == 'red' and checkers[x][y] == 'r':
        viable = 0
        if x2 == x + 1 and (y2 == y - 1 or y2 == y + 1) and checkers[x2][y2] == 'n':
            viable = 1 
        if x2 == x + 1 and ((y2 == y - 1 and checkers[x2 + 1][y2 - 1] == 'n') or (y2 == y + 1 and checkers[x2 + 1][y2 + 1] == 'n')) and checkers[x2][y2] == 'b':
            viable = 2
    elif t == 'black' and checkers[x][y] == 'b':
        viable = 0
        if x2 == x + 1 and (y2 == y - 1 or y2 == y + 1) and checkers[x2][y2] == 'n':
            viable = 1 
        if x2 == x + 1 and ((y2 == y - 1 and checkers[x2 + 1][y2 - 1] == 'n') or (y2 == y + 1 and checkers[x2 + 1][y2 + 1] == 'n')) and checkers[x2][y2] == 'r':
            viable = 2
    return viable

def displayMap():
    abc = "        A  |  B  |  C  |  D  |  E  |  F  |  G  |  H  "
    linebreak = "      -----------------------------------------------"
    ott = ["8" ,"7", "6", "5", "4", "3", "2", "1"]
    turnt = ("" if gamecontroller.currentTurn == "red" else " ") + "                  Ruch gracza " + "czerwonego." if gamecontroller.currentTurn == "red" else "czarnego."

    print(" ")
    print(linebreak)
    print(turnt)
    print(linebreak)
    print(" ")
    print(abc)
    print(linebreak)
    text = "  8  |  "
    for i in range(0, 7):
        for j in range(0, 7):
            text += checkers[i][j] + "  |  "
        text += checkers[i][j + 1] + "  |  " + ott[i]
        print(text) 
        print(linebreak)
        text = "  " + ott[i+1] + "  |  "
    for j in range(0, 7):
        text += checkers[i + 1][j] + "  |  "
    text += checkers[i + 1][j + 1] + "  |  " + ott[i + 1]
    print(text)
    print(linebreak)
    print(abc)
    print(" ")

def askForMove():
    t = True
    while t:
        input1 = "Podaj którego pionka wybierasz (np. C1)"
        input2 = "Podaj pole na które chcesz się ruszyć (np. D2)"
        actualI1 = -1
        actualI2 = -1
        if(input1[0].lower == 'a'):
            actualI1 = 0
        elif(input1[0].lower == 'b'):
            actualI1 = 1
        elif(input1[0].lower == 'c'):
            actualI1 = 2
        elif(input1[0].lower == 'd'):
            actualI1 = 3
        elif(input1[0].lower == 'e'):
            actualI1 = 4
        elif(input1[0].lower == 'f'):
            actualI1 = 5
        elif(input1[0].lower == 'g'):
            actualI1 = 6
        elif(input1[0].lower == 'h'):
            actualI1 = 7
        if(input2[0].lower == 'a'):
            actualI2 = 0
        elif(input2[0].lower == 'b'):
            actualI2 = 1
        elif(input2[0].lower == 'c'):
            actualI2 = 2
        elif(input2[0].lower == 'd'):
            actualI2 = 3
        elif(input2[0].lower == 'e'):
            actualI2 = 4
        elif(input2[0].lower == 'f'):
            actualI2 = 5
        elif(input2[0].lower == 'g'):
            actualI2 = 6
        elif(input2[0].lower == 'h'):
            actualI2 = 7
        if(checkAvailability(actualI1, int(input1[1]), actualI2, int(input2[1]), gamecontroller.currentTurn)):
            t = False

def makeMove(x, y, x2, y2, x3 = -1, y3 = -1):
    print("p")

# checkAvailability(2, 2, 3, 1, "b")
displayMap()
