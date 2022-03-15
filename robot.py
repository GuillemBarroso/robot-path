import numpy as np


class Robot():
    def __init__(self):
        self.x = None
        self.y = None
        self.face = None
        self.dx = None
        self.dy = None
        self.orientations = None
        self.orientList = ['NORTH', 'WEST', 'SOUTH', 'EAST']

    def Place(self, x0=0, y0=0, face0="NORTH"):
        self.x = x0
        self.y = y0
        self.face = face0
        self.getFirstOrientation()

    def Move(self):
        dx, dy = self.getMovingDir(self.face)
        self.x += dx
        self.y += dy

    def Report(self):
        return self.x, self.y, self.face

    def Rotate(self, rotation):
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
        self.orientations = np.roll(self.orientList, self.orientList.index(self.face))


class Tabletop():
    def __init__(self):
        self.lenX = None
        self.lenY = None

    def setTableDim(self, lenX, lenY):
        self.lenX = lenX
        self.lenY = lenY
