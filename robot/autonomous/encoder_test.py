import components.drive
from magicbot import AutonomousStateMachine, state

class EncoderTest(AutonomousStateMachine):
    
    MODE_NAME = "EncoderTest"
    
    drive = components.drive.Drive
    
    def on_enable(self):
        super().on_enable()
        self.drive.reset_encoder()
    
    @state(first=True)
    def drive_fwd(self):
        if self.drive.get_encoder_distance() > 24.0:
            self.next_state(self.drive_back)
        else:
            self.drive.move(-0.3, 0)
    
    @state
    def drive_back(self):
        if self.drive.get_encoder_distance() < 0:
            self.done()
        else:
            self.drive.move(0.3, 0)
    
    
