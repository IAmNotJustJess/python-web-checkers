# Example file showing a circle moving on screen
import pygame

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
WHITE = (220, 220, 220)
BLACK_DARKER = (30, 30, 30)
BLACK = (60, 60, 60)
BLACK_PIECE =(20, 20, 20)
RED_PIECE = (180, 20, 20)
GOLD = (219, 167, 71)
SELECTED = (32, 112, 216)
ALLOW = (32, 164, 216)
COMPULSORY = (145, 64, 232)

current_selection = 0
selected_grid = [[-1, -1], [-1, -1]]
allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
allow_grid_type = [-1, -1, -1, -1]
move_color = ""
changed = 0
checkers = [
    [" ", "b", " ", "b", " ", "b", " ", "b"],
    ["b", " ", "b", " ", "b", " ", "b", " "],
    [" ", "b", " ", "b", " ", "b", " ", "b"],
    ["n", " ", "n", " ", "n", " ", "n", " "],
    [" ", "n", " ", "n", " ", "n", " ", "n"],
    ["r", " ", "r", " ", "r", " ", "r", " "],
    [" ", "r", " ", "r", " ", "r", " ", "r"],
    ["r", " ", "r", " ", "r", " ", "r", " "]
       ]
red_pieces = 12
black_pieces = 12
ignore_compulsory_tile = [-1, -1]
last_move = [-1, -1]
compulsory_tiles = []
compulsory_moves_red = False
compulsory_moves_black = False
last_compulsory_move_red = False
last_compulsory_move_black = False
any_moves_available_red = True
any_moves_available_black = True
force_compulsory_black = False
force_compulsory_red = False
current_turn = "r"
running = True
turn_count = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Giga warcaby!", icontitle="")
clock = pygame.time.Clock()
dt = 0

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 24)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def checkForMovesAtCoords(x, y):

    tile = checkers[x][y]
    if tile == "r":
        if (x - 1 >= 0):
            if (y - 1 >= 0):
                tile2 = checkers[x - 1][y - 1]
                if(tile2 == "n"):
                    return True
            if (y + 1 <= 7):
                tile2 = checkers[x - 1][y + 1]
                if(tile2 == "n"):
                    return True
    if tile == "b":
        if (x + 1 <= 7):
            if (y - 1 >= 0):
                tile2 = checkers[x + 1][y - 1]
                if(tile2 == "n"):
                    return True
            if (y + 1 <= 7):
                tile2 = checkers[x + 1][y + 1]
                if(tile2 == "n"):
                    return True
    if tile == "rq" or tile == "bq":
        if (x - 1 >= 0):
            if (y - 1 >= 0):
                tile2 = checkers[x - 1][y - 1]
                if(tile2 == "n"):
                    return True
            if (y + 1 <= 7):
                tile2 = checkers[x - 1][y + 1]
                if(tile2 == "n"):
                    return True
        if (x + 1 <= 7):
            if (y - 1 >= 0):
                tile2 = checkers[x + 1][y - 1]
                if(tile2 == "n"):
                    return True
            if (y + 1 <= 7):
                tile2 = checkers[x + 1][y + 1]
                if(tile2 == "n"):
                    return True
    return False

