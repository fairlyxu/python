"""
Mini-project # 5 - Memory
需求：考察记忆力 https://class.coursera.org/interactivepython-005/human_grading/view/courses/972530/assessments/32/results/mine

"""
# implementation of card game - Memory

import simplegui
import random

list1=[]
exposed = {}
state = count = 0;
pre_index1 = pre_index2 = -1
# helper function to initialize globals
def new_game():
    global list1,state,count
    list1 = range(8)+range(8)
    random.shuffle(list1)
    label.set_text('Turns = 0')
    for i in range(16):
        exposed[i] = False;
     
# define event handlers
def mouseclick(pos):    
    # add game state logic here
    i = pos[0]/50 ;    
    global state,pre_index1,pre_index2,count    
    if state == 0:        
        if(not exposed[i]):
           state = 1
           exposed[i] = True;
           pre_index1 = i
    elif state == 1:       
        if(not exposed[i]):
           state = 2
           exposed[i]= True;
           pre_index2 = i
           count +=1
    else:        
        if(not exposed[i]):            
            if(list1[pre_index1]!= list1[pre_index2]):
                exposed[pre_index1]= exposed[pre_index2] = False;
            pre_index1=i;
            state = 1;
            exposed[i]=True               
    label.set_text('Turns = '+str(count))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    for i in range(16):           
        if(exposed[i]):
            canvas.draw_text(str('  ')+str(list1[i]), (50*i, 50), 22, 'Red');
        else:
            canvas.draw_line((50*(i)+25, 0), (50*(i)+25, 100), 50, 'Green')
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
# Always remember to review the grading rubric