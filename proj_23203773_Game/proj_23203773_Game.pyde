import random
import math
add_library('minim')

def setup():
    global count, currentLength1, currentLength2, currentLength3, arrow_count 
    count = 0
    currentLength1 = 0
    currentLength2 = 0
    currentLength3 = 0
    arrow_count = 35
    
    global MAIN_CHARACTER_WIDTH, MAIN_CHARACTER_HEIGHT, GAME_DURATION
    global ENEMY_WIDTH, ENEMY_HEIGHT, ARROW_WIDTH, ARROW_HEIGHT
    global HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT, main_character_x, main_character_y
    global arrows, enemies, enemy_arrows, score, health, game_over, in_progress
    GAME_DURATION = 50
    MAIN_CHARACTER_WIDTH = 100
    MAIN_CHARACTER_HEIGHT = 100
    ENEMY_WIDTH = 80
    ENEMY_HEIGHT = 80
    ARROW_WIDTH = 20
    ARROW_HEIGHT = 50
    HEALTH_BAR_WIDTH = 50
    HEALTH_BAR_HEIGHT = 10

    main_character_x = (width - MAIN_CHARACTER_WIDTH) // 2
    main_character_y = height - MAIN_CHARACTER_HEIGHT - 10
    arrows = []
    enemies = []
    enemy_arrows = []
    score = 0
    health = 3
    game_over = False
    in_progress = False
    
    size(800,800)
    frameRate(60)
    #noCursor()
    global start_time
    start_time = 0
    
    # Load arrow, enemy, and main character images
    global arrow_img, axe_img, enemy_img, main_character_img, round1bg, round1introbg
    global eomer,gandalf, aragorn, round2bg, round3bg, round2introbg, round3introbg
    global you_win, you_lose, hallsofmandos
    arrow_img = loadImage("Arrow.png")
    enemy_img = loadImage("enemy.png")
    axe_img = loadImage("Axe.png")
    round1bg = loadImage("round1bg.png")
    round2bg = loadImage("round2bg.png")
    round3bg = loadImage("round3bg.png")
    round1introbg = loadImage("helm's deep.png")
    round2introbg = loadImage("minastirith.png")
    round3introbg = loadImage("Mordor.jpg")
    eomer = loadImage("Eomer.png")
    gandalf = loadImage("Gandalf.png")
    aragorn = loadImage("Aragorn.png")
    you_win = loadImage("You Win.jpg")
    you_lose = loadImage("You Lose.jpg")
    hallsofmandos = loadImage("despair.png")
    
    global minim, player1, player2, player3, player4, player5, player6
    minim = Minim(this)
    player1 = minim.loadFile("lotrsong.mp3")
    player2 = minim.loadFile("Rohan.mp3")
    #player3 = minim.loadFile("siegeofgondor.mp3")
    #player4 = minim.loadFile("blackgates.mp3")
    #player5 = minim.loadFile("shadow.mp3")
    #player6 = minim.loadFile("anduril.mp3")
    
def draw():
    if count == 0:
        player1.play()
        loading_page()
    elif count == 1:
        instruction_page()
    elif count == 2:
        choose_character()
    elif count == 3:
        char1_round1_intro()
    elif count == 4:
        char2_round1_intro()
    elif count == 5:
        gameplay(round1bg, "ingamegimli.png", axe_img, 15, 7, 2, 10, 12)
    elif count == 6:
        gameplay(round1bg, "ingamelegolas.png", arrow_img, 15, 7, 2, 10, 15)
    elif count == 7:
        player2.play()
        char1_round2_intro()
    elif count == 8:
        player2.play()
        char2_round2_intro()
    elif count == 9:
        gameplay(round2bg, "ingamegimli.png", axe_img, 20, 9, 2.5, 11, 12)
    elif count == 10:
        gameplay(round2bg, "ingamelegolas.png", arrow_img, 20, 9, 2.5, 11, 15)
    elif count == 11:
        char1_round3_intro()
    elif count == 12:
        char2_round3_intro()
    elif count == 13:
        gameplay(round3bg, "ingamegimli.png", axe_img, 30, 14, 3, 12, 12)
    elif count == 14:
        gameplay(round3bg, "ingamelegolas.png", arrow_img, 30, 14, 3, 12, 15)
    elif count == 15:
        You_Win()
    elif count == 16:
        stats()
    elif count == 17:
        You_Lose()

    if count == 3:
        if not player1.isPlaying():
            player1.play()
        if player2.isPlaying():
            player2.pause()  # Pause or stop the second player
            player2.rewind()  # Rewind to the start of the track
    elif count == 4:
        if not player2.isPlaying():
            player2.play()
        if player1.isPlaying():
            player1.pause() 
            player1.rewind()

    
