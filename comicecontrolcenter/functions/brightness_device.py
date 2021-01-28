""" This functionaliy try to know the state of the brightness device in our Linux.
    By default, exists a file in /sys/class/backlight/<device>/brightness that hold
    the current brightness value.
"""
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib


class BrightnessInformation():
    
    def __init__(self):
        super().__init__()
        self.device = None
        self.brightness = 0
        
        command = """ls /sys/class/backlight/"""
        result = os.popen(command).read()
        
        if len(result) > 0:
            self.device = result.strip()
        else:
            self.device = None
        
        if self.device is not None:
            command2 = """cat /sys/class/backlight/{}/max_brightness""".format(self.device)
            result2 = os.popen(command2).read()
            if len(result2) > 0:
                self.max_brightness = int(result2)
            else:
                self.max_brightness = 100
            
            command3 = """cat /sys/class/backlight/{}/brightness""".format(self.device)
            result3 = os.popen(command3).read()
            self.brightness = int((int(result3) * 100) / self.max_brightness)
        else:
            self.brightness = 100
        
    def get_device(self):
        return self.device
    
    def get_max_brightness(self):
        return self.max_brightness
    
    def get_current_brightness(self):
        return self.brightness

