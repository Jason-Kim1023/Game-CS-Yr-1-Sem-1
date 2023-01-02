"""
CS1111 PROJECT: Jason Kim
Previously, in CP1 we were going to do fire boy and water girl, but we decided to change the idea.
This game is inspired by Johnny Upgrade - a game where you are racing against time to collect coins and buy upgrades in
                                            a shop to get to the final boss and survive!
                                            
Imported: pygame and gamebox (for the game development),
          math (for distance calculation),
          random (for randomizing spawning for final boss)

In the game, you can find a lot of the features easily.
To list them: User Input,
              Start Screen,
              Game Over,
              Small Enough Window,
              Graphics,
              Restart from Game Over,
              Sprite Animation,
              Enemies,
              Collectables,
              Scrolling Level,
              Timer, etc.
"""
import pygame
import gamebox
import math
import random

# This is main game interface items that is presented on the screen.
# There is the character and the enemies and the character's animation
camera = gamebox.Camera(800, 600)
character_Sheet = gamebox.load_sprite_sheet("mc.png", 1, 8)
character_FSheet = gamebox.load_sprite_sheet("flipmc.png", 1, 8)
character_Frame = 0
character = gamebox.from_image(50, 50, character_Sheet[character_Frame])
character.yspeed = 0
evilminion_Sheet = gamebox.load_sprite_sheet("mosterminion.png", 4, 6)
evilminion_Frame = 0
evilminions = [
    gamebox.from_image(2500, 1275, evilminion_Sheet[evilminion_Frame]),
    gamebox.from_image(550, 370, evilminion_Sheet[evilminion_Frame]),
    gamebox.from_image(300, 1570, evilminion_Sheet[evilminion_Frame]),
    gamebox.from_image(-1600, 3965, evilminion_Sheet[evilminion_Frame]),
    gamebox.from_image(-200, 3965, evilminion_Sheet[evilminion_Frame])
]

# Global variables for the game
counter = 0
monster_counter = 0
timevart = 30
timevar = 30
direction = 0
lifet = 3
life = 3
coinst = 0
coins = 3
ammot = 1
ammo = 3
score = 1
touchcounter = 0
bullettutspeed = 20
bulletstut = []
bullets = []
y = [6]
y1 = [6]
y2 = [6]
y3 = [6]
y4 = [6]
elevator_speed = [5]
tut_speed = 5
r_speed = 5
tut_jump = -15
r_jump = -15
a_t_s_u = 0
a_t_t_u = 0
a_t_j_u = 0
r_t_s_u = 0
r_t_t_u = 0
r_t_j_u = 0
xt = 0
x = 0
final_enemies = []

# Screen Managers
main_screen_text1 = gamebox.from_text(400, 300, "CS UPGRADE!", 100, "blue")
main_screen_text2 = gamebox.from_text(400, 200, "Press Enter to Start!", 50, "white")
main_screen_on = 1
shop_tut_screen = 0
tutorial_screen_on = 0
dead_tutorial_screen = 0
dead_screen = 0
shop_screen = 0
win_screen = 0

# walls and floor for tutorial
tutorial_walls = [
    gamebox.from_image(100, 590, "groundImage.jpeg"),
    gamebox.from_image(400, 590, "groundImage.jpeg"),
    gamebox.from_image(-200, 590, "groundImage.jpeg"),
    gamebox.from_image(700, 590, "groundImage.jpeg"),
    gamebox.from_image(1000, 700, "groundImage.jpeg"),
    gamebox.from_image(1300, 590, "groundImage.jpeg"),
    gamebox.from_image(1300, 890, "groundImage.jpeg"),
    gamebox.from_image(1300, 1190, "groundImage.jpeg"),
    gamebox.from_image(1900, 590, "groundImage.jpeg"),
    gamebox.from_image(1900, 290, "groundImage.jpeg"),
    gamebox.from_image(1900, 0, "groundImage.jpeg"),
    gamebox.from_image(1300, 1490, "groundImage.jpeg"),
    gamebox.from_image(1600, 1490, "groundImage.jpeg"),
    gamebox.from_image(1900, 1490, "groundImage.jpeg"),
    gamebox.from_image(2200, 1490, "groundImage.jpeg"),
    gamebox.from_image(1900, 890, "groundImage.jpeg"),
    gamebox.from_image(2200, 890, "groundImage.jpeg"),
    gamebox.from_image(2500, 1490, "groundImage.jpeg"),
    gamebox.from_image(2500, 890, "groundImage.jpeg"),
    gamebox.from_image(2800, 890, "groundImage.jpeg"),
    gamebox.from_image(2800, 1190, "groundImage.jpeg"),
    gamebox.from_image(2800, 1490, "groundImage.jpeg")
]

# Spikes used in the tutorial stage
tutorial_spikes = [
    gamebox.from_image(1000, 490, "http://www.clker.com/cliparts/a/R/p/k/g/4/spikes-md.png")
]

tutorial_ledge = [
    gamebox.from_image(1700, 500, "rockledge.png"),
    gamebox.from_image(1500, 800, "rockledge.png"),
    gamebox.from_image(1500, 1200, "rockledge.png")
]
tutorial_ledge[1].flip()
tutorial_ledge[2].flip()

