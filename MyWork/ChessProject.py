import chess

def evaluate_board(board):
  piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
  score = 0
  for square, piece in board.piece_map().items():
    if piece.color == chess.WHITE:
        score += piece_values[piece.piece_type]
    else:
        score -= piece_values[piece.piece_type]
  return score

def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
      return evaluate_board(board)
    if maximizing_player:
      max_eval = -float("inf")
      for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, False)
        board.pop()
        max_eval = max(max_eval, eval)
      return max_eval
    else:
      min_eval = float("inf")
      for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, True)
        board.pop()
        min_eval = min(min_eval, eval)
      return min_eval

def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    if maximizing_player:
        max_eval = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def getbestmove(board, depth):
  best_move = None
  if board.turn == chess.WHITE:
      best_value = -float("inf")
      for move in board.legal_moves:
          board.push(move)
          board_value = minimax_alpha_beta(board, depth - 1, -float("inf"), float("inf"), False)
          board.pop()
          if board_value > best_value:
              best_value = board_value
              best_move = move
  else:
      best_value = float("inf")
      for move in board.legal_moves:
          board.push(move)
          board_value = minimax_alpha_beta(board, depth - 1, -float("inf"), float("inf"), True)
          board.pop()
          if board_value < best_value:
              best_value = board_value
              best_move = move
  return best_move

def playgame(board,depth):
  while not board.is_game_over():
    if board.turn == chess.WHITE:
      move = input("Enter your move (e.g. e2e4): ")
      board.push_uci(move)
      print(board)
      print("---")
    else:
      botmove = getbestmove(board,depth)
      board.push(botmove)
      print("The Bot played " + str(botmove))
      print(board)
      print("---")
  print("Game Over!")  

board = chess.Board()
playgame(board,4)