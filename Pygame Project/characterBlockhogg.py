import pygame as pyg

class Character():
	def __init__(self, color, screen, screenWith, screenHeight, playernum):
		#getting info from the display
		infoObject = pyg.display.Info()
        width, height = infoObject.current_w, infoObject.current_h
		#determing starting position
		if playernum == 1:
			self.x = screenWidth/3
			self.y = screenHeight/2
		if playernum == 2:
			self.x = screenWidth*2/3
			self.y = screenHeight/2
		#defining variables based off of screen size. This should be done with tile size aswell.
		self.screen = screen
		self.wHeight = height
        self.wWidth = width
		self.movex = 0
		self.movey = 0
		#making the character object
		self.chaRect = pygame.Rect(self.x, self.y, self.wHeight, self.wWidth)
		self.speed = 5
		self.jumpHeight
		self.color = colors
		self.hp = 100
	def draw(self, playernum):
		if playernum == 1:
			self.chaRect = pyg.draw.rect(self.screen, (255,0,0))
		if playernum == 2:
			self.chaRect = pyg.draw.rect(self.screen, (0,0,255))
	#movement momentum system
	def control(self, x, y):
		if self.hp > 0:
			self.movex += x
			self.movey += y
	def jump(self): #COME BACK AND MAKE SURE YOU MAKE A VARIABLE ONGROUND 
		if chaRect.colliderect() == True:
			self.movey += self.jumpHeight #adding vertical momentum to the character
	def update(self):
        self.chaRect.x = self.chaRect.x + self.movex
        self.chaRect.y = self.cahRect.y + self.movey
	#Character Movement Control
		for e in pyg.event.get():
			if e.type == pygame.QUIT():
				pygame.quit()
			if self.playernum == 1:
				if event.type == pygame.KEYDOWN:
					if event.key == ord('a'):
						chaRect.control(-speed,0)
					if event.key == ord('d'):
						chaRect.control(speed,0)
					if event.key == ord('w'):
						jump(self)

				if event.type == pygame.KEYUP:
					if event.key == ord('a'):
						player.control(speed,0)
					if event.key == ord('d'):
						player.control(-speed,0)
					if event.key == ord('q'):
						pygame.quit()

			if self.playernum == 2:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						chaRect.control(-speed,0)
					if event.key == pygame.K_RIGHT:
						chaRect.control(speed,0)
					if event.key == pygame.K_UP:
						jump(self)

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:
						player.control(speed,0)
					if event.key == pygame.K_RIGHT:
						player.control(-speed,0)
					if event.key == ord('q'):
						pygame.quit()