def checkForCompulsoryMovesAtCoords(x, y):
    tile = checkers[x][y]
    if tile == "r":
        if (x - 1 >= 0):
            if (y - 1 >= 0):
                tile2 = checkers[x - 1][y - 1]
                if(tile2 == "b" or tile2 == 'bq'):
                    if (x - 2 >= 0):
                        if (y - 2 >= 0):
                            tile3 = checkers[x - 2][y - 2]
                            if(tile3 == "n"):
                                return True
            if (y + 1 <= 7):
                tile2 = checkers[x - 1][y + 1]
                if(tile2 == "b" or tile2 == 'bq'):
                    if (x - 2 >= 0):
                        if (y + 2 <= 7):
                            tile3 = checkers[x - 2][y + 2]
                            if(tile3 == "n"):
                                return True
    if tile == "b":
        if (x + 1 <= 7):
            if (y - 1 >= 0):
                tile2 = checkers[x + 1][y - 1]
                if(tile2 == "r" or tile2 == 'rq'):
                    if (x + 2 <= 7):
                        if (y - 2 >= 0):
                            tile3 = checkers[x + 2][y - 2]
                            if(tile3 == "n"):
                                return True
            if (y + 1 <= 7):
                tile2 = checkers[x + 1][y + 1]
                if(tile2 == "r" or tile2 == 'rq'):
                    if (x + 2 <= 7):
                        if (y + 2 <= 7):
                            tile3 = checkers[x + 2][y + 2]
                            if(tile3 == "n"):
                                return True
    if tile == "rq":
        if (x - 1 >= 0):
            if (y - 1 >= 0):
                tile2 = checkers[x - 1][y - 1]
                if(tile2 == "b" or tile2 == 'bq'):
                    if (x - 2 >= 0):
                        if (y - 2 >= 0):
                            tile3 = checkers[x - 2][y - 2]
                            if(tile3 == "n"):
                                return True
            if (y + 1 <= 7):
                tile2 = checkers[x - 1][y + 1]
                if(tile2 == "b" or tile2 == 'bq'):
                    if (x - 2 >= 0):
                        if (y + 2 <= 7):
                            tile3 = checkers[x - 2][y + 2]
                            if(tile3 == "n"):
                                return True
        if (x + 1 <= 7):
            if (y - 1 >= 0):
                tile2 = checkers[x + 1][y - 1]
                if(tile2 == "b" or tile2 == 'bq'):
                    if (x + 2 <= 7):
                        if (y - 2 >= 0):
                            tile3 = checkers[x + 2][y - 2]
                            if(tile3 == "n"):
                                return True
            if (y + 1 <= 7):
                tile2 = checkers[x + 1][y + 1]
                if(tile2 == "b" or tile2 == 'bq'):
                    if (x + 2 <= 7):
                        if (y + 2 <= 7):
                            tile3 = checkers[x + 2][y + 2]
                            if(tile3 == "n"):
                                return True
    if tile == "bq":
        if (x - 1 >= 0):
            if (y - 1 >= 0):
                tile2 = checkers[x - 1][y - 1]
                if(tile2 == "r" or tile2 == 'rq'):
                    if (x - 2 >= 0):
                        if (y - 2 >= 0):
                            tile3 = checkers[x - 2][y - 2]
                            if(tile3 == "n"):
                                return True
            if (y + 1 <= 7):
                tile2 = checkers[x - 1][y + 1]
                if(tile2 == "r" or tile2 == 'rq'):
                    if (x - 2 >= 0):
                        if (y + 2 <= 7):
                            tile3 = checkers[x - 2][y + 2]
                            if(tile3 == "n"):
                                return True
        if (x + 1 <= 7):
            if (y - 1 >= 0):
                tile2 = checkers[x + 1][y - 1]
                if(tile2 == "r" or tile2 == 'rq'):
                    if (x + 2 <= 7):
                        if (y - 2 >= 0):
                            tile3 = checkers[x + 2][y - 2]
                            if(tile3 == "n"):
                                return True
            if (y + 1 <= 7):
                tile2 = checkers[x + 1][y + 1]
                if(tile2 == "r" or tile2 == 'rq'):
                    if (x + 2 <= 7):
                        if (y + 2 <= 7):
                            tile3 = checkers[x + 2][y + 2]
                            if(tile3 == "n"):
                                return True
    return False

