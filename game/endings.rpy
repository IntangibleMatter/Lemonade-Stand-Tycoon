label endings:
    show julie happy at left
    show player happy
    if lovesDuck and deniedGeneral and tookTycoonDeal:
        jump bigEnding
    elif (not lovesDuck) and deniedGeneral and tookTycoonDeal:
        jump moneyNukeEnding
    elif lovesDuck and (not deniedGeneral) and tookTycoonDeal:
        jump richDuckEnding
    elif lovesDuck and deniedGeneral and not tookTycoonDeal:
        jump duckSavesDayEnding
    elif (not lovesDuck) and (not deniedGeneral) and tookTycoonDeal:
        jump tycoonEnding
    elif (not lovesDuck) and deniedGeneral and (not tookTycoonDeal):
        jump nukeEnding
    elif lovesDuck and (not deniedGeneral) and (not tookTycoonDeal):
        jump duckEnding
    elif (not lovesDuck) and (not deniedGeneral) and (not tookTycoonDeal):
        jump defaultEnding
    else:
        "{color=#f00}{b}Err: ending not found{/b}{/color}"

label endingstest:
    menu: 
        "Make ducklove false" if lovesDuck:
            $lovesDuck = False
        "Make ducklove true" if not lovesDuck:
            $lovesDuck = True
        "Make deniedGeneral false" if deniedGeneral:
            $deniedGeneral = False
        "make deniedGeneral true" if not deniedGeneral:
            $deniedGeneral = True
        "make tookTycoonDeal false" if tookTycoonDeal:
            $tookTycoonDeal = False
        "make tookTycoonDeal true" if not tookTycoonDeal:
            $tookTycoonDeal = True

    call endings

label bigEnding:
    show tycoon at right
    t "Alright, are you ready to give up your $oul and become a TYCOON?"
    show player happy
    p "I was born ready!"
    "{i}you rip your soul out of your chest{/i}"
    "{i}JULIE crushes your soul and hers to bits{/i}"
    t "Perfect."
    hide player happy
    show player tycoon
    hide julie happy
    show julie tycoon
    j "i'm a legit billionare now"
    hide tycoon
    with moveoutbottom
    show general angry at right
    g "I warned you, you little @$&@!!"
    g "{color=#f00}{cps=40}{b}NO ONE{/b}{/cps} denies me for Lemonade!{/color}"
    hide general angry
    show general insane at right
    g "Say hello to my little friend..."
    g "{b}{i}Mr. Nuke!!!!{/i}{/b}"
    g "HASTA LA BYE-BYE, Y-"
    d "QUACK!!!!!"
    show duck chad at right
    d "QUACK!!! <{i}I diverted the missile back at the general; he will die soon. You are safe now."
    p "Thank you...."
    d "QUACK <{i}Also I wanted thank you for your kindness good lady, please run away with me to the land where we eat only grapes and bread{/i}>"
    p "No thank you, I quite like my own place."
    d "QUACK QUACK <{i}damn. I very much appreciated you giving me grapes.{/i}>"
    j "oh my god"
    j "duck!!!!!!!!"
    j "how i missed you....."
    d "QUACK! <{i}Julie!{/i}>"
    j "i gotta be honest, getting you grapes was the highlight of my week."
    d "Quack <{i}*blushes and turns away* UwU{/i}"
    j "would you... like to run away together?"
    d "QUACK <{i}Yes!! Yes!!! A hundred times yes!!!{/i}>"
    j "bye [charname], i've found my true calling now."
    d "Quack <{i}Farewell, good [jname].{/i}>"
    hide julie tycoon
    with moveoutright
    hide duck chad
    with moveoutright
    "{b}True Ending{/b}"
    return

