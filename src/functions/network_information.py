import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib


class NetworkInformation():
    
    def __init__(self):
        super().__init__()
        self.device = self.get_wifi()
        
        if self.device != "unk0":
            command = """cat /sys/class/net/{}/carrier""".format(self.device)
            result = os.popen(command).read()
            if len(result.strip()) == 0:
                result = "0"
            carrier = int(result)
            if carrier > 0:
                wifi_name = os.popen("iwgetid").read()
                self.name = wifi_name.split(":")[1].replace ('"', "").strip()
                self.connected = True
            else:
                self.name = ""
                self.connected = False
        else:
            self.device = self.get_eth()
            self.name = "ETH"
            command = """cat /sys/class/net/{}/carrier""".format(self.device)
            result = os.popen(command).read()
            if len(result.strip()) == 0:
                result = "0"
            carrier = int(result)
            if carrier > 0:
                self.connected = True
            else:
                self.connected = False
    
    def get_wifi(self):
        command = """iw dev | grep Interface"""
        result = os.popen(command).read()
        if len(result) > 0:
            result = result.strip().split(" ")[1]
        else:
            result = "unk0"
            print("Cant read wireless interface!")
        return result
    
    def get_eth(self):
        command = """ip link | grep -v lo | grep -v vir | grep -v wl | grep -v br | grep -v veth | grep -v docker"""
        result = os.popen(command).read()
        if len(result) > 0:
            result = result.split(":")[1].strip()
        else:
            result = "unk0"
            print("Cant read ethernet interface!")
        return result
    
    def get_name(self):
        return self.name
    
    def get_device(self):
        return self.device
    
    def is_connected(self):
        return self.connected

