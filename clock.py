import pygame
import time
import math

# Initialize pygame
pygame.init()

# Set resolution
screen = pygame.display.set_mode((500,600))

# Assign color variables
GREY = (120,120,120)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

# Make some texts
font = pygame.font.SysFont('sans', 50)
text_1 = font.render('+m', True, BLACK)
text_2 = font.render('-m', True, BLACK)
text_3 = font.render('+s', True, BLACK)
text_4 = font.render('-s', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)
text_7 = font.render('Stop', True, BLACK)
text_8 = font.render('Conti', True, BLACK)

running = True
total_secs = 0 
total = 0
start = False
clock = pygame.time.Clock()

pausing = False

while running:
	clock.tick(120) # FPS

	screen.fill(GREY)

	# Set up mouse
	mouse_x, mouse_y = pygame.mouse.get_pos()

	# Draw interface
	pygame.draw.rect(screen, WHITE, (50,50,50,50))
	screen.blit(text_1, (50,50))
	pygame.draw.rect(screen,WHITE, (50,200,50,50))
	screen.blit(text_2, (50,200))
	pygame.draw.rect(screen,WHITE, (150,50,50,50))
	screen.blit(text_3, (150,50))
	pygame.draw.rect(screen,WHITE, (150,200,50,50))
	screen.blit(text_4, (150,200))
	pygame.draw.rect(screen,WHITE, (300,50,150,50))
	screen.blit(text_5, (300,50))
	pygame.draw.rect(screen,WHITE, (300,150,150,50))
	screen.blit(text_6, (300,150))
	pygame.draw.rect(screen,WHITE, (300,250,150,50))
	screen.blit(text_7, (300,250))
	pygame.draw.rect(screen,WHITE, (300,350,150,50))
	screen.blit(text_8, (300,350))

	pygame.draw.rect(screen,BLACK, (50,520,400,50))
	pygame.draw.rect(screen,WHITE, (60,530,380,30))

	pygame.draw.circle(screen, BLACK, (150,400), 100)
	pygame.draw.circle(screen, WHITE, (150,400), 95)
	pygame.draw.circle(screen, BLACK, (150,400), 5)

	# Set buttons
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:

				# +m button
				if (50 < mouse_x < 100) and (50 < mouse_y < 100):
					total_secs += 60
					total = total_secs

				# -m button
				if (50 < mouse_x < 100) and (200 < mouse_y < 250):
					total_secs -= 60
					total = total_secs

				# +s button
				if (150 < mouse_x < 200) and (50 < mouse_y < 100):
					total_secs += 1
					total = total_secs

				# -s button
				if (150 < mouse_x < 200) and (200 < mouse_y < 250):
					total_secs -= 1
					total = total_secs

				# Start button
				if (300 < mouse_x < 450) and (50 < mouse_y < 100):
					start = True
					total = total_secs

				# Reset button
				if (300 < mouse_x < 450) and (150 < mouse_y < 200):
					total_secs = 0

				# Stop button
				if (300 < mouse_x < 450) and (250 < mouse_y < 300) and start:
					start = False
					pausing = True

				# Conti button
				if (300 < mouse_x < 450) and (350 < mouse_y < 400) and pausing:
					start = True
					pausing = False

	if start:
		total_secs -= 1
		if total_secs == 0:
			start = False
		time.sleep(0.5)
	if total_secs < 0:
		start = False
		total_secs = 0

	mins = int(total_secs / 60)
	secs = total_secs - mins * 60
	time_now = str(mins) + " : " + str(secs)
	text_time = font.render(time_now, True, BLACK)
	screen.blit(text_time, (90,120))

	x_sec = 150 + 90 * math.sin(6 * secs * math.pi / 180)
	y_sec = 400 - 90 * math.cos(6 * secs * math.pi / 180)
	pygame.draw.line(screen, BLACK, (150,400), (int(x_sec),int(y_sec)))

	x_min = 150 + 40 * math.sin(6 * mins * math.pi / 180)
	y_min = 400 - 40 * math.cos(6 * mins * math.pi / 180)
	pygame.draw.line(screen, RED, (150,400), (int(x_min),int(y_min)))

	if total != 0:
		pygame.draw.rect(screen, RED, (60,530,int(380 * (total_secs / total)),30))

	pygame.display.flip()

pygame.quit()