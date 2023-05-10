import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the snake
SNAKE_SIZE = 10
snake = [pygame.Rect(250, 250, SNAKE_SIZE, SNAKE_SIZE)]

# Set up the food
FOOD_SIZE = 10
food = pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE), random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the initial direction
direction = 'up'

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
    
    # Update game state
    # Move snake
    head = snake[0]
    if direction == 'up':
        new_head = pygame.Rect(head.left, head.top - SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
    elif direction == 'down':
        new_head = pygame.Rect(head.left, head.top + SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
    elif direction == 'left':
        new_head = pygame.Rect(head.left - SNAKE_SIZE, head.top, SNAKE_SIZE, SNAKE_SIZE)
    elif direction == 'right':
        new_head = pygame.Rect(head.left + SNAKE_SIZE, head.top, SNAKE_SIZE, SNAKE_SIZE)
    snake.insert(0, new_head)
    
    # Check if the snake has collided with the food
    if snake[0].colliderect(food):
        food = pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE), random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE)
    else:
        snake.pop()
    
    # Check if the snake has collided with the walls or itself
    if snake[0].left < 0 or snake[0].right > WINDOW_WIDTH or snake[0].top < 0 or snake[0].bottom > WINDOW_HEIGHT:
        pygame.quit()
        sys.exit()
    for rect in snake[1:]:
        if snake[0].colliderect(rect):
            pygame.quit()
            sys.exit()
    
    # Draw game
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 255, 0), food)
    for rect in snake:
        pygame.draw.rect(window, (0, 0, 255), rect)
    pygame.display.update()
    
    # Set the game clock
    clock.tick(10)
