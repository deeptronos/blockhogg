import pygame as pyg
import characterBlockhogg as char

class Game():
	def __init__(self):
		#Set stuff up
		pyg.init()
		pyg.display.set_caption("Blockhogg")
		#Makes global width of tiles to use, in pixels
		self.tileWidth, self.tileHeight = 50, 50
		#Makes window size in relation to tile size
		self.screenWidth, self.screenHeight = self.tileWidth * 24, self.tileHeight * 14
		self.clock = pyg.time.Clock()
		self.screen = pyg.display.set_mode((self.screenWidth, self.screenHeight))
		#Sets variable used to determine if user wants to quit
		self.done = False
		self.gameRunning = True

		self.debugMode = True
		
		self.character = char.Character()

	def gravity(self):
		pass

	def run_game(self):
		#Put all logic inside this loop, above pyg.display.flip()
		while not self.done:
			for event in pyg.event.get():
				if event.type == pyg.QUIT:
					self.done = True

				if self.debugMode:
					self.debug()

				self.chracter.draw(1)
			pyg.display.flip()
	
	def drawStage(self):
		pass

	def debug(self):
		self.debugColor = (255,0,239)
		for vy in range(14):
			for vx in range(24):
				pyg.draw.rect(self.screen, self.debugColor, pyg.Rect((vx * self.tileWidth),(vy * self.tileHeight),((vx * self.tileWidth) + self.tileWidth),((vy * self.tileHeight) + self.tileHeight)),1 )      
		

#class stageData():
	def __init__(self, selectedStage):
		

Game().run_game()
