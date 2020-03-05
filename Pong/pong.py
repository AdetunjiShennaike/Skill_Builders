# import turtle which is built into Python 3, turtle is used for the graphics
import turtle
import winsound
import os

# Load the game/window with the screen method
window = turtle.Screen()
# The title of the window
window.title('Pong')
# The setup of the window
window.bgcolor('lightgreen')
window.setup(width=700, height=500)
window.tracer(0) #sets the delay for drawings in the window

# Dynamic Score
scoreA = 0
scoreB = 0

# Paddle A
# Set a game object with a name
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed that the paddle is drawn
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #alter the shape
paddle_a.color('black')
paddle_a.penup() #prevents the drawing when the object moves
paddle_a.goto(-300, 0)

# Paddle B
# Set a game object with a name
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed that the paddle is drawn
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #alter the shape
paddle_b.color('black')
paddle_b.penup() #prevents the drawing when the object moves
paddle_b.goto(300, 0)


# Ball
# Set a game object with a name
ball = turtle.Turtle()
ball.speed(0) #speed that the paddle is drawn
ball.shape('circle')
ball.color('black')
ball.penup() #prevents the drawing when the object moves
ball.goto(0, 0)
ball.dx = .1 #moves the ball x pixels right
ball.dy = .1 #moves the ball x pixels up

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,210)
pen.write(f'Player A: {scoreA} Player B: {scoreB}', align='center', font=('Courier', 24, 'normal'))

# Functions
def paddle_a_up():
  # Grab the y coordinate to move it 
  y = paddle_a.ycor()
  # Prevent it from going off screen
  if(y < 200):
    y += 40
    # Set the new y
    paddle_a.sety(y)

def paddle_a_down():
  # Grab the y coordinate to move it 
  y = paddle_a.ycor() 
  # Prevent it from going off screen
  if(y > -200):
    y -= 40
    # Set the new y
    paddle_a.sety(y)

def paddle_b_up():
  # Grab the y coordinate to move it 
  y = paddle_b.ycor()
  # Prevent it from going off screen
  if(y < 200):
    y += 40
    # Set the new y
    paddle_b.sety(y)

def paddle_b_down():
  # Grab the y coordinate to move it 
  y = paddle_b.ycor()
  # Prevent it from going off screen
  if(y > -200):
    y -= 40
    # Set the new y
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Class refactor for paddle and functions

# class Paddle:
#   def __init__(self, name):
#     self.name = name


# Game loop
while True:
  # Re-render the game
  window.update()

  # Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # Border check, to prevent paddles and ball from leaving the screen
  if ball.ycor() > 235:
    # Reset the ball and reverse the y direction (dy) 
    ball.sety(235)
    ball.dy *= -1
    # os.system('aplay bounce.mp3&') #linux
    # os.system('afplay bounce.mp3&') #mac
    winsound.PlaySound('bounce.mp3', winsound.SND_ASYNC) #windows
  
  if ball.ycor() < -235:
    # Reset the ball and reverse the y direction (dy) 
    ball.sety(-235)
    ball.dy *= -1
    # os.system('aplay bounce.mp3&') #linux
    # os.system('afplay bounce.mp3&') #mac
    winsound.PlaySound('bounce.mp3', winsound.SND_ASYNC) #windows

  if ball.xcor() > 340:
    # Reset the ball and reset the ball
    ball.goto(0, 0)
    ball.dx *= -1
    scoreA += 1
    pen.clear()
    pen.write(f'Player A: {scoreA} Player B: {scoreB}', align='center', font=('Courier', 24, 'normal'))

  if ball.xcor() < -340:
    # Reset the ball and reset the ball
    ball.goto(0, 0)
    ball.dx *= -1
    scoreB += 1
    pen.clear()
    pen.write(f'Player A: {scoreA} Player B: {scoreB}', align='center', font=('Courier', 24, 'normal'))

  # Paddle and Ball collision
  if (ball.xcor() > 300 and ball.xcor() < 315) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
    ball.setx(300)
    ball.dx *= -1
    # os.system('aplay bounce.mp3&') #linux
    # os.system('afplay bounce.mp3&') #mac
    winsound.PlaySound('bounce.mp3', winsound.SND_ASYNC) #windows
 
  if (ball.xcor() < -300 and ball.xcor() > -315) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
    ball.setx(-300)
    ball.dx *= -1
    # os.system('aplay bounce.mp3&') #linux
    # os.system('afplay bounce.mp3&') #mac
    winsound.PlaySound('bounce.mp3', winsound.SND_ASYNC) #windows