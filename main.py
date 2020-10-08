import pygame as pg

class GameEngine(object):
    def __init__(self, width, height, fps):
        pg.init()
        self.screen = pg.display.set_mode((width, height))

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return

            self.screen.fill((255, 255, 255))
            pg.display.flip()

if __name__ == "__main__":
    GE = GameEngine(800, 600, 60)
    GE.main_loop()
