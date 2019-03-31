import pygame as pyg
import characterBlockhogg as char
import random

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
		self.counter = 0
		#Sets variable used to determine if user wants to quit
		self.done = False
		self.gameRunning = True

		self.debugMode = True

		#self.stage = stageData(1)
		self.stage = randomStageData()
		self.collidableBlockColor = (255,255,255)

		self.randomlyGeneratedStageLength = 16
		self.randomlyGeneratedStageData = []
		self.randomlyGeneratedStageDataExists = False
		#Change to player movement speed once that's done
		self.scrollSpeed = 10
		self.black = (100,0,0)

	def gravity(self):
		pass

	def run_game(self):
		#Put all logic inside this loop, above pyg.display.flip()
		while not self.done:
			for event in pyg.event.get():
				if event.type == pyg.QUIT:
					self.done = True
				self.screen.fill((self.black))

				if self.debugMode:
					self.debug()
				
				if self.randomlyGeneratedStageDataExists == False:
					self.generateStageData()
				elif self.randomlyGeneratedStageDataExists == True:
					self.drawStage()
				
			pyg.display.flip()
	
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

	def drawStage(self):
		#print("drawing stage:", self.randomlyGeneratedStageData)
		for row in range(len(self.randomlyGeneratedStageData)):
			for col in range(len(self.randomlyGeneratedStageData[0])):
				if self.randomlyGeneratedStageData[row][col] == 0:
					pass
					#print("miss")
				elif self.randomlyGeneratedStageData[row][col] == 1 or self.randomlyGeneratedStageData[row][col] == 2:
					pyg.draw.rect(self.screen, self.collidableBlockColor, pyg.Rect((col * self.tileWidth), (row * self.tileHeight), self.tileWidth, self.tileHeight))
					#print("hit")

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
						#	print("running tempRow.append(self.stage.returnStageData('individual', ", row, ", ", vertSlice, "))")
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