def checkForMoves():

    checkForQueens()

    global any_moves_available_black
    global any_moves_available_red
    global compulsory_moves_black
    global compulsory_moves_red
    global last_compulsory_move_black
    global last_compulsory_move_red
    global ignore_compulsory_tile
    global last_move
    global compulsory_tiles

    compulsory_tiles = []

    last_compulsory_move_red = compulsory_moves_red
    last_compulsory_move_black = compulsory_moves_black

    any_moves_available_red = False
    any_moves_available_black = False
    compulsory_moves_red = False
    compulsory_moves_black = False

    break_out = False
    for x in range(0, 8):
        if break_out == True: continue
        for y in range(0, 8):
            if break_out == True: continue
            if (checkers[x][y] == 'r' or checkers[x][y] == 'rq'):
                if checkForMovesAtCoords(x, y) == True or checkForCompulsoryMovesAtCoords(x, y) == True: break_out = True
    if break_out == True:
        any_moves_available_red = True
    break_out = False
    for x in range(0, 8):
        if break_out == True: continue
        for y in range(0, 8):
            if break_out == True: continue
            if (checkers[x][y] == 'b' or checkers[x][y] == 'bq'):
                if checkForMovesAtCoords(x, y) == True or checkForCompulsoryMovesAtCoords(x, y) == True: break_out = True
    if break_out == True:
        any_moves_available_black = True

    if(current_turn == "r" and last_compulsory_move_red == True):
        result = checkForCompulsoryMovesAtCoords(last_move[0], last_move[1])
        if result == True:
            compulsory_moves_red = True
            compulsory_tiles.append([last_move[0], last_move[1]])
    elif(current_turn == "b" and last_compulsory_move_black == True):
        result = checkForCompulsoryMovesAtCoords(last_move[0], last_move[1])
        if result == True:
            compulsory_moves_black = True
            compulsory_tiles.append([last_move[0], last_move[1]])

    if(compulsory_moves_black == False and compulsory_moves_red == False):
        if(current_turn == "r"):
            break_out = False
            for x in range(0, 8):
                for y in range(0, 8):
                    if (checkers[x][y] == 'b' or checkers[x][y] == 'bq') and checkForCompulsoryMovesAtCoords(x, y) == True: 
                        break_out = True
                        compulsory_tiles.append([x, y])
            if break_out == True:
                compulsory_moves_black = True
        elif(current_turn == "b"):
            break_out = False
            for x in range(0, 8):
                for y in range(0, 8):
                    if (checkers[x][y] == 'r' or checkers[x][y] == 'rq') and checkForCompulsoryMovesAtCoords(x, y) == True:
                        break_out = True
                        compulsory_tiles.append([x, y])
            if break_out == True:
                compulsory_moves_red = True
        
    checkVictory()
    nextTurn()

def checkVictory():
    global red_pieces
    global black_pieces
    global any_moves_available_red
    global any_moves_available_black
    global running
    if(red_pieces <= 0 or any_moves_available_red == False):
        print("Wygrał gracz czarny!")
        running = False
    elif(black_pieces <= 0 or any_moves_available_black == False):
        print("Wygrał gracz czerwony!")
        running = False

def nextTurn():

    global current_turn
    global turn_count
    global running

    if(running == False):
        return

    turn_count += 1

    if compulsory_moves_red == True:
        print("Tura gracza czerwonego - wymuszone bicie.")
        current_turn = "r"
    elif compulsory_moves_black == True:
        print("Tura gracza czarnego - wymuszone bicie.")
        current_turn = "b"
    else:
        if current_turn == "r":
            current_turn = "b"
            print("Tura gracza czarnego.")
        elif current_turn == "b":
            current_turn = "r"
            print("Tura gracza czerwonego.")

def checkForQueens():
    for i in range(0, 4):
        if(checkers[0][(i * 2) + 1] == "r"):
            checkers[0][(i * 2) + 1] = "rq"
        if(checkers[7][(i * 2)] == "b"):
            checkers[7][(i * 2)] = "bq"
    print(''.join(str(x) for x in checkers))

