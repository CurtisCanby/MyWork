from stockfish import Stockfish
import chess
engine = Stockfish("C:\\Users\\16812\\OneDrive\\Desktop\\stockfish\\stockfish-windows-x86-64-avx2.exe")

# PART 1 MAKE THE RAW DATA FROM STOCKFISH EVALUATIONS

def generate_dataset(num_games=1):
    """Generates a dataset of chess positions with Stockfish evaluations."""
    dataset = []
    for _ in range(num_games):
        board = chess.Board()
        while not board.is_game_over():
            engine.set_fen_position(board.fen())
            best_move = engine.get_best_move()
            evaluation = engine.get_evaluation()
            # Store data in dataset
            if best_move and evaluation:
                dataset.append({
                    "FEN": board.fen(),
                    "Best Move": best_move,
                    "Evaluation": evaluation["value"]
                })
            board.push(chess.Move.from_uci(best_move))
    return dataset

print("Generating Data...")
chess_data = generate_dataset()
print("Finished generating")

# PART TWO: MAKE THE DATA USEFUL AND TRAIN MODEL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

def fen_to_vector(fen):
    board = chess.Board(fen)
    vector = np.zeros(64, dtype=np.float32)
    for square, piece in board.piece_map().items():
        vector[square] = piece.piece_type
    return vector

dataset = chess_data
X = np.array([fen_to_vector(entry["FEN"]) for entry in dataset])
y = np.array([entry["Evaluation"] for entry in dataset])
model = keras.Sequential([
    layers.Dense(64, activation="relu", input_shape=(len(X[0]),)),
    layers.Dense(32, activation="relu"),
    layers.Dense(1, activation="linear")
])
model.compile(optimizer="adam", loss="mse", metrics=["mae"])
print("Training model...")
model.fit(X, y, epochs=10, batch_size=16)

# PART 3: PREDICT AND COMPARE!
import random

def generate_random_fen():
    board = chess.Board()
    for _ in range(random.randint(10, 40)):
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            break
        move = random.choice(legal_moves)
        board.push(move)

    return board.fen()

random_fen = generate_random_fen()
print("Random FEN:", random_fen)

for i in range(1,10):
    test_vector = fen_to_vector(random_fen).reshape(1, -1)
    predicted_eval = model.predict(test_vector)
    print(f"My AI Evaluation: {predicted_eval[0][0]}")
engine.set_fen_position(random_fen)
# Get Stockfish's evaluation
stockfish_eval = engine.get_evaluation()
eval_value = stockfish_eval.get("value", "N/A")
print(f"Stockfish Evaluation: {eval_value}")