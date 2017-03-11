import wpilib
from robotpy_ext.common_drivers.navx import AHRS

from components.drive import Drive

class Turner:
    ahrs = AHRS
    drive = Drive
         
    if wpilib.RobotBase.isSimulation():
        # These PID parameters are used in simulation
        kP = 0.06
        kI = 0.00
        kD = 0.00
        kF = 0.00
    else:
        # These PID parameters are used on a real robot
        kP = 0.03
        kI = 0.00
        kD = 0.00
        kF = 0.00
    
    kToleranceDegrees = 2.0
    
    def setup(self):
        turnController = wpilib.PIDController(self.kP, self.kI, self.kD, self.kF, self.ahrs, output=self)
        turnController.setInputRange(-180.0,  180.0)
        turnController.setOutputRange(-1.0, 1.0)
        turnController.setAbsoluteTolerance(self.kToleranceDegrees)
        turnController.setContinuous(True)
        
        self.turnController = turnController
        self.last_angle_is_none = True
        
    def on_enable(self):
        self.angle = None
    
    def rotate_to(self, angle):
        self.angle = angle

    def reset(self):
        self.ahrs.reset()

    def execute(self):
        isNone = self.angle is None
        if isNone != self.last_angle_is_none:
            if isNone:
                self.turnController.disable()
            else:
                self.rotateToAngleRate = 0
                self.turnController.enable()
        
        if not isNone:
            self.turnController.setSetpoint(self.angle)
            self.drive.rotate(self.rotateToAngleRate)
            
        self.last_angle_is_none = isNone
        self.angle = None
            
    def pidWrite(self, output):
        self.rotateToAngleRate = output
