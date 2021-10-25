label endings:
    if tookTycoonDeal:
        jump tycoonEnding
    elif deniedGeneral:
        jump NukeEnding
    elif lovesDuck:
        jump duckEnding
    else:
        jump normalEnding

label NukeEnding:
    show general furious at right
    g "I warned you, you little @$&@!!"
    g "{color=#f00}{cps=40}{b}NO ONE{/b}{/cps} denies me for Lemonade!{/color}"
    hide general furious
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
    Fade(1.0, 1.863, 0.0, color="#fdd")
    scene black
    play sound "audio/atomic bomb roar.wav"
    "There were no survivors"
    "Nuke Ending"
    return

label TycoonEnding:
    pass
    return

label duckEnding:
    show duck chad at right
    play sound "audio/quack.wav"
    d "QUACK <thank you for your kindness good lady, please run away with me to the land where we eat only grapes and bread>"
    p "No thank you, I quite like my own place."
    d "QUACK QUACK <damn. I very much appreciated you giving me grapes."
    return

label normalEnding:
    pass
    return