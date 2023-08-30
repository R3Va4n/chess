"""
CHESS
How it works:
board is the currend state of the game in a 2 dimensional List
every piece has a value assinged, black uses the same numbers just negative:
            White   Black 
pawn:         1       -1
knight:       2       -2
bishop:       3       -3
rook:         4       -4
queen:        5       -5
king:         6       -6
"""
import pygame as pg
pg.init()
height = 1000
width = 1000
visual = pg.display.set_mode((width,height))
pg.display.set_caption("Chess")
snake_icon = pg.image.load("F:\Coden\python\chess\logo.png")
pg.display.set_icon(snake_icon)
pawn_pic_w = pg.image.load("F:\Coden\python\chess\pawn_w.png")
pawn_pic_b = pg.image.load("F:\Coden\python\chess\pawn_b.png")
rook_pic_w = pg.image.load("F:/Coden/python/chess/rook_w.png")
rook_pic_b = pg.image.load("F:/Coden/python/chess/rook_b.png")
knight_pic_w = pg.image.load("F:/Coden/python/chess/knight_w.png")
knight_pic_b = pg.image.load("F:/Coden/python/chess/knight_b.png")
bishop_pic_w = pg.image.load("F:/Coden/python/chess/bishop_w.png")
bishop_pic_b = pg.image.load("F:/Coden/python/chess/bishop_b.png")
king_pic_w = pg.image.load("F:/Coden/python/chess/king_w.png")
king_pic_b = pg.image.load("F:/Coden/python/chess/king_b.png")
queen_pic_w = pg.image.load("F:/Coden/python/chess/queen_w.png")
queen_pic_b = pg.image.load("F:/Coden/python/chess/queen_b.png")
import numpy as np  
player_to_move = 'white'
main_loop = True
green = (0,255,0)
black = (0,0,0)
blue = (0,0,255)
white = (255,255,255)
dark_gray = (61,61,61)
light_yellow =(199, 186, 111)
click_loked = False

def even(number):    #checks if number is even or odd using the remainder function. if the remainder is 0 after a division by two, the number is even. 
    if (number % 2)  == 0:
        out = True
    else:
        out = False
    return out

def reset_board():
    def mk_board():
        global board
        board = []
        a = []
        for i in range(8):
            a.append(0)
        for i in range(8):
            board.append(a)
        board = np.array(board)
    def populate_board():
        global board
        
        #PAWNS
        #black
        for i in board:
            i[1] = -1
        #white
        for i in board:
            i[6] = 1
        
        #ROOKS
        #black
        board[0][0] = -4
        board[7][0] = -4
        #white
        board[0][7] = 4
        board[7][7] = 4

        #KNIGHTS
        #black
        board[1][0] = -2
        board[6][0] = -2
        #white
        board[1][7] = 2
        board[6][7] = 2

        #BISHOPS
        #black
        board[2][0] = -3
        board[5][0] = -3
        #white
        board[2][7] = 3
        board[5][7] = 3

        #QUEEN
        #black
        board[3][0] = -5
        #white
        board[3][7] = 5

        #KING
        #black
        board[4][0] = -6
        #white
        board[4][7] = 6
    mk_board()
    populate_board()

def func_visual():
    visual.fill(black)
    coord_squares_x = 0
    coord_squares_y = 0
    for x in range(4):                      #drawing the bord
        for y in range(4):
            chess_rect  = pg.Rect(coord_squares_x,coord_squares_y,100,100)
            pg.draw.rect(visual,light_yellow,chess_rect)
            coord_squares_y += 100
            chess_rect  = pg.Rect(coord_squares_x,coord_squares_y,100,100)
            pg.draw.rect(visual,dark_gray,chess_rect)
            coord_squares_y += 100
        coord_squares_x += 100
        coord_squares_y = 0
        for y in range(4):
            chess_rect  = pg.Rect(coord_squares_x,coord_squares_y,100,100)
            pg.draw.rect(visual,dark_gray,chess_rect)
            coord_squares_y += 100
            chess_rect  = pg.Rect(coord_squares_x,coord_squares_y,100,100)
            pg.draw.rect(visual,light_yellow,chess_rect)
            coord_squares_y += 100   
        coord_squares_x += 100
        coord_squares_y = 0
    current_x = 0                               #drawing the pieces
    current_y = 0
    for x in board: 
        for y in x:
            if y == -1:
                visual.blit(pawn_pic_b,(current_x,current_y))
            if y == 1:
                visual.blit(pawn_pic_w,(current_x,current_y))
            if y == -4:
                visual.blit(rook_pic_b,(current_x,current_y))
            if y == 4:
                visual.blit(rook_pic_w,(current_x,current_y))
            if y == -2:
                visual.blit(knight_pic_b,(current_x,current_y))
            if y == 2:
                visual.blit(knight_pic_w,(current_x,current_y))
            if y == -3:
                visual.blit(bishop_pic_b,(current_x,current_y))
            if y == 3:
                visual.blit(bishop_pic_w,(current_x,current_y))
            if y == -6:
                visual.blit(king_pic_b,(current_x,current_y))
            if y == 6:
                visual.blit(king_pic_w,(current_x,current_y))
            if y == -5:
                visual.blit(queen_pic_b,(current_x,current_y))
            if y == 5:
                visual.blit(queen_pic_w,(current_x,current_y))
            current_y += 100
        current_y = 0
        current_x += 100
    pg.display.update()