label moneyNukeEnding:
    show tycoon at right
    t "Alright, are you ready to give up your $oul and become a TYCOON?"
    show player happy
    p "I was born ready!"
    "{i}you rip your soul out of your chest{/i}"
    "{i}JULIE crushes your soul and hers to bits{/i}"
    t "Perfect."
    hide player happy
    show player tycoon
    hide julie happy
    show julie tycoon
    j "i'm a legit billionare now"
    hide tycoon
    with moveoutbottom
    show general angry at right
    g "I warned you, you little @$&@!!"
    g "{color=#f00}{cps=40}{b}NO ONE{/b}{/cps} denies me for Lemonade!{/color}"
    hide general angry
    show general insane at right
    g "Say hello to my little friend..."
    g "{b}{i}Mr. Nuke!!!!{/i}{/b}"
    g "HASTA LA BYE-BYE, Y-"
    j "i will pay you a lot of money to not nuke us"
    g "..."
    g "You got off lucky this time....."
    hide general angry
    with moveoutright
    "{b}Money Nuke Ending{/b}"

label richDuckEnding:
    show tycoon at right
    with moveinright
    t "Before you sell your soul, I must tell you...."
    t "I'm not what I seem.."
    t "In reality, I am...."
    hide tycoon with moveouttop
    show duck tycoon at right with moveinbottom
    d "Quack <{i}the duck!!!{/i}>"
    d "quack <{i}and thanks to your grapes I am very rich, and I would like to share my money with you!{/i}>"
    hide duck tycoon
    show duck chad at right
    play sound "audio/quack.wav"
    d "QUACK <{i}so please run away with me to the land where we eat only grapes and bread{/i}>"
    p "No thank you, I quite like my own place."
    p "I {i}would{/i} like some money, though"
    d "quack <{i}gladly!{/i}>"
    "{i}DUCK gave [charname] MONEY"
    d "QUACK QUACK <{i}I very much appreciated you giving me grapes.{/i}>"
    j "oh my god"
    show julie happy at left
    j "duck!!!!!!!!"
    j "how i missed you....."
    d "QUACK! <{i}Julie!{/i}>"
    j "i gotta be honest, getting you grapes was the highlight of my week."
    d "Quack <{i}*blushes and turns away* UwU{/i}"
    j "would you... like to run away together?"
    d "QUACK <{i}Yes!! Yes!!! A hundred times yes!!!{/i}>"
    j "bye [charname], i've found my true calling now."
    d "Quack <{i}Farewell, good [jname].{/i}>"
    hide julie happy
    with moveoutright
    hide duck chad
    with moveoutright
    "{b}Duck Ending{/b}"
    return

label duckSavesDayEnding:
    show general angry at right
    g "I warned you, you little @$&@!!"
    g "{color=#f00}{cps=40}{b}NO ONE{/b}{/cps} denies me for Lemonade!{/color}"
    hide general angry
    show general insane at right
    g "Say hello to my little friend..."
    g "{b}{i}Mr. Nuke!!!!{/i}{/b}"
    g "HASTA LA BYE-BYE, YOU LITTLE @#$*!!!!"
    hide general insane
    show player sad
    p "{cps=4}....{/cps}"
    show julie sad at left
    j "{cps=3}...{/cps}Fiddlesticks"
    show player sad
    p "{cps=10}I love you,{/cps}{cps=1} {/cps}{cps=6}Mom..."
    p "{cps=5}R{alpha=0.95}e{/alpha}{alpha=0.9}m{/alpha}{alpha=0.85}e{/alpha}{alpha=0.8}m{/alpha}{alpha=0.75}b{/alpha}{alpha=0.7}e{/alpha}{alpha=0.65}r{/alpha} {alpha=0.6}m{/alpha}{alpha=0.55}e{/alpha}{alpha=0.5}.{/alpha}{alpha=0.45}.{/alpha}{alpha=0.4}.{/alpha}{/cps}"
    show player scared
    scene black
    with bombflash
    d "QUACK!!!!!"
    scene lemonade bg
    show duck chad at right
    d "QUACK!!! <{i}I diverted the missile back at the general; he will die soon. You are safe now."
    show player happy
    p "Thank you...."
    d "QUACK <{i}Also I wanted thank you for your kindness good lady, please run away with me to the land where we eat only grapes and bread{/i}>"
    p "No thank you, I quite like my own place."
    d "QUACK QUACK <{i}damn. I very much appreciated you giving me grapes.{/i}>"
    j "oh my god"
    show julie happy at left
    j "duck!!!!!!!!"
    j "how i missed you....."
    d "QUACK! <{i}Julie!{/i}>"
    j "i gotta be honest, getting you grapes was the highlight of my week."
    d "Quack <{i}*blushes and turns away* UwU{/i}"
    j "would you... like to run away together?"
    d "QUACK <{i}Yes!! Yes!!! A hundred times yes!!!{/i}>"
    j "bye [charname], i've found my true calling now."
    d "Quack <{i}Farewell, good [jname].{/i}>"
    hide julie happy
    with moveoutright
    hide duck chad
    with moveoutright
    "{b}Duck Saves Day Ending{/b}"
    return