# in game text descriptions in tutorial
descriptions = [
    gamebox.from_text(350, 50,
                      "Welcome to CS UPGRADE!  Above is the time, use L and R arrows to move! This is a tutorial, "
                      "follow the arrows!",
                      20, "black"),
    gamebox.from_text(400, 100,
                      "If you run out of time, you will start again at the start at the shop! Collect coins and when "
                      "you die, buy upgrades to complete game!",
                      20, "black"),
    gamebox.from_text(1000, 200, "Use the Space Bar to jump!  AVOID THESE SPIKES! They will take away a life!", 20,
                      "black"),
    gamebox.from_text(1000, 300,
                      "If you lose a life, you will be placed before the next spike or danger.  If you lose all your "
                      "lives, you die and start over at the shop",
                      20, "black"),
    gamebox.from_text(1600, 650, "THERE IS A LASER BELOW! YOU WILL LOSE A LIFE IF YOU HIT IT", 12, "black"),
    gamebox.from_text(1800, 1075,
                      "Use A Button to shoot LEFT and D button to shoot RIGHT!  Shoot the monster to collect the "
                      "coins! BE CAREFUL!  IT WILL TAKE A LIFE!",
                      15, "black"),
    gamebox.from_text(1750, 1100,
                      "Coins are used to upgrade speed, jump power, and buy ammo!  For now, we gave you one ammo for "
                      "this tutorial!",
                      15, "black"),
    gamebox.from_text(1800, 1125,
                      "Get the coins displayed at top right and ammo displayed top left!  After you kill the monster, "
                      "head to the portal to start the game!",
                      15, "black"),
    gamebox.from_text(400, 300, "You Died", 100, "Red"),
    gamebox.from_text(400, 400, "Press Enter to respawn at shop.", 50, "white"),
    gamebox.from_text(650, 150, "Tap the buttons to buy upgrade!", 20, "black"),
    gamebox.from_text(650, 200, "Once done, press "'0'" to go back to game!", 20, "black"),
    gamebox.from_text(400, 300, "You WON", 100, "blue"),
    gamebox.from_text(400, 400, "Congratulations You Have Upgraded and Defeated all the BUGS!", 30, "white"),
]

# In game collectable coins for tutorial
ingame_coinst = [
    gamebox.from_image(1700, 1300, "bitcoin.png"),
    gamebox.from_image(2000, 1300, "bitcoin.png"),
    gamebox.from_image(2300, 1300, "bitcoin.png"),
    gamebox.from_image(500, 400, "bitcoin.png"),
    gamebox.from_image(700, 400, "bitcoin.png"),
    gamebox.from_image(1000, 350, "bitcoin.png")
]

# In game collectable coins for actual game
coinslist = [
    gamebox.from_image(500, 400, "bitcoin.png"),
    gamebox.from_image(700, 400, "bitcoin.png"),
    gamebox.from_image(990, 250, "bitcoin.png"),
    gamebox.from_image(300, 1600, "bitcoin.png"),
    gamebox.from_image(100, 1600, "bitcoin.png"),
    gamebox.from_image(-200, 1450, "bitcoin.png"),
    gamebox.from_image(-500, 1300, "bitcoin.png"),
    gamebox.from_image(-1400, 850, "bitcoin.png"),
    gamebox.from_image(-1600, 3970, "bitcoin.png"),
    gamebox.from_image(-1000, 3970, "bitcoin.png"),
    gamebox.from_image(-400, 3970, "bitcoin.png")
]

# arrows to guide players
arrows = [
    gamebox.from_image(300, 200, "arrow.png"),
    gamebox.from_image(1570, 200, "arrowdown.png")
]

# THESE ARE SPIKES THAT WILL RESULT IN A LOSS OF LIFE
spikes = [
    gamebox.from_image(1000, 480, "http://www.clker.com/cliparts/a/R/p/k/g/4/spikes-md.png"),
    gamebox.from_image(-200, 1680, "http://www.clker.com/cliparts/a/R/p/k/g/4/spikes-md.png"),
    gamebox.from_image(-1400, 1090, "http://www.clker.com/cliparts/a/R/p/k/g/4/spikes-md.png")
]

# Invisible barriers for the monsters to bounce off of
invisible_bar = [
    gamebox.from_color(300, 380, "light blue", 10, 100),
    gamebox.from_color(850, 380, "light blue", 10, 100),
    gamebox.from_color(500, 1580, "light blue", 10, 100),
    gamebox.from_color(-50, 1580, "light blue", 10, 100),
    gamebox.from_color(-500, 1500, "light blue", 150, 10),
    gamebox.from_color(-500, 1000, "light blue", 150, 10),
    gamebox.from_color(-1800, 3950, "light blue", 10, 100),
    gamebox.from_color(-900, 3950, "light blue", 10, 100),
    gamebox.from_color(-880, 3950, "light blue", 10, 100),
    gamebox.from_color(0, 3950, "light blue", 10, 100),
    gamebox.from_color(100, 3890, "light blue", 10, 270)
]

# This is the elevator that is going up and down in the main game
elevator = gamebox.from_color(-500, 1300, "dark gray", 150, 10)

