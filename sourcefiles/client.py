# Example file showing a circle moving on screen
import pygame
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

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("PyGame Internet Checkers", icontitle="")
clock = pygame.time.Clock()
dt = 0

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 24)

def drawGrid(game, player):
    
    if not(game.connected()):
        screen.fill(FILL_NEUTRAL)
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render("Waiting for second player to connect.", True, (255,0,0))
        screen.blit(text, (720/2 - text.get_width()/2, 720/2 - text.get_height()/2))
    else:
        if(game.changed == 1):
            return
        screen.fill(FILL_RED if player == 'r' else FILL_BLACK)
        game.changed == 1
        blockSize = 64
        rect = pygame.Rect(86, 86, 544, 544)
        pygame.draw.rect(screen, BLACK_DARKER, rect)
        for x in range(0, 8):
            for y in range(0, 8):
                rect = pygame.Rect((102 + 64 * x), (102 + 64 * y), blockSize, blockSize)
                if(game.selected_grid[0] == [y, x] or game.selected_grid[1] == [y, x]):
                    pygame.draw.rect(screen, SELECTED, rect)
                elif(game.allow_grid[0] == [y, x] or game.allow_grid[1] == [y, x] or game.allow_grid[2] == [y, x] or game.allow_grid[3] == [y, x]):
                    pygame.draw.rect(screen, ALLOW, rect)
                elif([y, x] in game.compulsory_tiles):
                    pygame.draw.rect(screen, COMPULSORY, rect)
                else:
                    pygame.draw.rect(screen, WHITE if (x + y) % 2 == 0 else BLACK, rect)
                if(game.checkers[y][x][0] == "r"):
                    pygame.draw.circle(screen, RED_PIECE, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24)
                if(game.checkers[y][x][0] == "b"):
                    pygame.draw.circle(screen, BLACK_PIECE, pygame.Vector2((134 + 64 * x), (134 + 64 * y)), 24)
                if(game.checkers[y][x] == "rq" or game.checkers[y][x] == "bq"):
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
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        try:
            screen.fill((120, 120, 120))
            if(receivedAlready == False):
                game = n.send("get")
                if((game.connected() == True and game.current_turn == player) or (game.running == False)):
                    receivedAlready = True
            drawGrid(game, player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and receivedAlready == True:
                    x = pygame.mouse.get_pos()[1]
                    y = pygame.mouse.get_pos()[0]
                    x = (x - 102) // 64
                    y = (y - 102) // 64
                    changeOccoured = game.updateSelection(x, y)
                    if(changeOccoured == True):
                        data = "map:"+''.join(str(x) for x in game.checkers)+''.join(str(x) for x in game.last_move)
                        n.send(data)
                        receivedAlready = False
                        changeOccoured = False
        except:
            running = False
            print("Couldn't get the game instance.")
            break

        # fill the screen with a color to wipe away anything from last frame

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000

main()