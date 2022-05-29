from stockfish import Stockfish
def stockfish_help(data,depth):
    stockfish = Stockfish(path="users/stockfish/stockfish_14.1_win_x64_avx2.exe", depth=depth)
    #stockfish.set_position(["e2e4", "e7e6"])
    #stockfish.set_position(data)
    stockfish.set_fen_position(data)
    a=stockfish.get_best_move()
    print(a)
    return a

print("Working:")
    


    
