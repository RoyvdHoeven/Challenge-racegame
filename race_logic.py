import os
import keyboard
from time import sleep
from random import randint

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_race():
    # default_road = ["[]", "[]", "[]", "[]", "[]"]
    road = [
        ["[]", "[]", "[]", "[]", "[]"],
        ["[]", "[]", "[]", "[]", "[]"],
        ["[]", "[]", "[]", "[]", "[]"],
        ["[]", "[]", "[]", "[]", "[]"],
        ["[]", "[]", "[]", "[]", "[]"],
        ["[]", "[]", "[]", "[]", "[]"],
        ["[]", "[]", "oo", "[]", "[]"]
    ]

    position = 2

    while True:
        clear_console()

        for row in road:
            for tile in row:
                print(f"{tile:^2}", end="")
            print()
        new_road = ["[]", "[]", "[]", "[]", "[]"]
        # check if obstacle will be placed
        rng = randint(1, 100)
        if rng >= 30 and rng <= 40:
            random_tile = randint(0, 4)
            new_road[random_tile] = '11'
        road.insert(0, new_road)
        road.pop(7)
        count = 0
        pressed = False
        # Listen for input for 0.5 seconds
        while count < 10:
            if keyboard.is_pressed('a') or keyboard.is_pressed('left') and not pressed:
                position -= 1 if not position == 0 else 0
                pressed = True
            if keyboard.is_pressed('d') or keyboard.is_pressed('right') and not pressed:
                position += 1 if not position == 4 else 0
                pressed = True
            sleep(0.05)
            count += 1
        if road[6][position] == '11':
            break
        else:
            road[6][position] = 'oo'
        clear_console()