def player_input():
    global click_loked
    global picked_piece
    global picked_piece_x
    global picked_piece_y
    global main_loop
    has_output = False
    pos = pg.mouse.get_pos()
    picked_piece_x_raw = pos[0]
    picked_piece_y_raw = pos[1]
    for event in pg.event.get():
        if event.type == pg.QUIT:
            main_loop = False

        # player clicked on piece, getting piece
        if event.type == pg.MOUSEBUTTONDOWN:
            #print("down")
            if click_loked == False:
                piece_out_of_bounds = False
                if picked_piece_x_raw < 0: #checking for upper out of bounds
                    piece_out_of_bounds = True
                elif picked_piece_x_raw <= 100:
                    picked_piece_x = 0
                elif picked_piece_x_raw <= 200:
                    picked_piece_x = 1
                elif picked_piece_x_raw <= 300:
                    picked_piece_x = 2
                elif picked_piece_x_raw <= 400:
                    picked_piece_x = 3
                elif picked_piece_x_raw <= 500:
                    picked_piece_x = 4
                elif picked_piece_x_raw <= 600:
                    picked_piece_x = 5
                elif picked_piece_x_raw <= 700:
                    picked_piece_x = 6
                elif picked_piece_x_raw <= 800:
                    picked_piece_x = 7
                elif picked_piece_x_raw <= 800:
                    picked_piece_x = 8
                else:
                    piece_out_of_bounds = True #checking for lower out of bounds
                if picked_piece_y_raw < 0: #checking for left out of bounds
                    piece_out_of_bounds = True
                if picked_piece_y_raw <= 100:
                    picked_piece_y = 0
                elif picked_piece_y_raw <= 200:
                    picked_piece_y = 1
                elif picked_piece_y_raw <= 300:
                    picked_piece_y = 2
                elif picked_piece_y_raw <= 400:
                    picked_piece_y = 3
                elif picked_piece_y_raw <= 500:
                    picked_piece_y = 4
                elif picked_piece_y_raw <= 600:
                    picked_piece_y = 5
                elif picked_piece_y_raw <= 700:
                    picked_piece_y = 6
                elif picked_piece_y_raw <= 800:
                    picked_piece_y = 7
                elif picked_piece_y_raw <= 800:
                    picked_piece_y = 8
                else:
                    piece_out_of_bounds = True #checking for right out of bounds
            
                if piece_out_of_bounds == False:
                    picked_piece = board[picked_piece_x][picked_piece_y]
                    print (picked_piece)
                    click_loked = True

        # player clicked on place, getting place
        if event.type == pg.MOUSEBUTTONUP:
                #print("up")
                click_loked = False
                place_out_of_bounds = False
                picked_place_x_raw = pos[0]
                picked_place_y_raw = pos[1]
                if picked_place_x_raw <= 100:
                    picked_place_x = 0
                elif picked_place_x_raw <= 200:
                    picked_place_x = 1
                elif picked_place_x_raw <= 300:
                    picked_place_x = 2
                elif picked_place_x_raw <= 400:
                    picked_place_x = 3
                elif picked_place_x_raw <= 500:
                    picked_place_x = 4
                elif picked_place_x_raw <= 600:
                    picked_place_x = 5
                elif picked_place_x_raw <= 700:
                    picked_place_x = 6
                elif picked_place_x_raw <= 800:
                    picked_place_x = 7
                elif picked_place_x_raw <= 800:
                    picked_place_x = 8
                else:
                    place_out_of_bounds = True

                if picked_place_y_raw <= 100:
                    picked_place_y = 0
                elif picked_place_y_raw <= 200:
                    picked_place_y = 1
                elif picked_place_y_raw <= 300:
                    picked_place_y = 2
                elif picked_place_y_raw <= 400:
                    picked_place_y = 3
                elif picked_place_y_raw <= 500:
                    picked_place_y = 4
                elif picked_place_y_raw <= 600:
                    picked_place_y = 5
                elif picked_place_y_raw <= 700:
                    picked_place_y = 6
                elif picked_place_y_raw <= 800:
                    picked_place_y = 7
                elif picked_place_y_raw <= 800:
                    picked_place_y = 8
                else:
                    place_out_of_bounds = True

                if place_out_of_bounds:
                    picked_piece = 0
                    picked_place = 0

                else:
                    picked_place = (picked_place_x,picked_place_y)
                    has_output = True

                print((has_output, picked_piece, picked_place))
                return (has_output, picked_piece, picked_place)

def make_move(picked_piece,picked_place):
    print(board)
    if picked_piece != 0: #0 is no piece taken
        #TODO: implement move rules
        board[picked_place[0]][picked_place[1]] = picked_piece
    print(board)



"""
There is a basic rule of thumb to (roughly) evaluate a bord only on piece worth:
pawns count as one, knights and bishops as three, rooks as four, and the queen as seven, the king is not counted.
you do the evaluation by adding up all of your own pieces and subtract the enemys pieces of that total.
The func will alway evaluate in the eyes of white. Checks/mates arent used in the evaluation.
"""
def evaluate_on_piece_worth():
    total = 0        # total eval (the number)
    for i in board:  # loop through board
        for j in i:
            if j == 2:      # knights value is 3 but ist already taken by bishops, they have 2
                total += 3
            elif j == -2:
                total += -3
            elif j == 5:    #didnt like gaps in the nubering, so queen got 5 istead of 7
                total += 7
            elif j == -5:
                total += -7
            elif j == 6 or -6: # dont want kings make any problems with the eval
                pass
            else:
                total +=j
    return total


reset_board()
while main_loop:

    
    has_out = False
    while not has_out:
        print("2")
        has_out, piece, place = player_input()
    make_move(piece, place) # take a player input

    func_visual()
    print 
 