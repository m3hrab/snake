from turtle import *
from random import randrange
from freegames import square, vector

# Initialize the position of the food and the snake, and the snake's movement direction.
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Set the delay time for the snake's movement (in milliseconds).
delay_time = 100  # Adjust this value to change the snake's speed.

def change(x, y):
    "Change snake direction."
    # Update the snake's movement direction based on the arrow keys pressed.
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    # Check if the head of the snake is within the game boundaries.
    return -200 <= head.x <= 190 and -200 <= head.y <= 190

# Create a new function to move the food to a new random position.
def move_food():
    "Move food to a new random position when the snake eats it."
    # Check if the food is inside the snake (eaten).
    if food in snake:
        # Generate a new random position for the food.
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

        # Ensure that the new food position is not inside the snake's body.
        while food in snake:
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10

def move():
    "Move snake forward one segment."
    # Copy the head of the snake to create a new segment.
    head = snake[-1].copy()
    head.move(aim)

    # Check if the snake goes beyond the boundaries or collides with itself.
    if not inside(head):
        # Wrap around the edges by setting the new position.
        if head.x < -200:
            head.x = 190
        elif head.x > 190:
            head.x = -200
        elif head.y < -200:
            head.y = 190
        elif head.y > 190:
            head.y = -200

    # Check if the snake collides with itself.
    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # Append the new head to the snake.
    snake.append(head)

    # Check if the snake eats the food.
    if head == food:
        print('Snake:', len(snake))
        move_food()  # Move the food to a new random position.
    else:
        # If the snake doesn't eat the food, remove the tail segment.
        snake.pop(0)

    # Clear the screen and redraw the snake and food.
    clear()
    for body in snake:
        square(body.x, body.y, 9, 'black')
    square(food.x, food.y, 9, 'green')
    update()

    # Schedule the move() function to run again after a specific delay time.
    ontimer(move, delay_time)

# Set up the game window.
setup(420, 420, 370, 0)

# Hide the turtle cursor and turn off animation updates.
hideturtle()
tracer(False)

# Enable key events.
listen()

# Bind the arrow keys to the change() function.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Call the move_food() function after initializing the food vector.
move_food()

# Call the move() function to start the game.
move()

# Start the game loop.
done()
