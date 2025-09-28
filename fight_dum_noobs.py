import time
import random
import os

inventory = {}


def shop():
    global inventory
    print("choose any one of these: \n sword \n armor \n potion \n helper")
    
    shop_not_valid = True
    
    while shop_not_valid:
        type = input("Enter the thing you want: ")
        if type == "sword":
            types_av = {"level 1" : "wooden sword (10)",
                        "level 2" : "iron sword (20)",
                        "level 3" : "celestial bronze sword (30)",
                        "level 4" : "magic sword (50)",
                        "MAX" : "black hole summoner sword (80)"}
            type_not_valid = False
        elif type == "armor":
            types_av = {"level 1" : "wooden armor (10)",
                        "level 2" : "iron armor (20)",
                        "level 3" : "celestial bronze armor (30)",
                        "level 4" : "magic armor (50)",
                        "MAX" : "quantum armor (80)"}
            type_not_valid = False
        elif type == "potion":
            types_av = {"level 1" : "health potion (10)",
                        "level 2" : "speed potion (20)",
                        "level 3" : "poison potion (30)",
                        "level 4" : "destruction potion (50)",
                        "MAX" : "ultra stength potion (80)"}
            type_not_valid = False
        elif type == "helper":
            types_av = {"level 1" : "rat (10)",
                        "level 2" : "cat (20)",
                        "level 3" : "cyborg dog (30)",
                        "level 4" : "pheonix (50)",
                        "MAX" : "dragon (80)"}
            type_not_valid = False
        else:
            print("That's not valid.")
            type = input("Try again: ")
    print("Okay. Now, choose one of these:")
    print(types_av)
    weapon = input("So which one do you choose? ")

def get_insane_chest():
    gold = random.ranint(200, 1000)
    return gold

def get_dum_chest():
    gold = random.randint(1, 5)
    return gold

def rage_quit():
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
        print("You rage-quitted. You lost. Now get OUTTA here, ya sucker. ")
        os.abort

def hit_a_noob():
    weapon = input("Enter your weapon: ")
    time.sleep(0.5)

def game_loop():
    thing_to_do = input("Welcome to the satisfication game of battling dumb noobs. What do you want to do? \n battle,(1) \nbuy stuff(shop)(2), \n or rage-quit before you start playing?(3) ")

    if thing_to_do == "3":
        
    elif thing_to_do == "2":
        print("entering shop...")
        time.sleep(1)
        print("succesfully entered shop!")
        shop()

game_loop()