# LOADING PAGE    
    
def loading_page():
    bg = loadImage("loading screen.jpg")
    image(bg,0,0,width,height)
    
    fontTitle = createFont("Middleearth.ttf",80,80)
    textFont(fontTitle)
    textAlign(CENTER)
    fill(255)
    text("Archers",width/2,height/3)
    text("of",width/2,height/3+80)
    text("Middle Earth",width/2,height/3+160)
    fontOther = createFont("PartyBusiness.ttf",50)
    textFont(fontOther)
    text("Enter, friend...",width/2,height-100)
 
# INSTRUCTION PAGE        
                      
def instruction_page():
    bg = loadImage("loading screen.jpg")
    image(bg,0,0,width,height)
    
    fontOther = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther)
    textAlign(CENTER)
    text("In game Instructions",width/2,height/3+40)
    text("1 Press Right Key to Move Right",width/2,height/3+80)
    text("2 Press Left Key to Move Left",width/2,height/3+120)
    text("3 Press, Hold, and Release",width/2,height/3+160)
    text("Mousebutton to Shoot Arrow",width/2,height/3+200)
    text("Press any key to continue",width/2,height-40)

# CHOOSE YOUR CHARACTER

def choose_character():
    charBg = loadImage("characterBg.png")
    char1 = loadImage("Gimli.png")
    char2 = loadImage("Legolas.png")

    image(charBg,0,0,width,height)
    
    fontOther1 = createFont("RingbearerMedium.ttf",50)
    textFont(fontOther1)
    textAlign(CENTER)
    fill(0)
    text("Choose your Warrior",width/2,100)
    textAlign(CORNER)

    image(char1,50,200,300,300)
    image(char2,400,200,300,300)
    
    fontOther2 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther2)
    fill(0)
    text("Gimli son of Gloin",50,550)
    text("Moves faster",50,600)
    text("Better at evading",50,650)
    text("Legolas Greenleaf",400,550)
    text("Shoots faster",400,600)
    text("Better at killing",400,650)
    
    fill(76,193,68)
    rect(50,700,260,80)
    fill(0)
    text("Choose Gimli",70,735)
    fill(76,193,68)
    rect(400,700,280,80)
    fill(0)
    text("Choose Legolas",420,735)
  
# INTRO FOR CHARACTER 1 ROUND 1 
            
def char1_round1_intro():
    global currentLength1
    speeches = [
    "If we live through the night",
    "I will listen to you talk about",
    "the Lady of the Goldenwood gladly"
    ]
    image(round1introbg,0,0,width,height)
    image(eomer,500,300,300,500)
    
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(255)
    
    fill(251,223,122)
    rect(300,10,200,100)
    fill(0)
    text("Round 1",310,40)
    text("Helms Deep",310,80)
    
    fill(0,255,0)
    text("Instructions",10,260)
    text("Kill atleast 15 orcs",10,300)
    text("You have 50 seconds",10,340)
    text("You have 3 lives",10,380)
    text("Press Enter to continue",10,700)
    fill(255)
    
    for i in range(len(speeches)):
        y = 500 + i * 40
        text(speeches[i][:currentLength1], 10, y)

    for i in range(3):
        if currentLength1 < len(speeches[i]):
            currentLength1 += 1

# INTRO FOR CHARACTER 2 ROUND 1
                
def char2_round1_intro():
    global currentLength1
    speeches = [
    "May the blessings of your folk",
    "guide us through this dark night",
    "ere the sons of Eorl perish"
    ]
    image(round1introbg,0,0,width,height)
    image(eomer,500,300,300,500)
    
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(255)
    
    fill(251,223,122)
    rect(300,10,200,100)
    fill(0)
    text("Round 1",310,40)
    text("Helms Deep",310,80)
    
    fill(0,255,0)
    text("Instructions",10,260)
    text("Kill atleast 15 orcs",10,300)
    text("You have 50 seconds",10,340)
    text("You have 3 lives",10,380)
    text("Press Enter to continue",10,700)
    fill(255)
    
    for i in range(len(speeches)):
        y = 500 + i * 40
        text(speeches[i][:currentLength1], 10, y)

    for i in range(3):
        if currentLength1 < len(speeches[i]):
            currentLength1 += 1
        
