import pygame as pyg
from blockhogg import Game.screen

class Laser():
    def __init__(self):
        super().__init__()
        self.x = characterBlockhogg.x
        self.y = characterBlockhogg.y
        self.laser = pygame.Surface([4,12])
        self.laser.fill(RED)
        self.rect = self.laser.get_rect()
    def fire(self,laserpos):
        self.rect.x += 10
    def update(self):
        if colliderect(self.laser) == True:
            self.laser.kill()

class Character():
	def __init__(self, color, screen, screenWith, screenHeight, playernum):
		#getting info from the display
		infoObject = pyg.display.Info()
		width, height = infoObject.current_w, infoObject.current_h
		#determing starting position
		self.x = screenWidth/3
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
		self.color = colors
		self.hp = 100
	def draw(self, playernum):
		self.chaRect = pyg.draw.rect(self.screen, (255,0,0))
	#movement momentum system
	def control(self, x, y):
		if self.hp > 0:
			if chaRect.right < self.screenWidth:
				if chaRect.left > 0:
					self.movex += x
					self.movey += y
				else:
					self.movex = 0
					self.movey = 0

	laser_list = pygame.sprite.Group()
	def attack(self):
		laserpos = chaRect.center()
		laser = Laser()
		laser.rect.x = self.x
		laser.rect.y = self.y
		laser_list.add(laser)
		
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
						chaRect.control(0, -speed)
					if event.key == ord('s'):
						chaRect.control(0, speed)
					if event.key == ord('j'):
						attack()

				if event.type == pygame.KEYUP:
					if event.key == ord('a'):
						player.control(speed,0)
					if event.key == ord('d'):
						player.control(-speed,0)
					if event.key == ord('w'):
						chaRect.control(0, speed)
					if event.key == ord('s'):
						chaRect.control(0, -speed)
					if event.key == ord('q'):
						pygame.quit()