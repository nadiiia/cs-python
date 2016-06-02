# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
MAX_VEL = 100
position1 = [130, 55]
position2= [430,55]
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [WIDTH/2, HEIGHT/2]
paddle1_vel = 0 
paddle2_vel = 0 
right = 1
paddle1_pos =  ((HEIGHT / 2 - HALF_PAD_HEIGHT) + PAD_HEIGHT)
paddle2_pos =  ((HEIGHT / 2 - HALF_PAD_HEIGHT) + PAD_HEIGHT)

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]   
    if right == 1:
        ball_vel[0] = random.randrange(120, 240)/60
        ball_vel[1] = random.randrange(60, 180)/60
    else:
        ball_vel[0] = - random.randrange(120, 240)/60
        ball_vel[1] = - random.randrange(60, 180)/60

# define event handlers
def reset():
    new_game()
    
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, right  # these are floats
    global score1, score2  # these are ints
    score1 = 0 
    score2 = 0
    right = random.randint(0,1)
    ball_init(right)
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos,paddle1_vel,paddle2_vel,ball_pos, ball_vel, paddle1_pos, paddle2_pos
    
    # draw mid line and gutter
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos],[PAD_WIDTH, (paddle1_pos) + PAD_HEIGHT ],[0, (paddle1_pos) + PAD_HEIGHT]],1, "white", "White") 
    c.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]],1, "white", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel   
        
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "#White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH or ball_pos[0] <= BALL_RADIUS + PAD_WIDTH :
        if paddle1_pos < ball_pos[1] < paddle1_pos + PAD_HEIGHT and ball_vel[0] < 0 : #ball bounce off Paddle1 (PAD1)
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        elif paddle2_pos < ball_pos[1] < paddle2_pos + PAD_HEIGHT and ball_vel[0] > 0 : #ball bounce off Paddle2 (PAD2)
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else :
            if ball_vel[0] > 0 : #if ball falls in right gutter: score 1 point for side 1
                score1 += 1
            else :
                score2 += 1			#if ball falls in left gutter: score 1 point for side 2
            ball_init(ball_vel[0] < 0)
    if ball_pos[1] >= HEIGHT - BALL_RADIUS :   # ball bounce off bottom of screen
        ball_vel[1] *= -1
    elif ball_pos[1] <= BALL_RADIUS : #ball bounce off top of screen
        ball_vel[1] *= -1 


    # draw ball and scores
    c.draw_text(str(score1), position1, 40, "White")
    c.draw_text(str(score2), position2, 40, "White")
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 3 
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel  -=  vel 
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel   +=  vel 
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel  +=  vel 
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel  -=  vel 
      
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"] or key == simplegui.KEY_MAP["w"] :
       paddle1_vel   =  0
 
    if key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
       paddle2_vel = 0


new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 200)
# start frame
frame.start()