def makeMove(x, y, x2, y2, type):

    global allow_grid
    global allow_grid_type
    global move_color
    global selected_grid
    global current_selection
    global current_turn
    global black_pieces
    global red_pieces
    global ignore_compulsory_tile
    global last_move

    ignore_compulsory_tile = [-1, -1]

    if type == -1:
        return
    if type == 0 and ((compulsory_moves_black == True and current_turn == "b") or (compulsory_moves_red == True and current_turn == "r")):
        return
    elif type == 0:
        checkers[x][y] = "n"
        checkers[x2][y2] = move_color
        # ignore_compulsory_tile = [x2, y2]
    elif type == 1:
        checkers[x + 1][y - 1] = "n"
    elif type == 2:
        checkers[x + 1][y + 1] = "n"
    elif type == 3:
        checkers[x - 1][y - 1] = "n"
    elif type == 4:
        checkers[x - 1][y + 1] = "n"
    
    last_move = [x2, y2]

    if(type >= 1 and type <= 4):
        checkers[x][y] = "n"
        checkers[x2][y2] = move_color
        if(current_turn == "r"):
            black_pieces -= 1
        if(current_turn == "b"):
            red_pieces -= 1

    current_selection = 0
    selected_grid = [[-1, -1], [-1, -1]]
    allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    allow_grid_type = [-1, -1, -1, -1]
    
    checkForMoves() 

