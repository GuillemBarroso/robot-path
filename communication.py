import sys
import logging

class Operator():
    def __init__(self, robot, verbose):
        self.r = robot
        self.verbose = verbose
        self.report = None

    def parseOrders(self, orders):
        for order in orders:
            logging.debug("Order: {}".format(order))
            if self.r.x == None and order[:5] != "PLACE":
                logging.info("Ignoring order {} since the robot has not been placed yet.".format(order))
            else:
                self.translateOrder(order)
            logging.debug("Moved to: " + str(self.r.report()))

    def translateOrder(self, order):
        if order == 'MOVE':
            self.r.move()
        elif order == 'REPORT':
            self.report = self.r.report()
            if self.verbose:
                print(self.report)

        elif order[:5] == "PLACE":
            try:
                xStr, yStr, face = order[6:].split(',')
                x0 = int(xStr)
                y0 = int(yStr)

                self.r.place(x0,y0,face)
            except Exception as e:
                raise ValueError('PLACE order must be: PLACE "xCoord","yCoord","direction". {}'.format(e))   
            
        elif order == 'RIGHT' or order == 'LEFT':
            self.r.rotate(order)
        else:
            raise ValueError('Valid orders are "PLACE xCoord,yCoord,direction", "MOVE", "RIGHT", "LEFT", "REPORT"')