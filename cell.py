from point import Point
from line import Line

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2,):
        # low_x = 0
        # low_y = 0
        # high_x = 0
        # high_y = 0
        # self._x1 = x1
        # self._y1 = y1
        # self._x2 = x2
        # self._y2 = y2
        # 
        # if self._x1 > self._x2:
        #     low_x = self._x2
        #     high_x = self._x1
        # else:
        #     low_x = self._x1
        #     high_x = self._x2
        #
        # if self._y1 > self._y2:
        #     low_y = self._y2
        #     high_y = self._y1
        # else:
        #     low_y = self._y1
        #     high_y = self._y2

        self._x1, self._x2 = sorted([x1, x2])
        self._y1, self._y2 = sorted([y1, y2])

        if self.has_left_wall:
            self._win._Window__canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill = "black", width = 2)

        if self.has_top_wall:
            self._win._Window__canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill = "black", width = 2)

        if self.has_right_wall:
            self._win._Window__canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill = "black", width = 2)

        if self.has_bottom_wall:
            self._win._Window__canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill = "black", width = 2)

    def draw_move(self, to_cell, undo = False):
        assert self._x1 is not None and self._x2 is not None
        assert self._y1 is not None and self._y2 is not None

        src_middle_point = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        dest_middle_point = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        
        line = Line(src_middle_point, dest_middle_point)
        
        color = "red"
        if undo == True:
            color = "gray"

        self._win.draw_line(line, color)













