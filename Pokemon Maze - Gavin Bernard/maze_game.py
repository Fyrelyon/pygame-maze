# Imports
import pygame
import intersects
import random
import time

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Pokemon Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

def play():

    # Timer
    clock = pygame.time.Clock()
    refresh_rate = 60
    '''Time with refresh at 60.'''
    i = 0

    '''Time without refresh at 200.'''
    j = 0

    temporal = 5

    '''Speed of Start color change. Changes 200 in j too.'''
    fast = 3

    '''For the Fade effect.'''
    m = fast

    background = pygame.image.load('map_area/grass_type.png')

    # Music
    musics = pygame.mixer.music.load('music/music.wav')

    # Colors
    GREEN = (74, 247, 22)
    GREEN2 = (10,100,5)
    BLUE = (0,255,0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    fade = [200,200,150]
    up = False

    Fade = fast

    r_change = -fast
    g_change = -fast
    #b_change = fast

    f_change = 1

        
    # Make a block
    block =  [375, 250, 50, 50]
    vel = [0, 0]
    speed = 5
    score = 0
    last = True

    charmander_left = pygame.image.load('player_animation/charmander_left.png')
    charmander_right = pygame.image.load('player_animation/charmander_right.png')

    last = False


    # Make Coins
    coins1 = [35,175]
    coins2 = [725,25]
    coins3 = [725,525]
    coins4 = [260,180]
    coins5 = [750,350]
    coins6 = [675,350]
    coins7 = [35,525]
    coins8 = [500,350]
    
    coinslist = [coins1,coins2,coins3,coins4,coins5,coins6,coins7,coins8]
    
    coinlist = []

    for c in coinslist:
        coinlist.append([c[0],c[1],30,30])

    coin1 = pygame.image.load('coin_animation/coin1.png')
    coin2 = pygame.image.load('coin_animation/coin2.png')
    coin3 = pygame.image.load('coin_animation/coin3.png')
    coin4 = pygame.image.load('coin_animation/coin4.png')
    coin5 = pygame.image.load('coin_animation/coin5.png')
    coin6 = pygame.image.load('coin_animation/coin6.png')

    def coin(i):
        for c in coinlist:
            x = c[0]
            y = c[1]

            if 0 <= i <= 10:
                screen.blit(coin1,(x,y))
            if 11 <= i <= 20:
                screen.blit(coin2,(x,y))
            if 21 <= i <= 30:
                screen.blit(coin3,(x,y))
            if 31 <= i <= 40:
                screen.blit(coin4,(x,y))
            if 41 <= i <= 50:
                screen.blit(coin5,(x,y))
            if 51 <= i <= 60:
                screen.blit(coin6,(x,y))

    # make a wall
    ''' walls 1-4 = block outside of range to prevent the player from going out of bounds'''
    wall1 = [-1, 0, 1, 600]
    wall2 = [0, -1, 800, 1]
    wall3 = [0, 600, 800, 1]
    wall4 = [800,0,1,600]

    walls = [wall1, wall2, wall3, wall4]

    grass = pygame.image.load('map_area/grass.png')

    # make an enemy
    en1 = [20,225]
    en2 = [725,275]
    en3 = [660,150]
    en4 = [600,475]
    en5 = [600,545]

    enemylist = [en1,en2,en3,en4,en5]

    enemies = []

    for x in enemylist:
        enemies.append([x[0],x[1],75,52])

    haunter = pygame.image.load('enemy/haunter.png').convert()

    # make a tree

    treelist = []
    treelist1 = []
    treelist2 = []

    '''top 7 trees'''
    tree1 = [30,75]
    tree2 = [110,75]
    tree3 = [190,75]
    tree4 = [270,75]
    tree5 = [350,75]
    tree6 = [430,75]
    tree7 = [590,75]
    '''4 left trees in line'''
    tree8 = [110,155]
    tree9= [110,235]
    tree10 = [110,315]
    tree11 = [110,395]
    '''4 right trees in line'''
    tree12 = [590,155]
    tree13 = [590,235]
    tree14 = [590,315]
    tree15 = [590,395]
    '''bottom 4 trees'''
    tree16 = [510,395]
    tree17 = [430,395]
    tree18 = [350,395]
    tree19 = [270,395]
    '''left-most + right-most'''
    tree20 = [-50,75]
    tree21 = [670,395]
    ''''''
    tree22 = [750,395]
    tree23 = [350,150]
    tree24 = [350,300]

    treelist = [tree1,tree2,tree3,tree4,tree5,tree6,tree7,tree8,tree9,tree10]

    treelist1 = [tree11,tree12,tree13,tree14,tree15,tree16,tree17,tree18,tree19]

    treelist2 = [tree20,tree21,tree22,tree23,tree24]

    '''now add them all together and just use treelist2'''

    treelist2 = treelist + treelist1 + treelist2

    trees = []

    for x in treelist2:
        trees.append([x[0],x[1],72,78])

    # Game loop
    done = False

    # Stages
    start = True
    play = False
    end1 = False
    end2 = False
    one = True

    while not done:
        # Event processing (React to key presses, mouse clicks, etc.)
        ''' for now, we'll just check to see if the X is clicked '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'n'

        state = pygame.key.get_pressed()

        up = state[pygame.K_UP]
        down = state[pygame.K_DOWN]
        left = state[pygame.K_LEFT]
        right = state[pygame.K_RIGHT]
        space = state[pygame.K_SPACE]
        n = state[pygame.K_n]
        y = state[pygame.K_y]
        
        if start:
            if space:
                start = False
                play = True
                pygame.mixer.music.play()

        if play:
            if left:
                vel[0]  = -speed
                last = False
            elif right:
                vel[0]  = speed
                last = True
            else:
                vel[0]  = 0

            if up:
                vel[1] = -speed
            elif down:
                vel[1]  = speed
            else:
                vel[1]  = 0

        if end1 or end2:
            pygame.mixer.music.stop()
            if n:
                return 'n'
            if y:
                return 'y'

        # Game logic (Check for collisions, update points, etc.)

        '''time for animations'''
        i += 1
        j += 1
        Fade += m

        if j > int(200/fast):
            j = 0
            m *= -1

        if i >= 60:
            i = 0
            if play:
                temporal -= 1

        if Fade in range(0,255):
                haunter.set_alpha(int(Fade))
        
        ''' move the block in horizontal direction '''
        block[0] += vel[0]

        ''' resolve collisions '''
        for c in coinlist:
            if intersects.rect_rect(block, c):
                (pygame.mixer.Sound('sounds/ding.wav')).play()
                coinlist.remove(c)
                score += 1
                temporal += 3

        for w in walls:
            if intersects.rect_rect(block, w):
                if vel[0] > 0:
                    block[0] = w[0] - block[2]
                elif vel[0] < 0:
                    block[0] = w[0] + w[2]

        for t in trees:
            if intersects.rect_rect(block, t):
                if vel[0] > 0:
                    block[0] = t[0] - block[2]
                elif vel[0] < 0:
                    block[0] = t[0] + t[2]

        for e in enemies:
            if intersects.rect_rect(block, e):
                if Fade > 150:
                    play = False
                    end1 = True
    
        ''' move the block in vertical direction '''
        block[1] += vel[1]

        ''' resolve collisions '''
        for w in walls:
            if intersects.rect_rect(block, w):
                if vel[1] > 0:
                    block[1] = w[1] - block[2]
                elif vel[1] < 0:
                    block[1] = w[1] + w[3]

        for t in trees:
            if intersects.rect_rect(block, t):
                if vel[1] > 0:
                    block[1] = t[1] - block[2]
                elif vel[1] < 0:
                    block[1] = t[1] + t[3]

        for e in enemies:
            if intersects.rect_rect(block, e):
                if Fade > 150:
                    play = False
                    end1 = True

        
        # Drawing code (Describe the picture. It isn't actually drawn yet.)
        screen.blit(background, (0,0))

        if start or end1 or end2:
            screen.fill(fade)

            if fade[0] + r_change in range(0,200):
                fade[0] += r_change

            if fade[1] + g_change in range(0,200):
                fade[1] += g_change

            #if fade[2] + b_change in range(0,200):
                #fade[2] += b_change

            if j == int(200/fast)/2 or j == int(200/fast):
                
                if fade[0] <= 5:
                    r_change = fast*random.randint(0,1)
                if fade[0] >= 195:
                    r_change = -fast*random.randint(0,1)
                
                if fade[1] <= 5:
                    g_change = fast*random.randint(0,1)
                if fade[1] >= 195:
                    g_change = -fast*random.randint(0,1)
                
                #if fade[2] <= 5:
                    #b_change = fast*random.randint(0,1)
                #if fade[2] >= 195:
                    #b_change = -fast*random.randint(0,1)


        if play:
            coin(i)

            for t in trees:
                screen.blit(grass, (t[0],t[1]))

            for e in enemies:
                screen.blit(haunter, (e[0],e[1]))

            if vel[0] == 0:
                if last == True:
                    screen.blit(charmander_right, (block[0],block[1]))
                else:
                    screen.blit(charmander_left, (block[0],block[1]))

            if vel[0] > 0:
                screen.blit(charmander_right, (block[0],block[1]))
                last = True

            if vel[0] < 0:
                screen.blit(charmander_left, (block[0], block[1]))
                last = False

        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("monospace", 26)

        # render text

        if start:
            myfont = pygame.font.SysFont("monospace", 32)
            
            greetings = myfont.render("Welcome to Maze Game!", 1, (WHITE))

            gret = greetings.get_rect(center=(400, 200))
            
            greetings2 = myfont.render("Press SPACE to Begin", 1, (WHITE))

            gret2 = greetings2.get_rect(center=(400, 250))

            if i <= 30:
                screen.blit(greetings, gret)
                screen.blit(greetings2, gret2)


        if play:
            scores = myfont.render("Score: " + str(score) + "/8", 1, (WHITE))
            screen.blit(scores, (25, 15))

            times = myfont.render("Time Remaining: " + str(temporal), 1, (WHITE))

            if temporal > 10:
                screen.blit(times, (25, 40))

            if temporal <= 10:
                times = myfont.render("Time Remaining: " + str(temporal), 1, (WHITE))
            
                if i >= 30:
                    screen.blit(times, (25, 40))
        

        if end1:
            myfont = pygame.font.SysFont("monospace", 40)
            
            ending1 = myfont.render("Game Over", 1, (WHITE))
            
            endnum1 = ending1.get_rect(center=(400, 200))
            
            ending2 = myfont.render("You Lose!", 1, (WHITE))

            endnum2 = ending2.get_rect(center=(400, 300))

            restart = myfont.render("Play again? (y/n)", 1, (WHITE))

            re = restart.get_rect(center=(400, 450))

            if i <= 30:
                screen.blit(restart, re)
                
            if one:
                (pygame.mixer.Sound('sounds/lose.wav')).play()

            one = False

            screen.blit(ending1, endnum1)
            screen.blit(ending2, endnum2)


        if end2:
            myfont = pygame.font.SysFont("monospace", 40)
            
            ending1 = myfont.render("Congratulations,", 1, (WHITE))

            endnum1 = ending1.get_rect(center=(400, 200))
            
            ending2 = myfont.render("You Win!", 1, (WHITE))

            endnum2 = ending2.get_rect(center=(400, 300))

            restart = myfont.render("Play again? (y/n)", 1, (WHITE))

            re = restart.get_rect(center=(400, 450))

            if i <= 30:
                screen.blit(restart, re)

            if one:
                (pygame.mixer.Sound('sounds/win.wav')).play()

            one = False

            screen.blit(ending1, endnum1)
            screen.blit(ending2, endnum2)


        if score >= 8:
            play = False
            end2 = True

        if temporal <= 0:
            play = False
            end1 = True

        # Update screen (Actually draw the picture in the window.)
        pygame.display.flip()


        # Limit refresh rate of game loop 
        clock.tick(refresh_rate)


# Only two returns: "n" and "y", therefore "y" resets and "n" ends
while play() != 'n':
    print("Restart.")

# Close window and quit
pygame.quit()
