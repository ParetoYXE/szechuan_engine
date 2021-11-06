# Simple pygame program

# Import and initialize the pygame library
import pygame, random, time, threading, math
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



#50*50=2500
mapTotalSize = 2500
worldDimension = 50


map = [		 
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,1,8,8,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,8,8,8,8,1,8,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,1,8,8,8,8,8,8,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,4,1,1,1,3,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,8,1,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,8,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,9,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,8,8,8,8,0,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,1,1,1,8,8,8,8,1,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,1,1,0,8,8,8,8,1,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,1,1,1,8,8,8,8,1,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,1,1,1,1,8,1,8,8,1,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,1,8,8,8,8,1,1,1,1,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,1,1,8,8,8,8,8,1,1,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,1,1,3,8,8,8,8,1,1,1,1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,1,1,1,1,1,1,8,8,8,1,1,1,1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,1,1,1,1,1,1,8,0,0,0,1,8,1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,1,1,1,1,1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			]


localMobs = []

w, h = pygame.display.get_surface().get_size()


treeImage = pygame.image.load('Tree.png')
waterImage = pygame.image.load('water.png')
playerImage = pygame.image.load('Npc.png')
castleImage = pygame.image.load('castle.png')
houseImage = pygame.image.load('house.png')
click_zoneImage = pygame.image.load('click_zone.png')




# Run until the user asks to quit
running = True

playerMapPos = 0

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
	
	font = pygame.font.SysFont("System", 50)
	color = (0,60,20)

	pygame.draw.rect(screen, (0,0,0), pygame.Rect(xStart,0, tileDimension*10, tileDimension*20))
	
	xStart+=tileDimension

	for i in playerStats:
		if(i == 'Strength'):
			yStart+=tileDimension * 4
		text_surface = font.render(i+': '+str(playerStats[i]), False, color)
		screen.blit(text_surface, (xStart,yStart))
		yStart +=tileDimension
		
		

def mapGenerate():
	global playerMapPos
	count = 0
	for i in map: 
		if i == 9:
			playerMapPos = count
		count+=1
		

def mapGrowth():
	points = 0
	for i in range(len(map)):
		if(map[i] == 8):
			if(map[i+1] == 8):
				points += 1
			if(map[i-1] == 8):
				points += 1
			if(map[i - worldDimension] == 8):
				points += 1
			if(map[i + worldDimension] == 8):
				points += 1
			if(map[i - worldDimension - 1] == 8):
				points += 1
			if(map[i - worldDimension + 1] == 8):
				points += 1
			if(map[i + worldDimension - 1] == 8):
				points += 1
			if(map[i + worldDimension + 1] == 8):
				points += 1
		if(points > 7):
			map[i] = 4
		points = 0

def mapDeath():
	points = 0
	for i in range(len(map)):
		if(map[i] == 4):
			if(map[i+1] == 4):
				points += 1
			if(map[i-1] == 4):
				points += 1
			if(map[i - worldDimension] == 4):
				points += 1
			if(map[i + worldDimension] == 4):
				points += 1
			if(map[i - worldDimension - 1] == 4):
				points += 1
			if(map[i - worldDimension + 1] == 4):
				points += 1
			if(map[i + worldDimension - 1] == 4):
				points += 1
			if(map[i + worldDimension + 1] == 4):
				points += 1
		if(points > 2):
			map[i] = 8
		points = 0


