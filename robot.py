#!/usr/bin/env python3
'''
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
    
    WARNING: While it may look like a good choice to use for your code if
    you're inexperienced, don't. Unless you know what you are doing, complex
    code will be much more difficult under this system. Use IterativeRobot
    or Command-Based instead if you're new.
'''

import wpilib

VALUE = 1600

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''Robot initialization function'''
        
        # object that handles basic drive operations
        self.myRobot = wpilib.RobotDrive(0, 1)
        self.myRobot.setExpiration(0.1)
        
        self.encoder = wpilib.Encoder(0, 1)
        
        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)
        
    def autonomousPeriodic(self):
        if self.encoder.get() < VALUE:
            self.myRobot.drive(-0.5, 0)
        else:
            self.myRobot.drive(0, 0)
        
    def teleopInit(self):
        self.myRobot.setSafetyEnabled(True)
        
    def teleopPeriodic(self):
        '''Runs the motors with tank steering'''
        self.myRobot.tankDrive(self.leftStick, self.rightStick)
  
if __name__ == '__main__':
    wpilib.run(MyRobot)
