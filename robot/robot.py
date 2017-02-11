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
        
     
        
        self.robotdrive = wpilib.RobotDrive(0,1)
        self.xboxcontroller = wpilib.XboxController(0)
        self.leftdoormotor = wpilib.Spark(3)
        self.rightdoormotor = wpilib.Spark(4)
        
    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        if self.xboxcontroller.getBumper(self.xboxcontroller.Hand.kLeft):
            self.gears.open()
        if self.xboxcontroller.getBumper(self.xboxcontroller.Hand.kRight):
            self.gears.close()
            
        #try:
           # if self.joystick.getTrigger():
               # self.component2.do_something()
        #except:
            #self.onException()
            
if __name__ == '__main__':
    wpilib.run(MyRobot)