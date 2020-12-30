import sys
from cards import Card
from players import Player
from random import shuffle
import pygame as pg
from pygame import Vector2, mixer
suits = ["Hearts","Diamonds","Clubs","Spades"]
deck = []
playerList = []
screen = None
pg.init()
screen = pg.display.set_mode((1920,1080))
w = screen.get_width()
h = screen.get_height()
clock = pg.time.Clock()
numFont = pg.font.SysFont("Bahnschrift",28)
countFont = pg.font.SysFont("Bahnschrift",100)


def createDeck():
    global deck
    for suit in suits:
        deck.append(Card(suit,14,"A"+suit[0]+".png"))

        for i in range(2,11):
            deck.append(Card(suit,i,str(i)+suit[0]+".png"))
        deck.append(Card(suit,11,"J"+suit[0]+".png"))
        deck.append(Card(suit,12,"Q"+suit[0]+".png"))
        deck.append(Card(suit,13,"K"+suit[0]+".png"))

    shuffle(deck)  
    return deck

def createPlayers(players,deck):
    global playerList
    
    angle = int(360/len(players))
    
    startPos = Vector2(w/2,h/2)
    
    endHandPos = Vector2(0,-h/3-50)
    dist = Vector2(0,-h/3-50)

    for player in players:
        
        handPos = startPos + endHandPos
        deckPos = pg.Vector2(handPos.x, handPos.y)
        playerList.append(Player(deckPos,handPos,player,angle,screen,dist))
        endHandPos = endHandPos.rotate(angle)
        
        
    index = 0
    while deck:
        card = deck.pop()
        playerList[index].giveCard(card)


        if index == len(players)-1:
            index = 0
        else:
            index += 1
            

    return playerList
"""
def Countdown():
    t = 10
    while t:
        print(t)
        t -= 1
        clock.tick(1)
"""

def getConnected(players):
    connected = []
    disconnect = False
    for player in players:
        if player.active:
            connected.append(player)
            index = players.index(player)
            break
    

    for player in players[index+1:]:
        if player.linkNegative:
            connected.append(player)
        else:
            disconnect = True
            break

    if disconnect == False and players[0].linkNegative:

        connected.append(players[0])
    disconnect = False

    index -= 1        
    while index > -1:
        if players[index].linkPositive:
            connected.append(players[index])
            index -= 1  
        else:
            disconnect = True
            break
    if disconnect == False and players[-1].linkPositive:
        connected.append(players[-1])        
    return connected
    



def countSound(count):
    numSound = mixer.Sound(r"assets\sounds\\" + str(count) + ".mp3")
    mixer.Sound.play(numSound)
    #mixer.Sound.stop(numSound)



   
def main(players):
    highVal = 0
    frameCount = 0
    #timeElapsed = 0
    nextCard = False
    currentPlayer = 0
    #cardsLeft = 0
    countdown = False
    newFrame = True
    while True:
        screen.fill((255,215,10))





        ###########EVENT LOOP###############
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_SPACE:
                    nextCard = True
                    newFrame = True
                if event.key == pg.K_t:
                    countdown = True
                    getHighValue = True
                    frameCount = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
        ###########EVENT LOOP###############



        #DRAW PLAYERS AND CHECK CARDS LEFT IN PLAY
        cardsLeft = 0

        for player in players:
            player.drawBacks(screen)
        for player in players:
            player.drawLines(screen)
            cardsLeft += len(player.hand)
        for player in players:
            player.drawCards(screen)
            
                
        numText = numFont.render(str(cardsLeft),True,pg.Color("White"))
        screen.blit(numText,(0,0,1,1))



        #CHECK IF ANY CARDS ARE LEFT
        if cardsLeft == 0:
            #TODO - END STATE
            pass



        #PLACE NEXT CARD    
        if nextCard:
            highVal = 0
            players[currentPlayer].active = False
            if currentPlayer == len(players)-1:
                currentPlayer = 0
            else:
                currentPlayer += 1                    
            players[currentPlayer].active = True
            if len(players[currentPlayer].hand):                
                players[currentPlayer].dealCard()
                cardsLeft -= 1
                players[currentPlayer].checkNeighbours(players, currentPlayer)
            #else:
                #players[currentPlayer].active = False
            nextCard = False
        

        ###########TIMER###########
        if countdown:
            if getHighValue:
                connected = getConnected(players)
                for player in connected:
                    if player.currentCard:





                        if player.currentCard.value > highVal:
                            highVal = player.currentCard.value




                getHighValue = False
                highVal +=1
            frameCount += 1
            
            if frameCount > clock.get_fps():
                
                frameCount = 0
                highVal -= 1
                newFrame = True
                #if highVal > 0:
                    #countSound(highVal)
           
            print(highVal)
            if highVal == 0:
                countdown = False
                

        if countdown:

            if newFrame:
                countSound(highVal)
                newFrame = False
            countText = countFont.render(str(highVal),True,pg.Color("White"))
            screen.blit(countText,(w/2-countText.get_width()/2,h/2-countText.get_height()/2,0,0))

        


        print(highVal)
        pg.display.update()
        #print(clock.get_fps())
        clock.tick(60)
def __init__():
    players = []
    playerText = []
    with open(r"playerInfo\playerInfo.txt","r") as playerFile:
        playerText.append(playerFile.readlines())
    for player in playerText[0]:
        players.append(player.strip("\n"))
    
    print(players)
    deck = createDeck()
    players = createPlayers(players,deck)
    main(players)
    #return deck, players