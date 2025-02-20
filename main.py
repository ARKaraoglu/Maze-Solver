from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    point1 = Point(x = 100, y = 150)
    point2 = Point(x = 200, y = 250)
    point3 = Point(x = 50, y = 215)
    point4 = Point(x = 520, y = 440)

   # line1 = Line(point1, point2)
   # line2 = Line(point3, point4)
   #
   # win.draw_line(line1, "black")
   # win.draw_line(line2, "red")
   # line1 = Line(point1, point2)
   # line2 = Line(point3, point4)
   #
   # win.draw_line(line1, "black")
    # cell1 = Cell(win)
    # cell1.has_top_wall = False
    #
    # cell2 = Cell(win)
    # cell2.has_top_wall = False
    #
    # cell3 = Cell(win)
    # cell3.has_bottom_wall = False
    #
    # cell4 = Cell(win)
    # cell4.has_right_wall = False
    #
    # cell1.draw(100, 100, 200, 200) 
    # cell2.draw(300, 300, 500, 500)
    # cell3.draw(500, 800, 600, 1000)
    # cell4.draw(50, 50, 100, 100)
    
    # cell1 = Cell(win)
    # cell2 = Cell(win)
    #
    # cell1.draw(100, 100, 200, 200)
    # cell2.draw(300, 100, 400, 200)
    #
    # cell1.draw_move(cell2, undo = True)
    
    # cell1 = Cell(win)
    #
    # cell1.draw(100, 100, 500, 200)
    maze = Maze(x1 = 100, y1 = 100, num_rows = 6, num_cols = 6, cell_size_x = 75, cell_size_y = 75, win = win, seed = 110)
    maze._solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
