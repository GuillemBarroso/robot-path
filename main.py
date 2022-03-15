from robot import Robot
from communication import Operator
import logging
import argparse

def main(orders, verbose=True ,log="warning"):
    if log == "debug":
        logging.basicConfig(level=logging.DEBUG)
    elif log == "info":
        logging.basicConfig(level=logging.INFO)
    elif log == "warning":
        logging.basicConfig(level=logging.WARNING)
    elif log == "error":
        logging.basicConfig(level=logging.ERROR)
    elif log == "critical":
        logging.basicConfig(level=logging.CRITICAL)
    
    r = Robot(xLim = [0,5], yLim = [0,5])
    o = Operator(r, verbose)
    o.parseOrders(orders)

    return o

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Moving robot application')
    parser.add_argument('--orders', nargs="*", type=str, help='List of orders to be executed by the robot.'+
    'Implemented orders are "PLACE X,Y,DIR", "MOVE", "RIGHT", "LEFT" and "REPORT".', default = ['PLACE 0,0,NORTH', 'MOVE', 'REPORT'])
    parser.add_argument('--verbose', type=bool, help="Shows robot's report meassage if set to true",
        default = True)
    parser.add_argument('--log', type=str, help='Set logging level of the printed information. Can be set to"'+
     '"debug", "info", "warning", "error" and  "critical"',
        default = "warning")
    args   = parser.parse_args()

    main(args.orders, args.verbose, args.log)
    
    