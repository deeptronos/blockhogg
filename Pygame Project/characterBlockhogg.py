import pygame as pyg

class Character():
	def __init__(self, color, screenWith, screenHeight, playernum):
		if playernum == 1:
			self.x = screenWidth/3
			self.y = screenHeight/2
		if playernum == 2:
			self.x = screenWidth*2/3
			self.y = screenHeight/2
		self.speed = 5
		self.rect = pygame.Rect(self.x, self.y)
		self.color = colors
		self.hp = 100