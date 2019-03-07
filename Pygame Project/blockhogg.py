import pygame as pyg
import characterBlockhogg as char

class Game():
	def __init__(self):
		pyg.init()
		pyg.display.set_caption("Blockhogg")
		self.tileWidth, self.tileHeight = 50, 50
		self.screenWidth, self.screenHeight = self.tileWidth * 24, self.tileHeight * 14
		self.clock = pyg.time.Clock()
		self.screen = pyg.display.set_mode(self.screenWidth, self.screenHeight)
	def gravity(self):
		pass
	def run_game(self):
		pass


Game().run_game()