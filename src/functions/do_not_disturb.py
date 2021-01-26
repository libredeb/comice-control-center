""" This functionaliy try to know the state of *Do Not Disturb* feature
    in notification plugin for each desktop environment.
    Example:
      - For GNOME3: gsettings get org.gnome.desktop.notifications show-banners
      - For XFCE4: [command here]
"""
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib


class DoNotDisturbInformation():
    
    def __init__(self):
        super().__init__()
        self.state = None
        
        command = """gsettings get org.gnome.desktop.notifications show-banners"""
        result = os.popen(command).read()
        
        if result.strip() == "false":
            self.state = True
        else:
            self.state = False
    
    def get_state(self):
        return self.state

