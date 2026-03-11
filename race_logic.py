import os
from time import sleep
from random import randint

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    for row in road:
        for tile in row:
            print(f"{tile:^2}", end="")
        print()
    random_tile = randint(0, 4)
    new_road = ["[]", "[]", "[]", "[]", "[]"]
    new_road[random_tile] = '11'
    road.insert(0, new_road)
    road.pop(7)
    road[6][position] = 'oo'
    sleep(1)
    clear_console()


