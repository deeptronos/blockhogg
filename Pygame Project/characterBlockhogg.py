import pygame as pyg
#Can't import class attributes directly in the "import" statement, you have to do it elsewhere (see https://stackoverflow.com/questions/9155079/import-a-class-variable-from-another-module)
#from blockhogg import Game
#from Game import screen

class Laser():
    def __init__(self):
        super().__init__()
        self.x = characterBlockhogg.x
        self.y = characterBlockhogg.y
        self.laser = pyg.Surface([4,12])
        self.laser.fill(RED)
        self.rect = self.laser.get_rect()
    def fire(self,laserpos):
        self.rect.x += 10
    def update(self):
        if colliderect(self.laser) == True:
            self.laser.kill()

class Character():
	def __init__(self, color, screen, screenWidth, screenHeight, playerWidth, playerHeight, playernum):
		#getting info from the display
		infoObject = pyg.display.Info()
		width, height = infoObject.current_w, infoObject.current_h
		#determing starting position
		#self.x = screenWidth/3
		self.x = 25
		self.y = screenHeight/2
		#defining variables based off of screen size. This should be done with tile size aswell.
		self.screen = screen
		self.wHeight = height
		self.wWidth = width
		self.playerWidth = playerWidth
		self.playerHeight = playerHeight

		self.movex = 0
		self.movey = 0
		#making the character object
		self.chaRect = pyg.Rect(self.x, self.y, self.playerWidth, self.playerHeight)
		self.speed = 5
		self.color = color
		self.hp = 100
		self.playerNum = playernum
	def draw(self):
		#self.chaRect = pyg.draw.rect(self.screen, self.color, self.char)
		pyg.draw.rect(self.screen, self.color, self.chaRect)
	#movement momentum system
	def control(self, x, y):

		if self.hp > 0:
			if self.chaRect.right < self.wWidth:
				if self.chaRect.left >= 0:
					self.movex += x
					self.movey += y
					print("self.movex: ", self.movex, " self.movey: ", self.movey)
				else:
					self.movex = 0
					self.movey = 0



	laser_list = pyg.sprite.Group()
	def attack(self):
		laserpos = chaRect.center()
		laser = Laser()
		laser.rect.x = self.x
		laser.rect.y = self.y
		laser_list.add(laser)
		
	#old update function - im makin a new one	
	def oldupdate(self):
		self.chaRect.x = self.chaRect.x + self.movex
		self.chaRect.y = self.chaRect.y + self.movey
		#Character Movement Control
		for event in pyg.event.get():
			#We already have this in the blockhogg.py and it's making the game act weird when i hit "close" so i'm just commenting it out
			#if e.type == pyg.QUIT():
			#	pyg.quit()
			if self.playerNum == 1:
				if event.type == pyg.KEYDOWN:
					if event.key == ord('a'):
						chaRect.control(-speed,0)
					if event.key == ord('d'):
						chaRect.control(speed,0)
					if event.key == ord('w'):
						chaRect.control(0, -speed)
					if event.key == ord('s'):
						chaRect.control(0, speed)
					if event.key == ord('j'):
						attack()

				if event.type == pyg.KEYUP:
					if event.key == ord('a'):
						player.control(speed,0)
					if event.key == ord('d'):
						player.control(-speed,0)
					if event.key == ord('w'):
						chaRect.control(0, speed)
					if event.key == ord('s'):
						chaRect.control(0, -speed)
					#if event.key == ord('q'):
					#	pyg.quit()

	def newoldupdate(self):

		self.x = self.x + self.movex
		self.y = self.y + self.movey		
		self.chaRect = pyg.Rect(self.x, self.y, self.wHeight, self.wWidth)
		#Character Movement Control
		for event in pyg.event.get():

			#We already have this in the blockhogg.py and it's making the game act weird when i hit "close" so i'm just commenting it out
			#if e.type == pyg.QUIT():
			#	pyg.quit()
			if self.playerNum == 1:

				if event.type == pyg.KEYDOWN:
					print("pyg.KEYDOWN")
					print("event key: ", event.key)
					if event.key == pyg.K_a:
						self.control(-self.speed,0)
					if event.key == pyg.K_d:
						self.control(self.speed,0)
					if event.key == pyg.K_w:
						self.control(0, (-1 * self.speed))
					if event.key == pyg.K_s:
						self.control(0, self.speed)
					if event.key == pyg.K_j:
						self.attack()

				if event.type == pyg.KEYUP:
					print("pyg.KEYUP")
					print("event key: ", event.key)
					if event.key == pyg.K_a:
						self.control(self.speed,0)
					if event.key == pyg.K_d:
						self.control(-self.speed,0)
					if event.key == pyg.K_w:
						self.control(0, self.speed)
					if event.key ==  pyg.K_s:
						self.control(0, -self.speed)
					#if event.key == ord('q'):
					#	pyg.quit()
	
	def update(self):		
		self.chaRect = pyg.Rect(self.x, self.y, self.playerWidth, self.playerHeight)
		#Character Movement Control
		if self.playerNum == 1:
			pressed = pyg.key.get_pressed()
			if pressed[pyg.K_w]: self.y = self.y - self.speed
		#	if pressed[pyg.K_a]: self.x = self.x - self.speed
			if pressed[pyg.K_s]: self.y = self.y + self.speed
			if pressed[pyg.K_q]: pyg.quit()
		#	if pressed[pyg.K_d]: self.x = self.x + self.speed

