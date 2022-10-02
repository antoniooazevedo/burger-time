import pygame

class Level_load:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.player = pygame.Rect(self.x,self.y,16,17)

    def load(self, level, canvas):
        self.level_tuples = []
        h = 42
        w = 0
        r = 0
        for row in level:
            c = 0
            for col in row:
                self.level_tuples.append((col, c * 16 + w , 17 + r * 17 + h))
                if col == "p":
                    pygame.draw.rect(canvas, pygame.Color("blue"), ((c * 16 + w, h + 17 + 17*r), (16, 3)))
                elif col == "lp1":
                    pygame.draw.rect(canvas, pygame.Color("cyan"), ((c * 16 + w , h + 17 + 17*r), (16, 3)))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 15 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 13 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 11 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 9 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 7 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 5 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 3 + 17*r), (16, 1))))
                    
                elif col == "l":
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 17 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 15 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 13 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 11 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 9 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 7 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 5 + 17*r), (16, 1))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((c * 16 + w , h + 3 + 17*r), (16, 1))))
                    
                elif col == "lp2":
                    pygame.draw.rect(canvas, pygame.Color("cyan"), ((c * 16 + w , h + 17 + 17*r), (16, 3)))
                    
                elif col == "b1":
                    pygame.draw.rect(canvas, pygame.Color("blue"), ((c * 16 + w, h + 17 + 17*r), (16, 3)))
                    pygame.draw.rect(canvas, pygame.Color("gold3"), ((c * 16 + w , h + 15 + 17*r), (16, 6)))
                
                elif col == "b2":
                    pygame.draw.rect(canvas, pygame.Color("blue"), ((c * 16 + w, h + 17 + 17*r), (16, 3)))
                    pygame.draw.rect(canvas, pygame.Color("goldenrod4"), ((c * 16 + w , h + 15 + 17*r), (16, 6)))
                    
                elif col == "a":
                    pygame.draw.rect(canvas, pygame.Color("blue"), ((c * 16 + w, h + 17 + 17*r), (16, 3)))
                    pygame.draw.rect(canvas, pygame.Color("darkolivegreen3"), ((c * 16 + w , h + 15 + 17*r), (16, 6)))
                    
                elif col == "c":
                    pygame.draw.rect(canvas, pygame.Color("blue"), ((c * 16 + w, h + 17 + 17*r), (16, 3)))
                    pygame.draw.rect(canvas, pygame.Color("gold1"), ((c * 16 + w , h + 15 + 17*r), (16, 6)))
                
                elif col == "t":
                    pygame.draw.rect(canvas, pygame.Color("blue"), ((c * 16 + w, h + 17 + 17*r), (16, 3)))
                    pygame.draw.rect(canvas, pygame.Color("firebrick4"), ((c * 16 + w , h + 15 + 17*r), (16, 6)))
                    
                elif col == "m":
                    pygame.draw.rect(canvas, pygame.Color("blue"), ((c * 16 + w, h + 17 + 17*r), (16, 3)))
                    pygame.draw.rect(canvas, pygame.Color("indianred4"), ((c * 16 + w , h + 15 + 17*r), (16, 6)))
                    
                elif col == "plate":
                    ## plate 1
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((26 , 340), (74, 4))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((22 , 332), (4,12))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((100 , 332), (4,12))))
                    
                    ## plate 2
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((108 , 320), (74, 4))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((104 , 312), (4,12))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((180 , 312), (4,12))))
                    
                    ## plate 3
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((188 , 340), (74, 4))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((184 , 332), (4,12))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((260 , 332), (4,12))))
                    
                    ##plate 4
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((268 , 320), (74, 4))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((264 , 312), (4,12))))
                    pygame.draw.rect(canvas, pygame.Color("gray69"),(((340 , 312), (4,12))))
                
                c +=1
            r +=1

        self.bounding_box = pygame.Rect(w + 16, h, 320 + w, 204 + h)    



    def get_position(self):
        list_of_colisions = []
        for el in self.level_tuples:
            flag = pygame.Rect(el[1], el[2] - 17, 16, 17)
            #if self.y <= el[2]:
            #    if self.x <= el[1]:
            #        return el[0]
            if flag.colliderect(self.player):
                list_of_colisions.append(el[0])
        
        return list_of_colisions





    def is_outside(self):
        return not self.bounding_box.contains(self.player)
