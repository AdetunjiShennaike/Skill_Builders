# import turtle which is built into Python 3, turtle is used for the graphics
import turtle

# Load the game/window with the screen method
window = turtle.Screen()
# The title of the window
window.title('Pong')
# The setup of the window
window.bgcolor('lightgreen')
window.setup(width=1000, height=800)
window.tracer(0) #sets the delay for drawings in the window

# Paddle A
# Set a game object with a name
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed that the paddle is drawn
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #alter the shape
paddle_a.color('black')
paddle_a.penup() #prevents the drawing when the object moves
paddle_a.goto(-450, 0)

# Paddle B
# Set a game object with a name
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed that the paddle is drawn
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #alter the shape
paddle_b.color('black')
paddle_b.penup() #prevents the drawing when the object moves
paddle_b.goto(450, 0)


# Ball
# Set a game object with a name
ball = turtle.Turtle()
ball.speed(0) #speed that the paddle is drawn
ball.shape('circle')
ball.color('black')
ball.penup() #prevents the drawing when the object moves
ball.goto(0, 0)


# Functions
def paddle_a_up():
  # Grab the y coordinate to move it 
  y = paddle_a.ycor()
  y += 20
  # Set the new y
  paddle_a.sety(y)

def paddle_a_down():
  # Grab the y coordinate to move it 
  y = paddle_a.ycor()
  y -= 20
  # Set the new y
  paddle_a.sety(y)

def paddle_b_up():
  # Grab the y coordinate to move it 
  y = paddle_b.ycor()
  y += 20
  # Set the new y
  paddle_b.sety(y)

def paddle_a_down():
  # Grab the y coordinate to move it 
  y = paddle_b.ycor()
  y -= 20
  # Set the new y
  paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_down, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Class refactor for paddle and functions

# class Paddle:
#   def __init__(self, name):
#     self.name = name


# Game loop
while True:
  # Re-render the game
  window.update()