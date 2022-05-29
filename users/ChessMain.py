from users import ChessAI
from users import ChessEngine


def predictMove(gameState, player):
    game_state = ChessEngine.GameState()
    game_state.board = gameState


    if player == "white":
        game_state.white_to_move = True
    else:
        game_state.white_to_move = False

    for i in range(len(game_state.board)):
        for j in range(len(game_state.board[i])):
            if game_state.board[i][j] == "wK":
                game_state.white_king_location = (i, j)
            if game_state.board[i][j] == "bK":
                game_state.black_king_location = (i, j)

    valid_moves = game_state.getValidMoves()

    ai_move = ChessAI.findBestMove(game_state, valid_moves)
    if ai_move is None:
        ai_move = ChessAI.findRandomMove(valid_moves)
    game_state.makeMove(ai_move)
    moveLog = game_state.move_log
    text = moveLog[-1].getChessNotation()
    
    return text
