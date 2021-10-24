default getbombed = False
$price = .50

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
    menu:
        "I decided to charge..."
        "50 cents":
            $price = .50
        "1 dollar":
            $price = 1
    p "I decided to charge $[price] for a glass of Lemonade."
    jump NukeEnding


