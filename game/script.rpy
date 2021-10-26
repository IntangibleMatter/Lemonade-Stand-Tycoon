default deniedGeneral = False
default lovesDuck = False
default tookTycoonDeal = False

label start:
    scene lemonade glass
    $charname = renpy.input("What is your name?")
    $jname = charname[0] + "ibby"
    jump storystart

label storystart:
    play music "audio/lemonade stand.mp3"
    scene lemonade bg
    show player happy
    with moveinbottom
    p "When I was young, I decided to make a lemonade stand."
    p "So I set one up at the end of my Mom's yard"
    show mom at right
    with moveinright
    m "I'm so proud of you, sweetie."
    m "I've decided to buy you the supplies you need for lemoandery, after all, you don't have enough money to buy them yourself."
    m "And remember- your income, {i}i{/i}, is equivelent to the price, {i}p{/i}, times the amount of customers, {i}c{/i}!"
    m "Or {i}i = cp{/i}"
    m "Love youuuuuuuuuuuuuuuuuuu <3333333"
    hide mom
    with moveoutright
    p "I decided to charge $0.50 for a glass of Lemonade, as this seemed reasonable for my first day of lemonadery."
    jump dayone




label dayone:
    p "I decided to charge $0.50 for a glass of Lemonade, as this seemed reasonable for my first day of lemonadery."
    p "Then my friend Julie arrived."
    j "hey, [jname]!"
    show julie happy at left
    with moveinleft
    j "i heard you were starting a lemonade stand- without {i}me{/i}?"
    show player
    p "With your work ethic, I assumed you wouldn't want to help."
    show julie sad at left
    j "c'mon, [jname], don't be like that."
    j "you know i'd never miss a chance to get some [KROMER]."
    show julie spamton at left
    p "What?"
    show julie happy at left
    j "nevermind. my point is i like money."
    p "Fair enough. Let's get to work."
    hide julie happy
    hide player
    "{i}We had a fairly normal day with 19 customers, until...{/i}"
    show player happy
    show julie happy at left
    j "think anyone else is coming?"
    p "I don't think-{nw}"
    d "QUACK"
    show duck at right
    with moveinright
    p "Oh, hi."
    j "hiiiiiiiiiiiii...."
    d "QUACK <{i}greetings, ladies. I am but a humble duck.{/i}>"
    d "QUACK QUACK <{i}If possible, could you young ladies get me some glorious, wonderful grapes?{/i}>"
    j "i mean if you want? {jname}, should i?"
    menu:
        "Give the duck grapes":
            $lovesDuck = True
            j "i'll be right back"
            hide julie happy
            with moveoutleft
            p "She'll just be a-{nw}"
            show julie happy
            with moveinleft
            j "I'M BACK"
            d "quack <{i}ah! Grapes! thank you.{/i}>"
            "{b}DUCK{/b} got the {b}{color=#509}GRAPES{/color}{/b} from {b}JULIE{/b}"
            d "QUACK <{i}Ah, delicious. Thank you{/i}>"
            hide duck
            show duck chad at right
            d "quack quack <{i}Thank you for providing me with sustenance{/i}>"
            d "Quack <{i}Farewell.{/i}>"
            hide duck chad with moveoutright
            j "byyyyyyyeeeee~~~~"
        "Don't give the duck grapes":
            $lovesDuck = False
            p "I don't think you should, that wouldn't be a prudent business decision."
            j "aw damn. sorry ducky."
            d "quack <{i}That's perfectly fine, don't worry about it{/i}>"
            d "quack. <{i}I guess you won't get to see my hot bod then{/i}>"
            hide duck
            show duck chad at right
            hide duck chad
            with moveoutright
    jump dayoneend

label dayoneend:
    j "looks like we made..."
    if lovesDuck:
        "$10!"
    else:
        "$9.50!"
    p "Not bad."
    p "Can I see the chart?"
    j "sure"
    hide julie happy
    hide player happy
    window hide
    if lovesDuck:
        show chart day one duck
        pause
        hide chart day one duck
    else:
        show chart day one noduck
        pause
        hide chart day one noduck
    show julie happy at right
    show player happy
    p "Not bad for our first day!"
    j "yeah"
    p "Should we charge $1 tomorrow?"
    j "i think we can get away with that without losing any customers."
    p "Alright. See you tomorrow!"
    hide julie happy
    with moveoutleft
    hide player happy
    with moveoutright
    "{b}{i}Day one end{/i}{/b}"
    jump daytwo

label daytwo:
    j "gooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooood{nw}"
    show julie happy at right
    with moveinright
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
    show julie happy at right
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

label daythree:
    show player happy
    p "Day three. We got this."
    show julie happy
    with moveinright
    j "lemonadery we can do this lets go"
    "{i}Yet another average day, but then...{/i}"
    show tycoon at right
    with moveinright
    t "Hello, kid$!"
    t "You've got quite the $tand here. Want to make a deal?"
    t "$ay ye$ and I can make you very rich."
    t "All you have to do i$ de$troy your $oul!"
    menu:
        "Make a deal":
            $tookTycoonDeal = True
            p "I'm in."
            p "What do you need me to do"
            t "I'll be back with a contract $oon!"
            hide tycoon
            with moveoutright
        "Reject deal":
            p "I don't think that's a good idea, I'm sorry."
            t "My deal i$n't for everyone! Have a nice day kid!"
            hide tycoon
            with moveoutright
    jump daythreeend

label daythreeend:
    j "looks like we made..."
    if tookTycoonDeal:
        "$18.50, But soon we'll be Billionares!"
    else:
        "$18.50!"
    p "Pretty good."
    p "Can I see the chart?"
    j "sure"
    hide julie happy
    hide player happy
    window hide
    if tookTycoonDeal:
        show chart day three capitalist
        pause
        hide chart day three capitalist
    else:
        show chart day three nocapitalist
        pause
        hide chart day three nocapitalist
    show julie happy at right
    show player happy
    p "Not bad!"
    j "yeah"
    p "Do it again tomorrow?"
    j "i think we may've earned enough"
    p "Alright."
    jump endings