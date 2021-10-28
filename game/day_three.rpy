
label daythree:
    show player happy
    p "Day three. We got this."
    show julie happy at left
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
    show julie happy at left
    show player happy
    p "Not bad!"
    j "yeah"
    p "Do it again tomorrow?"
    j "i think we may've earned enough"
    p "Alright."
    jump endings