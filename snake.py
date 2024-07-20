import turtle
import time
import random

# Set up the game window
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)

# Initialize the snake
snake = []
snake_length = 1
snake_direction = "right"

# Function to change the snake's direction
def change_direction(new_direction):
    global snake_direction
    if new_direction == "up" and snake_direction != "down":
        snake_direction = "up"
    elif new_direction == "down" and snake_direction != "up":
        snake_direction = "down"
    elif new_direction == "left" and snake_direction != "right":
        snake_direction = "left"
    elif new_direction == "right" and snake_direction != "left":
        snake_direction = "right"

# Create the snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(0, 0)
snake.append(snake_head)

# Function to move the snake
def move_snake():
    global snake_length, snake_direction
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)
    if snake_direction == "right":
        snake_head.goto(snake_head.xcor() + 20, snake_head.ycor())
    elif snake_direction == "left":
        snake_head.goto(snake_head.xcor() - 20, snake_head.ycor())
    elif snake_direction == "up":
        snake_head.goto(snake_head.xcor(), snake_head.ycor() + 20)
    elif snake_direction == "down":
        snake_head.goto(snake_head.xcor(), snake_head.ycor() - 20)

# Main game loop
while True:
    window.update()
    time.sleep(0.1)
    move_snake()

    # Handle user input for changing direction
    new_direction = window.onkeypress(fun=change_direction)

    # Check for collisions with borders
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        break

    # Check for snake colliding with itself
    for segment in snake[1:]:
        if segment.distance(snake_head) < 20:
            break
    else:
        snake_length += 1
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        new_segment.goto(snake[-1].xcor(), snake[-1].ycor())
        snake.append(new_segment)

window.exitonclick()