# INTRO FOR CHARACTER 1 ROUND 2

def char1_round2_intro():
    global currentLength2
    speeches = [
    "Glad am I to see you Gimli",
    "Orcs to hew and bricks to build",
    "Fight on son of Gloin"
    ]
    image(round2introbg,0,0,width,height)
    image(gandalf,500,300,300,500)
    
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(255)
    
    fill(251,223,122)
    rect(300,10,200,100)
    fill(0)
    text("Round 1",310,40)
    text("Minas Tirith",310,80)
    
    fill(0,255,0)
    text("Instructions",10,260)
    text("Kill atleast 20 orcs",10,300)
    text("You have 50 seconds",10,340)
    text("You have 3 lives",10,380)
    text("Press Enter to continue",10,700)
    fill(255)
    
    for i in range(len(speeches)):
        y = 500 + i * 40
        text(speeches[i][:currentLength2], 10, y)

    for i in range(3):
        if currentLength2 < len(speeches[i]):
            currentLength2 += 1

# INTRO FOR CHARACTER 2 ROUND 2

def char2_round2_intro():
    global currentLength2
    speeches = [
    "Beware the gulls",
    "The Mumakil of Harad rampage",
    "The sea longing shall linger yet"
    ]
    image(round2introbg,0,0,width,height)
    image(gandalf,500,300,300,500)
    
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(255)
    
    fill(251,223,122)
    rect(300,10,200,100)
    fill(0)
    text("Round 1",310,40)
    text("Minas Tirith",310,80)
    
    fill(0,255,0)
    text("Instructions",10,260)
    text("Kill atleast 20 orcs",10,300)
    text("You have 50 seconds",10,340)
    text("You have 3 lives",10,380)
    text("Press Enter to continue",10,700)
    fill(255)
    
    for i in range(len(speeches)):
        y = 500 + i * 40
        text(speeches[i][:currentLength2], 10, y)

    for i in range(3):
        if currentLength2 < len(speeches[i]):
            currentLength2 += 1
    

# INTRO FOR CHARACTER 1 ROUND 3

def char1_round3_intro():
    global currentLength3
    speeches = [
    "A day shall come",
    "When the courage of men shall fail",
    "But it is not this day"
    ]
    image(round3introbg,0,0,width,height)
    image(aragorn,500,300,300,500)
    
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(255)
    
    fill(251,223,122)
    rect(300,10,200,100)
    fill(0)
    text("Last Round",310,40)
    text("The Black Gates",310,80)
    
    fill(0,255,0)
    text("Instructions",10,260)
    text("Kill atleast 15 orcs",10,300)
    text("You have 50 seconds",10,340)
    text("You have 3 lives",10,380)
    text("Press Enter to continue",10,700)
    fill(255)
    
    for i in range(len(speeches)):
        y = 500 + i * 40
        text(speeches[i][:currentLength3], 10, y)

    for i in range(3):
        if currentLength3 < len(speeches[i]):
            currentLength3 += 1

# INTRO FOR CHARACTER 2 ROUND 3

def char2_round3_intro():
    global currentLength3
    speeches = [
    "A day shall come",
    "When the courage of men shall fail",
    "But it is not this day"
    ]
    image(round3introbg,0,0,width,height)
    image(aragorn,500,300,300,500)
    
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(255)
    
    fill(251,223,122)
    rect(300,10,200,100)
    fill(0)
    text("Last Round",310,40)
    text("The Black Gates",10,80)
    
    fill(0,255,0)
    text("Instructions",10,260)
    text("Kill atleast 30 orcs",10,300)
    text("You have 50 seconds",10,340)
    text("You have 3 lives",10,380)
    text("Press Enter to continue",10,700)
    fill(255)
    
    for i in range(len(speeches)):
        y = 500 + i * 40
        text(speeches[i][:currentLength3], 10, y)

    for i in range(3):
        if currentLength3 < len(speeches[i]):
            currentLength3 += 1        

                                
def You_Win():
    image(you_win, 0, 0, width, height)
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(255)
    textAlign(CENTER)
    text("The One Ring is destroyed",width/2,50)
    text("The fourth age has begun",width/2,90)
    textAlign(CORNER)
    rectMode(CORNER)
    fill(76,193,68)
    rect(50,700,150,80)
    fill(0)
    text("Restart",70,735)
    fill(255,0,0)
    rect(400,700,150,80)
    fill(255)
    text("Quit",420,735)
    
