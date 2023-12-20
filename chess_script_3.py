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
"""
Game Manager:
- Manages that the Players (robots or humans) are able to make Moves, 
- Checks the Moves for Legality
- Handels The Initialization of Code (e.g. The Bots, The Graphics)
"""

"""
Libarys
"""
import numpy as np  
import pygame as pg

class Game_Manager():
    def __init__(self) -> None:
        """
        Game rules setup
        """
        player_to_move = 'white'
        main_loop = True
        game_loop = True
        two_player_game = True
        whites_move = True
        visual_mode = True

        
        """
        This Makes a Empty Board (8x8 array)
        and assigns it to the Constant EMPTY_BOARD
        """
        def mk_empty_board() -> np.ndarray:
            print(2)
            board = []
            col = []
            for i in range(8):
                col.append(0)
            for i in range(8):
                board.append(col)
            board = np.array(board)
            return board
        print(1)
        EMTPTY_BOARD  = mk_empty_board() 
        print(3)

        """
        Visuals setup
        """
        
        if visual_mode:
            pg.init()
            height = 1000
            width = 1000
            visual = pg.display.set_mode((width,height))
            pg.display.set_caption("Chess")
            snake_icon = pg.image.load("F:\Coden\python\chess\logo.png")
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
            pg.display.set_icon(snake_icon)
            green = (0,255,0)
            black = (0,0,0)
            blue = (0,0,255)
            white = (255,255,255)
            dark_gray = (61,61,61)
            light_yellow = (199, 186, 111)

            

    """
    This Makes a Empty Board (8x8 array)
    """
    def give_empty_board() -> np.ndarray:
        return EMTPTY_BOARD
    
    def reset_board():
        
        def populate_board():
            global board
            
            #PAWNS

            for i in board:
            #black
                i[1] = -1
            #white
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
        print("hi")

a = Game_Manager
a.__init__(a)
print(a.give_empty_board())