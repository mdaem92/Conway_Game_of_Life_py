from Cell import Cell
import random,pygame,time,logging,copy


logging.basicConfig(filename='gol.log',level=logging.DEBUG)

class Board:

    def __init__(self, width=540, height=540, cellWidth=180, cellHeight=180, radius=1 ,numberOfIntialActiveCells=100,initialPattern = None) -> None:
        self.ncol = width // cellWidth
        self.nrow = height // cellHeight
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.radius = radius
        if initialPattern is None:
            self.numberOfIntialActiveCells = numberOfIntialActiveCells
            self.cells = self.generateCells()
        else:
            self.cells = initialPattern
        self.captured = 0

    def generateCells(self):
        # here create an array containing cells corresponding to the width,height,nrow,ncol
        cells = [[0]*self.ncol for i in range(self.nrow)]
        iVals = random.sample(range(self.nrow), self.numberOfIntialActiveCells)
        jVals = random.sample(range(self.ncol), self.numberOfIntialActiveCells)
        for i in range(self.numberOfIntialActiveCells):
            cells[iVals[i]][jVals[i]]= 1

        return cells

    def drawBoard(self,surface):
        for i in range(self.nrow):
            for j in range(self.ncol):
                # self.cells[i][j].drawCube(surface)
                yPos = i * self.cellWidth
                xPos = j * self.cellHeight
                if self.cells[i][j] == 1:
                    pygame.draw.rect(surface, (0,0,0),(xPos,yPos, self.cellWidth ,self.cellHeight), 0)
        # if self.captured == 0:
        #     pygame.image.save(surface,"screenshot.jpg")
        #     self.captured += 1

    def findAndCountNeighbors(self,i,j):
        count=0
        radius = self.radius
        for x in range(i-radius,i+radius+1):
            for y in range(j-radius,j+radius+1):
                if (x != i or y != j) and (-1<y<self.nrow and -1<x<self.ncol):
                    if self.cells[x][y] == 1:
                        count+=1
        return count

    def checkSurvival(self, i, j):
        # check if 2 or 3 neighbors are alive
        logging.debug(f'checking for survival for index [{i}][{j}]')
        count = self.findAndCountNeighbors(i,j)
        logging.debug(f'found {count} live neighbors' )
        if 2<= count<= 3:
            logging.debug(f'index [{i}][{j}] will survive' )
        else:
            logging.debug(f'index [{i}][{j}] will NOT survive' )

        return 2<= count<= 3

        # return True

    def checkRevival(self,i,j):
        # check if 3 neighbors are alive
        logging.debug(f'checking for Revival for index [{i}][{j}]')
        count = self.findAndCountNeighbors(i,j)
        logging.debug(f'found {count} live neighbors' )
        return count == 3

    def live(self):
        newState = [[0]*self.ncol for i in range(self.nrow)]
        for i in range(self.nrow):
            for j in range(self.ncol):
                
                # if self.cells[i][j]== 1 and self.checkSurvival(i,j):
                #     # print('surviving')
                #     continue
                # elif self.cells[i][j] == 0 and self.checkRevival(i,j):
                #     # print('reviving')
                #     self.cells[i][j] = 1
                # else:
                #     self.cells[i][j] = 0
                if self.cells[i][j] == 0:
                    # logging.debug(f'for index[{i}][{j}]')
                    if self.checkRevival(i,j):
                        # self.cells[i][j] = 1
                        newState[i][j] = 1
                else:
                    if not self.checkSurvival(i,j):
                        # self.cells[i][j] = 0
                        newState[i][j] = 0
                    else:
                        newState[i][j] = 1
        logging.debug(f'new state: {newState}')
        self.cells = newState

                    

        


        



