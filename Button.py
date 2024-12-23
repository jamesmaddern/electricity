import pygame
class Button:
    def __init__(self,rectangle,font,text,colour):
        self.colour = pygame.Color(0,0,0)
        self.name = text
        self.rect = rectangle
        self.text = font.render(text,True, colour)
        self.textbox = self.allign_text(rectangle)
    
    def allign_text(self,rectangle):
        textPos = (rectangle.width - self.text.get_width())/2
        return pygame.Rect(rectangle.x+textPos,
                           rectangle.y,
                           self.text.get_width(),
                           self.text.get_height())
    def draw(self,screen):
        pygame.draw.rect(screen,self.colour,self.rect)
        screen.blit(self.text,self.textbox)