# THIS IS FOR ALL THE BLOCKS THAT THE USER WILL BE STANDING ON
walls_level1 = [
    # platforms
    gamebox.from_color(990, 300, "brown", 150, 10),
    gamebox.from_color(-200, 1500, "brown", 150, 10),
    gamebox.from_color(-1400, 900, "brown", 150, 10),
    # ground
    gamebox.from_image(100, 590, "groundImage.jpeg"),
    gamebox.from_image(400, 590, "groundImage.jpeg"),
    gamebox.from_image(-200, 590, "groundImage.jpeg"),
    gamebox.from_image(700, 590, "groundImage.jpeg"),
    gamebox.from_image(1000, 700, "groundImage.jpeg"),
    gamebox.from_image(1300, 590, "groundImage.jpeg"),
    gamebox.from_image(1300, 890, "groundImage.jpeg"),
    gamebox.from_image(1300, 1190, "groundImage.jpeg"),
    gamebox.from_image(1900, 590, "groundImage.jpeg"),
    gamebox.from_image(1900, 290, "groundImage.jpeg"),
    gamebox.from_image(1900, 0, "groundImage.jpeg"),
    gamebox.from_image(1900, 890, "groundImage.jpeg"),
    gamebox.from_image(1900, 1190, "groundImage.jpeg"),
    gamebox.from_image(1900, 1490, "groundImage.jpeg"),
    gamebox.from_image(1900, 1790, "groundImage.jpeg"),
    gamebox.from_image(2100, 0, "groundImage.jpeg"),
    gamebox.from_image(2100, 590, "groundImage.jpeg"),
    gamebox.from_image(2100, 290, "groundImage.jpeg"),
    gamebox.from_image(2100, 890, "groundImage.jpeg"),
    gamebox.from_image(2100, 1190, "groundImage.jpeg"),
    gamebox.from_image(2100, 1490, "groundImage.jpeg"),
    gamebox.from_image(2100, 1790, "groundImage.jpeg"),
    gamebox.from_image(1900, 1790, "groundImage.jpeg"),
    gamebox.from_image(1600, 1790, "groundImage.jpeg"),
    gamebox.from_image(1300, 1790, "groundImage.jpeg"),
    gamebox.from_image(1000, 1790, "groundImage.jpeg"),
    gamebox.from_image(700, 1790, "groundImage.jpeg"),
    gamebox.from_image(400, 1790, "groundImage.jpeg"),
    gamebox.from_image(100, 1790, "groundImage.jpeg"),
    gamebox.from_image(-500, 1790, "groundImage.jpeg"),
    gamebox.from_image(-800, 1790, "groundImage.jpeg"),
    gamebox.from_image(-800, 1490, "groundImage.jpeg"),
    gamebox.from_image(-800, 1190, "groundImage.jpeg"),
    gamebox.from_image(980, 1190, "groundImage.jpeg"),
    gamebox.from_image(680, 1190, "groundImage.jpeg"),
    gamebox.from_image(680, 890, "groundImage.jpeg"),
    gamebox.from_image(680, 590, "groundImage.jpeg"),
    gamebox.from_image(-480, 590, "groundImage.jpeg"),
    gamebox.from_image(-780, 590, "groundImage.jpeg"),
    gamebox.from_image(-1080, 590, "groundImage.jpeg"),
    gamebox.from_image(-1380, 590, "groundImage.jpeg"),
    gamebox.from_image(-1680, 590, "groundImage.jpeg"),
    gamebox.from_image(-1980, 590, "groundImage.jpeg"),
    gamebox.from_image(-2280, 590, "groundImage.jpeg"),
    gamebox.from_image(-1100, 1190, "groundImage.jpeg"),
    gamebox.from_image(-1700, 1190, "groundImage.jpeg"),
    gamebox.from_image(-1700, 1490, "groundImage.jpeg"),
    gamebox.from_image(-1700, 1790, "groundImage.jpeg"),
    gamebox.from_image(-1700, 2090, "groundImage.jpeg"),
    gamebox.from_image(-1700, 2390, "groundImage.jpeg"),
    gamebox.from_image(-1700, 2690, "groundImage.jpeg"),
    gamebox.from_image(-1700, 2990, "groundImage.jpeg"),
    gamebox.from_image(-1700, 3290, "groundImage.jpeg"),
    gamebox.from_image(-2280, 890, "groundImage.jpeg"),
    gamebox.from_image(-2280, 1190, "groundImage.jpeg"),
    gamebox.from_image(-2280, 1490, "groundImage.jpeg"),
    gamebox.from_image(-2280, 1790, "groundImage.jpeg"),
    gamebox.from_image(-2280, 2090, "groundImage.jpeg"),
    gamebox.from_image(-2280, 2390, "groundImage.jpeg"),
    gamebox.from_image(-2280, 2690, "groundImage.jpeg"),
    gamebox.from_image(-2280, 2990, "groundImage.jpeg"),
    gamebox.from_image(-2280, 3290, "groundImage.jpeg"),
    gamebox.from_image(-2280, 3590, "groundImage.jpeg"),
    gamebox.from_image(-2280, 3890, "groundImage.jpeg"),
    gamebox.from_image(-2280, 4190, "groundImage.jpeg"),
    gamebox.from_image(-1980, 4190, "groundImage.jpeg"),
    gamebox.from_image(-1680, 4190, "groundImage.jpeg"),
    gamebox.from_image(-1390, 4190, "groundImage.jpeg"),
    gamebox.from_image(-1080, 4190, "groundImage.jpeg"),
    gamebox.from_image(-780, 4190, "groundImage.jpeg"),
    gamebox.from_image(-480, 4190, "groundImage.jpeg"),
    gamebox.from_image(-180, 4190, "groundImage.jpeg"),
    gamebox.from_image(120, 4190, "groundImage.jpeg"),
    gamebox.from_image(-1400, 3290, "groundImage.jpeg"),
    gamebox.from_image(-1100, 3290, "groundImage.jpeg"),
    gamebox.from_image(-800, 3290, "groundImage.jpeg"),
    gamebox.from_image(-500, 3290, "groundImage.jpeg"),
    gamebox.from_image(-200, 3290, "groundImage.jpeg"),
    gamebox.from_image(100, 3290, "groundImage.jpeg"),
    gamebox.from_image(100, 3590, "groundImage.jpeg"),
    gamebox.from_image(400, 3590, "groundImage.jpeg"),
    gamebox.from_image(700, 3590, "groundImage.jpeg"),
    gamebox.from_image(1000, 3590, "groundImage.jpeg"),
    gamebox.from_image(1300, 3590, "groundImage.jpeg"),
    gamebox.from_image(1500, 3590, "groundImage.jpeg"),
    gamebox.from_image(120, 4490, "groundImage.jpeg"),
    gamebox.from_image(120, 4790, "groundImage.jpeg"),
    gamebox.from_image(120, 5090, "groundImage.jpeg"),
    gamebox.from_image(420, 5090, "groundImage.jpeg"),
    gamebox.from_image(720, 5090, "groundImage.jpeg"),
    gamebox.from_image(1020, 5090, "groundImage.jpeg"),
    gamebox.from_image(1320, 5090, "groundImage.jpeg"),
    gamebox.from_image(1500, 5090, "groundImage.jpeg"),
    gamebox.from_image(1500, 4790, "groundImage.jpeg"),
    gamebox.from_image(1500, 4690, "groundImage.jpeg"),
    gamebox.from_image(1500, 4390, "groundImage.jpeg"),
    gamebox.from_image(1500, 4090, "groundImage.jpeg"),
    gamebox.from_image(1500, 3890, "groundImage.jpeg"),
]


