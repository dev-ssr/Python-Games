### http://www.codeskulptor.org/#user48_meDRTRCIG9_27.py
import simplegui
import random
# define global variables
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2LEFT = False
RIGHT = Trueball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [5.0,1.0]
paddle1_vel = 0.0
paddle2_vel = 0.0
al = 8
bl = 240
cl = 0
dl = 160
ar = 592
br = 240
cr = 600
dr = 160
score1 = 0
score2 = 0
paddle1_pos = (bl+dl)/2
paddle2_pos = (br+dr)/2
LEFT = True
RIGHT = False
def spawn_ball(direction):    
global ball_pos, ball_vel 
# these are vectors stored as lists    
ball_pos = [WIDTH/2, HEIGHT/2]    
if(direction == "right"):        
ball_vel = [random.randrange(120,240)/60,-random.randrange(60,180)/60]    
if(direction == "left"):        
ball_vel = [-random.randrange(120,240)/60,-random.randrange(60,180)/60]

def new_game():    
global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
# these are numbers    
global score1, score2  
# these are ints    
spawn_ball("right")    
score1 = score2 = 0

def keydown(key):    
global paddle1_vel, paddle2_vel    
if key == simplegui.KEY_MAP["up"] :        
paddle2_vel -= 1    
elif key == simplegui.KEY_MAP["down"]:        
paddle2_vel += 1    
elif key == simplegui.KEY_MAP["w"]:        
paddle1_vel -= 1    
elif key == simplegui.KEY_MAP["s"]:        
paddle1_vel += 1
def keyup(key):    
if key == simplegui.KEY_MAP["up"] :        
paddle2_vel = 0    
elif key == simplegui.KEY_MAP["down"]:        
paddle2_vel = 0    
elif key == simplegui.KEY_MAP["w"]:        
paddle1_vel = 0    
elif key == simplegui.KEY_MAP["s"]:        
paddle1_vel = 0

def draw(canvas):
    global bl , dl, br, dr, ball_vel,score1,score2,paddle1_vel, paddle2_vel
    # drawing the center line
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
 #drawing the gutters
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    bl = bl+ paddle1_vel
    dl = dl + paddle1_vel
    br = br + paddle2_vel
    dr = dr + paddle2_vel
    paddle1_pos = (bl+dl)/2 + paddle1_vel
    paddle2_pos = (br+dr)/2 + paddle2_vel
    if paddle1_pos >= HEIGHT-HALF_PAD_HEIGHT or paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_vel = 0
    if paddle2_pos >= HEIGHT-HALF_PAD_HEIGHT or paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_vel = 0
        #drawing the pads
    canvas.draw_line((0,dl),(0,bl),PAD_WIDTH,'white')
    canvas.draw_line((600,dr),(600,br),PAD_WIDTH,'white')

    #display score
    canvas.draw_text(str(score1),((WIDTH/2)/2, 30),30,"white")
    canvas.draw_text(str(score2),((WIDTH/2) + (WIDTH/2)/2, 30),30,"white")
# update ball
    #ball hitting the gutters
    if ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        if ball_pos[1] <=bl and ball_pos[1]>=dl :
            ball_vel[0] = -ball_vel[0]
        else:
            score2 += 1
            spawn_ball("right")
            elif ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS:
            if ball_pos[1] <=br and ball_pos[1]>=dr :
            ball_vel[0] = -ball_vel[0]        
            else:            
            score1 += 1            
            spawn_ball("left")
            elif(ball_pos[1] >= HEIGHT-BALL_RADIUS) or (ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS,1,"white","white")
    frame = simplegui.create_frame("pong",WIDTH,HEIGHT)
frame.add_button("reset",new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
new_game()
