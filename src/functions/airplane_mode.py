""" This functionaliy try to know the state of AirPlane mode in our Linux
    with the help of rfkill utility.
      - When the output is [blocked] the AirPlane mode is turned on.
      - When the output is [unblocked] the AirPlane mode is turned off.
"""
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib


class AirPlaneInformation():
    
    def __init__(self):
        super().__init__()
        self.state = None
        
        command = """rfkill -n -o SOFT | sort | uniq | sed -n \$p"""
        result = os.popen(command).read()
        
        if result.strip() == "blocked":
            self.state = True
        else:
            self.state = False
    
    def get_state(self):
        return self.state

