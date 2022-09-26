#add what happens if right is chosen
init python:
    class cave_mon(object):
        def __init__(self, c, hp, att):
            self.c = c
            self.hp = hp
            self.att = att





label batmoves:
    call dice
    if d6 <= 4:
        $ dam = b.att
    else:
        $ dam = b.att * 2
    return


label cave_enemys:
    define b = cave_mon(Character("bat"), 20, 5)
    return

label one_bat_battle:
    call champs
    call cave_enemys
    while True:
        call m_turn
        $ b.hp -= dam
        "[b.c] has [b.hp], [m.c] did [dam]"
        if b.hp <= 0:
            "[m.c] has won"
            return
        call batmoves
        $ m.hp -= dam
        "[m.c] has [m.hp], [b.c] did [dam]"
        if m.hp <= 0:
            "you have lost"
            jump right_cave #add another enemy turn
    return


label right_cave:
    scene bg cave
    show lava tsun at right with fade
    l.c "fine lets go right"

    m.c "{i} As we walked threw the right side of the cave, I saw a figure dash across the cave {/i}"

    m.c "Did you see that [l.c]? I saw a figure fly across the cave"

    l.c "what are you talking about? I didn;t see anything. You must be imagining it or something."

    m.c "That could be. We must keep or guard up, who knows what is lurking in these cave."

    m.c "{i} Just then I hear a high pitch squeel. It sounded as if a speeding car had come to a sudden halt."

    l.c "Well I definately heard that. But that doesn't mean that it's a scary monster or anything."

    m.c "{i} While that is a possiblility, you can never be too sure"

    menu:
        "check out the sound":
            m.c "{i} As I closer to the sound I notice two glaring red eyes pircing threw me {/i}"

            m.c "looks like we got an angry fella. Lets fight."

            call one_bat_battle

            m.c "easy dubs"

            l.c "I could have taken it on by myself you know"

        "walk past the sound":
            m.c "We decide to wlk past the sound as it sounded super sus"

    "{i} This is the end of right cave {/i}"

    return
