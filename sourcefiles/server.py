import socket
from _thread import *
import pickle
from checkers import Checkers
from networkaddress import NetworkAddress

server = NetworkAddress().address
port = NetworkAddress().port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(5)
print("Server has launched successfully! Awaiting connections from players...")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = str(conn.recv(4096).decode())

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data[0:3] == "map":
                        last_move = data[-2:]
                        data = data[:-2]
                        data = data[4:]
                        foo = ([pos for pos, char in enumerate(data) if char == '['])
                        bar = [data[start:end] for start, end in zip([0] + foo, foo + [None])]
                        bar.pop(0)
                        x = [eval(bar[0]), eval(bar[1]), eval(bar[2]), eval(bar[3]), eval(bar[4]), eval(bar[5]), eval(bar[6]), eval(bar[7])]
                        y = [int(last_move[0]), int(last_move[1])]
                        game.checkers = x
                        game.selected_grid = [[-1, -1], [-1, -1]]
                        game.current_selection = 0
                        game.last_move = y
                        game.checkForMoves()    
                        conn.sendall(pickle.dumps(game))
                    else:
                        conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection!")
    try:
        del games[gameId]
        print("Closing game of id:", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("New connection on:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Checkers(gameId)
        print("Creating new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))