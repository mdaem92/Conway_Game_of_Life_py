from Board import Board
import pygame,time
class Game:

    def __init__(self,width:int, height:int,initialPattern) -> None:
        self.win = pygame.display.set_mode((width,height))
        pygame.display.set_caption('Game of Life')
        self.board = Board(width,height,initialPattern=initialPattern)
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.run = True
    
    def events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    self.run = False
    


    def play(self):
        
        while self.run:
            # print('running')
            self.clock.tick(20)
            self.win.fill([255,255,255])
            self.events()
            # newState = self.board.live()
            self.board.live()
            self.board.drawBoard(self.win)
            pygame.display.update()
            



