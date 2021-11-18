import pygame
import gamebox

camera = gamebox.Camera(800,600)
character = gamebox.from_color(50, 500, "red", 20, 35)
character.yspeed = 0



walls_level1 = [
    gamebox.from_color(100, 590, "white", 800, 20)
    
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
        character.x += 3
    if pygame.K_LEFT in keys:
        character.x -= 3


    #Makes sure that jumping works and that the character doesnt fall through the walls
    for wall in walls_level1:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -15   
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)
    

    camera.display()

    
ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
