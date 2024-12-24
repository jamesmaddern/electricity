import pygame
import sys
from Button import Button
from inputBox import InputBox
from pygame import Color
class Menu:
    def __init__(self):
        self.screen = pygame.surface.Surface((1920,1080))
        buttonFont = pygame.font.SysFont("Bahnschrift",28)
        self.logoFont = pygame.font.SysFont("Autodiagraphic",148)
        self.logo = pygame.image.load(r"assets/images/logo.png")
        self.logoRect = self.logo.get_rect()
        self.logoText = self.logoFont.render("ELECTRICITY",True,Color("Black"))
        self.numOfPlayers = 0
        self.startingPlayers = 9
        self.inputBoxList = []
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        self.buttonList = [Button(pygame.Rect(self.w-200,20,200,40),
                        buttonFont,
                        "Add Player",
                        Color(255,215,10)),
                Button(pygame.Rect(self.w-200,70,200,40),
                        buttonFont,
                        "Remove Player",
                        Color(255,215,10)),
                Button(pygame.Rect(self.w-200,120,200,40),
                        buttonFont,
                        "Clear Players",
                        Color(255,215,10)),
                Button(pygame.Rect(self.w-200,self.h-60,200,40),
                        buttonFont,
                        "Start Game",
                        Color(255,215,10)),
                Button(pygame.Rect(0,self.h-60,200,40),
                        buttonFont,
                        "Quit Game",
                        Color(255,215,10))]
        for i in range(self.startingPlayers):
            self.createInputBox()
    def createInputBox(self):
        i = self.numOfPlayers + 1
        self.inputBoxList.append(InputBox(
            i,
            pygame.Rect(self.w-300,
                        175+i*60,
                        250,
                        50)
        ))
        self.numOfPlayers+=1
    def destroyInputBox(self):
        self.inputBoxList.pop(-1)
        self.numOfPlayers -= 1
    def clearInputBoxes(self):
        for i, box in enumerate(self.inputBoxList, 1):
            box.text = f"PLAYER {i}"
    def update(self):
        self.screen.fill(Color(255,215,10))
        for button in self.buttonList:
            button.draw(self.screen)
        for inputBox in self.inputBoxList:
            inputBox.update(self.screen)
        self.screen.blit(self.logo,
                         (self.w/2-self.logoRect.width/2,
                          self.h/2-self.logoRect.width/2-100,
                          100,
                          100))
        self.screen.blit(self.logoText,
                         (self.w/2 - self.logoText.get_width()/2,
                          self.logoRect.height,
                          1,
                          1))
    def eventHandler(self,event,w,h):
        startGame = False
        xScale = 1920/w
        yScale = 1080/h
        if event.type == pygame.MOUSEBUTTONDOWN:
            mX,yX = event.pos
            mPos = (xScale * mX, yScale * yX)
            for button in self.buttonList:
                if button.rect.collidepoint(mPos):
                    match button.name:
                        case "Add Player":
                            if self.numOfPlayers < 9:
                                self.createInputBox()
                        case "Remove Player":
                            if self.numOfPlayers > 2:
                                self.destroyInputBox()
                        case "Clear Players":
                            self.clearInputBoxes()
                        case "Start Game":
                            startGame = True
                        case "Quit Game":
                            pygame.quit()
                            sys.exit(0)
            for box in self.inputBoxList:
                if box.rect.collidepoint(mPos):
                    box.active = not box.active
                else:
                    box.active = False
        if event.type == pygame.KEYDOWN:
            for box in self.inputBoxList:
                if box.active:
                    box.enterText(event)
        return startGame