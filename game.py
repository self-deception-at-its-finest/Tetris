import pygame.event
from grid import Grid
from tetromino import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.tetrominoes = [ITetromino(), JTetromino(), LTetromino(), OTetromino(), STetromino(), TTetromino(), ZTetromino()]
        self.next_tetromino = self.get_random_tetromino()
        self.current_tetromino = self.get_random_tetromino()
        self.gameover = False
        self.paused = False
        self.score = 0

    def update_score(self, lines_cleared):
        if lines_cleared == 1:
            self.score +=1
        elif lines_cleared == 2:
            self.score +=3
        elif lines_cleared == 3:
            self.score +=5

    def get_random_tetromino(self):
        if len(self.tetrominoes)==0:
            self.tetrominoes = [ITetromino(), JTetromino(), LTetromino(), OTetromino(), STetromino(), TTetromino(), ZTetromino()]
        tetromino = random.choice(self.tetrominoes)
        self.tetrominoes.remove(tetromino)
        return tetromino

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_tetromino.draw(screen, 206, 16)

        if self.next_tetromino.id == 3:
            self.next_tetromino.draw(screen,-45,280)
        elif self.next_tetromino.id == 4:
            self.next_tetromino.draw(screen, -45, 270)
        else:
            self.next_tetromino.draw(screen,-35,260)

    def move_left(self):
        self.current_tetromino.move(0, -1)
        if self.tetromino_inside() == False or self.tetromino_fits() == False:
            self.current_tetromino.move(0, 1)

    def move_right(self):
        self.current_tetromino.move(0, 1)
        if self.tetromino_inside() == False or self.tetromino_fits() == False:
            self.current_tetromino.move(0, -1)

    def move_down(self):
        self.current_tetromino.move(1, 0)
        if self.tetromino_inside() == False or self.tetromino_fits() == False:
            self.current_tetromino.move(-1, 0)
            self.lock_tetromino()


    def tetromino_inside(self):
        tiles = self.current_tetromino.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_tetromino.rotate()
        if self.tetromino_inside() == False or self.tetromino_fits() == False:
            self.current_tetromino.undo_rotation()

    def tetromino_fits(self):
        tiles = self.current_tetromino.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empy(tile.row,tile.column) == False:
                return False
        return True

    def lock_tetromino(self):
        tiles = self.current_tetromino.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_tetromino.id
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = self.get_random_tetromino()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared)
        if self.tetromino_fits() == False:
            self.gameover = True

    def reset(self):
        self.grid.reset()
        self.tetrominoes = [ITetromino(), JTetromino(), LTetromino(), OTetromino(), STetromino(), TTetromino(),ZTetromino()]
        self.current_tetromino = self.get_random_tetromino()
        self.next_tetromino = self.get_random_tetromino()
        self.score=0

    def pause(self):
        self.paused = True
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.paused = False