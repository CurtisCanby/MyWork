import random

def get_monster_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, monster):
    if player == monster:
        return "tie"
    elif (player == "rock" and monster == "scissors") or \
         (player == "paper" and monster == "rock") or \
         (player == "scissors" and monster == "paper"):
        return "win"
    else:
        return "lose"

def play_room(room_number):
    print(f"\nEntering Room {room_number}...")
    monster_choice = get_monster_choice()
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        return play_room(room_number)

    print(f"Monster chose: {monster_choice}")
    result = determine_winner(player_choice, monster_choice)

    if result == "win":
        print("You defeated the monster! Moving to the next room.")
        return True
    elif result == "tie":
        print("It's a tie! Try again.")
        return play_room(room_number)
    else:
        print("You lost! Try again.")
        return play_room(room_number)

def start_game():
    print("Welcome to the Dungeon!")
    for room in range(1, 6):
        if not play_room(room):
            break
    print("Congratulations! You conquered all 5 rooms!")

start_game()
