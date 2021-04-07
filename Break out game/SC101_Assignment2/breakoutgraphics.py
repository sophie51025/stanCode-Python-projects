"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random


#constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 100      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.__ball_radius = ball_radius
        self.__paddle_width = paddle_width
        self.__paddle_height = paddle_height
        self.__paddle_offset = paddle_offset
        self.__brick_rows = brick_rows
        self.__brick_cols = brick_cols
        self.__brick_width = brick_width
        self.__brick_height = brick_height
        self.__brick_offset = brick_offset
        self.__brick_spacing = brick_spacing

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(self.__paddle_width, self.__paddle_height,x=(self.window.width-paddle_width)/2,y=(self.window.height-paddle_height - self.__paddle_offset))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(self.__ball_radius*2, self.__ball_radius*2, x=self.window.width/2-self.__ball_radius, y=self.window.height/2 - self.__ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self._dy = INITIAL_Y_SPEED
        self._dx = random.randint(1, MAX_X_SPEED)
        if (random.random()>0.5):
            self._dx = -self._dx

        # Initialize our mouse listeners.
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_start)
        self.start = False

        # Draw bricks
        for i in range(self.__brick_rows):
            for j in range(self.__brick_cols):
                self.bricks = GRect(self.__brick_width,self.__brick_height, x=j*(self.__brick_width+self.__brick_spacing), y=self.__brick_offset + i*(self.__brick_height+self.__brick_spacing))
                self.bricks.filled = True
                if i % 10 == 0 or i % 10 == 1:
                    self.bricks.fill_color = 'red'
                elif i % 10 == 2 or i % 10 == 3:
                    self.bricks.fill_color = 'orange'
                elif i % 10 == 4 or i % 10 == 5:
                    self.bricks.fill_color = 'yellow'
                elif i % 10 == 6 or i % 10 == 7:
                    self.bricks.fill_color = 'green'
                elif i % 10 == 8 or i % 10 == 9:
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks)

    def paddle_move(self, paddle_position):
        if self.paddle.width <= paddle_position.x <= self.window.width-self.paddle.width :
            self.paddle.x = paddle_position.x - self.paddle.width/2
            self.paddle.y = self.window.height - self.paddle.height - self.__paddle_offset
        elif paddle_position.x <= self.paddle.width:
            self.paddle.x = 0
            self.paddle.y = self.window.height - self.paddle.height - self.__paddle_offset
        elif paddle_position.x >= self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width
            self.paddle.y = self.window.height - self.paddle.height - self.__paddle_offset


    def ball_start(self,ball_position):
        ball_start_position = self.window.get_object_at(self.window.width / 2, self.window.height / 2)
        if ball_start_position is self.ball:
            self.start = True

    #Getter

    def get_dy(self):
        return self._dy

    def get_dx(self):
        return self._dx

    def get_paddle_height(self):
        return self.__paddle_height

    def get_paddle_width(self):
        return self.__paddle_width

    def get_ball_radius(self):
        return self.__ball_radius

    def get_brick_cols(self):
        return self.__brick_cols

    def get_brick_rows(self):
        return self.__brick_rows

    def get_brick_spacing(self):
        return self.__brick_spacing

    def get_brick_offset(self):
        return self.__brick_offset

    def get_brick_height(self):
        return self.__brick_height

    def get_brick_width(self):
        return self.__paddle_width

