import numpy as np
import logging


class Robot():
    def __init__(self, xLim=(0,5), yLim=(0,5)):
        self.x = None
        self.y = None
        self.face = None
        self.dx = None
        self.dy = None
        self.orientations = None
        self.xLim = xLim
        self.yLim = yLim
        self.orientList = ['NORTH', 'WEST', 'SOUTH', 'EAST']

    def place(self, x0=0, y0=0, face0="NORTH"):
        self.x = x0
        self.y = y0
        self.face = face0
        self.getFirstOrientation()

    def move(self):
        dx, dy = self.getMovingDir(self.face)
        newX = self.x + dx
        newY = self.y + dy
        if self.xLim[0] <= newX <= self.xLim[1] and self.yLim[0] <= newY <= self.yLim[1]:
            self.x = newX
            self.y = newY
        else:
            logging.warning("Ilegal move ordered. Igoring order.")            

    def report(self):
        return self.x, self.y, self.face

    def rotate(self, rotation):
        if rotation == 'LEFT':
            self.orientations = np.roll(self.orientations, 1)
        elif rotation == 'RIGHT':
            self.orientations = np.roll(self.orientations, -1)
        self.face = self.orientations[0]

    def getMovingDir(self, face):
        if face == "NORTH":
            self.dx = 0
            self.dy = 1
        elif face == "SOUTH":
            self.dx = 0
            self.dy = -1
        elif face == "EAST":
            self.dx = -1
            self.dy = 0
        elif face == "WEST":
            self.dx = 1
            self.dy = 0

        return self.dx, self.dy

    def getFirstOrientation(self):
        self.orientations = np.roll(self.orientList, -self.orientList.index(self.face))
