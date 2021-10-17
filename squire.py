# Simple pygame program

# Import and initialize the pygame library
import pygame, random, time, threading
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

map = [0]*10000
localMobs = []




w, h = pygame.display.get_surface().get_size()


treeImage = pygame.image.load('Tree.png')
playerImage = pygame.image.load('Npc.png')



# Run until the user asks to quit
running = True

playerMapPos = random.randint(0,10000)

playerStats = {'HealthPoints':0,'Stamina':0,'Food':0,'Sleep':0,'Shekels':0, 'Strength':0,'Agility':0,'Dexterity':0,'Intelligence':0}
player = {'x':0,'y':0}

clock = pygame.time.Clock()



def statGeneration():

	playerStats['Strength'] = random.randint(3,18)
	playerStats['Agility'] = random.randint(3,18)
	playerStats['Dexterity'] = random.randint(3,18)
	playerStats['Intelligence'] = random.randint(3,18)
	playerStats['HealthPoints'] = playerStats['Strength'] + playerStats['Agility']
	playerStats['Stamina'] = playerStats['Agility'] + playerStats['Dexterity']

def renderStats():
	tileDimension = w / 30
	
	xStart = tileDimension * 20
	yStart = tileDimension * 1
	
	
	for i in playerStats:
		font = pygame.font.SysFont("System", 40)
		color = (0,60,20)
		if(i == 'Strength'):
			yStart+=tileDimension * 4
		text_surface = font.render(i+': '+str(playerStats[i]), False, color)
		screen.blit(text_surface, (xStart,yStart))
		yStart +=tileDimension
		
		

def mapGenerate():
	for i in range(10000):
		map[i] = random.randint(0,1)
		if(random.randint(0,1000) == 69 or random.randint(0,1000) == 420):
			map[i] = 2
		
		

def mapRender():
	global localMobs
	tileDimension = w / 30
	resizeImage = pygame.transform.scale(treeImage,(round(tileDimension),round(tileDimension)))
	playerImageResize = pygame.transform.scale(playerImage,(round(tileDimension),round(tileDimension)))
	
	renderX = 0
	renderY = 0
	
	localMobs = []
	mapRenderPos = playerMapPos - 150
	for j in range(15):
		for i in range(20):
			if(map[mapRenderPos] == 1):
				screen.blit(resizeImage,(renderX,renderY))
			renderX+=tileDimension
			mapRenderPos+=1
			if(j == 7 and i == 10):
				screen.blit(playerImageResize,(renderX,renderY))
				player['x'] = i 
				player['y'] = j
			if(map[mapRenderPos] == 2):
				screen.blit(playerImageResize,(renderX,renderY))
				localMobs.append({'mood':random.randint(1,3),'location':mapRenderPos,'x':i,'y':j})
		renderX = 0
		renderY+=tileDimension


		
def playerInteraction():
	if(map[playerMapPos] == 1):
		pass
		

		
		
def combat(pos):
	tileDimension = w / 30
	x = round(pos[0] / tileDimension)
	y = round(pos[1] / tileDimension)
	

	for i in localMobs:
		if(i['x'] + 1 == x or i['x'] - 1):
			if(i['y']+1 == y or i['y'] - 1):
				print('hit')
	
	
		
def npcAI():
	global localMobs
	for i in localMobs:
		movement = random.randint(0,3)
		
		playerRadius = False
		if(playerRadius):
			if(player['x'] < i['x']):
				map[i['location']-1] = 2
				map[i['location']] = 0
			elif(player['x'] > i['x']):
				map[i['location']+1] = 2
				map[i['location']] = 0
			elif(player['y']< i['y']):
				map[i['location']-20] = 2
				map[i['location']] = 0
			elif(player['y'] > i['y']):
				map[i['location']+20] = 2
				map[i['location']] = 0
		else:	
			if movement == 0:
				map[i['location']+1] = 2
				map[i['location']] = 0
			elif movement == 1:
				map[i['location']+20] = 2
				map[i['location']] = 0
			elif movement == 2:
				map[i['location']-1] = 2
				map[i['location']] = 0
			elif movement == 3:
				map[i['location']-20] = 2
				map[i['location']] = 0


			
			

mapGenerate()
statGeneration()
npcAI()


aiTimer = 0

while running:

    # Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if(event.key == pygame.K_w):
				playerMapPos -= 20
			if(event.key == pygame.K_s):
				playerMapPos += 20
			if(event.key == pygame.K_d):
				playerMapPos +=1
			if(event.key == pygame.K_a):
				playerMapPos -=1
			if(event.key == pygame.K_ESCAPE):
				running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			combat(pos)

			
	# Fill the background with white
	screen.fill((255, 255, 255))
	if(aiTimer > 60):
		aiTimer = 0
		npcAI()
	else:
		aiTimer +=1
	
	
	mapRender()
	renderStats()
    # Flip the display
	pygame.display.flip()
	
	clock.tick(60)

# Done! Time to quit.
pygame.quit()