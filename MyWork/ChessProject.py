import chess
import chess.engine
import random

engine = chess.engine.SimpleEngine.popen_uci("PATH TO STOCKFISH") # I NEED TO GET THE STOCKFISH ENGINE AND PUT THE PATH HERE
games = []

def generate_game(engine, min_elo, max_elo, max_moves):
  board = chess.Board()
  engine.configure({"Skill Level": random.randint(min_elo, max_elo)})

  moves = []
  while not board.is_game_over() and len(moves) < max_moves:
    result = engine.play(board, chess.engine.Limit(time=0.1))
    moves.append(result.move)
    board.push(result.move)

  return moves

for i in range(10000):
  moves = generate_game(engine, 1000, 2000, 150) 
  games.append(moves)

engine.quit()
# NOW THERE IS A GAMES LIST THAT IS FULL OF DATA!!!
# WITH THIS DATA WE WANT TO TRAIN AN ENGINE
# BUT AI CANT READ CHESS FEN NOTATION. ENCODE ALL THE MOVES INTO UNIQUE INTEGER IDs!
