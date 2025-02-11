from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    
    point1 = Point(x = 100, y = 150)
    point2 = Point(x = 200, y = 250)
    point3 = Point(x = 50, y = 215)
    point4 = Point(x = 520, y = 440)

    line1 = Line(point1, point2)
    line2 = Line(point3, point4)

    win.draw_line(line1, "black")
    win.draw_line(line2, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()
