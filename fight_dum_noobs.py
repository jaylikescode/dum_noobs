import time
import random
import os

inventory = {}

def shop():
    global inventory
    print("choose any one of these: \n sword \n armor \n potion \n helper")
    type = input("Enter the thing you want: ")
    if type == "sword":
        types_av = {"level 1" : "wooden sword",
                    "level 2" : "iron sword",
                    "level 3" : "celestial bronze sword",
                    "level 4" : "magic sword",
                    "MAX" : "black hole summoner sword"}
        print(types_av)
    elif type == "armor":
        types_av = {"level 1" : "wooden armor",
                    "level 2" : "iron armor",
                    "level 3" : "celestial bronze armor",
                    "level 4" : "magic armor",
                    "MAX" : "quantum armor"}
    elif type == "potion":
        types_av = {"level 1" : "health potion",
                    "level 2" : "speed potion",
                    "level 3" : "poison potion",
                    "level 4" : "destruction potion",
                    "MAX" : "ultra stength potion"}
    elif type == "helper":
        types_av = {"level 1" : "rat",
                    "level 2" : "cat",
                    "level 3" : "cyborg dog",
                    "level 4" : "pheonix",
                    "MAX" : "dragon"}

def get_insane_chest():
    gold = random.ranint(200, 1000)
    return gold

def get_dum_chest():
    gold = random.randint(1, 5)
    return gold

def hit_a_noob():
    weapon = input("Enter your weapon: ")
    time.sleep(0.5)

def game_loop():
    thing_to_do = input("Welcome to the satisfication game of battling dumb noobs. What do you want to do? \n battle,(1) \nbuy stuff(shop)(2), \n or rage-quit before you start playing?(3) ")

    if thing_to_do == "3":
        print("Okay.")
        time.sleep(2)
        print("That is fine.")
        time.sleep(1)
        print("you will rage-quit in...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("You rage-quitted. You lost.Maybe if you didn't, you could have won against noobs. ")
        os.abort
    elif thing_to_do == "2":
        print("entering shop...")
        time.sleep(1)
        print("succesfully entered shop!")
        shop()
game_loop()