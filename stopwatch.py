# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables
time = 0
interval = 100
timer_increment = 1 #increment of 0.1 second
position = [110, 150]
position_counter = [250, 25]
started = False
counter_successful = 0
counter_attempt  = 0
game_score = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t//600
    seconds = (t - minutes*600)//10
    tenths  = (t - minutes*600 - seconds*10)%10
    if seconds < 10:
        output = str(minutes) + ":0" + str(seconds) + "." + str(tenths)
    else:
        output = str(minutes) + ":" + str(seconds) + "." + str(tenths)
    return output
    pass 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global started
    started = True
    timer.start()
        
def stop():
    global started, counter_attempt, counter_successful, time, game_score
    started = True
    if time%10 == 0 and started == True:
        counter_attempt += 1
        counter_successful += 1
        started == False
        timer.stop()
    elif started == True:
        counter_attempt += 1
        started == False
        timer.stop()
    game_score = str(counter_successful)+"/"+ str(counter_attempt)
    return game_score
    
def reset():
    global started, time, game_score, counter_attempt, counter_successful
    time = 0
    started = False
    counter_attempt = 0
    counter_successful = 0
    game_score = "0/0"
    timer.start()

    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time, timer_increment
    time += timer_increment
    format(time)


# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), position, 40, "White")
    canvas.draw_text(game_score, position_counter, 20, "Lime")
# create frame
f = simplegui.create_frame("Stopwatch: The Game",300,300)
timer = simplegui.create_timer(interval, timer_handler)
f.set_draw_handler(draw)
# register event handlers


# start frame
f.start()
f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)
# Please remember to review the grading rubric
