

class Checkers:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.running = True
        self.checkers = [
            [" ", "b", " ", "b", " ", "b", " ", "b"],
            ["b", " ", "b", " ", "b", " ", "b", " "],
            [" ", "b", " ", "b", " ", "b", " ", "b"],
            ["n", " ", "n", " ", "n", " ", "n", " "],
            [" ", "n", " ", "n", " ", "n", " ", "n"],
            ["r", " ", "r", " ", "r", " ", "r", " "],
            [" ", "r", " ", "r", " ", "r", " ", "r"],
            ["r", " ", "r", " ", "r", " ", "r", " "]
            ]
        self.turn_count = 0
        self.red_pieces = 12
        self.black_pieces = 12
        self.ignore_compulsory_tile = [-1, -1]
        self.last_move = [-1, -1]
        self.compulsory_tiles = []
        self.compulsory_moves_red = False
        self.compulsory_moves_black = False
        self.last_compulsory_move_red = False
        self.last_compulsory_move_black = False
        self.any_moves_available_red = True
        self.any_moves_available_black = True
        self.force_compulsory_black = False
        self.force_compulsory_red = False
        self.current_turn = "r"
        self.changed = 0
        self.current_selection = 0
        self.selected_grid = [[-1, -1], [-1, -1]]
        self.allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
        self.allow_grid_type = [-1, -1, -1, -1]
        self.move_color = ""
    
    def connected(self):
        return self.ready

    def checkForMovesAtCoords(self, x, y):
        tile = self.checkers[x][y]
        if tile == "r":
            if (x - 1 >= 0):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x - 1][y - 1]
                    if(tile2 == "n"):
                        return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x - 1][y + 1]
                    if(tile2 == "n"):
                        return True
        if tile == "b":
            if (x + 1 <= 7):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x + 1][y - 1]
                    if(tile2 == "n"):
                        return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x + 1][y + 1]
                    if(tile2 == "n"):
                        return True
        if tile == "rq" or tile == "bq":
            if (x - 1 >= 0):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x - 1][y - 1]
                    if(tile2 == "n"):
                        return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x - 1][y + 1]
                    if(tile2 == "n"):
                        return True
            if (x + 1 <= 7):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x + 1][y - 1]
                    if(tile2 == "n"):
                        return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x + 1][y + 1]
                    if(tile2 == "n"):
                        return True
        return False
    
    def checkForCompulsoryMovesAtCoords(self, x, y):
        tile = self.checkers[x][y]
        if tile == "r":
            if (x - 1 >= 0):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x - 1][y - 1]
                    if(tile2 == "b" or tile2 == 'bq'):
                        if (x - 2 >= 0):
                            if (y - 2 >= 0):
                                tile3 = self.checkers[x - 2][y - 2]
                                if(tile3 == "n"):
                                    return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x - 1][y + 1]
                    if(tile2 == "b" or tile2 == 'bq'):
                        if (x - 2 >= 0):
                            if (y + 2 <= 7):
                                tile3 = self.checkers[x - 2][y + 2]
                                if(tile3 == "n"):
                                    return True
        if tile == "b":
            if (x + 1 <= 7):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x + 1][y - 1]
                    if(tile2 == "r" or tile2 == 'rq'):
                        if (x + 2 <= 7):
                            if (y - 2 >= 0):
                                tile3 = self.checkers[x + 2][y - 2]
                                if(tile3 == "n"):
                                    return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x + 1][y + 1]
                    if(tile2 == "r" or tile2 == 'rq'):
                        if (x + 2 <= 7):
                            if (y + 2 <= 7):
                                tile3 = self.checkers[x + 2][y + 2]
                                if(tile3 == "n"):
                                    return True
        if tile == "rq":
            if (x - 1 >= 0):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x - 1][y - 1]
                    if(tile2 == "b" or tile2 == 'bq'):
                        if (x - 2 >= 0):
                            if (y - 2 >= 0):
                                tile3 = self.checkers[x - 2][y - 2]
                                if(tile3 == "n"):
                                    return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x - 1][y + 1]
                    if(tile2 == "b" or tile2 == 'bq'):
                        if (x - 2 >= 0):
                            if (y + 2 <= 7):
                                tile3 = self.checkers[x - 2][y + 2]
                                if(tile3 == "n"):
                                    return True
            if (x + 1 <= 7):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x + 1][y - 1]
                    if(tile2 == "b" or tile2 == 'bq'):
                        if (x + 2 <= 7):
                            if (y - 2 >= 0):
                                tile3 = self.checkers[x + 2][y - 2]
                                if(tile3 == "n"):
                                    return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x + 1][y + 1]
                    if(tile2 == "b" or tile2 == 'bq'):
                        if (x + 2 <= 7):
                            if (y + 2 <= 7):
                                tile3 = self.checkers[x + 2][y + 2]
                                if(tile3 == "n"):
                                    return True
        if tile == "bq":
            if (x - 1 >= 0):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x - 1][y - 1]
                    if(tile2 == "r" or tile2 == 'rq'):
                        if (x - 2 >= 0):
                            if (y - 2 >= 0):
                                tile3 = self.checkers[x - 2][y - 2]
                                if(tile3 == "n"):
                                    return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x - 1][y + 1]
                    if(tile2 == "r" or tile2 == 'rq'):
                        if (x - 2 >= 0):
                            if (y + 2 <= 7):
                                tile3 = self.checkers[x - 2][y + 2]
                                if(tile3 == "n"):
                                    return True
            if (x + 1 <= 7):
                if (y - 1 >= 0):
                    tile2 = self.checkers[x + 1][y - 1]
                    if(tile2 == "r" or tile2 == 'rq'):
                        if (x + 2 <= 7):
                            if (y - 2 >= 0):
                                tile3 = self.checkers[x + 2][y - 2]
                                if(tile3 == "n"):
                                    return True
                if (y + 1 <= 7):
                    tile2 = self.checkers[x + 1][y + 1]
                    if(tile2 == "r" or tile2 == 'rq'):
                        if (x + 2 <= 7):
                            if (y + 2 <= 7):
                                tile3 = self.checkers[x + 2][y + 2]
                                if(tile3 == "n"):
                                    return True
        return False
            
    def checkForMoves(self):

        self.checkForQueens()

        self.compulsory_tiles = []

        self.last_compulsory_move_red = self.compulsory_moves_red
        self.last_compulsory_move_black = self.compulsory_moves_black

        self.any_moves_available_red = False
        self.any_moves_available_black = False
        self.compulsory_moves_red = False
        self.compulsory_moves_black = False

        break_out = False
        for x in range(0, 8):
            if break_out == True: continue
            for y in range(0, 8):
                if break_out == True: continue
                if (self.checkers[x][y] == 'r' or self.checkers[x][y] == 'rq'):
                    if self.checkForMovesAtCoords(x, y) == True or self.checkForCompulsoryMovesAtCoords(x, y) == True: break_out = True
        if break_out == True:
            self.any_moves_available_red = True
        break_out = False
        for x in range(0, 8):
            if break_out == True: continue
            for y in range(0, 8):
                if break_out == True: continue
                if (self.checkers[x][y] == 'b' or self.checkers[x][y] == 'bq'):
                    if self.checkForMovesAtCoords(x, y) == True or self.checkForCompulsoryMovesAtCoords(x, y) == True: break_out = True
        if break_out == True:
            self.any_moves_available_black = True

        if(self.current_turn == "r" and self.last_compulsory_move_red == True):
            result = self.checkForCompulsoryMovesAtCoords(self.last_move[0], self.last_move[1])
            if result == True:
                self.compulsory_moves_red = True
                self.compulsory_tiles.append([self.last_move[0], self.last_move[1]])
        elif(self.current_turn == "b" and self.last_compulsory_move_black == True):
            result = self.checkForCompulsoryMovesAtCoords(self.last_move[0], self.last_move[1])
            if result == True:
                self.compulsory_moves_black = True
                self.compulsory_tiles.append([self.last_move[0], self.last_move[1]])

        if(self.compulsory_moves_black == False and self.compulsory_moves_red == False):
            if(self.current_turn == "r"):
                break_out = False
                for x in range(0, 8):
                    for y in range(0, 8):
                        if (self.checkers[x][y] == 'b' or self.checkers[x][y] == 'bq') and self.checkForCompulsoryMovesAtCoords(x, y) == True: 
                            break_out = True
                            self.compulsory_tiles.append([x, y])
                if break_out == True:
                    self.compulsory_moves_black = True
            elif(self.current_turn == "b"):
                break_out = False
                for x in range(0, 8):
                    for y in range(0, 8):
                        if (self.checkers[x][y] == 'r' or self.checkers[x][y] == 'rq') and self.checkForCompulsoryMovesAtCoords(x, y) == True:
                            break_out = True
                            self.compulsory_tiles.append([x, y])
                if break_out == True:
                    self.compulsory_moves_red = True
            
        self.checkVictory()
        self.nextTurn()

    def checkVictory(self):
        self.red_pieces = 0
        self.black_pieces = 0
        for x in range(0, 8):
            for y in range(0, 8):
                if self.checkers[x][y][0] == 'r':
                    self.red_pieces += 1
                if self.checkers[x][y][0] == 'b':
                    self.black_pieces += 1
        if(self.red_pieces <= 0 or self.any_moves_available_red == False):
            print(self.id, self.turn_count, "Black was victorious!")
            self.running = False
        elif(self.black_pieces <= 0 or self.any_moves_available_black == False):
            print(self.id, self.turn_count, "Red was victorious!")
            self.running = False

    def nextTurn(self):

        if(self.running == False):
            return

        self.turn_count += 1

        if self.compulsory_moves_red == True:
            print(self.id, self.turn_count, "Red's turn - compulsory take!")
            self.current_turn = "r"
        elif self.compulsory_moves_black == True:
            print(self.id, self.turn_count, "Black's turn - compulsory take!")
            self.current_turn = "b"
        else:
            if self.current_turn == "r":
                self.current_turn = "b"
                print(self.id, self.turn_count, "Black's turn.")
            elif self.current_turn == "b":
                self.current_turn = "r"
                print(self.id, self.turn_count, "Red's turn.")

    def checkForQueens(self):
        for i in range(0, 4):
            if(self.checkers[0][(i * 2) + 1] == "r"):
                self.checkers[0][(i * 2) + 1] = "rq"
            if(self.checkers[7][(i * 2)] == "b"):
                self.checkers[7][(i * 2)] = "bq"
    
    def makeMove(self, x, y, x2, y2, type):

        self.ignore_compulsory_tile = [-1, -1]

        if type == -1:
            return
        if type == 0 and ((self.compulsory_moves_black == True and self.current_turn == "b") or (self.compulsory_moves_red == True and self.current_turn == "r")):
            return
        elif type == 0:
            self.checkers[x][y] = "n"
            self.checkers[x2][y2] = self.move_color
        elif type == 1:
            self.checkers[x + 1][y - 1] = "n"
        elif type == 2:
            self.checkers[x + 1][y + 1] = "n"
        elif type == 3:
            self.checkers[x - 1][y - 1] = "n"
        elif type == 4:
            self.checkers[x - 1][y + 1] = "n"
        
        self.last_move = [x2, y2]

        if(type >= 1 and type <= 4):
            self.checkers[x][y] = "n"
            self.checkers[x2][y2] = self.move_color

        self.current_selection = 0
        self.selected_grid = [[-1, -1], [-1, -1]]
        self.allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
        self.allow_grid_type = [-1, -1, -1, -1]
        
        # self.checkForMoves()
        return True

    def updateSelection(self, x, y):

        if(self.running == False):
            return False

        if(x >= 0 and y >= 0 and x <= 7 and y <= 7 and (x + y) % 2 == 1):

            if(self.current_selection == 1 and self.checkers[x][y] != "n"):
                self.current_selection = 0
                self.allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]

            self.selected_grid[self.current_selection] = [x, y]

            if((self.current_selection == 0 and self.checkers[x][y][0] != self.current_turn) or (self.current_selection == 1 and self.checkers[self.selected_grid[0][0]][self.selected_grid[0][1]][0] != self.current_turn)):
                self.current_selection = 0
                self.selected_grid = [[-1, -1], [-1, -1]]
                self.allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
                self.allow_grid_type = [-1, -1, -1, -1]
                return False

            if(self.current_selection == 1):
                for i in range(0, 4):
                    if(self.allow_grid[i] == [x, y]):
                        return self.makeMove(self.selected_grid[0][0], self.selected_grid[0][1], self.selected_grid[1][0], self.selected_grid[1][1], self.allow_grid_type[i])
                    
            if(self.checkers[x][y] == "b"):
                self.move_color = "b"
                if(x + 1 <= 7 and y - 1 >= 0 and self.checkers[x + 1][y - 1] == "n"):
                    self.allow_grid[0] = [x + 1, y - 1]
                    self.allow_grid_type[0] = 0
                elif(x + 2 <= 7 and y - 2 >= 0 and self.checkers[x + 1][y - 1][0] == "r" and self.checkers[x + 2][y - 2] == "n"):
                    self.allow_grid[0] = [x + 2, y - 2]
                    self.allow_grid_type[0] = 1
                if(x + 1 <= 7 and y + 1 <= 7 and self.checkers[x + 1][y + 1] == "n"):
                    self.allow_grid[1] = [x + 1, y + 1]
                    self.allow_grid_type[1] = 0
                elif(x + 2 <= 7 and y + 2 <= 7 and self.checkers[x + 1][y + 1][0] == "r"  and self.checkers[x + 2][y + 2] == "n"):
                    self.allow_grid[1] = [x + 2, y + 2]
                    self.allow_grid_type[1] = 2
                self.allow_grid[2] = [-1, -1]
                self.allow_grid_type[2] = -1
                self.allow_grid[3] = [-1, -1]
                self.allow_grid_type[2] = -1

            elif(self.checkers[x][y] == "r"):
                self.move_color = "r"
                if(x - 1 >= 0 and y - 1 >= 0 and self.checkers[x - 1][y - 1] == "n"):
                    self.allow_grid[0] = [x - 1, y - 1]
                    self.allow_grid_type[0] = 0
                elif(x - 2 >= 0 and y - 2 >= 0 and self.checkers[x - 1][y - 1][0] == "b" and self.checkers[x - 2][y - 2] == "n"):
                    self.allow_grid[0] = [x - 2, y - 2]
                    self.allow_grid_type[0] = 3
                if(x - 1 >= 0 and y + 1 <= 7 and self.checkers[x - 1][y + 1] == "n"):
                    self.allow_grid[1] = [x - 1, y + 1]
                    self.allow_grid_type[1] = 0
                elif(x - 2 >= 0 and y + 2 <= 7 and self.checkers[x - 1][y + 1][0] == "b" and self.checkers[x - 2][y + 2] == "n"):
                    self.allow_grid[1] = [x - 2, y + 2]
                    self.allow_grid_type[1] = 4
                self.allow_grid[2] = [-1, -1]
                self.allow_grid_type[2] = -1
                self.allow_grid[3] = [-1, -1]
                self.allow_grid_type[2] = -1
            
            elif(self.checkers[x][y] == "rq"):
                self.move_color = "rq"
                if(x - 1 >= 0 and y - 1 >= 0 and self.checkers[x - 1][y - 1] == "n"):
                    self.allow_grid[0] = [x - 1, y - 1]
                    self.allow_grid_type[0] = 0
                elif(x - 2 >= 0 and y - 2 >= 0 and self.checkers[x - 1][y - 1][0] == "b" and self.checkers[x - 2][y - 2] == "n"):
                    self.allow_grid[0] = [x - 2, y - 2]
                    self.allow_grid_type[0] = 3
                if(x - 1 >= 0 and y + 1 <= 7 and self.checkers[x - 1][y + 1] == "n"):
                    self.allow_grid[1] = [x - 1, y + 1]
                    self.allow_grid_type[1] = 0
                elif(x - 2 >= 0 and y + 2 <= 7 and self.checkers[x - 1][y + 1][0] == "b" and self.checkers[x - 2][y + 2] == "n"):
                    self.allow_grid[1] = [x - 2, y + 2]
                    self.allow_grid_type[1] = 4
                if(x + 1 <= 7 and y - 1 >= 0 and self.checkers[x + 1][y - 1] == "n"):
                    self.allow_grid[2] = [x + 1, y - 1]
                    self.allow_grid_type[2] = 0
                elif(x + 2 <= 7 and y - 2 >= 0 and self.checkers[x + 1][y - 1][0] == "b" and self.checkers[x + 2][y - 2] == "n"):
                    self.allow_grid[2] = [x + 2, y - 2]
                    self.allow_grid_type[2] = 1
                if(x + 1 <= 7 and y + 1 <= 7 and self.checkers[x + 1][y + 1] == "n"):
                    self.allow_grid[3] = [x + 1, y + 1]
                    self.allow_grid_type[3] = 0
                elif(x + 2 <= 7 and y + 2 <= 7 and self.checkers[x + 1][y + 1][0] == "b" and self.checkers[x + 2][y + 2] == "n"):
                    self.allow_grid[3] = [x + 2, y + 2]
                    self.allow_grid_type[3] = 2
            
            elif(self.checkers[x][y] == "bq"):
                self.move_color = "bq"
                if(x - 1 >= 0 and y - 1 >= 0 and self.checkers[x - 1][y - 1] == "n"):
                    self.allow_grid[0] = [x - 1, y - 1]
                    self.allow_grid_type[0] = 0
                elif(x - 2 >= 0 and y - 2 >= 0 and self.checkers[x - 1][y - 1][0] == "r" and self.checkers[x - 2][y - 2] == "n"):
                    self.allow_grid[0] = [x - 2, y - 2]
                    self.allow_grid_type[0] = 3
                if(x - 1 >= 0 and y + 1 <= 7 and self.checkers[x - 1][y + 1] == "n"):
                    self.allow_grid[1] = [x - 1, y + 1]
                    self.allow_grid_type[1] = 0
                elif(x - 2 >= 0 and y + 2 <= 7 and self.checkers[x - 1][y + 1][0] == "r" and self.checkers[x - 2][y + 2] == "n"):
                    self.allow_grid[1] = [x - 2, y + 2]
                    self.allow_grid_type[1] = 4
                if(x + 1 <= 7 and y - 1 >= 0 and self.checkers[x + 1][y - 1] == "n"):
                    self.allow_grid[2] = [x + 1, y - 1]
                    self.allow_grid_type[2] = 0
                elif(x + 2 <= 7 and y - 2 >= 0 and self.checkers[x + 1][y - 1][0] == "r" and self.checkers[x + 2][y - 2] == "n"):
                    self.allow_grid[2] = [x + 2, y - 2]
                    self.allow_grid_type[2] = 1
                if(x + 1 <= 7 and y + 1 <= 7 and self.checkers[x + 1][y + 1] == "n"):
                    self.allow_grid[3] = [x + 1, y + 1]
                    self.allow_grid_type[3] = 0
                elif(x + 2 <= 7 and y + 2 <= 7 and self.checkers[x + 1][y + 1][0] == "r" and self.checkers[x + 2][y + 2] == "n"):
                    self.allow_grid[3] = [x + 2, y + 2]
                    self.allow_grid_type[3] = 2
            
            if(self.current_selection == 0):
                self.current_selection = 1
            else:
                self.selected_grid = [[-1, -1], [-1, -1]]
                self.current_selection = 0
            self.changed = 0
        else:
            self.current_selection = 0
            self.selected_grid = [[-1, -1], [-1, -1]]
            self.allow_grid = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
            self.allow_grid_type = [-1, -1, -1, -1]

        self.changed = 0
        return False