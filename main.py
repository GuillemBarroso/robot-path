from multiprocessing.sharedctypes import Value
from robot import Robot, Tabletop
from communication import Translator
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # orders = ['PLACE 0,0,NORTH', 'MOVE', 'REPORT']
    # orders = ['PLACE 0,0,NORTH', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE', 'RIGHT', 'MOVE','REPORT']
    # orders = ['MOVE','RIGHT','PLACE 2,2,SOUTH', 'MOVE', 'REPORT']
    orders = ['PLACE 0,0,SOUTH', 'MOVE', 'REPORT']

    r = Robot()
    t = Translator(r)
    Tabletop().setTableDim(5,5)

    t.parseOrders(orders)

    