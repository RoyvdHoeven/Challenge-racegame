import json
import os
import time

from race_logic import start_race

GAME_FILE = "players.json"


def load_players():
    if os.path.exists(GAME_FILE):
        with open(GAME_FILE, "r") as file:
            return json.load(file)
    else:
        return {}


def save_players(players):
    with open(GAME_FILE, "w") as file:
        json.dump(players, file, indent=4)


def start_screen():
    print("╔═══════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                               ║")
    print("║                        WELCOME TO ⚡ [Terminal Racer] ⚡                        ║")
    print("║                                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════╝")
    time.sleep(1)


def create_player(players):
    print("\n\n=== Create new player ===")
    gamertag = input("Enter your name: ").strip()

    if gamertag in players:
        print("This gamertag already exists!")
        time.sleep(1)
        return players

    players[gamertag] = {
        "car_model": "Standard",
        "car_color": "Silver"
    }

    save_players(players)
    print(f"Player '{gamertag}' created!")
    time.sleep(1)
    return players


def customize_car(players):
    print("\n\n=== Car Customs ===")

    if not players:
        print("Create a player first!")
        time.sleep(2)
        return players

    print("Available players:")
    for name in players:
        print("- ", name)

    chosen = input("Choose a player: ").strip()
    if chosen not in players:
        print("Player not found.")
        time.sleep(1)
        return players

    models = ["Sport", "Muscle", "SUV", "Classic"]
    print("\nChoose a model:")
    for num, model in enumerate(models, 1):
        print(f"{num}. {model}")
    model_choice = int(input("Model number: "))
    players[chosen]["car_model"] = models[model_choice - 1]

    colors = ["Red", "Blue", "Black", "Wit", "Yellow", "Green"]
    print("\nChoose a color:")
    for num, color in enumerate(colors, 1):
        print(f"{num}. {color}")
    color_choice = int(input("Color number: "))
    players[chosen]["car_color"] = colors[color_choice - 1]

    save_players(players)
    print(f"\nCar of {chosen} customized!")
    time.sleep(1)
    return players


def main_menu():
    players = load_players()

    while True:
        print("\n\n=== STARTMENU ===")
        print("1. Create a new player")
        print("2. Car customizer")
        print("3. Play")
        print("4. Quit")

        choice = input("\nMake a choice: ")

        if choice == "1":
            players = create_player(players)
        elif choice == "2":
            players = customize_car(players)
        elif choice == "3":
            print("\n\nStarting Game...")
            time.sleep(1)
            start_race()
        elif choice == "4":
            print("\n\nGoodbye!")
            break
        else:
            print("\n\nInvalid Choice, try again...")
            time.sleep(2)


start_screen()
main_menu()
