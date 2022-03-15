from robot import Robot
from main import main   
import pytest

def test_getFirstOrientation():
    r = Robot()
    faces = ["NORTH", "WEST", "EAST", "SOUTH"]
    for face in faces:
        r.face = face
        r.getFirstOrientation()
        assert(face == r.orientations[0]), "The fist entry in orientations must match the specified face when placing"

    print("Unit testing for getFirstOrientation() successful!")

def test_rotate():
    r = Robot()
    tests = [["NORTH", "LEFT", "WEST"],
             ["WEST", "LEFT", "SOUTH"],
             ["SOUTH", "LEFT", "EAST"],
             ["EAST", "LEFT", "NORTH"],
             ["NORTH", "RIGHT", "EAST"],
             ["WEST", "RIGHT", "NORTH"],
             ["SOUTH", "RIGHT", "WEST"],
             ["EAST", "RIGHT", "SOUTH"]]

    for test in tests:
        r.place(0,0,test[0])
        r.rotate(test[1])
        assert(r.orientations[0] == test[2])

    print("Unit testing for rotate() successful!")
    

def test_system():
    # Note that all tests must finish with a REPORT, so the final position is recovered for assessment
    orders = [
        ['PLACE 0,0,NORTH', 'MOVE', 'REPORT'],
        ['PLACE 0,0,NORTH', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE','REPORT'],
        ['MOVE','RIGHT','PLACE 2,2,SOUTH', 'MOVE', 'REPORT'],
        ['PLACE 0,0,SOUTH', 'MOVE', 'REPORT'],
        ['PLACE 1,1,WEST', 'MOVE', 'MOVE', 'REPORT'],
        ['PLACE 2,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'MOVE', 'REPORT'],
        ['PLACE 4,5,SOUTH', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'MOVE', 'MOVE', 'LEFT', 'LEFT', 'MOVE','REPORT'],
        ['PLACE 4,0,NORTH', 'RIGHT', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'LEFT', 'MOVE', 'LEFT', 'LEFT', 'MOVE', 'MOVE', 'LEFT', 'MOVE','REPORT'],
        ['PLACE 0,4,EAST', 'RIGHT', 'REPORT','MOVE','REPORT'],
        ['PLACE 2,1,WEST', 'RIGHT', 'MOVE','PLACE 5,5,NORTH', 'REPORT'],
        ["PLACE -1,0,NORTH", "MOVE","RIGHT", "PLACE 1,1,SOUTH", "MOVE", "REPORT"],
        ["PLACE 0,0,NORTH", "LEFT", "REPORT"],
        ["PLACE 1,2,EAST", "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"],
        ]
    targets = [
        [0,1,"NORTH"],
        [0,0,"WEST"],
        [2,1,"SOUTH"],
        [0,0,"SOUTH"],
        [0,1,"WEST"],
        [5,1,"SOUTH"],
        [4,5,"WEST"],
        [5,2,"NORTH"],
        [0,3,"SOUTH"],
        [5,5,"NORTH"],
        [1,0,"SOUTH"],
        [0,0,"WEST"],
        [3,3,"NORTH"],
    ]

    for i, order in enumerate(orders):
        out = main(order, verbose=False, log="critical")
        assert(targets[i][0] == out.report[0]), "Test {} failed. Position X incorrect: got {}, want {}".format(i, out.report[0], targets[i][0])
        assert(targets[i][1] == out.report[1]), "Test {} failed. Position Y incorrect: got {}, want {}".format(i, out.report[1], targets[i][1])
        assert(targets[i][2] == out.report[2]), "Test {} failed. Direction incorrect: got {}, want {}".format(i, out.report[2], targets[i][2])

    print("System testing successful!")

if __name__ == '__main__':

    # Unit testing
    test_getFirstOrientation()
    test_rotate()

    # System testing 
    test_system()
    