import random
import sys
import tkinter as tk
from tkinter import messagebox

inventory = {
    "sword": None,
    "armor": None,
    "potion": None,
    "helper": None
}
carried_items = {
    "sword": None,
    "armor": None,
    "potion": None,
    "helper": None
}
CARRY_LIMIT = 3

types_av_sword = {
    "level 1": "wooden sword (10)",
    "level 2": "iron sword (20)",
    "level 3": "celestial bronze sword (30)",
    "level 4": "magic sword (50)",
    "MAX": "black hole summoner sword (80)"
}
types_av_armor = {
    "level 1": "wooden armor (10)",
    "level 2": "iron armor (20)",
    "level 3": "celestial bronze armor (30)",
    "level 4": "magic armor (50)",
    "MAX": "quantum armor (80)"
}
types_av_potion = {
    "level 1": "health potion (10)",
    "level 2": "speed potion (20)",
    "level 3": "poison potion (30)",
    "level 4": "destruction potion (50)",
    "MAX": "ultra strength potion (80)"
}
types_av_helper = {
    "level 1": "rat (10)",
    "level 2": "cat (20)",
    "level 3": "cyborg dog (30)",
    "level 4": "phoenix (50)",
    "MAX": "dragon (80)"
}

# Flavor actions and sounds for each item (add more as you wish)
SWORD_ACTIONS = {
    "wooden sword": ["(swings awkwardly)", "(splinters fly everywhere)"],
    "iron sword": ["(thrusts mightily)", "(clangs with force)"],
    "celestial bronze sword": ["(shimmers and slashes)", "(sparkles of bronze)"],
    "magic sword": ["(glows and hums)", "(casts a spell mid-swing)"],
    "black hole summoner sword": ["(summons a black hole)", "(gravity distorts reality) *WWWHHOOOOSH* *FWIP*"],
}
ARMOR_ACTIONS = {
    "wooden armor": ["(creaks and groans)", "(splinters, but absorbs some damage)"],
    "iron armor": ["(deflects with a clang)", "(stands strong)"],
    "celestial bronze armor": ["(shields shimmer)", "(absorbs cosmic force)"],
    "magic armor": ["(radiates with energy)", "(barrier shimmers brightly)"],
    "quantum armor": ["(phases in/out)", "(quantum shield up) *ZZZZZZT*"],
}
POTION_ACTIONS = {
    "health potion": ["(glug glug)", "(feels better instantly)"],
    "speed potion": ["(drinks quickly)", "(zips around)"],
    "poison potion": ["(tosses poison)", "(hisses and sizzles)"],
    "destruction potion": ["(throws, *BOOM*)", "(devastating blast) *KABOOM*"],
    "ultra strength potion": ["(muscles bulge)", "(roars with power) *RRRROOOAAARRR*"],
}
HELPER_ACTIONS = {
    "rat": [
        "scurries around, nipping ankles",
        "(squeaks) tries to trip the enemy!"
    ],
    "cat": [
        "(scratches) meow!  meow!",
        "(arches back, hisses) HIISSS!"
    ],
    "cyborg dog": [
        "(barks in binary, causes sonic boom) *bleep* *bloop* *KKRRRANNG*",
        "(launches a missile from back) *BBOOOOMMMM* RRUUFF!"
    ],
    "phoenix": [
        "(bursts into flames, destroys the enemy) *FWWOOSH* *CRACKLE* *SCREECH*",
        "(sings a magical song, confuses) *la-dee-daaa...*"
    ],
    "dragon": [
        "(breathes blue fire at the enemy) RROOOOAARRR!!!!!",
        "(stomps, -- ...) RUURRR? *SQUISH* "
    ],
}

def get_value_from_item(item):
    """Extract number from item string, e.g. 'wooden sword (10)' -> 10"""
    if not item:
        return 0
    if "(" in item and ")" in item:
        try:
            return int(item.split("(")[-1].split(")")[0])
        except Exception:
            return 0
    return 0

def get_base_item_name(item):
    if not item:
        return ""
    return item.split(" (")[0].strip().lower()

