import pygame as pg
pg.init()
FONT = pg.font.SysFont("Bahnschrift", 32)

class InputBox:
    def __init__(self,index,rect):
        self.index = index
        self.rect = rect
        self.active = False
        self.text = "PLAYER "+ str(index)
        self.bg = "Black"
        self.colour = (255,215,10)
        self.txt_surface = FONT.render(self.text, True, self.colour)
        print("created",self.index)
    def __del__(self):
        print("deleted",self.index)

    def enterText(self, event):
        
        
        if event.type == pg.KEYDOWN:
            if self.active:
                
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.active = not self.active
                    self.text = self.text.upper()
                    self.colour = "black"
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < 9:
                    
                    self.text += event.unicode

                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.colour)    
    def draw(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.bg, self.rect,0)  
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
                  
    def update(self,screen):
        #width = max(200, self.txt_surface.get_width()+10)
        #self.rect.w = width
        if self.active:
            self.colour = "cyan"
            
        else:
            self.colour = (255,215,10)
        self.txt_surface = FONT.render(self.text, True, self.colour)
        self.draw(screen)