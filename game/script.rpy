default deniedGeneral = False
default lovesDuck = False
default tookTycoonDeal = False

label start:
    scene lemonade glass
    $charname = renpy.input("What is your name?")
    $jname = charname[0] + "ibby"
    if name == "endings":
        jump ending_test
    else:
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
