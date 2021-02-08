import pygame
from random import randint

# Initialize pygame
pygame.init()

# Set resolution
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Flappy Bird')
running = True

clock = pygame.time.Clock()

# Create variables
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)

TUBE_WIDTH = 50
TUBE_VELOCITY = 1
TUBE_GAP1 = randint(200,300)
TUBE_GAP2 = randint(200,300)
TUBE_GAP3 = randint(200,300)

tube1_x = 500
tube2_x = 700
tube3_x = 900

tube1_height = randint(50,400)
tube2_height = randint(50,400)
tube3_height = randint(50,400)

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
bird_drop_velocity = 0
GRAVITY = 0.03

score = 0
font = pygame.font.SysFont('sans', 20)

tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False
background_img = pygame.image.load('background.png')
bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH,BIRD_HEIGHT))

while running:
	clock.tick(120)

	screen.blit(background_img, (0,0))

	# Draw interface
	tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x,0,TUBE_WIDTH,tube1_height))
	tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x,0,TUBE_WIDTH,tube2_height))
	tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x,0,TUBE_WIDTH,tube3_height))

	tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x,tube1_height + TUBE_GAP1,TUBE_WIDTH,HEIGHT - tube1_height - TUBE_GAP1))
	tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x,tube2_height + TUBE_GAP2,TUBE_WIDTH,HEIGHT - tube2_height - TUBE_GAP2))
	tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x,tube3_height + TUBE_GAP3,TUBE_WIDTH,HEIGHT - tube3_height - TUBE_GAP3))

	tube1_x = tube1_x - TUBE_VELOCITY
	tube2_x = tube2_x - TUBE_VELOCITY
	tube3_x = tube3_x - TUBE_VELOCITY

	sand_rect = pygame.draw.rect(screen, YELLOW, (0,550,400,50))

	bird_rect = screen.blit(bird_img, (BIRD_X,bird_y,BIRD_WIDTH,BIRD_HEIGHT))

	bird_y += bird_drop_velocity
	bird_drop_velocity += GRAVITY

	if tube1_x < -TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(50,400)
		tube1_pass = False
	if tube2_x < -TUBE_WIDTH:
		tube2_x = 550
		tube2_height = randint(50,400)
		tube2_pass = False
	if tube3_x < -TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(50,400)
		tube3_pass = False

	score_txt = font.render('Score: ' + str(score), True, WHITE)
	screen.blit(score_txt, (5,5))

	if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
		score += 1
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
		score += 1
		tube2_pass = True
	if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
		score += 1
		tube3_pass = True

	for tube in [tube1_rect,tube2_rect,tube3_rect,tube1_rect_inv,tube2_rect_inv,tube3_rect_inv,sand_rect]:
		if bird_rect.colliderect(tube):
			pausing = True
			TUBE_VELOCITY = 0
			bird_drop_velocity = 0
			game_over_txt = font.render('Game over, score: ' + str(score), True, WHITE)
			screen.blit(game_over_txt, (150,300))	
			press_space_txt = font.render('Press Space to continue', True, WHITE)
			screen.blit(press_space_txt, (150,400))

	# Set buttons
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			
			# Space button
			if event.key == pygame.K_SPACE:
				if pausing:
					tube1_x = 500
					tube2_x = 700
					tube3_x = 900
					bird_y = 400
					TUBE_VELOCITY = 1
					score = 0
					pausing = False

				bird_drop_velocity = 0
				bird_drop_velocity -= 1.5
				
	pygame.display.flip()

pygame.quit()