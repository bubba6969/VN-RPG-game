# main stats of the game
init python:
    class stats(object):
        def __init__(self, c, name, hp, att):
            self.c = c
            self.name = name
            self.hp = hp
            self.att = att



# dice used for rng
label dice:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d8 = renpy.random.randint(1, 8)
    $ d10 = renpy.random.randint(1, 10)
    return
#

# currency the player can spend
label currency:
    $ gold = 0
    $ gems = 0
    return
#

# moves the hero can use
label m_turn:
    menu:
        "sword swing":
            call sword_swing
            return
        "sword stab":
            call sword_stab
            return
    return
#

# all attacks
label sword_swing:
    $ min = 1
    $ max = 3
    $ rang = renpy.random.randint(min, max)
    $ dam = rang + m.att
    return

label sword_stab:
    call dice
    $ min = 3
    $ max = 6
    $ rang = renpy.random.randint(min, max)
    if d4 >= 2:
        $ dam = rang + m.att
    else:
        $ dam = m.att
    return

label gobo_att:
    $ dam = g.att
    return
###

#player input a name

label player_name:
    $ main_name = renpy.input("what is your name? ", "protag")
    return
#

# uses the stats class to define enemies and heros
label champs:
    define m = stats(Character("[main_name]"), "[main_name]", 100, 10)
    define l = stats(Character("Lava"), "Lava", 10, 10)
    define g = stats(Character("gobos"), "gobo", 10, 2)
    return
#

# make the moves for hero into a class, have it use the varables from the stats class
# find a way to add currency into the game
# find a way to add experence points and a leveling up system (might add that in the stats class with monsters scaling as well)
# make a battle system class with turn order and such (so that it becomes eaier to add fights later on)

# NOTES
# calling an image it, renpy removes capital letters so don't name an image with capital letters to avoid confusion

# battle with gobo v main
label one_gobo_battle:
    call champs
    while True:
        call m_turn
        $ g.hp -= dam
        "[g.c] has [g.hp], [m.c] did [dam]"
        if g.hp <= 0:
            "[m.c] has won"
            jump start2 #add another hero turn
        call gobo_att
        $ m.hp -= dam
        "[m.c] has [m.hp], [g.c] did [dam]"
        if m.hp <= 0:
            "you have lost"
            jump start #add another enemy turn
    return
#
