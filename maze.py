from point import Point
from line import Line
from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed

        if self._seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(i = 0, j = 0)
        self._reset_cells_visited()
        # tl_point = Point(current_x, current_y)
        # tr_point = Point(current_x + self._cell_size_x, current_y)
        # bl_point = Point(current_x, current_y + self._cell_size_y)
        # bl_point = Point(current_x + self._cell_size_x, current_y + self._cell_size_y)
        # 
        # current_x += self._cell_size_x

    def _create_cells(self):
        if self._num_rows == None or self._num_cols == None:
            return []

        self._cells = []

        for row in range(0, self._num_rows): # Y is going to increase
            self._cells.append([])
            for col in range(0, self._num_cols): # X is going to increase
                cell = Cell(self._win)
                self._cells[row].append(cell)

        for row in range(0, self._num_rows):
            for col in range(0, self._num_cols):
                pass
                self._draw_cell(row, col)


    def _draw_cell(self, i, j):
        maze_position_x = self._x1
        maze_position_y = self._y1

        cell_x1 = maze_position_x + (self._cell_size_x * j)
        cell_y1 = maze_position_y + (self._cell_size_y * i)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        row_len = len(self._cells)
        col_len = len(self._cells[row_len - 1])
        self._cells[0][0].has_top_wall = False
        self._cells[row_len - 1][col_len - 1].has_bottom_wall = False
        
        self._draw_cell(0, 0)
        self._draw_cell(row_len - 1, col_len - 1)


    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        while True:
            to_visit = []

            if i > 0 and self._cells[i - 1][j]._visited == False: # Above 1
                to_visit.append([i - 1, j])

            if i + 1 != len(self._cells) and self._cells[i + 1][j]._visited == False: # Below 1
                to_visit.append([i + 1, j])

            if j > 0 and self._cells[i][j - 1]._visited == False: # Left 1
                to_visit.append([i, j - 1])

            if j + 1 != len(self._cells[0]) and self._cells[i][j + 1]._visited == False: # Right 1
                to_visit.append([i, j + 1])

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                next_random_cell = random.choice(to_visit)
                if i == next_random_cell[0]:
                    if j < next_random_cell[1]:
                        self._cells[i][j].has_right_wall = False
                        self._cells[next_random_cell[0]][next_random_cell[1]].has_left_wall = False
                    else:
                        self._cells[i][j].has_left_wall = False
                        self._cells[next_random_cell[0]][next_random_cell[1]].has_right_wall = False
                else:
                    if i < next_random_cell[0]:
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[next_random_cell[0]][next_random_cell[1]].has_top_wall = False
 
                    else:
                        self._cells[i][j].has_top_wall = False
                        self._cells[next_random_cell[0]][next_random_cell[1]].has_bottom_wall = False
                self._break_walls_r(i = next_random_cell[0], j = next_random_cell[1])


    def _reset_cells_visited(self):
        for row in self._cells:
            for col in row:
                col._visited = False
    
    def _solve(self):
        return self._solve_r(i = 0, j = 0)

    
    def _solve_r(self,i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell._visited = True

        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True

        #Up
        if i != 0 and current_cell.has_top_wall == False:
            if self._cells[i - 1][j]._visited == False:
                current_cell.draw_move(self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                current_cell.draw_move(self._cells[i - 1][j], undo = True)
                
        #Down
        if i != len(self._cells) - 1 and current_cell.has_bottom_wall == False:
            if self._cells[i + 1][j]._visited == False:
                current_cell.draw_move(self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                current_cell.draw_move(self._cells[i + 1][j], undo = True)
        #Right
        if j != len(self._cells[0]) and current_cell.has_right_wall == False:
            if self._cells[i][j + 1]._visited == False:
                current_cell.draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                current_cell.draw_move(self._cells[i][j + 1], undo = True)
        #Left
        if j != 0 and current_cell.has_left_wall == False:
            if self._cells[i][j - 1]._visited == False:
                current_cell.draw_move(self._cells[i][j - 1])
                if self._solve_r(i , j - 1):
                    return True
                current_cell.draw_move(self._cells[i][j - 1], undo = True)

        return False











