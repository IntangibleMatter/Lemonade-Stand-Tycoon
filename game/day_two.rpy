label daytwo:
    j "gooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooood{nw}"
    show julie happy at left
    with moveinleft
    j "morning [jname]!!!!!!"
    p "*{i}yawn{/i}*"
    show player sad
    with moveinbottom
    p "Good morning...."
    show player happy
    p "Are you ready for another day of Lemonadery?"
    j "obviously"
    p "Alright, let's go."
    "{i}We had another fairly normal day with 19 customers, until...{/i}"
    g "{b}Maggots!{/b}"
    hide player happy
    show player scared
    p "Who is {i}that{/i}?"
    show general at right
    with moveinright
    g "{b}I am your superior, you little @$*#{/b}"
    g "{b}And I {i} DEMAND some #*#@** lemonade!{/b}"
    p "I don't know, you're kind of rude..."
    g "{b}*@$* you. Give me some god damn lemonade, *@$#*."
    hide julie happy
    show julie sad at left
    menu:
        "Give him the lemonade":
            $deniedGeneral = False
            "{i}You reluctantly hand the general the lemonade{/i}"
            g "Finally, some god damn service..."
            "{i}the general sips the lemonade{/i}"
            show general insane at right
            g "{b}PBBBBBBBBBT{/b}"
            show general angry at right
            g "{b}This tastes like... {cps=20}communism!{/cps}{/b}"
            g "{b}How dare you serve me, a god damn American general COMMUNIST lemonade????{/b}"
            j "this is canada"
            g "{b}How {i}DARE{/i} you talk to me that way!{/b}"
            g "{b}I'd be more angry but-{/b}"
            hide general angry
            hide general insane
            show general at right
            g "{b}You gave me what I wanted so I can't be too mad.{/b}"
            hide general with moveoutright
            j "well"
        "Don't give him the lemonade":
            hide general
            show general angry at right
            g "{b}You will regret this.{/b}"
            hide general angry
            with moveoutright
            j "i think we made the right choice, right?"
    jump daytwoend

label daytwoend:
    j "looks like we made..."
    if deniedGeneral:
        "$19!"
    else:
        "$20!"
    p "Pretty good."
    p "Can I see the chart?"
    j "sure"
    hide julie sad
    hide player scared
    window hide
    if deniedGeneral:
        show chart day two nogeneral
        pause
        hide chart day two nogeneral
    else:
        show chart day two general
        pause
        hide chart day two general
    show julie happy at left
    show player happy
    p "Not bad for our second day!"
    j "yeah"
    p "Should we charge $1.50 tomorrow?"
    j "i think we may lose a few customers, but we should get some good money."
    p "Alright. See you tomorrow!"
    hide julie happy
    with moveoutleft
    hide player happy
    with moveoutright
    "{b}{i}Day two end{/i}{/b}"
    jump daythree
