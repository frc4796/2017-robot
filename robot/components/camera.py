
from networktables.util import ntproperty

from components.turner import Turner

class Camera:
    
    turner = Turner

    target = ntproperty('/camera/target', (0, 0, 0))
    
    def on_enable(self):
        self.do_align = False
    
    def align(self):
        self.do_align = True
    
    def execute(self):
    
        if self.do_align:
            self.turner.rotate_to(0)
    
        self.do_align = None
