import pygame
import tier3engine
import os

x = 1920 // 4
y = 150

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

def boot():
    global on
    pygame.init()

    size = width, height = 800, 300

    black = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0

    font = pygame.font.Font('freesansbold.ttf', 32)
    #WORKBENCH 1
        #Img
    t1 = pygame.image.load("C:\\Users\\Einar\\Desktop\\Python\\python home projects\\Rust\\img\\workbench1.png")
    rect1 = t1.get_rect()
    rect1.center = 266 // 2, height // 2
        #Text
    t1text = font.render('Workbench 1', True, RED)
    text1Rect = t1text.get_rect()
    text1Rect.center = 266 // 2, height // 2 - 100


    #WORKBENCH 2
        #Img
    t2 = pygame.image.load("C:\\Users\\Einar\\Desktop\\Python\\python home projects\\Rust\\img\\workbench2.png")
    rect2 = t2.get_rect()
    rect2.center = width // 2, height // 2
        #Text
    t2text = font.render('Workbench 2', True, RED)
    text2Rect = t2text.get_rect()
    text2Rect.center = width // 2, height // 2 - 100


    #WORKBENCH 3
        #Img
    t3 = pygame.image.load("C:\\Users\\Einar\\Desktop\\Python\\python home projects\\Rust\\img\\workbench3.png")
    rect3 = t3.get_rect()
    rect3.center = 680, height // 2
        #Text
    t3text = font.render('Workbench 3', True, RED)
    text3Rect = t3text.get_rect()
    text3Rect.center = 680, height // 2 - 100


    screen = pygame.display.set_mode(size)

    done = False
    clock = pygame.time.Clock()

    score1 = 0
    score2 = 0
    score3 = 0
    slider = 10
    # MAIN LOOP
    while not done:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                on = False
            screen.fill(black)
            posx = pygame.mouse.get_pos()[0]
            posy = pygame.mouse.get_pos()[1]

    #WORKBENCH1
            if posx >= 100 and posy >= 105 and posx < 170 and posy < 190:
                if event.type == pygame.MOUSEBUTTONDOWN:
    # ON MOUSE CLICK
                    print("click")
                if score1 <= 240:
                    score1 = score1 + 10
                pygame.draw.rect(screen, (0 + score1, 0 + score1, 0 + score1), [0, 0, 266, 300])

            else:
                if score1 > 0:
                    score1 = score1 - 20
    # WORKBENCH2
            if posx >= 365 and posy >= 105 and posx < 440 and posy < 190:
                if event.type == pygame.MOUSEBUTTONDOWN:
    # ON MOUSE CLICK
                    print("click")
                if score2 <= 240:
                    score2 = score2 + 10
                pygame.draw.rect(screen, (0 + score2, 0 + score2, 0 + score2), [268, 0, 266, 300])
            else:
                if score2 > 0:
                    score2 = score2 - 20
    # WORKBENCH3
            if posx >= 650 and posy >= 105 and posx < 720 and posy < 190:
                if event.type == pygame.MOUSEBUTTONDOWN:
    #ON MOUSE CLICK
                    print("click")
                    tier3engine.tier3window()
                    done = True
                if score3 <= 240:
                    score3 = score3 + 10
                pygame.draw.rect(screen, (0 + score3, 0 + score3, 0 + score3), [534, 0, 800, 300])
            else:
                if score3 > 0:
                    score3 = score3 - 20



        # screen.fill(black)
        pygame.draw.line(screen, WHITE, [266, 0], [266, 300], 2)
        pygame.draw.line(screen, WHITE, [532, 0], [532, 300], 2)


        screen.blit(t1text, text1Rect)
        screen.blit(t2text, text2Rect)
        screen.blit(t3text, text3Rect)
        screen.blit(t1, rect1)
        screen.blit(t2, rect2)
        screen.blit(t3, rect3)

        pygame.display.flip()
on = True
while on:
    boot()