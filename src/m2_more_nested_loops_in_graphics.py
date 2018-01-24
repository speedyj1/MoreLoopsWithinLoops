"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jack Speedy.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    original_x = rectangle.corner_1.x
    original_y = rectangle.corner_1.y
    original_x1 = rectangle.corner_2.x
    original_y1 = rectangle.corner_2.y
    x = original_x
    y = original_y
    x1 = original_x1
    y1 = original_y1
    change_x_by = x1 - x
    change_y_by = y1 - y
    for j in range(n):
        for k in range(j+1):
            new_rectangle_corner_1 = rg.Point(x, y)
            new_rectangle_corner_2 = rg.Point(x1, y1)
            new_rectangle = rg.Rectangle(new_rectangle_corner_1, new_rectangle_corner_2)
            new_rectangle.attach_to(window)
            window.render(.5)
            x = x + change_x_by
            x1 = x1 + change_x_by
        y = y - change_y_by
        y1 = y1 - change_y_by
        x = original_x - ((k+1)*.5) * change_x_by
        x1 = original_x1 - ((k+1)*.5) * change_x_by

    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