def updateSelection(x, y):

    global running

    if(running == False):
        return

    global allow_grid
    global allow_grid_type
    global selected_grid
    global move_color
    global current_selection
    global changed
    
    if(x >= 0 and y >= 0 and x <= 7 and y <= 7 and (x + y) % 2 == 1):

        if(current_selection == 1 and checkers[x][y] != "n"):
            current_selection = 0
            allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]

        selected_grid[current_selection] = [x, y]

        if((current_selection == 0 and checkers[x][y][0] != current_turn) or (current_selection == 1 and checkers[selected_grid[0][0]][selected_grid[0][1]][0] != current_turn)):
            current_selection = 0
            selected_grid = [[-1, -1], [-1, -1]]
            allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
            allow_grid_type = [-1, -1, -1, -1]
            return

        if(current_selection == 1):
            for i in range(0, 4):
                if(allow_grid[i] == [x, y]):
                    makeMove(selected_grid[0][0], selected_grid[0][1], selected_grid[1][0], selected_grid[1][1], allow_grid_type[i])
                    return
                
        if(checkers[x][y] == "b"):
            move_color = "b"
            if(x + 1 <= 7 and y - 1 >= 0 and checkers[x + 1][y - 1] == "n"):
                allow_grid[0] = [x + 1, y - 1]
                allow_grid_type[0] = 0
            elif(x + 2 <= 7 and y - 2 >= 0 and checkers[x + 1][y - 1][0] == "r" and checkers[x + 2][y - 2] == "n"):
                allow_grid[0] = [x + 2, y - 2]
                allow_grid_type[0] = 1
            if(x + 1 <= 7 and y + 1 <= 7 and checkers[x + 1][y + 1] == "n"):
                allow_grid[1] = [x + 1, y + 1]
                allow_grid_type[1] = 0
            elif(x + 2 <= 7 and y + 2 <= 7 and checkers[x + 1][y + 1][0] == "r"  and checkers[x + 2][y + 2] == "n"):
                allow_grid[1] = [x + 2, y + 2]
                allow_grid_type[1] = 2
            allow_grid[2] = [-1, -1]
            allow_grid_type[2] = -1
            allow_grid[3] = [-1, -1]
            allow_grid_type[2] = -1

        elif(checkers[x][y] == "r"):
            move_color = "r"
            if(x - 1 >= 0 and y - 1 >= 0 and checkers[x - 1][y - 1] == "n"):
                allow_grid[0] = [x - 1, y - 1]
                allow_grid_type[0] = 0
            elif(x - 2 >= 0 and y - 2 >= 0 and checkers[x - 1][y - 1][0] == "b" and checkers[x - 2][y - 2] == "n"):
                allow_grid[0] = [x - 2, y - 2]
                allow_grid_type[0] = 3
            if(x - 1 >= 0 and y + 1 <= 7 and checkers[x - 1][y + 1] == "n"):
                allow_grid[1] = [x - 1, y + 1]
                allow_grid_type[1] = 0
            elif(x - 2 >= 0 and y + 2 <= 7 and checkers[x - 1][y + 1][0] == "b" and checkers[x - 2][y + 2] == "n"):
                allow_grid[1] = [x - 2, y + 2]
                allow_grid_type[1] = 4
            allow_grid[2] = [-1, -1]
            allow_grid_type[2] = -1
            allow_grid[3] = [-1, -1]
            allow_grid_type[2] = -1
        
        elif(checkers[x][y] == "rq"):
            move_color = "rq"
            if(x - 1 >= 0 and y - 1 >= 0 and checkers[x - 1][y - 1] == "n"):
                allow_grid[0] = [x - 1, y - 1]
                allow_grid_type[0] = 0
            elif(x - 2 >= 0 and y - 2 >= 0 and checkers[x - 1][y - 1][0] == "b" and checkers[x - 2][y - 2] == "n"):
                allow_grid[0] = [x - 2, y - 2]
                allow_grid_type[0] = 3
            if(x - 1 >= 0 and y + 1 <= 7 and checkers[x - 1][y + 1] == "n"):
                allow_grid[1] = [x - 1, y + 1]
                allow_grid_type[1] = 0
            elif(x - 2 >= 0 and y + 2 <= 7 and checkers[x - 1][y + 1][0] == "b" and checkers[x - 2][y + 2] == "n"):
                allow_grid[1] = [x - 2, y + 2]
                allow_grid_type[1] = 4
            if(x + 1 <= 7 and y - 1 >= 0 and checkers[x + 1][y - 1] == "n"):
                allow_grid[2] = [x + 1, y - 1]
                allow_grid_type[2] = 0
            elif(x + 2 <= 7 and y - 2 >= 0 and checkers[x + 1][y - 1][0] == "b" and checkers[x + 2][y - 2] == "n"):
                allow_grid[2] = [x + 2, y - 2]
                allow_grid_type[2] = 1
            if(x + 1 <= 7 and y + 1 <= 7 and checkers[x + 1][y + 1] == "n"):
                allow_grid[3] = [x + 1, y + 1]
                allow_grid_type[3] = 0
            elif(x + 2 <= 7 and y + 2 <= 7 and checkers[x + 1][y + 1][0] == "b" and checkers[x + 2][y + 2] == "n"):
                allow_grid[3] = [x + 2, y + 2]
                allow_grid_type[3] = 2
        
        elif(checkers[x][y] == "bq"):
            move_color = "bq"
            if(x - 1 >= 0 and y - 1 >= 0 and checkers[x - 1][y - 1] == "n"):
                allow_grid[0] = [x - 1, y - 1]
                allow_grid_type[0] = 0
            elif(x - 2 >= 0 and y - 2 >= 0 and checkers[x - 1][y - 1][0] == "r" and checkers[x - 2][y - 2] == "n"):
                allow_grid[0] = [x - 2, y - 2]
                allow_grid_type[0] = 3
            if(x - 1 >= 0 and y + 1 <= 7 and checkers[x - 1][y + 1] == "n"):
                allow_grid[1] = [x - 1, y + 1]
                allow_grid_type[1] = 0
            elif(x - 2 >= 0 and y + 2 <= 7 and checkers[x - 1][y + 1][0] == "r" and checkers[x - 2][y + 2] == "n"):
                allow_grid[1] = [x - 2, y + 2]
                allow_grid_type[1] = 4
            if(x + 1 <= 7 and y - 1 >= 0 and checkers[x + 1][y - 1] == "n"):
                allow_grid[2] = [x + 1, y - 1]
                allow_grid_type[2] = 0
            elif(x + 2 <= 7 and y - 2 >= 0 and checkers[x + 1][y - 1][0] == "r" and checkers[x + 2][y - 2] == "n"):
                allow_grid[2] = [x + 2, y - 2]
                allow_grid_type[2] = 1
            if(x + 1 <= 7 and y + 1 <= 7 and checkers[x + 1][y + 1] == "n"):
                allow_grid[3] = [x + 1, y + 1]
                allow_grid_type[3] = 0
            elif(x + 2 <= 7 and y + 2 <= 7 and checkers[x + 1][y + 1][0] == "r" and checkers[x + 2][y + 2] == "n"):
                allow_grid[3] = [x + 2, y + 2]
                allow_grid_type[3] = 2
        
        if(current_selection == 0):
            current_selection = 1
        else:
            selected_grid = [[-1, -1], [-1, -1]]
            current_selection = 0
        changed = 0
    else:
        current_selection = 0
        selected_grid = [[-1, -1], [-1, -1]]
        allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
        allow_grid_type = [-1, -1, -1, -1]

    changed = 0

