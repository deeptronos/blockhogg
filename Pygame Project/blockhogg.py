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

		#currently working with stage 1
		self.stage = stageData(1)
		self.collidableBlockColor = (255,255,255)

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
				self.drawStage()
			pyg.display.flip()
	
	def drawStage(self):
		for row in range(len(self.stage.returnStageVar())):
			for col in range(len(self.stage.returnStageVar()[0])):

				print("row: " + str(row) + ", col: "+ str(col))
				print(self.stage.returnStageData(row, col))
				if self.stage.returnStageData(row,col) == 0:
					pass
				if self.stage.returnStageData(row,col) == 1:
					pyg.draw.rect(self.screen, self.collidableBlockColor, pyg.Rect((col * self.tileWidth), (row * self.tileHeight),self.tileWidth, self.tileHeight), )
					#print("hit")

	def debug(self):
		self.debugColor = (255,0,239)
		for vy in range(14):
			for vx in range(24):
				pyg.draw.rect(self.screen, self.debugColor, pyg.Rect((vx * self.tileWidth),(vy * self.tileHeight),(self.tileWidth),( self.tileHeight)),1 )      
		

class stageData():
	def __init__(self, selectedStage):
		self.selectedStage = selectedStage

		#initialize stageData with 1 as the selectedStage parameter to use this stage:
		self.stage1 =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


	def returnStageData(self, yPosInStageList, xPosInStageList):
		if self.selectedStage == 1:
			return self.stage1[yPosInStageList][xPosInStageList]

	def returnStageVar(self):
		if self.selectedStage == 1:
			return self.stage1

Game().run_game()
#Game().drawStage()
