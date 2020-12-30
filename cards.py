import pygame as pg
class Card:
    def __init__(self, suit, val,path):
        self.suit = suit
        self.value = val
        self.img = pg.image.load(r"assets\images\cards\\"+path)
        
        #self.img = pg.transform.scale(img, (int(img.get_width()*0.2), int(img.get_height()*0.2)))
        
        
    def draw(self):
        print("{:} of {:}".format(self.value, self.suit))
    def remove(self):
        pass

