# robot-path

Application that moves a robot on a tabletop

## Decription

Two main classes are defined in order to implement this application.

1. Robot: has the information of the current position of the robot and contains methods that can alter
its position by moving, placing and rotating the robot.

2. Operator: translates orders and passes them to the robot. 

As can be seen in `main.py`, Robot is first initialised defining the limits of the tabletop. Then, Opeator is initialised with the just created Robot and the verbose input. After that, the application is ready to recieve user-defined orders.

## Install dependencies

Install pipenv and initiate environment with

```
pipenv shell
```

Once activated, install dependencies

```
pipenv install -r requirements.txt
```

## Execute application

Use help command for agruments of main.py

```
pipenv run python main.py -h
```

to obtain

```
usage: main.py [-h] [--orders [ORDERS ...]] [--verbose VERBOSE] [--log LOG]

Moving robot application

optional arguments:
  -h, --help            show this help message and exit
  --orders [ORDERS ...]
                        List of orders to be executed by the robot.Implemented orders are "PLACE X,Y,DIR", "MOVE",
                        "RIGHT", "LEFT" and "REPORT".
  --verbose VERBOSE     Shows robot's report meassage if set to true
  --log LOG             Set logging level of the printed information. Can be set to""debug", "info", "warning",
                        "error" and "critical"
```

An example of the command to execute the application with some orders is

```
pipenv run python main.py --orders "PLACE 0,0,NORTH" "MOVE" "MOVE" "RIGHT" "MOVE" "REPORT"
```

## Testing

The file `test.py` contains unit testing for two of the main functions of the application. Moreover, a collection of paths with known end point are executed in order to test the system.

To run all tests use

```
pipenv run python test.py
```