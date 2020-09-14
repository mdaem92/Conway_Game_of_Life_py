from Game import Game

def main():
    initialPattern = [
                        [0,1,0],
                        [0,1,0],
                        [0,1,0],
                        
                    ]
    game = Game(540,540,initialPattern=initialPattern)
    game.play()

if __name__ == "__main__":
    main()