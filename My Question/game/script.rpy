image bg meadow = "meadow.jpg"
image bg uni = "uni.jpg"

image sylvie smile = "sylvie_smile.png"
image sylvie surprised = "sylvie_surprised.png"

define s = Character('Sylvie', color = "#c8c8ff")
define m = Character('Me', color = "#c8c8ff")

label start:
    $ bl_game = False
    play music "priceoffailure.ogg" fadein 1.0
    scene bg meadow
    with None
    show sylvie smile at right
    with dissolve
    
    "I'll ask her..."

    m "Um... will you..."
    m "Will you be my artist for a visual novel?"
    
    show sylvie surprised

    "Silence."
    "She is shocked, and then..."
    
    show sylvie smile

    s "Sure, but what is a \"visual novel?\""
    
    menu:
        "It's a story with pictures.":
            jump vn
            
        "It's a hentai game.":
            jump hentai
    
    label vn:
        m "It's a story with pictures and music."
        jump marry
        
    label hentai:
        
        $ bl_game = True
        
        m "Why it's a game with lots of sex."
        s "You mean, like a boy's love game?"
        s "I've always wanted to make one of those."
        s "I'll get right on it!"
        jump marry
        
    label marry:
        scene black
        with dissolve
        "--- years later ---"
        "And so, we became a visual novel creating team."
        "We made games and had a lot of fun making them."
        
        if bl_game:
            "Well, apart from that boy's love game she insisted on making."
            
        "And one day..."
        show sylvie smile
        with dissolve
        s "Hey! Marry me!"
    
        ".:. Good Ending"
        return
        
