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
    play sound "sound/bomb drop.wav"
    Fade(1.0, 1.863, 0.0, color="#fdd")
    jump black

label black:
    scene black
    play sound "sound/atomic bomb roar.wav"
    p "There were no survivors"
    "Nuke Ending"
    return

label TycoonEnding:
