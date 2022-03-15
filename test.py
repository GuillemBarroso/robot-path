from robot import Robot
from main import main

def getFirstOrientation_test():
    r = Robot()
    faces = ["NORTH", "WEST", "EAST", "SOUTH"]
    for face in faces:
        r.face = face
        r.getFirstOrientation()
        assert(face == r.orientations[0]), "The fist entry in orientations must match the specified face when placing"

    print("Unit testing for getFirstOrientation() successful!")

def rotate_test():
    r = Robot()
    tests = [["NORTH", "LEFT", "EAST"],
             ["WEST", "LEFT", "NORTH"],
             ["SOUTH", "LEFT", "WEST"],
             ["EAST", "LEFT", "SOUTH"],
             ["NORTH", "RIGHT", "WEST"],
             ["WEST", "RIGHT", "SOUTH"],
             ["SOUTH", "RIGHT", "EAST"],
             ["EAST", "RIGHT", "NORTH"]]

    for test in tests:
        r.place(0,0,test[0])
        r.rotate(test[1])
        assert(r.orientations[0] == test[2])

    print("Unit testing for rotate() successful!")
    

if __name__ == '__main__':

    # Unit testing
    getFirstOrientation_test()
    rotate_test()

    # System testing 
    orders = [
        ['PLACE 0,0,NORTH', 'MOVE', 'REPORT'],
        ['PLACE 0,0,NORTH', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE','REPORT'],
        ['MOVE','RIGHT','PLACE 2,2,SOUTH', 'MOVE', 'REPORT'],
        ['PLACE 0,0,SOUTH', 'MOVE', 'REPORT'],
        ['PLACE 1,1,WEST', 'MOVE', 'MOVE', 'MOVE', 'MOVE', 'MOVE', 'REPORT'],
        ['PLACE 2,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'MOVE', 'REPORT'],
        ['PLACE 4,5,SOUTH', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'MOVE', 'MOVE', 'LEFT', 'LEFT', 'MOVE','REPORT'],
        ['PLACE 4,0,NORTH', 'RIGHT', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'LEFT', 'MOVE', 'LEFT', 'LEFT', 'MOVE', 'MOVE', 'LEFT', 'MOVE','REPORT'],
        ['PLACE 0,4,EAST', 'RIGHT', 'REPORT','MOVE','REPORT']
        ]
    targets = [
        [0,1,"NORTH"],
        [0,0,"EAST"],
        [2,1,"SOUTH"],
        [0,0,"SOUTH"],
        [5,1,"WEST"],
        [0,3,"NORTH"],
        [4,5,"EAST"],
        [5,2,"NORTH"],
        [0,5,"NORTH"],
    ]

    for i, order in enumerate(orders):
        out = main(order, verbose=False, log="critical")
        assert(targets[i][0] == out.report[0]), "Position X incorrect: got {}, want {}".format(out.report[0], targets[i][0])
        assert(targets[i][1] == out.report[1]), "Position Y incorrect: got {}, want {}".format(out.report[1], targets[i][1])
        assert(targets[i][2] == out.report[2]), "Direction incorrect: got {}, want {}".format(out.report[2], targets[i][2])

    print("System testing successful!")