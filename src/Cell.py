import pygame
class Cell:

    def __init__(self,val,row,col,width=90,height=90) -> None:
        self.val = val
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def drawCube(self,surface):

        xPos = self.col * self.width
        yPos = self.row * self.height
        if self.val == 1:
            pygame.draw.rect(surface, (0,0,0),(xPos,yPos, self.width ,self.height), 0)
        # else:
        #     pygame.draw.rect(surface, (255,255,255),(xPos,yPos, self.width ,self.height), 2)
    
    def isAlive(self):
        return self.val == 1

    def __str__(self) -> str:
        return self.row + ','+self.col 
