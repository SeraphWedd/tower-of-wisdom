import pygame as pg
import numpy as np

class GameEngine(object):
    def __init__(self, width, height, fps):
        pg.init()
        
        self.screen = pg.display.set_mode((width, height))
        self.buffer = 50
        self.width = width
        self.height = height
        self.game_width = 5 * width
        self.game_height = 5 * height
        
        self.screen_state = 'splash'
        self.screen_center = pg.Vector2(width//2, height//2)

        self.timer = pg.time.Clock()
        self.fps = fps

        self.current_floor = 0
        self.n_floors = 101
        self.n_entities = 1000
        self.x = np.zeros((self.n_floors, self.n_entities))
        self.y = np.zeros((self.n_floors, self.n_entities))
        self.entities = []
        
    def manhattan_distance(self):
        #Get screen items
        self.dx = self.x - self.screen_center[0]
        self.dy = self.y - self.screen_center[1]
        self.to_blit = ((np.abs(self.dx)<=self.width+self.buffer) &
                        (np.abs(self.dy)<=self.height+self.buffer))

    def main_loop(self):
        count = 0
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                
            self.manhattan_distance()
            self.screen.fill((255, 255, 255))

            dt = self.timer.get_time()/1000
            rendering = 0
            for entity in self.entities:
                if entity.floor != self.current_floor:
                    if count == entity.floor:
                        entity.update(self.fps*dt)
                else:
                    entity.update(dt)
                    if entity.floor == self.current_floor and \
                       self.to_blit[entity.floor, entity.i]:
                        rendering += 1
                        entity.draw(self.screen)

            count = (1 + count)%self.n_floors
            
            pg.display.set_caption("TOWER OF WISDOM FPS: %.2f Items: %i"
                                   %(self.timer.get_fps(), rendering))
            pg.display.flip()
            self.timer.tick_busy_loop(self.fps)

if __name__ == "__main__":
    from Scripts.game_objects import GameObject
    GE = GameEngine(800, 600, 60)
    for j in range(101):
        for i in range(1000):
            GE.entities.append(GameObject(GE, i, j))
            GE.x[j, i] = np.random.randint(0, GE.game_width)
            GE.y[j, i] = np.random.randint(0, GE.game_height)
    GE.main_loop()
    
