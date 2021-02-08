import pygame
from random import randint
from time import sleep

# Initialize pygame
pygame.init()

# Set resolution
screen = pygame.display.set_mode((601,601))

pygame.display.set_caption('Snake')
running = True

# Create color variables
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
clock = pygame.time.Clock()

# Snake coordinate
snakes = [[randint(2,17),randint(2,17)]]

# Apple coordinate
apple = [randint(1,18),randint(1,18)]

font_small = pygame.font.SysFont('sans', 20)
font_big = pygame.font.SysFont('sans', 50)
score = 0

pausing = False

direction = randint(0,3)
if direction == 0:
	direction = 'up'
if direction == 1:
	direction = 'down'
if direction == 2:
	direction = 'left'
if direction == 3:
	direction = 'right'

while running:		
	clock.tick(60)
	screen.fill(BLACK)

	tail_x = snakes[0][0]
	tail_y = snakes[0][1]

	# Draw snake
	for snake in snakes:
		pygame.draw.rect(screen, GREEN, (snake[0] * 30,snake[1] * 30,30,30))

	# Draw apple
	pygame.draw.rect(screen, WHITE, (apple[0] * 30,apple[1] * 30,30,30))

	# Point
	if snakes[-1][0] == apple[0] and snakes [-1][1] == apple[1]:
		snakes.insert(0,[tail_x, tail_y])
		score += 1
		while True:
			temp_apple = [randint(0,19),randint(0,19)]
			if temp_apple not in snakes and temp_apple not in [[0,0],[0,19],[19,0],[19,19]]:
				apple = temp_apple
				break		

	# Crash 1
	if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
		pausing = True

	# Snake move
	if pausing == False:
		if direction == 'right':
			snakes.append([snakes[-1][0] + 1,snakes[-1][1]])
			snakes.pop(0)
		if direction == 'left':
			snakes.append([snakes[-1][0] - 1,snakes[-1][1]])
			snakes.pop(0)
		if direction == 'up':
			snakes.append([snakes[-1][0],snakes[-1][1] - 1])
			snakes.pop(0)
		if direction == 'down':
			snakes.append([snakes[-1][0],snakes[-1][1] + 1])
			snakes.pop(0)

	# Crash 2
	for i in range(len(snakes) - 1):
		if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
			pausing = True

	# End game		
	if pausing:
		game_over_txt = font_big.render('LOSER, SCORE: ' + str(score), True, WHITE)
		play_again_txt = font_small.render('Press Space to continue', True, WHITE)
		screen.blit(game_over_txt, (125,250))
		screen.blit(play_again_txt, (125,300))

	sleep(0.06)

	# Set buttons
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:

			# Up arrow button
			if event.key == pygame.K_UP and direction != 'down':
				direction = 'up'

			# Down arrow button
			if event.key == pygame.K_DOWN and direction != 'up':
				direction = 'down'

			# Left arrow button
			if event.key == pygame.K_LEFT and direction != 'right':
				direction = 'left'

			# Right arrow button
			if event.key == pygame.K_RIGHT and direction != 'left':
				direction = 'right'

			# Space button
			if event.key == pygame.K_SPACE and pausing == True:
				pausing = False
				snakes = [[randint(2,17),randint(2,17)]]
				apple = [randint(1,18),randint(1,18)]
				score = 0
				
	pygame.display.flip()

pygame.quit()