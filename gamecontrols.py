#ideas: laser u base off the time.  Make the shop in top right and have global varaibles to keep count of how many times something is bought. Since there are no buttons figure something out with an if statement with pressdown and mouse cord.
#for saws at the one part just do it so that there are bounds and if it reaches it will change the x direction to the opposite.
import pygame
import gamebox

camera = gamebox.Camera(800,600)
character = gamebox.from_color(50, 500, "red", 50, 50)
character.yspeed = 0

life = 3

spikes = [
    gamebox.from_image(1000, 500, "http://www.clker.com/cliparts/a/R/p/k/g/4/spikes-md.png")
]

walls_level1 = [
    #platforms
    gamebox.from_color(990, 300, "brown", 150, 10),
    #ground
    gamebox.from_image(100, 590, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(400, 590, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(-200, 590, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(-200, 290, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(700, 590, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1000, 700, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1300, 590, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1300, 890, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1300, 1190, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 590, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 290, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 0, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 890, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 1190, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 1490, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 1790, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(2100, 0, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(2100, 590, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(2100, 290, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(2100, 890, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(2100, 1190, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(2100, 1490, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(2100, 1790, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1900, 1790, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1600, 1790, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1300, 1790, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg"),
    gamebox.from_image(1000, 1790, "https://i.pinimg.com/564x/9a/1f/e2/9a1fe282ad6d12391828ae0ed4ed9a86.jpg")
]

def tick(keys):
    """this is doing all the functions for the program like the movement, ending the game, timing the game, keeping the character on the screen,, etc."""
    global counter
    global score
    character.yspeed += 1
    character.y = character.y + character.yspeed
    camera.clear("light blue")
    camera.draw(character)
    
    #Camera follows player
    camera.y = character.y - 150
    camera.x = character.x



    if pygame.K_RIGHT in keys:
        character.x += 10
    if pygame.K_LEFT in keys:
        character.x -= 10
    if pygame.K_DOWN in keys:
        character.y += 10


    #Makes sure that jumping works and that the character doesnt fall through the walls
    for wall in walls_level1:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -18  
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    for spike in spikes:
        global life
        if character.bottom_touches(spike):
            life -= 1
        camera.draw(spike)
    

    camera.display()

    
ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