def checkAvailability():
    return

def drawGrid():
    if(changed == 1):
        return
    changed == 1
    blockSize = 64
    rect = pygame.Rect(86, 86, 544, 544)
    pygame.draw.rect(screen, BLACK_DARKER, rect)
    for x in range(0, 8):
        for y in range(0, 8):
            rect = pygame.Rect((102 + 64 * x), (102 + 64 * y), blockSize, blockSize)
            if(selected_grid[0] == [y, x] or selected_grid[1] == [y, x]):
                pygame.draw.rect(screen, SELECTED, rect)
            elif(allow_grid[0] == [y, x] or allow_grid[1] == [y, x] or allow_grid[2] == [y, x] or allow_grid[3] == [y, x]):
                pygame.draw.rect(screen, ALLOW, rect)
            elif([y, x] in compulsory_tiles):
                pygame.draw.rect(screen, COMPULSORY, rect)
            else:
                pygame.draw.rect(screen, WHITE if (x + y) % 2 == 0 else BLACK, rect)
            if(checkers[y][x][0] == "r"):
                pygame.draw.circle(screen, RED_PIECE, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24)
            if(checkers[y][x][0] == "b"):
                pygame.draw.circle(screen, BLACK_PIECE, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24)
            if(checkers[y][x] == "rq" or checkers[y][x] == "bq"):
                pygame.draw.circle(screen, GOLD, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24, 4)
    if(current_turn == "r" and compulsory_moves_red == False): text_surface = my_font.render("Tura gracza czerwonego.", False, RED_PIECE)
    if(current_turn == "r" and compulsory_moves_red == True): text_surface = my_font.render("Tura gracza czerwonego - musisz zbić przeciwnika!", False, RED_PIECE)
    if(current_turn == "b" and compulsory_moves_black == False): text_surface = my_font.render("Tura gracza czarnego.", False, BLACK_PIECE)
    if(current_turn == "b" and compulsory_moves_black == True): text_surface = my_font.render("Tura gracza czarnego - musisz zbić przeciwnika!", False, BLACK_PIECE)
    if(red_pieces <= 0): text_surface = my_font.render("Wygrał gracz czarny!", False, BLACK_PIECE)
    if(black_pieces <= 0): text_surface = my_font.render("Wygrał gracz czerwony!", False, RED_PIECE)
    if(any_moves_available_black == False): text_surface = my_font.render("Wygrał gracz czerwony! Gracz czarny nie ma ruchów!", False, RED_PIECE)
    if(any_moves_available_red == False): text_surface = my_font.render("Wygrał gracz czarny! Gracz czerwony nie ma ruchów!", False, BLACK_PIECE)
    screen.blit(text_surface, (0,0))
    

def main():
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[1]
                y = pygame.mouse.get_pos()[0]
                x = (x - 102) // 64
                y = (y - 102) // 64
                updateSelection(x, y)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((120, 120, 120))
        drawGrid()

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000


main()