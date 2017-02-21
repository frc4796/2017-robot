#!/usr/bin/env python3

import wpilib
from robotpy_ext.common_drivers.navx import AHRS

from magicbot import MagicRobot

from components.drive import Drive
from components.climber import Climber
from components.gears import Gears

class MyRobot(MagicRobot):

    #
    # Define components here
    #

    drive = Drive
    climber = Climber
    gears = Gears

    practice_robot = False


    def createObjects(self):
        """Initialize all wpilib motors & sensors"""

        if self.practice_robot:
            left = wpilib.Spark(0)
            right = wpilib.Spark(1)
            right.setInverted(True)
            left.setInverted(True)
        else:
            left = wpilib.TalonSRX(1)
            right = wpilib.TalonSRX(0)
            right.setInverted(True)
            left.setInverted(True)

        self.robotdrive = wpilib.RobotDrive(left, right)
        #self.xboxcontroller = wpilib.XboxController(0)
        self.leftdoormotor = wpilib.Spark(2)
        self.rightdoormotor = wpilib.Spark(3)
        self.encoder = wpilib.Encoder(0,1)
        self.stick = wpilib.Joystick(0)

        self.light = wpilib.Relay(0)
        self.light.set(self.light.Value.kOn)
        wpilib.CameraServer.launch()
        self.ahrs = AHRS.create_spi()

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        #if self.xboxcontroller.getBumper(self.xboxcontroller.Hand.kLeft):
        if self.stick.getRawButton(2):
            self.gears.open()
        elif self.stick.getRawButton(3):
            self.gears.close()
        #if self.xboxcontroller.getBumper(self.xboxcontroller.Hand.kRight):
        #    self.gears.close()
        self.drive.move(self.stick.getY(), self.stick.getX())


if __name__ == '__main__':
    wpilib.run(MyRobot)
