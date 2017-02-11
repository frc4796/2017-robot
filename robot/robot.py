import wpilib

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
    
    def createObjects(self):
        """Initialize all wpilib motors & sensors"""
        
        # TODO: create button example here
        
        self.component1_motor = wpilib.Talon(1)
        self.some_motor = wpilib.Talon(2)
        
        self.joystick = wpilib.Joystick(0)
        
    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        
        try:
            if self.joystick.getTrigger():
                self.component2.do_something()
        except:
            self.onException()
            
if __name__ == '__main__':
    wpilib.run(MyRobot)