def hp_bar(val, maxval=10):
    # val: 0-10
    bars = int(round(val))
    return "[" + "I" * bars + " " * (maxval - bars) + "]"

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Satisfication Game of Battling Dumb Noobs")
        self.dialog = None
        self.battle_sequence = []
        self.battle_index = 0
        self.main_menu()

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Satisfication Game of Battling Dumb Noobs!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.root, text="Battle a noob", width=30, command=self.prepare_battle).pack(pady=3)
        tk.Button(self.root, text="Buy stuff (shop)", width=30, command=self.shop).pack(pady=3)
        tk.Button(self.root, text="Rage-quit", width=30, command=self.rage_quit).pack(pady=3)
        tk.Button(self.root, text="Show inventory", width=30, command=self.show_inventory).pack(pady=3)
        tk.Button(self.root, text="Open a chest", width=30, command=self.open_chest).pack(pady=3)
        tk.Button(self.root, text="Quit", width=30, command=self.root.quit).pack(pady=3)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def shop(self):
        self.clear_screen()
        tk.Label(self.root, text="Choose any one of these:", font=("Arial", 12)).pack(pady=8)
        tk.Button(self.root, text="Sword", width=20, command=lambda: self.shop_type('sword')).pack(pady=2)
        tk.Button(self.root, text="Armor", width=20, command=lambda: self.shop_type('armor')).pack(pady=2)
        tk.Button(self.root, text="Potion", width=20, command=lambda: self.shop_type('potion')).pack(pady=2)
        tk.Button(self.root, text="Helper", width=20, command=lambda: self.shop_type('helper')).pack(pady=2)
        tk.Button(self.root, text="Back to menu", width=20, command=self.main_menu).pack(pady=8)

    def shop_type(self, item_type):
        self.clear_screen()
        types_dict = {
            "sword": types_av_sword,
            "armor": types_av_armor,
            "potion": types_av_potion,
            "helper": types_av_helper
        }
        types_av = types_dict[item_type]
        tk.Label(self.root, text=f"Which {item_type} do you want?", font=("Arial", 12)).pack(pady=8)
        for level, item in types_av.items():
            tk.Button(self.root, text=f"{level}: {item}", width=30, command=lambda l=level: self.add_to_inventory(item_type, l)).pack(pady=1)
        tk.Button(self.root, text="Back to shop", width=20, command=self.shop).pack(pady=8)

    def add_to_inventory(self, item_type, level):
        types_dict = {
            "sword": types_av_sword,
            "armor": types_av_armor,
            "potion": types_av_potion,
            "helper": types_av_helper
        }
        inventory[item_type] = types_dict[item_type][level]
        messagebox.showinfo("Shop", f"Added {types_dict[item_type][level]} to inventory!")
        self.main_menu()

    def get_insane_chest(self):
        gold = random.randint(200, 1000)
        messagebox.showinfo("Chest", f"You found an INSANE chest! You got {gold} gold coins!")
        return gold

    def get_dum_chest(self):
        gold = random.randint(1, 5)
        messagebox.showinfo("Chest", f"You found a dum chest! You got {gold} gold coins!")
        return gold

    def rage_quit(self):
        self.clear_screen()
        tk.Label(self.root, text="Okay.", font=("Arial", 12)).pack(pady=3)
        self.root.update()
        self.root.after(1500, self.rage_quit_countdown, 3)

    def rage_quit_countdown(self, count):
        if count > 0:
            self.clear_screen()
            tk.Label(self.root, text=f"You will rage-quit in...\n{count}...", font=("Arial", 14)).pack(pady=15)
            self.root.update()
            self.root.after(1000, self.rage_quit_countdown, count - 1)
        else:
            self.clear_screen()
            tk.Label(self.root, text="You rage-quitted. You lost. Now get OUTTA here, ya sucker.", font=("Arial", 12, "bold")).pack(pady=15)
            self.root.update()
            self.root.after(2000, self.root.quit)

    def show_inventory(self):
        self.clear_screen()
        tk.Label(self.root, text="Your Inventory:", font=("Arial", 12, "bold")).pack(pady=8)
        for k, v in inventory.items():
            txt = v if v else "-"
            tk.Label(self.root, text=f"{k.title()}: {txt}").pack()
        tk.Label(self.root, text="\nItems to carry in next battle:").pack()
        carried = [v for k, v in carried_items.items() if v]
        if not carried:
            tk.Label(self.root, text="(None selected)").pack()
        else:
            for k, v in carried_items.items():
                if v:
                    tk.Label(self.root, text=f"{k.title()}: {v}").pack()
        tk.Button(self.root, text="Back to menu", command=self.main_menu).pack(pady=10)

    def open_chest(self):
        if random.random() > 0.5:
            self.get_insane_chest()
        else:
            self.get_dum_chest()
        self.main_menu()

    def prepare_battle(self):
        self.clear_screen()
        tk.Label(self.root, text="Choose up to 3 items to carry (sword, armor, potion, helper):", font=("Arial", 11, "bold")).pack(pady=8)

        for k in carried_items:
            carried_items[k] = None

        options = []
        for k in ["sword", "armor", "potion", "helper"]:
            if inventory[k]:
                var = tk.IntVar()
                cb = tk.Checkbutton(self.root, text=f"{k.title()}: {inventory[k]}", variable=var)
                cb.var = var
                cb.pack(anchor="w")
                options.append((k, var, cb))
            else:
                tk.Label(self.root, text=f"{k.title()}: (none owned)").pack(anchor="w")

        def confirm():
            chosen = [k for k, var, _ in options if var.get()]
            if len(chosen) > CARRY_LIMIT:
                messagebox.showinfo("Battle", f"You can only carry {CARRY_LIMIT} items!")
            elif len(chosen) == 0:
                messagebox.showinfo("Battle", "Pick at least one item to battle!")
            else:
                for k, var, _ in options:
                    carried_items[k] = inventory[k] if var.get() else None
                self.start_battle()

        tk.Button(self.root, text="Start Battle!", command=confirm).pack(pady=8)
        tk.Button(self.root, text="Back to menu", command=self.main_menu).pack()

    def start_battle(self):
        self.clear_screen()
        # Generate the noob's defense stats
        noob_items = {
            "sword": random.choice(list(types_av_sword.values())),
            "armor": random.choice(list(types_av_armor.values())),
            "potion": random.choice(list(types_av_potion.values())),
            "helper": random.choice(list(types_av_helper.values()))
        }
        dialog = []
        round_names = ["Sword", "Armor", "Potion", "Helper"]
        player_hps = {"sword": 10, "armor": 10, "potion": 10, "helper": 10}
        noob_hps = {"sword": 10, "armor": 10, "potion": 10, "helper": 10}

        dialog.append("Scene: The battlefield. You and the Noob stare each other down.\n")
        dialog.append("You ready your equipment:")
        for k in ["sword", "armor", "potion", "helper"]:
            if carried_items[k]:
                dialog.append(f'  - {k.title()}: {carried_items[k]}')
        if not any(carried_items.values()):
            dialog.append("  - (You are empty-handed!)")
        dialog.append("\nThe Noob readies their gear:")
        for k in ["sword", "armor", "potion", "helper"]:
            dialog.append(f'  - {k.title()}: {noob_items[k]}')
        dialog.append("\n[The fight begins!]\n")

        # For dramatic play, each round is a scene
        your_score = 0
        noob_score = 0
        round_num = 1
        rounds = ["sword", "armor", "potion", "helper"]
        for idx, kind in enumerate(rounds):
            your_item = carried_items[kind]
            noob_item = noob_items[kind]
            yval = get_value_from_item(your_item)
            nval = get_value_from_item(noob_item)
            yname = get_base_item_name(your_item)
            nname = get_base_item_name(noob_item)

            dialog.append(f"ROUND {idx+1}:")
            dialog.append(f"the noob:  {nname if nname else '(none)'}")
            dialog.append(f"you: {yname if yname else '(none)'}")
            dialog.append("BATTLE START")
            # Noob action
            if nname in HELPER_ACTIONS:
                dialog.append(f"{nname}: {random.choice(HELPER_ACTIONS[nname])}")
            elif nname in SWORD_ACTIONS:
                dialog.append(f"{nname}: {random.choice(SWORD_ACTIONS[nname])}")
            elif nname in ARMOR_ACTIONS:
                dialog.append(f"{nname}: {random.choice(ARMOR_ACTIONS[nname])}")
            elif nname in POTION_ACTIONS:
                dialog.append(f"{nname}: {random.choice(POTION_ACTIONS[nname])}")
            else:
                dialog.append(f"{nname}: (looks confused!)")

            # If critical hit
            if yval > nval and yval > 50:
                dialog.append("<<CRITICAL HIT>>")

            # Your action
            if yname in HELPER_ACTIONS:
                dialog.append(f"{yname}: {random.choice(HELPER_ACTIONS[yname])}")
            elif yname in SWORD_ACTIONS:
                dialog.append(f"{yname}: {random.choice(SWORD_ACTIONS[yname])}")
            elif yname in ARMOR_ACTIONS:
                dialog.append(f"{yname}: {random.choice(ARMOR_ACTIONS[yname])}")
            elif yname in POTION_ACTIONS:
                dialog.append(f"{yname}: {random.choice(POTION_ACTIONS[yname])}")
            else:
                dialog.append(f"{yname}: (just stands there)")

            # HP display: each item starts with 10, loses difference or 1 minimum, capped at 0
            yhp = 10
            nhp = 10
            if yval > nval:
                nhp = max(0, 10 - min((yval - nval)//5, 10))
                yhp = 10
                winner = yname.upper()
                your_score += 1
            elif yval < nval:
                yhp = max(0, 10 - min((nval - yval)//5, 10))
                nhp = 10
                winner = nname.upper()
                noob_score += 1
            else:
                winner = "DRAW"

            dialog.append(f"HP: ({nname} {hp_bar(nhp)}) ({yname} {hp_bar(yhp)})")

            # More flavor lines
            if nname and yval < nval:
                dialog.append(f"{nname}: (taunts you!)")
            elif yname and yval > nval:
                dialog.append(f"{yname}: (flexes victoriously!)")
            elif yval == nval:
                dialog.append(f"{nname} and {yname}: (circle each other warily)")
            # End of round
            if winner == "DRAW":
                dialog.append("IT'S A DRAW!")
            else:
                dialog.append(f"{winner} WINS!")
            dialog.append("")

        # Final result
        dialog.append("Final Score:")
        dialog.append(f"  You: {your_score}")
        dialog.append(f"  Noob: {noob_score}")

        if your_score > noob_score:
            dialog.append("\n[You stand victorious! The noob flees in shame!]")
        elif your_score < noob_score:
            dialog.append("\n[The noob overpowers you! Better luck next time!]")
        else:
            dialog.append("\n[It's a draw! You stare at each other awkwardly.]")

        self.battle_sequence = dialog
        self.battle_index = 0
        self.show_next_battle_line()

    def show_next_battle_line(self):
        # Only clear and create the Text widget on the very first line!
        if self.battle_index == 0 or not hasattr(self, 'dialog') or self.dialog is None:
            self.clear_screen()
            self.dialog = tk.Text(self.root, width=75, height=22, font=("Courier", 10), wrap="word")
            self.dialog.pack(padx=12, pady=8)
        # Remove old navigation buttons if any
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        # Insert all lines up to the current one
        self.dialog.delete("1.0", tk.END)
        for i in range(self.battle_index + 1):
            self.dialog.insert("end", self.battle_sequence[i] + "\n")
        self.dialog.see("end")
        # Show "Next" or "Back to menu" button
        if self.battle_index < len(self.battle_sequence) - 1:
            next_button = tk.Button(self.root, text="Next", command=self.show_next_battle_line)
            next_button.pack(pady=4)
            self.battle_index += 1
        else:
            tk.Button(self.root, text="Back to menu", command=self.main_menu).pack(pady=8)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
