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
    "We had a fairly normal day with 19 customers, until..."
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
            show duck chad
            hide duck chad
            with moveoutright