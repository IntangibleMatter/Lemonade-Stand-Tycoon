default getbombed = False

label start:
    charname = input("What is your name?", default="")
    jump storystart

label storystart:
    scene lemonade day one
    show player happy
    p "When I was young, I decided to make a lemonade stand."
    p "So I set one up at the end of my Mom's yard"
    show mom proud at right
    m "I'm so proud of you, sweetie."
    m "I've decided to buy you the supplies you need for the first day of lemoandery, but tomorrow you'll have to but the supplies for yourself"
    p "AAAAAAAAAa"


