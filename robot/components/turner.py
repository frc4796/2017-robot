import wpilib
from robotpy_ext.common_drivers.navx import AHRS

from components.drive import Drive

class Turner:
    ahrs = AHRS
    drive = Drive

    def rotate_to(self, angle):
        pass

    def reset(self):
        self.ahrs.reset()

    def execute(self):

        self.ahrs_count = self.ahrs.getAngle()
