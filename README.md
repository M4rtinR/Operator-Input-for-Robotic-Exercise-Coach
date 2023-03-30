# Operator Input
This repo contains code for running the stroke rehabilitation system on Pepper. he operator input replaces any sensing software used in the squash system, and allows the operator to signal completion of each exercise repitition to the robot. Written in Python 3. The main code can be found here: https://github.com/M4rtinR/coachingPolicies.

## Downloading the Code
Similar to the main coaching policy code, clone the robot test repo into a new Pycharm project. 

## Running the Demo
1. Set the Python Interpreter and configuration in the same way as you did for the main coaching policy program, using Python3.8 for the interpreter.

2. After all of the other parts of the code are running, click Run.

3. Watch the user of the system perform the exercises. When they start performing the first exercise in a set, press the enter key on the keyboard. Press enter again when they complete each repetition. This will send a signal to the robot indicating a completed rep, and the counter should be updated on the screen. NOTE: There is a small bug which means the counter does not update if the robot is still performing the previous behaviour (e.g. if it is mid-demonstration, the counter won't update).
