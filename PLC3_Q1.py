from itertools import chain
import pygame
pygame.init()
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRAY = (142, 142, 142)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
def reset_game():
global running, player, active_squares, row_sum, column_sum, diagonal_sum, locke
running = True
player = 1
active_squares = []
row_sum = [0, 0, 0]
column_sum = [0, 0, 0]
diagonal_sum = [0, 0]
locked = False
reset_game()
while running:
board = [[None for i in range(3)] for j in range(3)]
21-805-0106: Python Programming Lab
screen.fill((255, 255, 255))
x = 20
y = 20
for i in range(3):
for j in range(3):
board[i][j] = pygame.draw.rect(screen, GRAY, (x, y, 80, 80))
x += 90
x = 20
y += 90
reset = pygame.draw.rect(
screen, GRAY, ((SCREEN_WIDTH / 2) - 50, 2 * SCREEN_HEIGHT / 3, 100, 50)
)
font = pygame.font.Font(None, 35)
text = font.render("RESET", True, BLACK)
text_rect = text.get_rect(center=reset.center)
screen.blit(text, text_rect)
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False
if event.type == pygame.MOUSEBUTTONDOWN:
pos = pygame.mouse.get_pos()
if reset.collidepoint(pos):
reset_game()
if not locked:
for i in range(3):
for j in range(3):
if board[i][j].collidepoint(pos):
if player == 1:
img = pygame.image.load("assets/X.png")
elif player == -1:
img = pygame.image.load("assets/O.png")
img.convert()
img = pygame.transform.scale(img, (80, 80))
rect = img.get_rect()
rect.center = board[i][j].center
active_squares.append((img, rect))
row_sum[i] += player
column_sum[j] += player
if i == j:
diagonal_sum[0] += player
if i + j == 2:
diagonal_sum[1] += player
player *= -1
for square in active_squares:
screen.blit(*square)
for sum_ in chain(row_sum, column_sum, diagonal_sum):
if abs(sum_) == 3:
locked = True
font = pygame.font.Font(None, 50)
if sum_ == 3:
text = font.render("X wins!", True, BLACK)
elif sum_ == -3:
text = font.render("O wins!", True, BLACK)
text_rect = text.get_rect(
center=(SCREEN_WIDTH / 2, (2 * SCREEN_HEIGHT / 3) - 50)
)
screen.blit(text, text_rect)
pygame.display.flip()
