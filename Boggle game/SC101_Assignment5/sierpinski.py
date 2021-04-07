"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine, GPolygon, GOval
from campy.gui.events.timer import pause
import math

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:draw sierpinski triangle of given layer and triangle initial info
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: decide how many layer of sierpinski triangle
	:param length: length of triangle's side
	:param upper_left_x: x coordinate of first triangle's start point
	:param upper_left_y: y coordinate of first triangle's start point
	:return: sierpinski triangle of given order
	"""

	if order == 0:
		pass
	else:
		triangle = GPolygon()
		triangle.add_vertex((upper_left_x, upper_left_y))
		triangle.add_vertex((upper_left_x + length, upper_left_y))
		triangle.add_vertex((upper_left_x + 0.5 * length, upper_left_y + 0.866 * length))

		circle = GOval(math.sqrt(3) * length / 3, math.sqrt(3) * length /3, x=upper_left_x + 0.5 * length - math.sqrt(3) * length /6, y=upper_left_y )
		circle.filled = True
		circle.fill_color ='snow'


		window.add(circle)
		window.add(triangle)


		sierpinski_triangle(order - 1, length/2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length/2, upper_left_x + 0.25 * length, upper_left_y + 0.433 * length)
		sierpinski_triangle(order - 1, length/2, upper_left_x + 0.5 * length, upper_left_y)





if __name__ == '__main__':
	main()