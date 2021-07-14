import pygame
import t3


def tier3window():
    pygame.init()
    RED = (255, 0, 0)
    size = width, height = 800, 850

    font = pygame.font.Font('freesansbold.ttf', 84)
    cost = font.render("", True, RED)
    costrect = cost.get_rect()
    costrect.center = 591, 152

    screen = pygame.display.set_mode(size)

    name = []
    price = 0

    background = pygame.image.load("C:\\Users\\Einar\\Desktop\\Python\\python home projects\\Rust\\img\\tier3finish.png")
    rectbackground = background.get_rect()

    done = False
    clock = pygame.time.Clock()
    while not done:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            screen.blit(background, rectbackground)
            posx = pygame.mouse.get_pos()[0]
            posy = pygame.mouse.get_pos()[1]

#Reinforced Glass Window
            if posx >= 216 and posy >= 31 and posx < 275 and posy < 91:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        if "ReinforcedGlassWindow" not in name:
                            name.append("ReinforcedGlassWindow")
                            price = price + 125
                        else:
                            name.remove("ReinforcedGlassWindow")
                            price = price - 125
                    else:
                            math = t3.reinforcedglasswindow(0) - price
                            cost = font.render(str(math), True, RED)
                            costrect = cost.get_rect()
                            costrect.center = 591, 152
# armored door
            elif posx >= 91 and posy >= 127 and posx < 152 and posy < 185:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        if "armoreddoor" not in name:
                            name.append("armoreddoor")
                            price = price + 500
                        else:
                            name.remove("armoreddoor")
                            price = price - 500
                    else:
                        math = t3.armoreddoor(0) - price
                        cost = font.render(str(math), True, RED)
                        costrect = cost.get_rect()
                        costrect.center = 591, 152

# armored double door
            elif posx >= 91 and posy >= 220 and posx < 152 and posy < 281:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        if "armoreddoubledoor" not in name:
                            name.append("armoreddoubledoor")
                            price = price + 500
                        else:
                            name.remove("armoreddoubledoor")
                            price = price - 500
                    else:
                        math = t3.armoreddoubledoor() - price
                        cost = font.render(str(math), True, RED)
                        costrect = cost.get_rect()
                        costrect.center = 591, 152
# mp5a4
            elif posx >= 217 and posy >= 127 and posx < 275 and posy < 183:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.mp5a4(0)), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
#Weapon Lasersight
            elif posx >= 217 and posy >= 222 and posx < 277 and posy < 280:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.weaponlasersight(0)), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# hv rifle ammo
            elif posx >= 217 and posy >= 314 and posx < 277 and posy < 372:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.hvrifleammo(0)), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# explosive riffle ammo
            elif posx >= 185 and posy >= 409 and posx < 309 and posy < 469:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.explosiverifleammo(0)) + "-750", True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# metal chest plate
            elif posx >= 185 and posy >= 502 and posx < 309 and posy < 561:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.metalchestplate(0)) + "-1625", True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# assault rifle
            elif posx >= 215 and posy >= 594 and posx < 278 and posy < 655:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.assaultrifle(0)), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# bolt action rifle
            elif posx >= 217 and posy >= 690 and posx < 276 and posy < 748:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.boltactionrifle(0)), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# eightx zoom scope
            elif posx >= 217 and posy >= 782 and posx < 278 and posy < 843:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.eightxzoomscope()), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# explosives
            elif posx >= 372 and posy >= 502 and posx < 434 and posy < 561:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.explosives(0)), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# timed explosive charge
            elif posx >= 372 and posy >= 594 and posx < 433 and posy < 654:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.timedexplosivecharge(0)), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152
# rocket
            elif posx >= 373 and posy >= 691 and posx < 432 and posy < 749:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cost = font.render(str(t3.rocket()), True, RED)
                    costrect = cost.get_rect()
                    costrect.center = 591, 152

        screen.blit(cost, costrect)
        pygame.display.flip()

tier3window()