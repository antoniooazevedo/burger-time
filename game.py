
import pygame, burger_levels
from animation import Animation
from level_load import Level_load


#Screen Init
pygame.init()
display_w = display_h = 368
screen = pygame.display.set_mode((display_w, display_h))
canvas = pygame.Surface((display_w, display_h))
###


## Animation Setups

spr_x = 48
spr_y = 42
sprites = pygame.sprite.Group()


chef_animation = Animation(48, 0, "chef")
egg_animation = Animation(200,200, "egg")


sprites.add(chef_animation)
sprites.add(egg_animation)

right_key = left_key = up_key = down_key = False
clock = pygame.time.Clock()
keys_pressed = []

# Game Loop
while True:

    loading =  Level_load(spr_x, spr_y)
    loading.load(burger_levels.level1, canvas)

    # Key events
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
               
                egg_animation.character_anim_selector("egg_left")
                egg_animation.start()
                left_key = True
                
                keys_pressed.append("l")
                
            elif event.key == pygame.K_d:
                
                egg_animation.character_anim_selector("egg_right")
                egg_animation.start()
                right_key = True
            
                keys_pressed.append("r")
            
            elif event.key == pygame.K_w:
                
                up_key = True
                
                keys_pressed.append("u")
                
            elif event.key == pygame.K_s:
                
                down_key = True
                
                keys_pressed.append("d")
                
        if event.type == pygame.KEYUP:
            
    
            if event.key == pygame.K_a:

                egg_animation.end("egg")
                #left_key = False
                
                keys_pressed.remove("l")
                chef_animation.end("chef")
                
            elif event.key == pygame.K_d:
                
                egg_animation.end("egg")
                right_key = False
                
                keys_pressed.remove("r")
                chef_animation.end("chef")
                
            elif event.key == pygame.K_w:
                
                keys_pressed.remove("u")
                #chef_animation.end("chef")
                
            elif event.key == pygame.K_s:
                
                keys_pressed.remove("d")
                #chef_animation.end("chef")
    
    
    if len(keys_pressed) > 1:
        chef_animation.pause()
        for key in keys_pressed:
            if key == "l":
                left_key = False
            if key == "r":
                right_key = False
            if key == "d":
                down_key = False
            if key == "u":
                up_key = False
                
    if len(keys_pressed) == 1:
        
        for key in keys_pressed:
            if key == "l":
                chef_animation.character_anim_selector("chef_left")
                chef_animation.start()
                left_key = True
            if key == "r":
                chef_animation.character_anim_selector("chef_right")
                chef_animation.start()
                right_key = True
            if key == "d":
                chef_animation.character_anim_selector("chef_down")
                chef_animation.start()
                down_key = True
            if key == "u":
                chef_animation.character_anim_selector("chef_up")
                chef_animation.start()
                up_key = True
        
        
    # Game Physics
    pos = loading.get_position()[0]

    dt = clock.tick()
    if left_key and lateral_unlock:
        amt = 0
        spr_x -= 0.05 * dt
        amt += spr_x
        print(abs(amt)%16)

        if abs(amt) == 16:
            amt = 0
            left_key = False
        
    elif right_key and lateral_unlock:
        spr_x += 0.05 * dt
    elif up_key and upward_unlock:
        spr_y -= 0.03 * dt
        if pos == "lp2":
            up_key = False
            chef_animation.end("chef")
    elif down_key and downward_unlock:
        spr_y += 0.03 * dt
        if pos == "lp1":
            down_key = False
            chef_animation.end("chef") 
    

    chef_animation.moving(spr_x % display_w,spr_y % display_h)
    
    # Draw on screen
    canvas.fill(pygame.Color("black"))
    loading.load(burger_levels.level1, canvas)
    
    upward_unlock = (pos == "lp1" or pos == "l")
    downward_unlock = (pos == "lp2" or pos == "l")

    lateral_unlock = not(pos == "l")
    
    sprites.draw(canvas)
    sprites.update()
    screen.blit(canvas, (0,0))
    pygame.display.update()