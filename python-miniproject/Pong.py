"""
Mini-project # 4 - "Pong"
需求：乒乓  https://class.coursera.org/interactivepython-005/human_grading/view/courses/972530/assessments/31/results/mine
In this project, we will build a version of Pong, 
one of the first arcade video games (1972). 
While Pong is not particularly exciting compared to today's video games,
 Pong is relatively simple to build and provides a nice opportunity to work on the skills
 that you will need to build a game like Asteroids.
"""

# Implementation of classic arcade game Pong

import simplegui
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

ball_pos = [0,0]
ball_vel = [0,0]

paddle1_pos = [HALF_PAD_WIDTH,HEIGHT/2]
paddle2_pos = [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]

paddle1_vel = [0,0]
paddle2_vel = [0,0]

paddle_move = 10
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel,paddle_move # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2] 
    v_h = random.randrange(120, 240)/50  #x-speed
    v_v = random.randrange(60, 180)/50   #y-speed      
    if (direction == LEFT):    
        v_h = -v_h
    ball_vel[0] = v_h
    ball_vel[1] =-v_v
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    #上下墙碰撞检测
    if((ball_pos[1]+BALL_RADIUS>HEIGHT-1)or(ball_pos[1]<BALL_RADIUS)):
        ball_vel[1] =- ball_vel[1]
    #球板碰撞检测    
    if (ball_pos[0]<BALL_RADIUS+PAD_WIDTH):
       if(ball_pos[1]> paddle1_pos[1]-HALF_PAD_HEIGHT-BALL_RADIUS) and (ball_pos[1]< paddle1_pos[1]+HALF_PAD_HEIGHT+BALL_RADIUS) : 
            ball_vel[0] =- ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
       else:
            score2+=1
            spawn_ball(RIGHT)
    elif(ball_pos[0]+BALL_RADIUS>WIDTH-PAD_WIDTH-1):
        if(ball_pos[1]> paddle2_pos[1]-HALF_PAD_HEIGHT-BALL_RADIUS) and (ball_pos[1]< paddle2_pos[1]+HALF_PAD_HEIGHT+BALL_RADIUS) :
            ball_vel[0] =- ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1           
        else:
            score1+=1
            spawn_ball(LEFT)
            
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]    
     
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,'White','White')
    # update paddle's vertical position, keep paddle on the screen
       
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
        
    if(paddle1_pos[1]<=HALF_PAD_HEIGHT):
        paddle1_pos[1] = HALF_PAD_HEIGHT
    if(paddle2_pos[1]<=HALF_PAD_HEIGHT):
        paddle2_pos[1] = HALF_PAD_HEIGHT
    if(paddle1_pos[1] + HALF_PAD_HEIGHT >= HEIGHT-1):
        paddle1_pos[1] = HEIGHT-HALF_PAD_HEIGHT
    if(paddle2_pos[1] + HALF_PAD_HEIGHT >= HEIGHT-1):
        paddle2_pos[1] = HEIGHT-HALF_PAD_HEIGHT
        
        
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1]-HALF_PAD_HEIGHT],[paddle1_pos[0], paddle1_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH, "White")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1]-HALF_PAD_HEIGHT],[paddle2_pos[0], paddle2_pos[1]+HALF_PAD_HEIGHT],PAD_WIDTH, "White")    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/4, HEIGHT/4), 32, 'White')
    canvas.draw_text(str(score2), (3*WIDTH/4, HEIGHT/4), 32, 'White')    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key==simplegui.KEY_MAP['w']):
        paddle1_vel[1] -= paddle_move  
    elif(key==simplegui.KEY_MAP['s']):
        paddle1_vel[1] += paddle_move 
    elif(key==simplegui.KEY_MAP['up']):
        paddle2_vel[1] -= paddle_move 
    elif(key==simplegui.KEY_MAP['down']):
        paddle2_vel[1] += paddle_move 
              
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key==simplegui.KEY_MAP['w']):
        paddle1_vel[1] = 0 
    elif(key==simplegui.KEY_MAP['s']):
        paddle1_vel[1] = 0
    elif(key==simplegui.KEY_MAP['up']):
        paddle2_vel[1] = 0 
    elif(key==simplegui.KEY_MAP['down']):
        paddle2_vel[1] = 0
        
#def button_handler():
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Restart', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
