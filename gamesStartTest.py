def Wizard():
    global_vars = {}
    with open("Attempt_1.py") as f:
        exec(f.read(), global_vars)
    globals().update(global_vars)

def Cijevi():
    global_vars2 = {}
    with open("cijevi_game.py") as f:
        exec(f.read(), global_vars2)
    globals().update(global_vars2)

def Zombie():
    global_vars3 = {}
    with open("No_Name_Game.py") as f:
        exec(f.read(), global_vars3)
    globals().update(global_vars3)
