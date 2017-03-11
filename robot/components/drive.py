import wpilib

from magicbot import tunable

class Drive:
    encoder = wpilib.Encoder
    circumference = 18.85 #inches
    robotdrive = wpilib.RobotDrive
    
    encoder_count = tunable(default=0)
    encoder_inches = tunable(default=0)
    
    def on_enable(self):
        self.speed = 0
        self.rotation = 0
    
    def move(self,speed,rotation):
        self.speed = speed
        self.rotation = rotation
    
    def rotate(self, rotation):
        self.rotation = rotation
    
    def get_encoder_distance(self):
        '''Returns distance in inches'''
        return self.encoder.get() * (self.circumference / 360.0)
    
    def reset_encoder(self):
        self.encoder.reset()
    
    def execute(self):
        
        self.encoder_count = self.encoder.get()
        self.encoder_inches = self.get_encoder_distance()
        
        self.robotdrive.arcadeDrive(self.speed,self.rotation)
        self.speed = 0
        self.rotation = 0
    