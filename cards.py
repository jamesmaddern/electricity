import pygame as pg
class Card:
    def __init__(self, suit, val,path):
        self.suit = suit
        self.value = val
        self.img = pg.image.load(r"assets\images\cards\\"+path)
        
     
        
        
    