label tycoonEnding:
    show tycoon at right
    t "Alright, are you ready to give up your $oul and become a TYCOON?"
    show player happy
    p "I was born ready!"
    "{i}you rip your soul out of your chest{/i}"
    "{i}JULIE crushes your soul and hers to bits{/i}"
    t "Perfect."
    hide player happy
    show player tycoon
    hide julie happy
    show julie tycoon
    j "i'm a legit billionare now"
    hide tycoon
    with moveoutright
    hide player tycoon
    with moveoutright
    hide julie tycoon
    with moveoutright
    "{b}{i}Tycoon Ending{/b}{/b}"
    return

label nukeEnding:
    show general angry at right
    g "I warned you, you little @$&@!!"
    g "{color=#f00}{cps=40}{b}NO ONE{/b}{/cps} denies me for Lemonade!{/color}"
    hide general angry
    show general insane at right
    g "Say hello to my little friend..."
    g "{b}{i}Mr. Nuke!!!!{/i}{/b}"
    g "HASTA LA BYE-BYE, YOU LITTLE @#$*!!!!"
    hide general insane
    show player sad
    p "{cps=4}....{/cps}"
    show julie sad at left
    j "{cps=3}...{/cps}Fiddlesticks"
    show player sad
    p "{cps=10}I love you,{/cps}{cps=1} {/cps}{cps=6}Mom..."
    p "{cps=5}R{alpha=0.95}e{/alpha}{alpha=0.9}m{/alpha}{alpha=0.85}e{/alpha}{alpha=0.8}m{/alpha}{alpha=0.75}b{/alpha}{alpha=0.7}e{/alpha}{alpha=0.65}r{/alpha} {alpha=0.6}m{/alpha}{alpha=0.55}e{/alpha}{alpha=0.5}.{/alpha}{alpha=0.45}.{/alpha}{alpha=0.4}.{/alpha}{/cps}"
    show player scared
    play sound "audio/bomb drop.wav"
    scene black
    with bombflash
    hide player scared
    hide julie sad
    play sound "audio/atomic bomb roar.wav"
    "There were no survivors"
    "{b}Nuke Ending{/b}"
    return


label duckEnding:
    show duck chad at right
    play sound "audio/quack.wav"
    d "QUACK <{i}thank you for your kindness good lady, please run away with me to the land where we eat only grapes and bread{/i}>"
    p "No thank you, I quite like my own place."
    d "QUACK QUACK <{i}damn. I very much appreciated you giving me grapes.{/i}>"
    j "oh my god"
    show julie happy at left
    j "duck!!!!!!!!"
    j "how i missed you....."
    d "QUACK! <{i}Julie!{/i}>"
    j "i gotta be honest, getting you grapes was the highlight of my week."
    d "Quack <{i}*blushes and turns away* UwU{/i}"
    j "would you... like to run away together?"
    d "QUACK <{i}Yes!! Yes!!! A hundred times yes!!!{/i}>"
    j "bye [charname], i've found my true calling now."
    d "Quack <{i}Farewell, good [jname].{/i}>"
    hide julie happy
    with moveoutright
    hide duck chad
    with moveoutright
    "{b}Duck Ending{/b}"
    return


label defaultEnding:
    j "So why did you only give lemonade to our rudest customer?"
    p "I was scared of him."
    j "That's fair. I wonder what would've happened if you had made different choices..."
    p "Only way I could do that were if this were a free to download Visual Novel on {a=https://intangiblematter.itch.io}intangiblematter.itch.io"
    j "This is probably the most boring end"
    "{b}Play Again Ending{/b}"
    return