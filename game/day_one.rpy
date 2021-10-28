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
    j "you know i'd never miss a chance to get some [[KROMER]]."
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
    j "i mean if you want? [jname], should i?"
    menu:
        "Give the duck grapes":
            $lovesDuck = True
            j "i'll be right back"
            hide julie happy
            with moveoutleft
            p "She'll just be a-{nw}"
            show julie happy at left
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
    show julie happy at left
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