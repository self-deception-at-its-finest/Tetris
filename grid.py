import pygame
from colours import Colours


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colours = Colours.cell_colour()

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +206, row*self.cell_size +16, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colours[cell_value], cell_rect)

    def is_inside(self,row,column):
        if row >= 0 and row<self.num_rows and column >= 0 and column <self.num_cols:
            return True
        else:
            return False

    def is_empy(self,row,column):
        if self.grid[row][column] == 0:
            return True
        return False

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1,0,-1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed+=1
            elif completed>0:
                self.move_row_down(row,completed)
        return completed

    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self,row,num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0