# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random


#-----game configuration----
turtleshape= "turtle"
trtlcolor= "crimson"
trtlsize= random.choice([0.5, 2, 4, 6, 8, 10])
score = 0


font_setup = ("papyrus", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

counter = trtl.Turtle()
counter.ht()
counter.penup
counter.goto(200, 275)

#-----initialize turtle-----
cocojumbo = trtl.Turtle(shape=turtleshape)
cocojumbo.color(trtlcolor)
cocojumbo.shapesize(trtlsize)
cocojumbo.speed(100)

scortle = trtl.Turtle()
scortle.penup()
scortle.goto(-300, 50)
scortle.ht()
font_setup= ("papyrus", 30, "bold")
scortle.write(score, font=font_setup)

#-----game functions--------
def cocojumbo_clicked(x,y):
    print("cocojumbo was clicked")
    change_position()
    update_score()
    trtlsize = random.choice([0.5, 2, 4, 6, 8, 10])

def change_position():
    cocojumbo.penup()
    cocojumbo.ht()
    if not timer_up:
        cocojumbox = random.randint(-400, 400)
        cocojumboy = random.randint(-300, 300)
        cocojumbo.goto(cocojumbox, cocojumboy)
        cocojumbo.st()

def update_score():
    global score
    score += 1
    print(score)
    scortle.clear()
    scortle.write(score, font=font_setup)
    

def cocojumbo_clicked(x,y):
    print("you got a point")
    change_position()
    update_score()
   

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font = font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)



#-----events----------------
wn = trtl.Screen()
cocojumbo.onclick(cocojumbo_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()