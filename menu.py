import pygame, math, sys
from Button import Button
from inputBox import InputBox as ib
from pygame import draw,Color,Rect,mixer

#SETUP
pygame.init()
display = pygame.display.set_mode((600,600),pygame.RESIZABLE)
screen = pygame.surface.Surface((1920,1080))
clock = pygame.time.Clock()

#FONTS
buttonFont = pygame.font.SysFont("Bahnschrift",28)
logoFont = pygame.font.SysFont("Autodiagraphic", 148)

#LOGO
logo = pygame.image.load(r"assets/images/logo.png")
logoRect = logo.get_rect()
logoText = logoFont.render("ELECTRICITY",True,Color("Black"))

#INITIALISING GLOBAL VARIABLES
numOfPlayers = 0
startingPlayers = 9
inputBoxList = []
w = screen.get_width()
h = screen.get_height()
startGame = False

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

#INITIALISE BUTTONS
buttonList = [Button(pygame.Rect(w-200,20,200,40),
                        buttonFont,
                        "Add Player",
                        Color(255,215,10)),
                Button(pygame.Rect(w-200,70,200,40),
                        buttonFont,
                        "Remove Player",
                        Color(255,215,10)),
                Button(pygame.Rect(w-200,120,200,40),
                        buttonFont,
                        "Clear Players",
                        Color(255,215,10)),
                Button(pygame.Rect(w-200,h-60,200,40),
                        buttonFont,
                        "Start Game",
                        Color(255,215,10)),
                Button(pygame.Rect(0,h-60,200,40),
                        buttonFont,
                        "Quit Game",
                        Color(255,215,10))]

#RESETING COLOUR OF INPUT BOX TEXT WHEN NOT ACTIVE
def resetColour():
    global addColour, rmvColour, clrColour
    addColour = "Black"
    rmvColour = "Black"
    clrColour = "Black"
resetColour()

#############GAME LOOP#################
while startGame == False:
    w = display.get_width()
    h = display.get_height()
    xScale = 1920/w
    yScale = 1080/h
    #EVENT LOOP
    for event in pygame.event.get():
        #QUIT
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #ENTERING TEXT INTO THE INPUT BOXES
        if event.type == pygame.KEYDOWN:
            for box in inputBoxList:
                if box.active:
                    box.enterText(event)
        #CLICK HANDLING    
        if event.type == pygame.MOUSEBUTTONDOWN:
            #SCALE MOUSE POSITION TO WINDOW SIZE
            mX,yX = event.pos
            mPos = (xScale * mX, yScale * yX)
            for button in buttonList:
                if button.rect.collidepoint(mPos):
                    match button.name:
                        case "Add Player":
                            if numOfPlayers < 9:
                                createInputBox()
                        case "Remove Player":
                            if numOfPlayers > 2:
                                destroyInputBox()
                        case "Clear Players":
                            clearInputBox()
                        case "Start Game":
                            startGame = True
                        case "Quit Game":
                            pygame.quit()
                            sys.exit(0)
            for button in inputBoxList:
                if button.rect.collidepoint(mPos):
                    button.active = not button.active
                else:
                    button.active = False
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode(event.size, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)    
                
        if event.type == pygame.MOUSEBUTTONUP:
            resetColour()
    ###############EVENT LOOP###############

    #DRAW SCREEN BACKGROUND
    screen.fill(Color(255,215,10))

    #DRAWING BUTTONS
    for button in buttonList:
        button.draw(screen)

    #DRAWING LOGO
    screen.blit(logo,(screen.get_width()/2-logoRect.width/2,screen.get_height()/2-logoRect.width/2-100,100,100))
    screen.blit(logoText,(screen.get_width()/2 - logoText.get_width()/2,logoRect.height,1,1))

    #DRAWING INPUT BOXES
    for box in inputBoxList:
        box.update(screen)    

    #UPDATE DISPLAY
    display.blit(pygame.transform.scale(screen, display.get_rect().size), (0, 0))
    pygame.display.update()
    clock.tick(30)
#############GAME LOOP#################

playerList = []
with open(r"playerInfo\playerInfo.txt","w") as playerFile:
    for box in inputBoxList:
        playerFile.write(box.text + "\n")

pygame.quit()
        
   
    
        
            


        