import wpilib
class Gears:
    leftdoormotor = wpilib.Spark
    rightdoormotor = wpilib.Spark
    
    def on_enable(self):
        #Insure that motor isn't activated when the robot turns on
        self.do_open = None
        
    def open(self):
        self.do_open = True
    
    def close(self):
        self.do_open = False
    
    def execute(self):
        if self.do_open == True:
            self.rightdoormotor.set(1)
            self.leftdoormotor.set(-1)
        
        elif self.do_open == False:
            self.rightdoormotor.set(-1)
            self.leftdoormotor.set(1)
        else:
            self.rightdoormotor.set(0)
            self.leftdoormotor.set(0)
            
        