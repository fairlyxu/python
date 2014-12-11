"""
需求： 暂停整点秒  https://class.coursera.org/interactivepython-005/human_grading/view/courses/972530/assessments/30/results/mine
Our mini-project for this week will focus on combining text drawing in the canvas with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second. 
The stopwatch should contain "Start", "Stop" and "Reset" buttons.
"""

# template for "Stopwatch: The Game"
import simplegui
# define global variables
times = 0 
total = 0
success = 0
form_time ='' 
flag = False 
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(times):
    D = times % 10
    A = times / 600
    B = (times %600/10)/10
    C = (times %600/10)%10 
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global flag
    flag = True
    timer.start()
 
    
def button_stop():        
    global total,success,flag
    if flag and not times % 10:
        success += 1
        total   += 1        
    elif flag:
        total   += 1
    timer.stop()
    flag = False
    
def button_reset():
    timer.stop()
    global times,total,success,flag
    flag = False
    times = 0
    total = 0
    success = 0
  

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global times,flag
    if(flag):
       times+=1

# define draw handler
def draw_handler(canvas): 
    global form_time 
    form_time = format(times)   
    canvas.draw_text(str(form_time),(100, 100), 30, 'Red')
    canvas.draw_text(str(success)+"/"+str(total),(200, 30), 20, 'green')
     
    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",250,200)
Start = frame.add_button('Start', button_start,150)
Stop = frame.add_button('Stop', button_stop, 150)
Reset = frame.add_button('Reset', button_reset, 150)

frame.start()

# register event handlers

frame.set_draw_handler(draw_handler)
# start frame

timer = simplegui.create_timer(100, timer_handler)
timer.start()

# Please remember to review the grading rubric