def You_Lose():
    image(you_lose, 0, 0, width, height)
    fontOther3 = createFont("RingbearerMedium.ttf",30)
    textFont(fontOther3)
    fill(0)
    textAlign(CENTER)
    text("The blood of Numenor is spent",width/2,50)
    text("The dominion of Sauron is complete",width/2,90)
    textAlign(CORNER)
    rectMode(CORNER)
    fill(76,193,68)
    rect(50,700,150,80)
    fill(0)
    text("Restart",70,735)
    fill(255,0,0)
    rect(400,700,150,80)
    fill(255)
    text("Quit",420,735)
    
def stats():
    global hallsofmandos
    image(hallsofmandos, 0, 0, width, height)
    fill(76,193,68)
    rectMode(CENTER)
    rect(width/2,height/2,300,150)
    textSize(32)
    fill(255, 0, 0)
    textAlign(CENTER)
    text("Game Over", width // 2, height // 2 - 40)
    textSize(24)
    text("Score: " + str(score), width // 2, height // 2)
    text("Press Enter to continue", width // 2, height // 2 + 40)
    textAlign(CORNER)
    
def stop():
    player1.close()
    player2.close()
    minim.stop()
        
def keyPressed():
    global count
    
    if count == 0 and key == ENTER:
        count = 1
    elif count == 1:
        count = 2
    elif count == 3 and key == ENTER:
        start_new_round()
        count = 5
    elif count == 4 and key == ENTER:
        start_new_round()
        count = 6
    elif count == 5 and key == ENTER and game_over:
        count = 7
    elif count == 6 and key == ENTER and game_over:
        count = 8
    elif count == 7 and key == ENTER:
        start_new_round()
        count = 9
    elif count == 8 and key == ENTER:
        start_new_round()
        count = 10
    elif count == 9 and key == ENTER and game_over:
        count = 11
    elif count == 10 and key == ENTER and game_over:
        count = 12
    elif count == 11 and key == ENTER:
        start_new_round()
        count = 13
    elif count == 12 and key == ENTER:
        start_new_round()
        count = 14
    elif (count == 13 or count == 14) and key == ENTER and game_over:
        count = 15
    elif count == 16 and key == ENTER:
        count = 17
        
    global main_character_x
    if count == 5 or count == 9 or count == 13:
        if keyCode == LEFT and main_character_x > 0:
            main_character_x -= 10
        elif keyCode == RIGHT and main_character_x + MAIN_CHARACTER_WIDTH < width:
            main_character_x += 10
    elif count == 6 or count == 10 or count == 14:
        if keyCode == LEFT and main_character_x > 0:
            main_character_x -= 5
        elif keyCode == RIGHT and main_character_x + MAIN_CHARACTER_WIDTH < width:
            main_character_x += 5
        
def mousePressed():
    global count, arrow_count
    
    if count == 2 and mouseX>50 and mouseY>700 and mouseX<310 and mouseY<780:
        count = 3
    elif count == 2 and mouseX>400 and mouseY>700 and mouseX<680 and mouseY<780:
        count = 4
    elif (count == 15 or count == 17) and mouseX>50 and mouseY>700 and mouseX<200 and mouseY<780:
        setup()
    elif (count == 15 or count == 17) and mouseX>400 and mouseY>700 and mouseX<550 and mouseY<780:
        exit()

    if arrow_count > 0 and (count == 5 or count == 6 or count == 9 or count == 10 or count == 13 or count == 14):
        arrow_x = main_character_x + MAIN_CHARACTER_WIDTH // 2 - ARROW_WIDTH // 2
        arrow_y = main_character_y
        angle = math.atan2(mouseY - arrow_y, mouseX - arrow_x)
        arrows.append([arrow_x, arrow_y, math.cos(angle), math.sin(angle)])
        arrow_count -= 1
        
        
def gameplay(bgimage, imgname, weaponimg, win_value, how_many, how_fast, enemy_arrow_speed, arrow_speed):
    global score, health, game_over, enemy_generation_timer, count, start_time, in_progress 
    image(bgimage, 0, 0, width, height)
    main_character_img = loadImage(imgname)
    enemy_generation_timer = 0
    enemy_generation_interval= 2
    max_enemies = how_many
    enemy_speed = how_fast
    
    # Calculate elapsed time
    elapsed_time = (millis() - start_time) // 1000
    
    if not game_over: 
        # Generate enemies at regular intervals
        if len(enemies) < max_enemies and elapsed_time >= enemy_generation_timer + enemy_generation_interval and elapsed_time <= GAME_DURATION and not game_over:
            enemy_x = random.randint(0, width - ENEMY_WIDTH)
            enemy_y = random.randint(0, height // 2 - ENEMY_HEIGHT)
            enemies.append([enemy_x, enemy_y])
            enemy_generation_timer = elapsed_time
        
        # Move and draw the enemies
        for enemy in enemies:
            enemy[0] += enemy_speed
            image(enemy_img, enemy[0], enemy[1], ENEMY_WIDTH, ENEMY_HEIGHT)
            
            # Enemy shooting arrows
            if random.random() < 0.01 and not game_over:  # Probability of shooting arrow
                arrow_x = enemy[0] + ENEMY_WIDTH // 2 - ARROW_WIDTH // 2
                arrow_y = enemy[1] + ENEMY_HEIGHT
                angle = math.atan2(main_character_y - arrow_y, main_character_x - arrow_x)
                enemy_arrows.append([arrow_x, arrow_y, math.cos(angle), math.sin(angle)])
        
        # Move and draw the arrows
        for arrow in arrows:
            arrow[0] += arrow[2] * arrow_speed  # Move the arrow horizontally
            arrow[1] += arrow[3] * arrow_speed  # Move the arrow vertically
            image(weaponimg, arrow[0], arrow[1], ARROW_WIDTH, ARROW_HEIGHT)
            
            # Check for collision with enemies
            for enemy in enemies:
                if (not game_over and arrow[1] + ARROW_HEIGHT >= enemy[1] and arrow[1] <= enemy[1] + ENEMY_HEIGHT and arrow[0] + ARROW_WIDTH >= enemy[0] and arrow[0] <= enemy[0] + ENEMY_WIDTH):
                    score += 1
                    arrows.remove(arrow)
                    enemies.remove(enemy)
                    break
                if (enemy[0] >= width):
                    enemies.remove(enemy)
        
        # Move and draw the enemy arrows
        for enemy_arrow in enemy_arrows:
            enemy_arrow[0] += enemy_arrow[2] * enemy_arrow_speed  # Move the arrow towards the main character on the x-axis
            enemy_arrow[1] += enemy_arrow[3] * enemy_arrow_speed  # Move the arrow towards the main character on the y-axis
            image(weaponimg, enemy_arrow[0], enemy_arrow[1], ARROW_WIDTH, ARROW_HEIGHT)
            
            # Check for collision with main character
            if (enemy_arrow[1] + ARROW_HEIGHT >= main_character_y and enemy_arrow[1] <= main_character_y + MAIN_CHARACTER_HEIGHT and enemy_arrow[0] + ARROW_WIDTH >= main_character_x and enemy_arrow[0] <= main_character_x + MAIN_CHARACTER_WIDTH):
                health -= 1
                enemy_arrows.remove(enemy_arrow)
        
        # Draw the main character
        image(main_character_img, main_character_x, main_character_y, MAIN_CHARACTER_WIDTH, MAIN_CHARACTER_HEIGHT)
        
        # Draw score
        text("Score: " + str(score), 20, 30)
        
        text("Time: " + str(elapsed_time), 20, 70)
        
        text("Arrows left: " + str(arrow_count), 20, 110)
        
        # Draw health bar
        for i in range(health):
            fill(255,0,0)
            rect(10 + i * (HEALTH_BAR_WIDTH + 10), 130, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT)
    
    # Check game over condition
    if (elapsed_time >= GAME_DURATION and score < win_value) or health <= 0:
        game_over = True
        count = 16 
    elif score >= win_value:
        game_over = True
        textSize(32)
        fill(255, 0, 0)
        textAlign(CENTER)
        text("Congratulations", width // 2, height // 2)
        textSize(24)
        text("Final Score: " + str(score), width // 2, height // 2 + 40)
        text("Press Enter to continue", width // 2, height // 2 + 80)
        textAlign(CORNER)
        
def start_new_round():
    global score, health, game_over, enemies, arrows, enemy_arrows, start_time, arrow_count
    score = 0
    health = 3
    arrow_count = 35
    game_over = False
    enemies = []
    arrows = []
    enemy_arrows = []
    start_time = millis() 
