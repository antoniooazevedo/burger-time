import pygame
from spritesheet import spritesheet

class Animation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, name):
        super().__init__()
        self.sprites = spritesheet("sprites.png")
        self.is_animating = False
        
        if name == "chef":
            self.sprite_list = [self.sprites.parse_sprite("fstopped.png")]
        elif name == "egg":
            self.sprite_list = [self.sprites.parse_sprite("estopped.png")]
        
        self.current_sprite = 0
        self.image = self.sprite_list[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def start(self):
        self.is_animating = True
    
    def end(self, name):
        
        if name == "chef":
            self.sprite_list = [self.sprites.parse_sprite("fstopped.png")]
        elif name == "egg":
            self.sprite_list = [self.sprites.parse_sprite("estopped.png")]
            
        
        
        
        
        
        
        self.image = self.sprite_list[0]
        self.is_animating = False

    def pause(self):
        self.is_animating = False

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.006
                        
            self.image = self.sprite_list[int(self.current_sprite)%len(self.sprite_list)]
    
    def moving(self, pos_x, pos_y):
        self.rect.topleft = [pos_x, pos_y]
        
    def character_anim_selector(self, name):
        self.sprite_list = []
        
        if name == "chef_left":
           self.sprite_list.append(self.sprites.parse_sprite("w1.png"))
           self.sprite_list.append(self.sprites.parse_sprite("w2.png"))
           
        elif name == "chef_right":
            self.sprite_list.append(pygame.transform.flip(self.sprites.parse_sprite("w1.png"), True, False))
            self.sprite_list.append(pygame.transform.flip(self.sprites.parse_sprite("w2.png"), True, False))
            
        elif name == "chef_up":
            self.sprite_list.append(self.sprites.parse_sprite("b1.png"))
            self.sprite_list.append(self.sprites.parse_sprite("b2.png"))
            
        elif name == "chef_down":
            self.sprite_list.append(self.sprites.parse_sprite("fw1.png"))
            self.sprite_list.append(self.sprites.parse_sprite("fw2.png"))
           
        elif name == "egg_left":
            self.sprite_list.append(self.sprites.parse_sprite("ew1.png"))
            self.sprite_list.append(self.sprites.parse_sprite("ew2.png"))
        
        elif name == "egg_right":
            self.sprite_list.append(pygame.transform.flip(self.sprites.parse_sprite("ew1.png"), True, False))
            self.sprite_list.append(pygame.transform.flip(self.sprites.parse_sprite("ew2.png"), True, False))
            
        
            