def mapRender():
	global localMobs
	tileDimension = w / 30
	
	resizeImageWater = pygame.transform.scale(waterImage,(round(tileDimension),round(tileDimension)))
	resizeImageTree = pygame.transform.scale(treeImage,(round(tileDimension),round(tileDimension)))
	resizeImageCastle = pygame.transform.scale(castleImage,(round(tileDimension),round(tileDimension)))
	resizeImageHouse = pygame.transform.scale(houseImage,(round(tileDimension),round(tileDimension)))
	playerImageResize = pygame.transform.scale(playerImage,(round(tileDimension),round(tileDimension)))
	
	renderX = 0
	renderY = 0
	
	localMobs = []
	mapRenderPos = int(playerMapPos - (worldDimension*8) - (20 / 2))
	mapRenderPosX = 0

	
	for j in range(17):
		for i in range(20):
			if(map[mapRenderPos+mapRenderPosX] == 0):
				screen.blit(resizeImageWater,(renderX,renderY))
			if(map[mapRenderPos+mapRenderPosX] == 1):
				screen.blit(resizeImageTree,(renderX,renderY))
			if(map[mapRenderPos+mapRenderPosX] == 2):
				screen.blit(playerImageResize,(renderX,renderY))
				localMobs.append({'mood':random.randint(1,3),'location':mapRenderPos,'x':i,'y':j})
			if(map[mapRenderPos+mapRenderPosX] == 3):
				screen.blit(resizeImageCastle,(renderX,renderY))
			if(map[mapRenderPos+mapRenderPosX] == 4):
				screen.blit(resizeImageHouse,(renderX,renderY))
			renderX+=round(tileDimension)
			mapRenderPosX+=1
	
		renderX = 0
		mapRenderPosX = 0
		mapRenderPos+=worldDimension
		renderY+=round(tileDimension)

	screen.blit(playerImageResize,(tileDimension*10,tileDimension*8))


		
def playerInteraction():
	if(map[playerMapPos] == 1):
		pass
		

		
		
def combat(pos):
	tileDimension = w / 30
	x = math.floor(pos[0] / tileDimension)
	y = math.floor(pos[1] / tileDimension)




	#print('Click location')
	#print('X:'+str(x))
	#print('Y:'+str(y))


	click_zoneImageResize = pygame.transform.scale(click_zoneImage,(round(tileDimension),round(tileDimension)))
	screen.blit(click_zoneImageResize,(x*tileDimension,y*tileDimension))

	#print(localMobs)
	for i in localMobs:
		if(i['x'] == x   and i['y'] == y):
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
				map[i['location']-worldDimension] = 2
				map[i['location']] = 0
			elif(player['y'] > i['y']):
				map[i['location']+worldDimension] = 2
				map[i['location']] = 0
		else:	
			if movement == 0:
				map[i['location']+1] = 2
				map[i['location']] = 0
			elif movement == 1:
				map[i['location']+worldDimension] = 2
				map[i['location']] = 0
			elif movement == 2:
				map[i['location']-1] = 2
				map[i['location']] = 0
			elif movement == 3:
				map[i['location']-worldDimension] = 2
				map[i['location']] = 0


mapGenerate()
statGeneration()
npcAI()


aiTimer = 0
combatCheck = False
pos = [0,0]

timer = pygame.time.get_ticks()
cycleToggle = True
while running:

    # Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if(event.key == pygame.K_w):
				playerMapPos -= worldDimension
			if(event.key == pygame.K_s):
				playerMapPos += worldDimension
			if(event.key == pygame.K_d):
				playerMapPos +=1
			if(event.key == pygame.K_a):
				playerMapPos -=1
			if(event.key == pygame.K_ESCAPE):
				running = False
			if(event.key == pygame.K_RETURN):
				map[playerMapPos] = 4
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			combatCheck = True

			
	# Fill the background with white
	screen.fill((0,110,51))

	if pygame.time.get_ticks()-timer > 1000:
		timer = pygame.time.get_ticks()
		if(cycleToggle):
			mapGrowth()
			cycleToggle = False
		else:
			mapDeath()
			cycleToggle = True

		print(cycleToggle)
	#if(aiTimer > 60):
	#	aiTimer = 0
	#	npcAI()
	#	print('test')
	#else:
	#	aiTimer +=1
	
	
	mapRender()
	renderStats()
	if(combatCheck):
		combat(pos)
		combatCheck = False
    # Flip the display
	pygame.display.flip()
	



	clock.tick(60)

# Done! Time to quit.
pygame.quit()