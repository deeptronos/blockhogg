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

	def gravity(self):
		pass
	def run_game(self):
		#Loop to make sure that window will stay open unless user wants to quit
		while not self.done:
			for event in pyg.event.get():
				if event.type == pyg.QUIT:
					self.done = True
		pyg.display.flip()


Game().run_game()