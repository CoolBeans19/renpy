#backgrounds
image bg stadium = "stadium.jpg"
image bg stadium_close = "stadium2lrg.jpg"
image bg neotokyo = "neotokyo.jpg"
image bg explosion = "akira_explosion.jpg"
image bg monster1 = "t_monster_bg.jpg"
image bg monster2 = "t_monster_bg2.jpg"
image bg gameover = "gameover.jpg"
image bg credits = "credits.jpg"
image bg winscreen = "winscreen.jpg"

#character images
image kaneda = "kaneda_idle.png"
image k_bike = "kaneda_bike.png"
image k_gun1 = "kaneda_gun1.png"
image k_gun2 = "kaneda_gun2.png"
image tetsuo = "tetsuo.png"
image t_arm = "tetsuo_arm.png"
image t_arm2 = "tetsuo_arm2.png"

#item images
image battery = "lgunbattery.png"

#character tags
define k = Character('Kaneda', color = "#b22222")
define t = Character('Tetsuo', color = "#556b2f")

init:
    #define transitions
    $ teleport = ImageDissolve("teleport.png", 0.75, 0)
    $ flash = Fade(.25, 0, .75, color="#fff")

label start:
    #variables
    $battery = False
    $player_health = 100
    $tetsuo_health = 100
    $ammo = 8
    $show_player_health = True
    $show_ammo = True
    $show_tetsuo_health = True
    $vp = False
    $cover = False
    
    #defines overlays
    python:
        def player_health_overlay():
            if show_player_health:
                ui.text("health: %d" % player_health, size =20, xpos = 6, color = "#cc0000")
                
    python:
        def ammo_overlay():
            if show_ammo:
                ui.text("ammo: %d" % ammo, size =20, xpos= 700, color = "#cc0000")
                
    python:
        def tetsuo_overlay():
            if show_tetsuo_health:
                ui.text("tetsuo health: %d" % tetsuo_health, size =20, xpos= 600, ypos= 30, color = "#cc0000")
    
    # this is the intro
    scene black # background of the intro
    play music "eclipse.ogg" fadein 3.0 
    "The year is 2019."
    scene bg neotokyo with fade
    "Neotokyo is a sprawling metropolis gripped by gang violence and anti-govenment terrorism."
    "A new generation of children is born, some with unnatural abilities..."
    "One of these children, Tetsuo Shima, has the incredible power to control the energy of the universe."
    scene bg explosion with fade
    "Tetsuo uses his abilities to cause immense havoc, destroying much of Neotokyo and sending the city into chaos."
    "In the ruins of the city, Tetsuo becomes the leader of a new empire of superhuman children, and his power continue to grow..."
    scene black with dissolve
    "Now, Shotaro Kaneda sets out to kill Tetsuo, once his childhood friend, and restore order to Neotokyo before Tetsuo can destroy the world..."
    stop music fadeout 1.0
    $ renpy.pause(3.0) # makes a delay between this scene and the next
    
    play music "ghostdancers.ogg" fadein 3.0
    $ config.overlay_functions.append(player_health_overlay)
    $ config.overlay_functions.append(ammo_overlay)
    scene bg stadium
    "TOKYO OLYMPIC STADIUM" "11:27 PM"
    $ renpy.pause(2.0)
    show k_bike
    with dissolve
    
    k "Where is that bastard?"
    
    menu:
        "Look for Tetsuo":
            jump tetsuo_search
        "Yell \"TETSUOOOO\"":
            jump tetsuo_yell
    
    label tetsuo_search:
        scene bg stadium_close
        with dissolve
        "Strange, no one seems to be around..."
        show battery at truecenter with dissolve
        "but there's a battery here..."
        "take it?"
        menu:
            "Take the battery":
                $ battery = True
                $ ammo = ammo + 7
                hide battery
                "You got the battery! You will move slower, but have more ammunition."
            "Leave it":
                $ battery = False
                "You leave the battery there. You will have more limited ammunition, but will be able to move faster."
                
        t "KANEDAAAAAA!!!"
        jump tetsuo_encounter
    
    label tetsuo_yell:
        k "TETSUOOOO!!!"
        t "KANEDAAAAAA!!!"
        jump tetsuo_encounter


    label tetsuo_encounter:
        scene bg stadium
        with dissolve
        show tetsuo at right
        with teleport
        t "So, you finally found the balls to face me, huh?"
        $ config.overlay_functions.append(tetsuo_overlay)
        t "Go home, Kaneda! You can't stop me now!"
        
        menu:
            "\"You're crazy!\"":
                jump tetsuo_battle
            "\"You're right, I should just go home.\"":
                jump go_home
        
        label tetsuo_battle:
            hide tetsuo
            show k_bike
            with dissolve
            k "You're crazy, Tetsuo! You'll tear the world apart!"
            k "If I have to die trying to stop you, so be it!"
            hide k_bike
            show k_gun1 at left
            with dissolve
            k "EAT THIS!"
            hide k_gun1
            with flash
            play sound "blast.wav"
            $ ammo = ammo - 1
            show tetsuo at right
            t "Argh!!!"
            t "So... that's how it's gonna be, huh? All right, then..."
            hide tetsuo
            show t_arm
            with hpunch
            play sound "squelch.wav"
            t "Hrrrrrk..."
            hide t_arm
            show k_gun2
            with dissolve
            k "Huh?"
            hide k_gun2
            show t_arm2
            with vpunch
            play sound "squelch.wav"
            t "Ka... ne... da..."
            stop music fadeout 1.0
            play music "lilith.ogg"
            scene bg monster1
            with hpunch
            play sound "roar.wav"
            t "EEEAAAAAUUURGHHHHH"
            k "WHAT THE-"
            scene bg monster2
            with dissolve
            "Tetsuo has turned into a giant monster! What do you do?"
            menu:
                "Shoot Tetsuo":
                    scene bg monster2
                    with flash
                    play sound "blast.wav"
                    $ ammo = ammo - 1
                    $ shot1 = renpy.random.random()
                    if shot1 >= 0.5:
                        $ tetsuo_health= tetsuo_health - 25
                        "Tetsuo took damage!"
                        jump tetsuo_attack
                    else:
                        "You missed!"
                        jump tetsuo_attack
                "Run away!":
                    jump game_over
            return
        
        label tetsuo_attack:
            scene bg monster1
            "Tetsuo attacks!"
            $ attack1 = renpy.random.random()
            if vp:
                if attack1 >= 0.4:
                    $ player_health = player_health - 20
                    "You took damage!"
                    $ vp = False
                    "You were knocked from your vantage point!"
                    if player_health == 0:
                        "You've been defeated!"
                        jump game_over
                    else:
                        jump player_attack
                else:
                    "Tetsuo misses!"
                    jump player_attack
            elif cover:
                if attack1 >= 0.5:
                    "Tetsuo destroyed your cover! You're out in the open!"
                    $ cover = False
                    jump player_attack
                else:
                    "Tetsuo misses!"
                    jump player_attack
            else:
                if attack1 >= 0.5:
                    $ player_health = player_health - 20
                    "You took damage!"
                    if player_health == 0:
                        "You've been defeated!"
                        jump game_over
                    else:
                        jump player_attack
                else:
                    "Tetsuo misses!"
                    jump player_attack
                    
                    
        label player_attack:
            scene bg monster2
            if ammo == 0:
                "You're out of ammo!"
                jump game_over
            else:
                "Your turn..."
                if vp:
                    "You have the high ground."
                elif cover:
                    "You're hidden behind cover!"
                menu:
                    "Shoot tetsuo":
                        scene bg monster2 with flash
                        play sound "blast.wav"
                        $ ammo = ammo - 1
                        $ shot2 = renpy.random.random()
                        if vp:
                            if shot2 >= 0.25:
                                $ tetsuo_health= tetsuo_health - 25
                                "Tetsuo took damage!"
                                if tetsuo_health == 0:
                                    "Tetsuo is defeated!"
                                    jump game_win
                                jump tetsuo_attack
                            else:
                                "You missed!"
                                jump tetsuo_attack
                        elif cover:
                            if shot2 >= 0.6:
                                $ tetsuo_health= tetsuo_health - 25
                                "Tetsuo took damage!"
                                if tetsuo_health == 0:
                                    "Tetsuo is defeated!"
                                    jump game_win
                                jump tetsuo_attack
                            else:
                                "You missed!"
                                jump tetsuo_attack
                        else:
                            if shot2 >= 0.5:
                                $ tetsuo_health= tetsuo_health - 25
                                "Tetsuo took damage!"
                                if tetsuo_health == 0:
                                    "Tetsuo is defeated!"
                                    jump game_win
                                jump tetsuo_attack
                            else:
                                "You missed!"
                                jump tetsuo_attack
                    "Find a better vantage point":
                        $ find_vantage = renpy.random.random()
                        if cover:
                            $cover = False
                            "You leave your cover."
                        if battery:
                            if find_vantage >= 0.6:
                                "You found a better vantage point. Your attacks now have a higher chance of hitting their target, but so do Tetuo's!"
                                $ vp = True
                                jump tetsuo_attack
                            else:
                                "Your battery slows you down! You don't get to the vantage point in time..."
                                jump tetsuo_attack
                        else:
                            if find_vantage >= 0.3:
                                "You found a better vantage point. Your attacks now have a higher chance of hitting."
                                $ vp = True
                                jump tetsuo_attack
                            else:
                                "You don't find a vantage point..."
                                jump tetsuo_attack
                                
                    "Hide behind cover":
                        $ find_cover = renpy.random.random()
                        if vp:
                            $vp = False
                            "You leave your vantage point."
                        if battery:
                            if find_cover >= 0.6:
                                "You duck behind some nearby cover. You will be protected from Tetsuo's attacks, but your attacks will have a lower chance of hitting."
                                $cover = True
                                jump tetsuo_attack
                            else:
                                "The battery weighs you down! You don't reach cover in time!"
                                jump tetsuo_attack
                        else:
                            if find_cover >= 0.4:
                                "You duck behind some nearby cover. You will be protected from Tetsuo's attacks, but your attacks will have a lower chance of hitting."
                                $cover = True
                                jump tetsuo_attack
                            else:
                                "You don't find any cover..."
                                jump tetsuo_attack
        
        label go_home:
            hide tetsuo
            show kaneda
            with dissolve
            k "You're right, I should just go home."
            jump game_over
            
        label game_over:
            stop music fadeout 1.0
            scene bg gameover with dissolve
            play music "nakedtongues.ogg" fadein 2.0
            $ renpy.pause(2.0)
            "The world is doomed..."
            "Bad End .:."
            scene bg credits with teleport
            pause
            return
            
        label game_win:
            stop music fadeout 1.0
            play music "iamthenight.ogg" fadein 2.0
            scene bg winscreen with Dissolve(6.0, alpha=False, time_warp=None)
            $ renpy.pause(2.0)
            "With Tetsuo gone, the world is saved, all thanks to Kaneda!"
            "Good End .:."
            scene bg credits with teleport
            pause
            return