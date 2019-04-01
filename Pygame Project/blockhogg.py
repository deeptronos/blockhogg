import pygame as pyg
import characterBlockhogg as char
import random

class Game():
	def __init__(self):
		#Set stuff up
		pyg.init()
		pyg.display.set_caption("Chesz 2")
		#pyg.display.toggle_fullscreen()
		#Makes global width of tiles to use, in pixels
		self.tileWidth, self.tileHeight = 50, 50
		#Makes window size in relation to tile size
		self.screenWidth, self.screenHeight = self.tileWidth * 24, self.tileHeight * 5

		#Sets variable used to determine if user wants to quit
		self.done = False
		self.gameRunning = True

		self.debugMode = False

		#self.stage = stageData(1)
		self.stage = randomStageData()
		self.collidableBlockColor = (255,255,255)
		#Set to whatever size ya want. Looks best if it's at least screenWidth/tileWidth (24, in this case) but it still works if it's less.
		self.randomlyGeneratedStageLength = 24
		self.randomlyGeneratedStageData = []
		self.randomlyGeneratedStageDataExists = False
	
		self.scrollSpeed = 5
		self.bgX = 0
		self.bgX2 = 0

		self.black = (0,0,0)
		self.red = (255,0,0)

		self.clock = pyg.time.Clock()
		self.tickSpeed = 30
		self.screen = pyg.display.set_mode((self.screenWidth, self.screenHeight), (pyg.FULLSCREEN))
		#Surface we're drawing the blocks to, so we can blit it onto the main screen to move it
		self.blockSurface = pyg.Surface((self.tileWidth * self.randomlyGeneratedStageLength, self.screenHeight))
		self.blockSurfaceBlitted = False
		self.counter = 0


		self.player1 = char.Character(self.red, self.screen, self.screenWidth, self.screenHeight, 50, 25, 1)

	def run_game(self):
		#Put all logic inside this loop, above pyg.display.flip()
	#	pyg.key.set_repeat(1, 25)
	#	pyg.key.set_repeat()
		while not self.done:
			self.bgX -= self.scrollSpeed
			self.bgX2 -= self.scrollSpeed 
			if self.bgX < self.blockSurface.get_width() * -1:
				self.bgX = self.blockSurface.get_width()
			if self.bgX2 < self.blockSurface.get_width() * -1:
				self.bgX2 = self.blockSurface.get_width()

			self.clock.tick(self.tickSpeed)
			for event in pyg.event.get():
				if event.type == pyg.QUIT:
					self.done = True
			self.screen.fill((self.black))

			if self.debugMode:
				self.debug()
				
			if self.randomlyGeneratedStageDataExists == False:
				self.generateStageData()
			elif self.randomlyGeneratedStageDataExists == True:
				#self.detectCollision()

				self.drawStage(self.bgX, 0)
				self.player1.update()
				self.player1.draw()

				pyg.display.update()
		
	#Old stage drawing method - outdated
	def drawStageOld(self):
		for row in range(len(self.stage.returnStageVar())):
			for col in range(len(self.stage.returnStageVar()[0])):

				print("row: " + str(row) + ", col: "+ str(col))
				print(self.stage.returnStageData(col, row))
				if self.stage.returnStageData(col,row) == 0:
					pass
				if self.stage.returnStageData(col,row) == 1:
					pyg.draw.rect(self.screen, self.collidableBlockColor, pyg.Rect((col * self.tileWidth), (row * self.tileHeight),self.tileWidth, self.tileHeight), )
					#print("hit")

	def drawStage(self, x, y):
		#print("drawing stage:", self.randomlyGeneratedStageData)
		if self.blockSurfaceBlitted == False:
			for row in range(len(self.randomlyGeneratedStageData)):
				for col in range(len(self.randomlyGeneratedStageData[0])):
					if self.randomlyGeneratedStageData[row][col] == 0:
						pass
						#print("miss")
					elif self.randomlyGeneratedStageData[row][col] == 1 or self.randomlyGeneratedStageData[row][col] == 2:
						
						pyg.draw.rect(self.blockSurface, self.collidableBlockColor, pyg.Rect((col * self.tileWidth), (row * self.tileHeight), self.tileWidth, self.tileHeight))
						self.bgX2 = self.blockSurface.get_width()
						self.screen.blit(self.blockSurface, (x,y))

			self.blockSurfaceBlitted = True
		else:
			#Draws screen-width rects on the top 5th and bottom 5th of the screen to close visible gaps between the two blits ;) because i don't know whats makin em do that
			pyg.draw.rect(self.screen, self.collidableBlockColor, pyg.Rect(0, 0, self.screenWidth, self.screenHeight/5))
			pyg.draw.rect(self.screen, self.collidableBlockColor, pyg.Rect(0, self.screenHeight - (self.screenHeight/5), self.screenWidth, self.screenHeight))

			self.screen.blit(self.blockSurface, (self.bgX, 0))
			self.screen.blit(self.blockSurface, (self.bgX2, 0))

					#print("hit")
					#pyg.

	def generateStageData(self):
				#Randomly generates stage data to a size determined by the original stage data variable from the randomStageData class and by the randomlyGeneratedStageLength variable
				counter = 0
				self.randomlyGeneratedStageData = []
				for row in range(len(self.stage.randomStageData)):
					tempRow = []
					for col in range(self.randomlyGeneratedStageLength):
						if counter < 3:
							tempRow.append(self.stage.returnStageData("individual", row, 10))
							counter = counter + 1
						elif counter == 3:
							#Randomly choose a vertical slice from the stage data to append onto the game stage. A certain value is added to the retrieved variable length, because when a value is generated that's above the retrieved variable length, it's changed to select the last value of the list. Thus, the odds of retrieving the last value of the list are increased.
							vertSlice = random.randint(0, (len(self.stage.randomStageData[0]) - 1))
							tempRow.append(self.stage.returnStageData("individual", row, vertSlice))
							counter = 0

					self.randomlyGeneratedStageData.append(tempRow)
					print(tempRow)

				#Loop to make sure that there arent any "walls" (vertical columns of anything other than 0)	
				#Works by moving column by column, not row by row as the generation loop does, since we're looking for vertical columns in this case.
				for col in range(len(self.randomlyGeneratedStageData[0])):
					#blockCounter is added to each time anything that isnt a 0 is detected in a column. Each column should have at least two, a top and bottom, with potentially more if there are obsticles.
					blockCounter = 0
					for row in range(len(self.randomlyGeneratedStageData)):	

						if (self.randomlyGeneratedStageData[row][col] == 1) or (self.randomlyGeneratedStageData[row][col] == 2):
							blockCounter +=1 

					#If blockCounter detects that there is a full vertical column which has only blocks (represented by anything other than 0), it will re-generate the data and reset all variables that could have potentially changed
					if blockCounter == len(self.randomlyGeneratedStageData):
						print("wall generated, re-running self.generateStageData()")
						self.randomlyGeneratedStageDataExists = False
						self.errorCatcher = True
						self.generateStageData()

					else:
						self.randomlyGeneratedStageDataExists = True	
		
	def debug(self):
		self.debugColor = (255,0,239)
		for vy in range(14):
			for vx in range(24):
				pyg.draw.rect(self.screen, self.debugColor, pyg.Rect((vx * self.tileWidth),(vy * self.tileHeight),(self.tileWidth),( self.tileHeight)),1 )  

	#def detectCollision(self):


	def goCrazy(self):
		return (random.randrange(255), random.randrange(255),random.randrange(255))

		
#old stage data returning function - do not use:
class stageData():
	def __init__(self, selectedStage):
		self.selectedStage = selectedStage

		#initialize stageData with 1 as the selectedStage parameter to use this stage:
		#dont use this anymore it's for the old version
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

#new stage data returning method:
class randomStageData():
	def __init__(self):				
		self.randomStageData =		[[1,1,1,1,1,1,1,1,1,1,1],
									 [1,0,1,0,0,1,2,0,0,1,0],
									 [0,0,0,1,1,1,0,0,2,2,0],
									 [0,1,1,0,1,0,0,2,1,0,0],
									 [1,1,1,1,1,1,1,1,1,1,1]]
	
	def returnStageData(self, returnMode, yPosition, xPosition):
		if returnMode == "individual":
			return self.randomStageData[yPosition][xPosition]

		if returnMode == "column":
			for i in range(len(self.randomStageData)):
				if 'columnData' in locals():
					columnData.append(self.randomStageData[i][xPosition])
				else: 
					columnData = [self.randomStageData[i][xPosition]]
			return columnData


Game().run_game()
#Game().drawStage()
