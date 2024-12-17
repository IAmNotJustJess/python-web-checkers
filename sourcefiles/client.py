# Example file showing a circle moving on screen
import pygame
import pathlib
import random
from checkers import Checkers
from connection import Connection

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
FILL_RED = (160, 120, 120)
FILL_BLACK = (100, 100, 100)
FILL_NEUTRAL = (120, 120, 120)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("PyGame Web Checkers", icontitle="")
clock = pygame.time.Clock()
dt = 0

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 24)

pygame.mixer.init()
soundlist = [
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-1.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-2.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-3.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-4.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-5.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-6.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-7.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-8.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-9.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-10.wav"))),
    pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("piece-11.wav")))
    ]

victory_sfx = pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("victory.mp3")))
defeat_sfx = pygame.mixer.Sound(str(pathlib.Path(__file__).parent.resolve().joinpath("sfx").joinpath("defeat.mp3")))

for i in range(0, 11):
    pygame.mixer.Sound.set_volume(soundlist[i], 0.12)
pygame.mixer.Sound.set_volume(victory_sfx, 0.12)
pygame.mixer.Sound.set_volume(defeat_sfx, 0.12)

def flippedBoard(board):
    new = board[::-1]
    for x in range(0, 8):
        new[x] = new[x][::-1]
    return new

def drawGrid(game, player):
    
    if not(game.connected()):
        screen.fill(FILL_NEUTRAL)
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render("Waiting for second player to connect.", True, (255,0,0))
        screen.blit(text, (720/2 - text.get_width()/2, 720/2 - text.get_height()/2))
    else:
        if(game.changed == 1):
            return
        board = game.checkers.copy()
        selected_grid = game.selected_grid.copy()
        allow_grid = game.allow_grid.copy()
        compulsory_tiles = game.compulsory_tiles.copy()
        if player == 'b':
            board = flippedBoard(board)
            for i in range(0, len(selected_grid)):
                if selected_grid[i] != [-1, -1]:
                    selected_grid[i] = [7 - selected_grid[i][0], 7 - selected_grid[i][1]]
            for i in range(0, len(allow_grid)):
                if allow_grid[i] != [-1, -1]:
                    allow_grid[i] = [7 - allow_grid[i][0], 7 - allow_grid[i][1]]
            for i in range(0, len(compulsory_tiles)):
                if compulsory_tiles[i] != [-1, -1]:
                    compulsory_tiles[i] = [7 - compulsory_tiles[i][0], 7 - compulsory_tiles[i][1]]
        screen.fill(FILL_RED if player == 'r' else FILL_BLACK)
        blockSize = 64
        rect = pygame.Rect(86, 86, 544, 544)
        pygame.draw.rect(screen, BLACK_DARKER, rect)
        for x in range(0, 8):
            for y in range(0, 8):
                rect = pygame.Rect((102 + 64 * x), (102 + 64 * y), blockSize, blockSize)
                if([y, x] in selected_grid):
                    pygame.draw.rect(screen, SELECTED, rect)
                elif([y, x] in allow_grid):
                    pygame.draw.rect(screen, ALLOW, rect)
                elif([y, x] in compulsory_tiles):
                    pygame.draw.rect(screen, COMPULSORY, rect)
                else:
                    pygame.draw.rect(screen, WHITE if (x + y) % 2 == 0 else BLACK, rect)
                if(board[y][x][0] == "r"):
                    pygame.draw.circle(screen, RED_PIECE, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24)
                if(board[y][x][0] == "b"):
                    pygame.draw.circle(screen, BLACK_PIECE, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24)
                if(board[y][x] == "rq" or board[y][x] == "bq"):
                    pygame.draw.circle(screen, GOLD, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24, 4)
        if(game.current_turn == "r" and game.compulsory_moves_red == False): text_surface = my_font.render("Red's turn.", True, RED_PIECE)
        if(game.current_turn == "r" and game.compulsory_moves_red == True): text_surface = my_font.render("Red's turn - compulsory take!", True, RED_PIECE)
        if(game.current_turn == "b" and game.compulsory_moves_black == False): text_surface = my_font.render("Black's turn.", True, BLACK_PIECE)
        if(game.current_turn == "b" and game.compulsory_moves_black == True): text_surface = my_font.render("Black's turn - compulsory!", True, BLACK_PIECE)
        if(game.red_pieces <= 0): text_surface = my_font.render("Black was victorious!", True, BLACK_PIECE)
        if(game.black_pieces <= 0): text_surface = my_font.render("Red was victorious!", True, RED_PIECE)
        if(game.any_moves_available_black == False): text_surface = my_font.render("Red was victorious! Black has ran out of moves!", True, RED_PIECE)
        if(game.any_moves_available_red == False): text_surface = my_font.render("Black was victorious! Red has ran out of moves!", True, BLACK_PIECE)
        screen.blit(text_surface, (720/2 - text_surface.get_width()/2, 0))
        if(player == 'b'): text_surface = my_font.render("You are playing as black!", True, BLACK_PIECE)
        if(player == 'r'): text_surface = my_font.render("You are playing as red!", True, RED_PIECE)
        screen.blit(text_surface, (720/2 - text_surface.get_width()/2, 676))
    

def main():
    running = True
    n = Connection()
    player = 'r' if int(n.getP()) == 0 else 'b'
    print("You are playing as", 'red.' if int(n.getP()) == 0 else 'black.')
    receivedAlready = False
    changeOccoured = False
    game = Checkers(0)
    while running:
        try:
            screen.fill((120, 120, 120))
            if(receivedAlready == False):
                game = n.send("get")
                if((game.connected() == True and game.current_turn == player) or (game.running == False)):
                    if game.running == False:
                        if player == 'b':
                            if(game.any_moves_available_black == False or game.black_pieces <= 0):
                                defeat_sfx.play()
                            if(game.any_moves_available_red == False or game.red_pieces <= 0):
                                victory_sfx.play()
                        else:
                            if(game.any_moves_available_black == False or game.black_pieces <= 0):
                                victory_sfx.play()
                            if(game.any_moves_available_red == False or game.red_pieces <= 0):
                                defeat_sfx.play()
                    else:
                        soundlist[random.randint(0, 10)].play()
                    receivedAlready = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and receivedAlready == True:
                    x = pygame.mouse.get_pos()[1]
                    y = pygame.mouse.get_pos()[0]
                    x = (x - 102) // 64
                    y = (y - 102) // 64
                    if player == 'b':
                        x = 7 - x
                        y = 7 - y
                    changeOccoured = game.updateSelection(x, y)
                    if(changeOccoured == True):
                        soundlist[random.randint(0, 10)].play()
                        data = "map:"+''.join(str(x) for x in game.checkers)+''.join(str(x) for x in game.last_move)
                        n.send(data)
                        receivedAlready = False
                        changeOccoured = False
            drawGrid(game, player)
        except:
            running = False
            print("Couldn't get the game instance.")
            break

        pygame.display.flip()

        dt = clock.tick(120) / 1000

main()