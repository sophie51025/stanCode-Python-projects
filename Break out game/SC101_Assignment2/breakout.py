"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3

def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!


    window = graphics.window

    dx = graphics.get_dx()
    dy = graphics.get_dy()
    ball = graphics.ball
    paddle = graphics.paddle
    paddle_height = graphics.get_brick_height()
    ball_radius = graphics.get_ball_radius()
    brick_cols = graphics.get_brick_cols()
    brick_rows = graphics.get_brick_rows()
    brick_spacing = graphics.get_brick_spacing()
    brick_offset = graphics.get_brick_offset()
    brick_width = graphics.get_brick_width()
    brick_height = graphics.get_brick_height()
    remain_live = NUM_LIVES
    live_label = GLabel('Life:' + str(remain_live))
    window.add(live_label, x=0, y=brick_offset/2)

    brick_left = brick_cols * brick_rows


    while True:
        # game main animation
        ball_upper_left = window.get_object_at(ball.x, ball.y)
        ball_upper_right = window.get_object_at(ball.x + 2 * ball_radius, ball.y)
        ball_lower_left = window.get_object_at(ball.x, ball.y + 2 * ball_radius)
        ball_lower_right = window.get_object_at(ball.x + 2 * ball_radius, ball.y + 2 * ball_radius)
        if brick_left == 0:
            window.remove(ball)
            you_win = GLabel('YOU WIN')
            you_win.color = 'Navy'
            window.add(you_win, x=(window.width-you_win.width)/2, y=(window.height-you_win.height)/2)
            break
        elif remain_live == 0:
            window.remove(ball)
            you_win = GLabel('YOU LOSE')
            you_win.color = 'Red'
            window.add(you_win, x=(window.width-you_win.width)/2, y=(window.height-you_win.height)/2)
            break
        elif graphics.start is True and remain_live > 0:
            ball.move(dx, dy)
            if ball.y + 2 * ball_radius >= window.height:
                remain_live -= 1
                live_label.text = 'Life:' + str(remain_live)
                window.add(ball, x=window.width / 2 - ball_radius, y=window.height / 2 - ball_radius)
                graphics.start = False
            elif ball.x <= 0 or ball.x + 2 * ball_radius >= window.width:
                dx = -dx
            elif ball.y <= 0:
                dy = -dy
            elif ball_lower_right is paddle and dy >= 0:
                dy = -dy
            elif ball_lower_right is paddle and dy >= 0:
                dy = -dy
            elif ball_upper_left is not None and ball_upper_left is not paddle and ball_upper_left is not live_label:
                window.remove(ball_upper_left)
                brick_left -= 1
                dy = -dy
            elif ball_upper_right is not None and ball_upper_right is not paddle and ball_upper_right is not live_label:
                window.remove(ball_upper_right)
                brick_left -= 1
                dy = -dy
            elif ball_lower_right is not None and ball_lower_right is not paddle and ball_lower_right is not live_label:
                window.remove(ball_lower_right)
                brick_left -= 1
                dx = -dx
                dy = -dy
            elif ball_lower_left is not None and ball_lower_left is not paddle and ball_lower_left is not live_label:
                window.remove(ball_lower_left)
                brick_left -= 1
                dx = -dx
                dy = -dy
        pause(FRAME_RATE)



if __name__ == '__main__':
    main()
