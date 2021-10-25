default getbombed = False


label start:
    scene lemonade glass
    $charname = renpy.input("What is your name?")
    jump storystart

label storystart:
    play music "audio/lemonade stand.mp3"
    scene lemonade bg
    show player happy
    p "When I was young, I decided to make a lemonade stand."
    p "So I set one up at the end of my Mom's yard"
    show mom at right
    m "I'm so proud of you, sweetie."
    m "I've decided to buy you the supplies you need for the first day of lemoandery, but tomorrow you'll have to buy the supplies for yourself"
    hide mom
    p "I decided to charge $0.50 for a glass of Lemonade, as this seemed reasonable for my first day of lemonadery."





