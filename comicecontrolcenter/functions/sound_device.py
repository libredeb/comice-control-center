""" This functionaliy try to know the volume level of the sound device in our Linux.
    By default, we use a amixer (ALSA Mixer) to know that.
"""
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib


class SoundInformation():
    
    def __init__(self):
        super().__init__()
        self.device = None
        
        command = """amixer -D pulse sget Master | awk -F"[][]" '/Left:/ { print $2 }'"""
        result = os.popen(command).read()
        
        if len(result) > 0:
            self.volume = result.strip().replace("%", "")
        else:
            self.volume = 0
        
    def get_volume(self):
        return int(self.volume)

