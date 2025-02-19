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
            random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(i = 0, j = 0)

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

        # cell = Cell(self._win)
        # print(f"Row:{i},Col: {j}, tl_x1:{cell_x1}, tl_y1:{cell_y1}, br_x2:{cell_x2}, br_y2:{cell_y2}")
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        # assert self._win is not None
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # row_len = len(self._cells)
        # col_len = len(self._cells[row_len - 1])
        #
        # entrance_cell = self._cells[row_len - row_len][0]
        # exit_cell = self._cells[row_len - 1][col_len - 1]
        # entrance_cell.has_top_wall = False
        # exit_cell.has_bottom_wall = False
        # 
        # print(self._cells[row_len - row_len][0].__repr__())
        # print(self._cells[row_len - 1][col_len - 1].__repr__())
        # entrance_cell.draw(entrance_cell._x1, entrance_cell._y1, entrance_cell._x2, entrance_cell._y2)
        # exit_cell.draw(exit_cell._x1, exit_cell._y1, exit_cell._x2, exit_cell._y2)
        
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

                



