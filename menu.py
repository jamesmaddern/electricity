import pygame, math, sys
from inputBox import InputBox as ib
from pygame import draw,Color,Rect,mixer

pygame.init()
screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()
w = screen.get_width()
h = screen.get_height()


buttonFont = pygame.font.SysFont("Bahnschrift",28)
logoFont = pygame.font.SysFont("Autodiagraphic", 148)


logo = pygame.image.load(r"assets\images\logo.png")
logoRect = logo.get_rect()
logoText = logoFont.render("ELECTRICITY",True,Color("Black"))


numOfPlayers = 0
startingPlayers = 9



inputBoxList = []

def createInputBox():
    global numOfPlayers
    i = numOfPlayers + 1
    inputBoxList.append(ib(i,Rect(w-300,175+i*60,250,50)))
    numOfPlayers += 1
    
def destroyInputBox():
    global numOfPlayers
    
    inputBoxList.pop(-1)
    numOfPlayers -= 1

def clearInputBox():
    index = 1
    for i in inputBoxList:
        i.text = "PLAYER " + str(index)   
        index += 1
for i in range(1,startingPlayers+1):
    createInputBox()
    print(numOfPlayers)





spacePressed = False
index = 0
def allignText(button,text):
    
    textPos = (button.width - text.get_width())/2
    return pygame.Rect(button.x+textPos, button.y,text.get_width(),text.get_height())



#BUTTONS
addPlayerBtn = pygame.Rect(w-200,20,200,40)
addPlayerTxt = buttonFont.render("Add Player",True,Color(255,215,10))
addPlayerTxtBox = allignText(addPlayerBtn, addPlayerTxt)

rmvPlayerBtn = pygame.Rect(w-200,70,200,40)
rmvPlayerTxt = buttonFont.render("Remove Player",True,Color(255,215,10))
rmvPlayerTxtBox = allignText(rmvPlayerBtn, rmvPlayerTxt)

clrPlayerBtn = pygame.Rect(w-200,120,200,40)
clrPlayerTxt = buttonFont.render("Clear Players",True,Color(255,215,10))
clrPlayerTxtBox = allignText(clrPlayerBtn, clrPlayerTxt)

startGameBtn = pygame.Rect(w-200,h-60,200,40)
startGameTxt = buttonFont.render("Start Game",True,Color(255,215,10))
startGameTxtBox = allignText(startGameBtn, startGameTxt)

quitGameBtn = pygame.Rect(0,h-60,200,40)
quitGameTxt = buttonFont.render("Quit Game",True,Color(255,215,10))
quitGameTxtBox = allignText(quitGameBtn, quitGameTxt)
#BUTTONS






#mPos = pygame.mouse.get_pos()
def resetColour():
    global addColour, rmvColour, clrColour
    addColour = "Black"
    rmvColour = "Black"
    clrColour = "Black"
    


buttonPressed = False



resetColour()

startGame = False
#playsound(r"C:\Users\James\Music\quizsongs\feel.mp3")
mixer.music.load(r"assets\sounds\naive.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.05)
    
while startGame == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            for box in inputBoxList:
                if box.active:
                    box.enterText(event)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
                        
            if addPlayerBtn.collidepoint(event.pos):
                if numOfPlayers < 9:
                    createInputBox()
                    addColour = "yellow"
                else:
                    addColour = "red"
            elif rmvPlayerBtn.collidepoint(event.pos):
                if numOfPlayers > 2:
                    destroyInputBox()
                    rmvColour = "yellow"
                else:
                    rmvColour = "red"
            elif clrPlayerBtn.collidepoint(event.pos):
                
                clearInputBox()
                clrColour = "yellow"
            elif startGameBtn.collidepoint(event.pos):
                startGame = True
            elif quitGameBtn.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            else:
                for box in inputBoxList:
                    if box.rect.collidepoint(event.pos):
                        box.active = not box.active
                    else:
                        box.active = False
                        
                
        if event.type == pygame.MOUSEBUTTONUP:
            resetColour()

    screen.fill(Color(255,215,10))


    draw.rect(screen,Color(addColour),addPlayerBtn)
    screen.blit(addPlayerTxt,addPlayerTxtBox)
    draw.rect(screen,Color(rmvColour),rmvPlayerBtn)
    screen.blit(rmvPlayerTxt,rmvPlayerTxtBox)
    draw.rect(screen,Color(clrColour),clrPlayerBtn)
    screen.blit(clrPlayerTxt,clrPlayerTxtBox)
    draw.rect(screen,Color("Black"),startGameBtn)
    screen.blit(startGameTxt,startGameTxtBox)
    draw.rect(screen,Color("Black"),quitGameBtn)
    screen.blit(quitGameTxt,quitGameTxtBox)

    

    screen.blit(logo,(w/2-logoRect.width/2,h/2-logoRect.width/2-100,100,100))
    screen.blit(logoText,(w/2 - logoText.get_width()/2,logoRect.height,1,1))
    for box in inputBoxList:
        box.update(screen)
        
    #for box in inputBoxList:
        
        
        #box.draw(screen)

    
    
    
    

    pygame.display.update()
    clock.tick(30)




playerList = []

    
with open(r"playerInfo\playerInfo.txt","w") as playerFile:
    for box in inputBoxList:
        playerFile.write(box.text + "\n")

pygame.quit()
        
   
    
        
            


        