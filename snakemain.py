# import tkinter as tk
# import random

# # Game constants
# GAME_WIDTH = 600
# GAME_HEIGHT = 600
# SPEED = 100  # milliseconds
# SPACE_SIZE = 20
# INITIAL_BODY_PARTS = 3
# SNAKE_COLOR = "#00FF00"
# FOOD_COLOR = "#FF0000"
# BACKGROUND_COLOR = "#000000"

# class Snake:
#     def __init__(self):
#         self.body_parts = INITIAL_BODY_PARTS
#         self.coordinates = [[0, 0] for _ in range(INITIAL_BODY_PARTS)]
#         self.squares = []
#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(
#                 x, y, x + SPACE_SIZE, y + SPACE_SIZE,
#                 fill=SNAKE_COLOR, tag="snake"
#             )
#             self.squares.append(square)

# class Food:
#     def __init__(self):
#         x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
#         self.coordinates = [x, y]
#         canvas.create_oval(
#             x, y, x + SPACE_SIZE, y + SPACE_SIZE,
#             fill=FOOD_COLOR, tag="food"
#         )

# def next_turn(snake, food):
#     global direction, score

#     x, y = snake.coordinates[0]
#     if direction == "up":
#         y -= SPACE_SIZE
#     elif direction == "down":
#         y += SPACE_SIZE
#     elif direction == "left":
#         x -= SPACE_SIZE
#     elif direction == "right":
#         x += SPACE_SIZE

#     snake.coordinates.insert(0, [x, y])
#     square = canvas.create_rectangle(
#         x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
#     )
#     snake.squares.insert(0, square)

#     if x == food.coordinates[0] and y == food.coordinates[1]:
#         score += 1
#         label.config(text=f"Score: {score}")
#         canvas.delete("food")
#         food = Food()
#     else:
#         del snake.coordinates[-1]
#         canvas.delete(snake.squares[-1])
#         del snake.squares[-1]

#     if check_collisions(snake):
#         game_over()
#     else:
#         window.after(SPEED, next_turn, snake, food)

# def change_direction(new_dir):
#     global direction
#     opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
#     if new_dir != opposites.get(direction):
#         direction = new_dir

# def check_collisions(snake):
#     x, y = snake.coordinates[0]
#     # Collision with walls:
#     if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
#         return True
#     # Collision with itself:
#     if [x, y] in snake.coordinates[1:]:
#         return True
#     return False

# def game_over():
#     canvas.delete(tk.ALL)
#     canvas.create_text(
#         GAME_WIDTH / 2, GAME_HEIGHT / 2,
#         text=f"Game Over! Final Score: {score}",
#         fill="white", font=('Arial', 24)
#     )

# def start_game():
#     global window, canvas, label, score, direction
#     window = tk.Tk()
#     window.title("Snake Game (Bro Code Style)")

#     score = 0
#     direction = "right"

#     label = tk.Label(window, text=f"Score: {score}", font=('Arial', 14))
#     label.pack()

#     canvas = tk.Canvas(
#         window, bg=BACKGROUND_COLOR,
#         height=GAME_HEIGHT, width=GAME_WIDTH
#     )
#     canvas.pack()

#     window.bind("<Up>", lambda e: change_direction("up"))
#     window.bind("<Down>", lambda e: change_direction("down"))
#     window.bind("<Left>", lambda e: change_direction("left"))
#     window.bind("<Right>", lambda e: change_direction("right"))

#     snake = Snake()
#     food = Food()

#     next_turn(snake, food)
#     window.mainloop()

# if __name__ == "__main__":
#     start_game()













































































import pygame
import random
import time

# Initialize game
pygame.init()
window_x, window_y = 720, 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')
fps_controller = pygame.time.Clock()

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red   = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
fruit_pos = [random.randrange(1, (window_x // 10)) * 10,
             random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_surface = my_font.render('Your Score is: ' + str(score), True, red)
    game_rect = game_surface.get_rect(center=(window_x / 2, window_y / 4))
    game_window.blit(game_surface, game_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == fruit_pos:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (window_x // 10)) * 10,
                     random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Game over conditions
    if (snake_pos[0] < 0 or snake_pos[0] >= window_x
        or snake_pos[1] < 0 or snake_pos[1] >= window_y):
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    show_score(white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(15)
