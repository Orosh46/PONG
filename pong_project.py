# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-400.123 / 60.0, -400.0 / 60.0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if LEFT == 0:
        vel[0] = -400.123 / 60.0
    if LEFT == 1:
        vel[0] = 400.123 / 60.0


def spawn_ball_clicked():
    spawn_ball("left")


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are numbers
    global score1, score2  # these are ints
    LEFT = random.randrange(0, 1)




def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

def draw_handler():
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    if LEFT == False
        spawn_ball(True)




    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
    if ball_pos[0] >= WIDTH - BALL_RADIUS:
        vel[0] = - vel[0]
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = -vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel[1] = -vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen

    # draw paddles

    # determine whether paddle and ball collide

    # draw scores


def keydown(key):
    global paddle1_vel, paddle2_vel


def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("spown", spawn_ball_clicked)
# start frame
new_game()
frame.start()