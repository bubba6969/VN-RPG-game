label start:
    scene forest s1 nightlights
    show lava tsun at truecenter
    play music "audio/VN_theme_4.mp3"

    #from classes
    call player_name
    call champs
    #

    # testing
    jump right_cave
    #

    m.c "hey im [main_name] the main character. I have [m.hp] hp and [m.att] att"

    l.c "So why are we on this stupid quest."

    m.c "To get the ring of power"

    l.c "Yes for this soo called \"ring of magic\". Let me guess, is it going to grant 3 wishes as well. "

    l.c "God what a joke"

    l.c "It's sad that a soo called {b} adventurer {/b} can't even cast a {size=+25}simple spell{/size}."

    m.c "Well I managed to get my {b} adventure certification {/b}"

    l.c "Just because you have one doesn't make you a good adventurer in my eyes. "

    m.c "..."

    m.c "{i} I bet she had {u} bitch stew {/u} by the way she is acting today.{/i} "

    m.c "Look up ahead. Do you see that? "

    l.c "What are you talking about, I don't see anything. "

    m.c "It's a small green figure to the right of that tree"

    l.c "{size=+35} OOOHHHHH {/size} now I see it. That might be a goblin. "

    m.c "{i} I don't want to mess with it. It's dark and could be using this as a trap.{/i}"

    show goblin happy at offscreenright
    show goblin happy at topright with move

    show lava tsun:
        xpos 0.6

    l.c "AAAAAAAAHHHHHH!!!"

    m.c "Shit they flanked us."

    g.c "Give us your gold or we will have some fun with your little friend here."

    m.c "{i} I don't have any gold to give them. I had to spend it on feild gear. {/i}"

    l.c "Are you going to keep thinking or fight them"

    m.c "{i} Oh yeah I almost forgot that I have a sword. {/i}"

    m.c "Not over my dead body. {size=+10}Let's fight!!!{/size}."

    call one_gobo_battle

    return

    label start2_cave:
        call champs
        scene forest s1 nightlights # still be forest
        show lava tsun at truecenter

        m.c "that was a good fight"

        m.c "now where did you say the ring of power was?"

        l.c "the ring of power is in the cave of dispare"

        m.c "{i} why do all of the places here have such dramatic names {/i}"

        l.c "what are you waiting for lets gooooo"

        scene bg cave

        m.c "{i} as we make it to the entrance of the cave, I notice a stange bag next to the entrace {/i}"

        # bag of loot event
        menu:
            "pick up bag":
                m.c "I wonder what is in this bag"
                call dice
                call currency
                if d4 >= 3:
                    m.c "sweet some gold"
                    $ gold += 100
                    "{i} you now have [gold] gold {/i}"
                else:
                    m.c "gems, lets go"
                    $ gems += 10
                    "{i} you now have [gems] gems {/i}"
            "leave bag":
                m.c "better to be safe than sorry"
        #

        m.c "{i} walking in the cave, a smell of dank air fills my nose. It's as if a someone had left a steak out for a week in the hot sun.{/i}"

        l.c "{i} cough ... cough ... {/i} this place smells awful. This cave should be called the cave of shitass because that's hat it smells like."

        l.c "... don't tell me that the smell is comming from {size=+10} you {/size}."

        m.c "I can garentee you that it is not me"

        m.c "{i} after walking around in the cave for about 10 mins I see a fork in the road {/i}"

        l.c "well which way do you want to go, not that I care or anything."

        m.c "let's see... "

        menu:
            "right":
                m.c "lets go right"
                call right_cave
                # add call or jump
                return

            "left":
                m.c "lets go left"
                # add call or jump
                return






        return