def tick(keys):
    """
    This contains everything:  All the screens that utilize global variables to switch on and off the screens
                                            (essentially utilizing global variables to scene manage)
                               User Input (Through movement and buying through shop screens),
                               Start Screen (There is a start screen before game actually starts),
                               Game Over (there is a lives system that shows game over screen if character dies),
                               Small Enough Window (window is kept at a small size),
                               Graphics and Images (the characters are animated and there are many sprites),
                               Restart From Game Over (game restarts if player dies),
                               Sprite Animation (there is a sprite animation for the enemies an the main character),
                               Enemies (there are enemies and there is a final enemy level with a bunch of bugs that
                                        try to kill you),
                               Collectables (there are coins to collect and use for buying upgrades),
                               Scrolling Level (the map is a lot larger than the screen),
                               Timer (there is a timer and you will die if time runs out), etc.
    """
    global score
    global dead_tutorial_screen
    global main_screen_on
    global life
    global tutorial_screen_on
    global evilminion_Frame
    global counter
    global direction
    global touchcounter
    global y
    global coinst
    global ammot
    global lifet
    global shop_tut_screen
    global a_t_s_u
    global a_t_j_u
    global a_t_t_u
    global tut_jump
    global tut_speed
    global character_Frame
    global timevart
    global timevar
    global xt
    global x
    global r_speed
    global r_jump
    global coins
    global ammo
    global bullets
    global dead_screen
    global shop_screen
    global r_t_s_u
    global r_t_t_u
    global r_t_j_u
    global elevator
    global monster_counter
    global win_screen

    monster_counter += 1

    # This is for the main screen
    if main_screen_on == 1:
        camera.clear("black")
        camera.draw(main_screen_text1)
        camera.draw(main_screen_text2)
        if pygame.K_RETURN in keys:
            tutorial_screen_on += 1
            main_screen_on = 0
        camera.display()
        return

    # This is for a new scene after the main screen for tutorial
    if tutorial_screen_on == 1:
        camera.clear("light blue")
        camera.draw(descriptions[0])
        camera.draw(descriptions[1])
        camera.draw(descriptions[2])
        camera.draw(descriptions[3])
        camera.draw(descriptions[4])
        camera.draw(descriptions[5])
        camera.draw(descriptions[6])
        camera.draw(descriptions[7])
        camera.draw(arrows[0])
        camera.draw(arrows[1])
        camera.draw(tutorial_ledge[0])
        camera.draw(tutorial_ledge[1])
        camera.draw(tutorial_ledge[2])
        character.yspeed += 1
        character.y = character.y + character.yspeed
        # Camera follows player
        camera.y = character.y - 150
        camera.x = character.x

        # shop code for tutorial
        shop_for_tut = gamebox.from_image(-200, 225, "shopp.png")
        camera.draw(shop_for_tut)
        if character.touches(shop_for_tut):
            character.move_both_to_stop_overlapping(shop_for_tut)

        # portal
        portal_to_main = gamebox.from_image(2550, 1200, "portal.png")
        camera.draw(portal_to_main)
        if character.touches(portal_to_main):
            tutorial_screen_on = 0
            character.x = 50
            character.y = 50

        # evil minion pathing
        # tutorial evil minion
        if evilminions[0].touches(tutorial_walls[20]):
            evilminions[0].move_to_stop_overlapping(tutorial_walls[20])
        elif evilminions[0].touches(tutorial_walls[7]):
            evilminions[0].move_to_stop_overlapping(tutorial_walls[7])

        if character.touches(evilminions[0]):
            character.x = 1500
            character.y = 1000
            lifet -= 1

        if evilminions[0].right_touches(tutorial_walls[20]):
            touchcounter += 1
            y.remove(6)
            y.append(-6)
            if touchcounter == 1:
                evilminions[0].flip()
            touchcounter = 0
        elif evilminions[0].left_touches(tutorial_walls[7]):
            touchcounter += 1
            y.remove(-6)
            y.append(6)
            if touchcounter == 1:
                evilminions[0].flip()
            touchcounter = 0
        evilminions[0].x += y[0]

        # animation section for evil minions
        evilminion_Frame += 1
        if evilminion_Frame == 24:
            evilminion_Frame = 0
        if counter % 1 == 0:
            evilminions[0].image = evilminion_Sheet[evilminion_Frame + direction * 2]
        camera.draw(evilminions[0])

        # player movement and animation
        if pygame.K_RIGHT in keys:
            character.x += tut_speed
            character_Frame += 1
            if character_Frame == 8:
                character_Frame = 0
            if counter % 11 == 0:
                character.image = character_Sheet[character_Frame]
        if pygame.K_LEFT in keys:
            character.x -= tut_speed
            character_Frame += 1
            if character_Frame == 8:
                character_Frame = 0
            if counter % 11 == 0:
                character.image = character_FSheet[character_Frame]

        # Makes sure that jumping works and that the character doesnt fall through the walls
        for wallt in tutorial_walls:
            if character.bottom_touches(wallt):
                character.yspeed = 0
                if pygame.K_SPACE in keys:
                    character.yspeed = tut_jump
            if character.touches(wallt):
                character.move_to_stop_overlapping(wallt)
            camera.draw(wallt)

        # the life system (lose a life if touch tutorial spike)
        if character.bottom_touches(tutorial_spikes[0]):
            character.x = 700
            character.y = 300
            lifet -= 1
        camera.draw(tutorial_spikes[0])

        # this is all the timer stuff
        score -= 1
        seconds = str(int((score / ticks_per_second) % timevart)).zfill(2)
        timer = gamebox.from_text(camera.x, camera.y - 280, seconds, 30, "red")
        if seconds == "01":
            xt += 1
        if seconds == "01" and xt > 1:
            dead_tutorial_screen += 1
            tutorial_screen_on -= 1

        # Code for ledges
        for ledget in tutorial_ledge:
            if character.bottom_touches(ledget):
                character.yspeed = 0
                if pygame.K_SPACE in keys:
                    character.yspeed = -18
            if character.touches(ledget):
                character.move_to_stop_overlapping(ledget)

        # TUTORIAL CODE FOR LASERS
        lasers = []
        if int(seconds) % 2 == 0:
            lasers.append(gamebox.from_color(1600, 840, "red", 280, 40))
        elif int(seconds) % 2 == 1:
            lasers.append(gamebox.from_color(1600, 840, "lightblue", 280, 40))
        camera.draw(lasers[0])
        for i in range(0, len(lasers), 2):
            if character.touches(lasers[i]) and int(seconds) % 2 == 0:
                character.x = 1300
                character.y = 200
                lifet -= 1

        # coin drawing and coin system
        coin_icont = gamebox.from_image(camera.x - 360, camera.y - 250, "bitcoin.png")
        coin_textt = gamebox.from_text(camera.x - 300, camera.y - 250, ": " + str(coinst), 50, "black")
        camera.draw(coin_textt)
        camera.draw(coin_icont)

        for coinstut in ingame_coinst:
            if character.touches(coinstut):
                coinstut.x = -4000
                coinstut.y = 4000
                coinst += 1

        camera.draw(ingame_coinst[0])
        camera.draw(ingame_coinst[1])
        camera.draw(ingame_coinst[2])
        camera.draw(ingame_coinst[3])
        camera.draw(ingame_coinst[4])
        camera.draw(ingame_coinst[5])

        # gun drawing
        gun_icont = gamebox.from_image(camera.x + 300, camera.y - 250, "toygun.png")
        gun_textt = gamebox.from_text(camera.x + 360, camera.y - 250, ": " + str(ammot), 50, "black")
        camera.draw(gun_textt)
        camera.draw(gun_icont)

        # CODE FOR BULLETS IN TUTORIAL
        if pygame.K_a in keys and ammot > 0:
            bullet = gamebox.from_color(character.x, character.y, "dark green", 20, 10)
            bullet.xspeed = -bullettutspeed
            bulletstut.append(bullet)
            ammot -= 1
            keys.clear()
        if pygame.K_d in keys and ammot > 0:
            bullet = gamebox.from_color(character.x, character.y, "dark green", 20, 10)
            bullet.xspeed = bullettutspeed
            bulletstut.append(bullet)
            ammot -= 1
            keys.clear()
        for bullet in bulletstut:
            bullet.y += bullet.yspeed
            bullet.x += bullet.xspeed

            if math.sqrt((character.x - bullet.x) ** 2) > 400:
                bullet.x = -10000
                bullet.y = 10000

            for enemy in evilminions:
                if bullet.touches(enemy):
                    enemy.x = -4000
                    enemy.y = 4000
            camera.draw(bullet)

        # this is all the life stuff and description
        descrip_life = gamebox.from_text(camera.x + 250, camera.y + 230, "This is where your lives will be shown.", 20,
                                         "black")
        lifeTextt = gamebox.from_text(camera.x + 250, camera.y + 270, "Lives: " + str(lifet), 50, "black")
        camera.draw(lifeTextt)
        camera.draw(descrip_life)

        if lifet == 0:
            dead_tutorial_screen += 1
            tutorial_screen_on -= 1

        camera.draw(timer)
        # draw character
        camera.draw(character)

        camera.display()
        return

    # Dead tutorial screen
    if dead_tutorial_screen == 1:
        camera.x = 400
        camera.y = 400
        camera.clear("black")
        camera.draw(descriptions[8])
        camera.draw(descriptions[9])
        if pygame.K_RETURN in keys:
            dead_tutorial_screen = 0
            shop_tut_screen += 1
            lifet = 3
            character.x = 0
            character.y = 50
        camera.display()
        return

    # shop for tutorial screen
    if shop_tut_screen == 1:
        camera.x = 400
        camera.y = 400
        camera.clear("beige")

        ingame_coinst[0].x = 500
        ingame_coinst[0].y = 400
        ingame_coinst[1].x = 700
        ingame_coinst[1].y = 400
        ingame_coinst[2].x = 1000
        ingame_coinst[2].y = 350
        ingame_coinst[3].x = 1700
        ingame_coinst[3].y = 1300
        ingame_coinst[4].x = 2000
        ingame_coinst[4].y = 1300
        ingame_coinst[5].x = 2300
        ingame_coinst[5].y = 1300

        speed_tut_upgrade = gamebox.from_text(150, 225, "SPEED: 1 COIN", 50, "red")
        time_tut_upgrade = gamebox.from_text(150, 350, "TIME: 1 COIN", 50, "red")
        jump_tut_upgrade = gamebox.from_text(220, 475, "JUMP POWER: 1 COIN", 50, "red")
        ammo_tut_upgrade = gamebox.from_text(150, 600, "AMMO: 1 COIN", 50, "red")
        upgradeBtn_tut = [
            gamebox.from_image(360, 225, "upgradebutton1.png"),
            gamebox.from_image(360, 350, "upgradebutton2.png"),
            gamebox.from_image(500, 475, "upgradebutton3.png"),
            gamebox.from_image(360, 600, "upgradebutton4.png")
        ]
        coin_iconshopt = gamebox.from_image(600, 350, "bitcoin.png")
        coin_textshopt = gamebox.from_text(650, 350, ": " + str(coinst), 50, "black")
        gun_iconshopt = gamebox.from_image(600, 275, "toygun.png")
        gun_textshopt = gamebox.from_text(650, 275, ": " + str(ammot), 50, "black")
        camera.draw(upgradeBtn_tut[0])
        camera.draw(upgradeBtn_tut[1])
        camera.draw(upgradeBtn_tut[2])
        camera.draw(upgradeBtn_tut[3])
        camera.draw(speed_tut_upgrade)
        camera.draw(time_tut_upgrade)
        camera.draw(jump_tut_upgrade)
        camera.draw(ammo_tut_upgrade)
        camera.draw(descriptions[10])
        camera.draw(descriptions[11])
        camera.draw(coin_iconshopt)
        camera.draw(coin_textshopt)
        camera.draw(gun_iconshopt)
        camera.draw(gun_textshopt)

        # This is setting new values when they upgrade
        if (pygame.K_1 in keys) and (coinst > 0) and (a_t_s_u <= 2):
            tut_speed += 2
            a_t_s_u += 1
            coinst -= 1
            keys.clear()
        if (pygame.K_2 in keys) and (coinst > 0) and (a_t_t_u <= 2):
            timevart += 24
            a_t_t_u += 1
            coinst -= 1
            keys.clear()
        if (pygame.K_3 in keys) and (coinst > 0) and (a_t_j_u <= 2):
            tut_jump -= 2
            a_t_j_u += 1
            coinst -= 1
            keys.clear()
        if (pygame.K_4 in keys) and (coinst > 0) and (ammot <= 2):
            ammot += 1
            coinst -= 1
            keys.clear()

        if a_t_s_u == 3:
            maxt1 = gamebox.from_text(360, 225, "MAX", 50, "red", bold=True)
            camera.draw(maxt1)
        if a_t_t_u == 3:
            maxt2 = gamebox.from_text(360, 350, "MAX", 50, "red", bold=True)
            camera.draw(maxt2)
        if a_t_j_u == 3:
            maxt3 = gamebox.from_text(500, 475, "MAX", 50, "red", bold=True)
            camera.draw(maxt3)

        if pygame.K_0 in keys:
            shop_tut_screen = 0
            tutorial_screen_on += 1
            character.x = 50
            character.y = 50
            score = 1
        camera.display()
        return

    # Dead screen
    if dead_screen == 1:
        camera.x = 400
        camera.y = 400
        camera.clear("black")
        camera.draw(descriptions[8])
        camera.draw(descriptions[9])
        if pygame.K_RETURN in keys:
            dead_screen = 0
            shop_screen += 1
            life = 3
            character.x = 0
            character.y = 50
        camera.display()
        return

    # win screen
    if win_screen == 1:
        camera.x = 400
        camera.y = 400
        camera.clear("black")
        camera.draw(descriptions[12])
        camera.draw(descriptions[13])
        camera.display()
        return

    # shop screen
    if shop_screen == 1:
        camera.x = 400
        camera.y = 400
        camera.clear("beige")

        coinslist[7].x = -1600
        coinslist[7].y = 3970
        coinslist[8].x = -1000
        coinslist[8].y = 3970
        coinslist[9].x = -400
        coinslist[9].y = 3970

        speed_upgrade = gamebox.from_text(150, 225, "SPEED: 1 COIN", 50, "red")
        time_upgrade = gamebox.from_text(150, 350, "TIME: 1 COIN", 50, "red")
        jump_upgrade = gamebox.from_text(220, 475, "JUMP POWER: 1 COIN", 50, "red")
        ammo_upgrade = gamebox.from_text(150, 600, "AMMO: 1 COIN", 50, "red")
        upgradeBtn = [
            gamebox.from_image(360, 225, "upgradebutton1.png"),
            gamebox.from_image(360, 350, "upgradebutton2.png"),
            gamebox.from_image(500, 475, "upgradebutton3.png"),
            gamebox.from_image(360, 600, "upgradebutton4.png")
        ]
        coin_iconshop = gamebox.from_image(600, 350, "bitcoin.png")
        coin_textshop = gamebox.from_text(650, 350, ": " + str(coins), 50, "black")
        gun_iconshop = gamebox.from_image(600, 275, "toygun.png")
        gun_textshop = gamebox.from_text(650, 275, ": " + str(ammo), 50, "black")
        camera.draw(upgradeBtn[0])
        camera.draw(upgradeBtn[1])
        camera.draw(upgradeBtn[2])
        camera.draw(upgradeBtn[3])
        camera.draw(speed_upgrade)
        camera.draw(time_upgrade)
        camera.draw(jump_upgrade)
        camera.draw(ammo_upgrade)
        camera.draw(descriptions[10])
        camera.draw(descriptions[11])
        camera.draw(coin_iconshop)
        camera.draw(coin_textshop)
        camera.draw(gun_iconshop)
        camera.draw(gun_textshop)

        # This is setting new values when they upgrade
        if (pygame.K_1 in keys) and (coins > 0) and (r_t_s_u <= 2):
            r_speed += 2
            r_t_s_u += 1
            coins -= 1
            keys.clear()
        if (pygame.K_2 in keys) and (coins > 0) and (r_t_t_u <= 2):
            timevar += 15
            r_t_t_u += 1
            coins -= 1
            keys.clear()
        if (pygame.K_3 in keys) and (coins > 0) and (r_t_j_u <= 2):
            r_jump -= 2
            r_t_j_u += 1
            coins -= 1
            keys.clear()
        if (pygame.K_4 in keys) and (coins > 0) and (ammo <= 4):
            ammo += 1
            coins -= 1
            keys.clear()

        if r_t_s_u == 3:
            max1 = gamebox.from_text(360, 225, "MAX", 50, "red", bold=True)
            camera.draw(max1)
        if r_t_t_u == 3:
            max2 = gamebox.from_text(360, 350, "MAX", 50, "red", bold=True)
            camera.draw(max2)
        if r_t_j_u == 3:
            max3 = gamebox.from_text(500, 475, "MAX", 50, "red", bold=True)
            camera.draw(max3)

        if pygame.K_0 in keys:
            shop_screen = 0
            character.x = 50
            character.y = 50
            score = 1
        camera.display()
        return

    camera.clear("light blue")

    character.yspeed += 1
    character.y = character.y + character.yspeed
    # Camera follows player
    camera.y = character.y - 150
    camera.x = character.x

    # shop code for tutorial
    shop = gamebox.from_image(-200, 225, "shopp.png")
    camera.draw(shop)
    if character.touches(shop):
        character.move_both_to_stop_overlapping(shop)

    # controls for player movement left and right
    if pygame.K_RIGHT in keys:
        character.x += r_speed
        character_Frame += 1
        if character_Frame == 8:
            character_Frame = 0
        if counter % 11 == 0:
            character.image = character_Sheet[character_Frame]
    if pygame.K_LEFT in keys:
        character.x -= r_speed
        character_Frame += 1
        if character_Frame == 8:
            character_Frame = 0
        if counter % 11 == 0:
            character.image = character_FSheet[character_Frame]

    # Makes sure that jumping works and that the character doesnt fall through the walls
    for wall in walls_level1:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = r_jump
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    # ledge stuff
    for ledge in tutorial_ledge:
        if character.bottom_touches(ledge):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -18
        if character.touches(ledge):
            character.move_to_stop_overlapping(ledge)
    camera.draw(tutorial_ledge[0])
    camera.draw(tutorial_ledge[1])
    camera.draw(tutorial_ledge[2])

    # invisible barriers and monsters
    camera.draw(invisible_bar[0])
    camera.draw(invisible_bar[1])
    camera.draw(invisible_bar[2])
    camera.draw(invisible_bar[3])
    camera.draw(invisible_bar[4])
    camera.draw(invisible_bar[5])
    camera.draw(invisible_bar[6])
    camera.draw(invisible_bar[7])
    camera.draw(invisible_bar[8])
    camera.draw(invisible_bar[9])
    camera.draw(invisible_bar[10])

    if character.touches(evilminions[1]):
        character.x = 50
        character.y = 50
        life -= 1
    if character.touches(evilminions[2]):
        character.x = 1620
        character.y = 1650
        life -= 1
    if character.touches(evilminions[3]):
        character.x = -1850
        character.y = 3950
        life -= 1
    if character.touches(evilminions[4]):
        character.x = -1850
        character.y = 3950
        life -= 1

    if evilminions[1].right_touches(invisible_bar[1]):
        touchcounter += 1
        y1.remove(6)
        y1.append(-6)
        if touchcounter == 1:
            evilminions[1].flip()
        touchcounter = 0
    elif evilminions[1].left_touches(invisible_bar[0]):
        touchcounter += 1
        y1.remove(-6)
        y1.append(6)
        if touchcounter == 1:
            evilminions[1].flip()
        touchcounter = 0
    if evilminions[2].right_touches(invisible_bar[2]):
        touchcounter += 1
        y2.remove(6)
        y2.append(-6)
        if touchcounter == 1:
            evilminions[2].flip()
        touchcounter = 0
    elif evilminions[2].left_touches(invisible_bar[3]):
        touchcounter += 1
        y2.remove(-6)
        y2.append(6)
        if touchcounter == 1:
            evilminions[2].flip()
        touchcounter = 0
    if evilminions[3].right_touches(invisible_bar[7]):
        touchcounter += 1
        y3.remove(6)
        y3.append(-6)
        if touchcounter == 1:
            evilminions[3].flip()
        touchcounter = 0
    elif evilminions[3].left_touches(invisible_bar[6]):
        touchcounter += 1
        y3.remove(-6)
        y3.append(6)
        if touchcounter == 1:
            evilminions[3].flip()
        touchcounter = 0
    if evilminions[4].right_touches(invisible_bar[9]):
        touchcounter += 1
        y4.remove(6)
        y4.append(-6)
        if touchcounter == 1:
            evilminions[4].flip()
        touchcounter = 0
    elif evilminions[4].left_touches(invisible_bar[8]):
        touchcounter += 1
        y4.remove(-6)
        y4.append(6)
        if touchcounter == 1:
            evilminions[4].flip()
        touchcounter = 0

    evilminions[1].x += y1[0]
    evilminions[2].x += y2[0]
    evilminions[3].x += y3[0]
    evilminions[4].x += y4[0]

    # animation section for evil minions
    evilminion_Frame += 1
    if evilminion_Frame == 24:
        evilminion_Frame = 0
    if counter % 1 == 0:
        evilminions[1].image = evilminion_Sheet[evilminion_Frame + direction * 2]
        evilminions[2].image = evilminion_Sheet[evilminion_Frame + direction * 10]
        evilminions[3].image = evilminion_Sheet[evilminion_Frame + direction * 2]
        evilminions[4].image = evilminion_Sheet[evilminion_Frame + direction * 10]
    camera.draw(evilminions[1])
    camera.draw(evilminions[2])
    camera.draw(evilminions[3])
    camera.draw(evilminions[4])

    # elevator
    if character.bottom_touches(elevator):
        character.yspeed = 0
        if pygame.K_SPACE in keys:
            character.yspeed = r_jump
    if character.touches(elevator):
        character.move_to_stop_overlapping(elevator)
    camera.draw(elevator)

    if elevator.top_touches(invisible_bar[5]):
        elevator_speed.remove(-5)
        elevator_speed.append(5)
    elif elevator.bottom_touches(invisible_bar[4]):
        elevator_speed.remove(5)
        elevator_speed.append(-5)
    elevator.y += elevator_speed[0]

    # spikes
    if character.bottom_touches(spikes[0]):
        character.x = 700
        character.y = 300
        life -= 1
    elif character.bottom_touches(spikes[1]):
        character.x = 1620
        character.y = 1650
        life -= 1
    elif character.bottom_touches(spikes[2]):
        character.x = -720
        character.y = 960
        life -= 1
    camera.draw(spikes[0])
    camera.draw(spikes[1])
    camera.draw(spikes[2])

    # timer
    score -= 1
    seconds = str(int((score / ticks_per_second) % timevar)).zfill(2)
    timer = gamebox.from_text(camera.x, camera.y - 280, seconds, 30, "red")
    if seconds == "01":
        x += 1
    if seconds == "01" and x > 1:
        dead_screen += 1
    camera.draw(timer)

    # lasers
    lasers = []
    laser_set_two = []
    laser_set_three = []
    if int(seconds) % 2 == 0:
        lasers.append(gamebox.from_color(1600, 540, "red", 280, 30))
        lasers.append(gamebox.from_color(1600, 840, "red", 280, 30))
        lasers.append(gamebox.from_color(1600, 1250, "red", 280, 30))
    elif int(seconds) % 2 == 1:
        lasers.append(gamebox.from_color(1600, 540, "light blue", 280, 30))
        lasers.append(gamebox.from_color(1600, 840, "light blue", 280, 30))
        lasers.append(gamebox.from_color(1600, 1250, "light blue", 280, 30))
    if int(seconds) % 2 == 0:
        laser_set_two.append(gamebox.from_color(1400, 1490, "red", 30, 280))
        laser_set_two.append(gamebox.from_color(1200, 1490, "red", 30, 280))
        laser_set_two.append(gamebox.from_color(1000, 1490, "red", 30, 280))
        laser_set_two.append(gamebox.from_color(800, 1490, "red", 30, 280))
        laser_set_two.append(gamebox.from_color(600, 1490, "red", 30, 280))
    elif int(seconds) % 2 == 1:
        laser_set_two.append(gamebox.from_color(1400, 1490, "light blue", 30, 280))
        laser_set_two.append(gamebox.from_color(1200, 1490, "light blue", 30, 280))
        laser_set_two.append(gamebox.from_color(1000, 1490, "light blue", 30, 280))
        laser_set_two.append(gamebox.from_color(800, 1490, "light blue", 30, 280))
        laser_set_two.append(gamebox.from_color(600, 1490, "light blue", 30, 280))
    if int(seconds) % 2 == 0:
        laser_set_three.append(gamebox.from_color(-1250, 890, "red", 30, 280))
        laser_set_three.append(gamebox.from_color(-1000, 890, "red", 30, 280))
        laser_set_three.append(gamebox.from_color(-800, 890, "red", 30, 280))
    elif int(seconds) % 2 == 1:
        laser_set_three.append(gamebox.from_color(-1250, 890, "light blue", 30, 280))
        laser_set_three.append(gamebox.from_color(-1000, 890, "light blue", 30, 280))
        laser_set_three.append(gamebox.from_color(-800, 890, "light blue", 30, 280))

    camera.draw(lasers[0])
    camera.draw(lasers[1])
    camera.draw(lasers[2])
    camera.draw(laser_set_two[0])
    camera.draw(laser_set_two[1])
    camera.draw(laser_set_two[2])
    camera.draw(laser_set_two[3])
    camera.draw(laser_set_two[4])
    camera.draw(laser_set_three[0])
    camera.draw(laser_set_three[1])
    camera.draw(laser_set_three[2])

    for i in range(0, len(lasers)):
        if character.touches(lasers[i]) and int(seconds) % 2 == 0:
            character.x = 1300
            character.y = 200
            life -= 1
    for i in range(0, len(laser_set_two)):
        if character.touches(laser_set_two[i]) and int(seconds) % 2 == 0:
            character.x = 1620
            character.y = 1650
            life -= 1
    for i in range(0, len(laser_set_three)):
        if character.touches(laser_set_three[i]) and int(seconds) % 2 == 0:
            character.x = -720
            character.y = 960
            life -= 1

    # coin drawing and coin system
    coin_icon = gamebox.from_image(camera.x - 360, camera.y - 250, "bitcoin.png")
    coin_text = gamebox.from_text(camera.x - 300, camera.y - 250, ": " + str(coins), 50, "black")
    camera.draw(coin_text)
    camera.draw(coin_icon)

    camera.draw(coinslist[0])
    camera.draw(coinslist[1])
    camera.draw(coinslist[2])
    camera.draw(coinslist[3])
    camera.draw(coinslist[4])
    camera.draw(coinslist[5])
    camera.draw(coinslist[6])
    camera.draw(coinslist[7])
    camera.draw(coinslist[8])
    camera.draw(coinslist[9])
    camera.draw(coinslist[10])

    for coin in coinslist:
        if character.touches(coin):
            coin.x = -4000
            coin.y = 4000
            coins += 1

    # gun drawing
    gun_icont = gamebox.from_image(camera.x + 300, camera.y - 250, "toygun.png")
    gun_textt = gamebox.from_text(camera.x + 360, camera.y - 250, ": " + str(ammo), 50, "black")
    camera.draw(gun_textt)
    camera.draw(gun_icont)

    # CODE FOR BULLETS IN TUTORIAL
    if (320 < character.x < 1250) and (character.y > 4450):
        if pygame.K_w in keys:
            bullet = gamebox.from_color(character.x, character.y, "dark green", 10, 20)
            bullet.yspeed = -bullettutspeed
            bullets.append(bullet)
            keys.clear()
        if pygame.K_a in keys:
            bullet = gamebox.from_color(character.x, character.y, "dark green", 20, 10)
            bullet.xspeed = -bullettutspeed
            bullets.append(bullet)
            keys.clear()
        if pygame.K_d in keys:
            bullet = gamebox.from_color(character.x, character.y, "dark green", 20, 10)
            bullet.xspeed = bullettutspeed
            bullets.append(bullet)
            keys.clear()
    else:
        if pygame.K_a in keys and ammo > 0:
            bullet = gamebox.from_color(character.x, character.y, "dark green", 20, 10)
            bullet.xspeed = -bullettutspeed
            bullets.append(bullet)
            ammo -= 1
            keys.clear()
        if pygame.K_d in keys and ammo > 0:
            bullet = gamebox.from_color(character.x, character.y, "dark green", 20, 10)
            bullet.xspeed = bullettutspeed
            bullets.append(bullet)
            ammo -= 1
            keys.clear()

    for bullet in bullets:
        bullet.y += bullet.yspeed
        bullet.x += bullet.xspeed

        if math.sqrt((character.x - bullet.x) ** 2) > 400:
            bullet.x = -10000
            bullet.y = 10000

        for enemy in evilminions:
            if bullet.touches(enemy):
                enemy.x = -10000
                enemy.y = 10000
        for enemy in final_enemies:
            if bullet.touches(enemy):
                final_enemies.remove(enemy)
        camera.draw(bullet)

    # text on screen for life
    lifeText = gamebox.from_text(camera.x + 250, camera.y + 270, "Lives: " + str(life), 50, "black")
    camera.draw(lifeText)
    if life == 0:
        dead_screen += 1
        tutorial_screen_on -= 1

    # Final Boss:
    if character.touches(invisible_bar[10]):
        life = 5
        character.x = 500
        character.y = 4500

    if (320 < character.x < 1250) and (character.y > 4050):
        finaltext = gamebox.from_text(camera.x + 260, camera.y - 150, "USE W, A, D to shoot the Computer Bugs!", 15,
                                      "black")
        finaltext2 = gamebox.from_text(camera.x + 260, camera.y - 140,
                                       "Survive the time to win! You have Infinite Ammo", 15, "black")
        camera.draw(finaltext)
        camera.draw(finaltext2)
        timevar = 120
        if monster_counter % 50 == 0:
            enemy = gamebox.from_image(random.randint(200, 1200), random.randint(4300, 4400), "computerbug.png")
            final_enemies.append(enemy)

        for enemy in final_enemies:
            if character.x < enemy.x:
                if timevar > 60:
                    enemy.x -= 6
                else:
                    enemy.x -= 9
            if character.x >= enemy.x:
                if timevar > 60:
                    enemy.x += 6
                else:
                    enemy.x += 9
            if character.y < enemy.y:
                if timevar > 60:
                    enemy.y -= 6
                else:
                    enemy.y -= 9
            if character.y >= enemy.y:
                if timevar > 60:
                    enemy.y += 6
                else:
                    enemy.y += 9
            if character.touches(enemy):
                life -= 1
                final_enemies.remove(enemy)
            camera.draw(enemy)
        if seconds == "02":
            win_screen += 1

    # draws character
    camera.draw(character)

    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
