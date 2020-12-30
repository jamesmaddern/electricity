import pygame as pg
from random import randint
pg.init()
font = pg.font.SysFont("Bahnschrift",22)
class Player:
    def __init__(self, deckPos,handPos, name,angle,screen,dist):
        h = screen.get_height()
        w = screen.get_width()

        self.active = False
        self.name = name
        self.handPos = handPos
        self.deckPos = deckPos
        self.hand = []
        self.currentCard = None
        self.linkNegative = False
        self.linkPositive = False
        self.deckImg = pg.image.load(r"assets\images\cards\cardback.png")
        self.text = font.render(self.name,True,pg.Color("Black"))
        
        center = pg.math.Vector2(w/2,h/2)
        dist = self.handPos - center 

        self.leftNeighbour = center + dist.rotate(angle*-1)
        self.rightNeighbour = center + dist.rotate(angle)

        a = handPos
        dist = (self.leftNeighbour - a) / 10
        lineList = []
        for i in range(11):
            lineList.append(a)
            a = a + dist
        self.leftList = lineList 


        a = handPos
        dist = (self.rightNeighbour - a)/10
        lineList = []
        for i in range(11):
            lineList.append(a)
            a = a + dist
        self.rightList = lineList  
            
         
        
    def drawLines(self,screen):
        if self.active:
            colour = "cyan"
        else:
            colour = "white"
        if self.linkNegative:
            lineList = []
            lineList.append((self.handPos.x,self.handPos.y))
            for point in self.leftList[1:-1]:
                x = point.x + randint(-20,20)
                y = point.y + randint(-20,20)
                lineList.append((x,y))
            lineList.append((self.leftNeighbour.x,self.leftNeighbour.y))

            pg.draw.lines(screen,pg.Color(colour),False,lineList,4)
        if self.linkPositive:
            lineList = []
            lineList.append((self.handPos.x, self.handPos.y))
            for point in self.rightList[1:-1]:
                x = point.x + randint(-20,20) 
                y = point.y + randint(-20,20)
                lineList.append((x,y))
            lineList.append((self.rightNeighbour.x,self.rightNeighbour.y))
            pg.draw.lines(screen,pg.Color(colour),False,lineList,4)
        
        
        
    def drawCards(self,screen):
        imgH = self.deckImg.get_height()
        imgW = self.deckImg.get_width()
        

        
        
        if self.currentCard:
            if self.active:
                pg.draw.rect(screen,pg.Color("Cyan"),(self.handPos.x-imgW/2-5,self.handPos.y-imgH/2-5,imgW+10,imgH+10),border_radius=15)
            screen.blit(self.currentCard.img,(self.handPos.x-imgW/2,self.handPos.y-imgH/2,10,10)) 
            screen.blit(self.text,(self.handPos.x-imgW/4,self.handPos.y-imgH/2,10,10))
    
    def drawBacks(self,screen):
        imgH = self.deckImg.get_height()
        imgW = self.deckImg.get_width()
        
        if self.hand:
            for i in range(0,len(self.hand)):
                pg.draw.rect(screen,pg.Color("White"),(self.handPos.x-imgW/3+(i*2),self.handPos.y-imgH/3+(i*2),imgW-1,imgH-2),border_radius=7)
            i +=1
            screen.blit(self.deckImg,(self.handPos.x-imgW/3+(i*2),self.handPos.y-imgH/3+(i*2),10,10))

    def giveCard(self,card):
        self.hand.append(card)
    
    def dealCard(self):
        card = self.hand.pop()
        self.currentCard = card
        
        
        

    def checkNeighbours(self, players, index):
        
        if index == 0:
            if players[len(players)-1].currentCard:   
                if players[len(players)-1].currentCard.value == self.currentCard.value or players[len(players)-1].currentCard.suit == self.currentCard.suit:
                    self.linkNegative = True
                    players[len(players)-1].linkPositive = True
                else:
                    self.linkNegative = False
                    players[len(players)-1].linkPositive = False
            if players[1].currentCard:
                if players[1].currentCard.value == self.currentCard.value or players[1].currentCard.suit == self.currentCard.suit:
                    self.linkPositive = True
                    players[1].linkNegative = True
                else:
                    self.linkPositive = False
                    players[1].linkNegative = False
            
        
        
        
        elif index == len(players)-1:
            if players[len(players)-2].currentCard:
                if players[len(players)-2].currentCard.value == self.currentCard.value or players[len(players)-2].currentCard.suit == self.currentCard.suit:
                    self.linkNegative = True
                    players[len(players)-2].linkPositive = True
                else:
                    self.linkNegative = False
                    players[len(players)-2].linkPositive = False
            if players[0].currentCard:
                if players[0].currentCard.value == self.currentCard.value or players[0].currentCard.suit == self.currentCard.suit:
                    self.linkPositive = True
                    players[0].linkNegative = True
                else:
                    self.linkPositive = False
                    players[0].linkNegative = False
        
        
        else:
            if players[index -1].currentCard:
                if players[index-1].currentCard.value == self.currentCard.value or players[index-1].currentCard.suit == self.currentCard.suit:
                    self.linkNegative = True
                    players[index-1].linkPositive = True
                else:
                    self.linkNegative = False
                    players[index-1].linkPositive = False
            if players[index +1].currentCard:
                if players[index+1].currentCard.value == self.currentCard.value or players[index+1].currentCard.suit == self.currentCard.suit:
                    self.linkPositive = True
                    players[index+1].linkNegative = True
                else:
                    self.linkPositive = False
                    players[index+1].linkNegative = False
        




