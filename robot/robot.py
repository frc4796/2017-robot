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
        
        left = wpilib.Spark(0)
        right = wpilib.Spark(1)
        right.setInverted(True)
        left.setInverted(True)
        
        self.robotdrive = wpilib.RobotDrive(left, right)
        #self.xboxcontroller = wpilib.XboxController(0)
        self.leftdoormotor = wpilib.Spark(2)
        self.rightdoormotor = wpilib.Spark(3)
        self.encoder = wpilib.Encoder(0,1)
        self.stick = wpilib.Joystick(0)
        
    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        #if self.xboxcontroller.getBumper(self.xboxcontroller.Hand.kLeft):
        #    self.gears.open()
        #if self.xboxcontroller.getBumper(self.xboxcontroller.Hand.kRight):
        #    self.gears.close()
        self.drive.move(self.stick.getY(), self.stick.getX())
            
if __name__ == '__main__':
    wpilib.run(MyRobot)