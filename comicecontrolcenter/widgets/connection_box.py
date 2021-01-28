import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio
from comicecontrolcenter.functions.network_information import NetworkInformation
from comicecontrolcenter.functions.bluetooth_information import BluetoothInformation
from comicecontrolcenter.functions.airplane_mode import AirPlaneInformation


class ConnectionsBox(Gtk.Box):

    def __init__(self):
        """ Connections Box."""
        super().__init__()
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        # Network (WiFi or Ethernet) - icon with labels
        network = NetworkInformation()
        network_status = ""
        
        network_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        net_name_conn_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        network_icon = None
        if network.get_name() == "ETH":
            if network.is_connected():
                network_icon = Gtk.Image.new_from_file("icons/eth.png")
                network_status = "Connected"
            else:
                network_icon = Gtk.Image.new_from_file("icons/eth-d.png")
                network_status = "Not Connected"
        else:
            if network.is_connected ():
                network_icon = Gtk.Image.new_from_file("icons/wifi.png")
                network_status = network.get_name()
            else:
                network_icon = Gtk.Image.new_from_file("icons/wifi-d.png")
                network_status = "Not Connected"
        
        network_device_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        network_device = Gtk.Label("")
        
        if network.get_name () == "ETH":
            network_device.set_markup("<b>Ethernet</b>")
        else:
            network_device.set_markup ("<b>Wi-Fi</b>")
            
        network_device.get_style_context().add_class("general_title")
        network_device_box.pack_start(network_device, False, True, 0)
        
        network_name_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        network_name = Gtk.Label("")
        network_name.set_markup(network_status)
        network_name.get_style_context().add_class("general_desc")
        width_separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        width_separator.set_opacity(0.0)
        network_name_box.pack_start(network_name, False, True, 0)
        network_name_box.pack_start(width_separator, False, True, 5)
        
        net_name_conn_box.pack_start(network_device_box, False, True, 0)
        net_name_conn_box.pack_start(network_name_box, False, True, 0)
        
        network_box.pack_start(network_icon, False, True, 10)
        network_box.pack_start(net_name_conn_box, False, True, 0)
        
        # Bluetooth icon
        bluetooth = BluetoothInformation()
        bluetooth_status = ""
        
        bluetooth_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        bluetooth_conn_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        bluetooth_icon = None
        if bluetooth.exists():
            if bluetooth.is_powered_on():
                bluetooth_icon = Gtk.Image.new_from_file("icons/bluetooth.png")
                if len(bluetooth.get_name()) > 0:
                    bluetooth_status = bluetooth.get_name()
                else:
                    bluetooth_status = "On"
            else:
                bluetooth_icon = Gtk.Image.new_from_file("icons/bluetooth-d.png")
                bluetooth_status = "Off"
        else:
            bluetooth_icon = Gtk.Image.new_from_file("icons/bluetooth-d.png")
            bluetooth_status = "Not Available"
        
        bluetooth_device_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        bluetooth_device = Gtk.Label("")
        bluetooth_device.set_markup("<b>Bluetooth</b>")
        bluetooth_device.get_style_context().add_class("general_title")
        bluetooth_device_box.pack_start(bluetooth_device, False, True, 0)
        
        bluetooth_name_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        bluetooth_name = Gtk.Label("")
        bluetooth_name.set_markup(bluetooth_status)
        bluetooth_name.get_style_context().add_class("general_desc")
        width_separator_2 = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        width_separator_2.set_opacity(0.0)
        bluetooth_name_box.pack_start(bluetooth_name, False, True, 0)
        bluetooth_name_box.pack_start(width_separator_2, False, True, 5)
        
        bluetooth_conn_box.pack_start(bluetooth_device_box, False, True, 0)
        bluetooth_conn_box.pack_start(bluetooth_name_box, False, True, 0)
        
        bluetooth_box.pack_start(bluetooth_icon, False, True, 10)
        bluetooth_box.pack_start(bluetooth_conn_box, False, True, 0)
        
        # AirPlane Mode icon
        airplane = AirPlaneInformation()
        airplane_status = ""
        
        airplane_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        airplane_conn_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        airplane_icon = None
        if airplane.get_state():
            airplane_icon = Gtk.Image.new_from_file("icons/airplane.png")
            airplane_status = "On"
        else:
            airplane_icon = Gtk.Image.new_from_file("icons/airplane-d.png")
            airplane_status = "Off"
        airplane_device_box = Gtk.Box(Gtk.Orientation.HORIZONTAL, 0)
        airplane_device = Gtk.Label("")
        airplane_device.set_markup("<b>AirPlane</b>")
        airplane_device.get_style_context().add_class("general_title")
        airplane_device_box.pack_start (airplane_device, False, True, 0)
        
        airplane_name_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        airplane_name = Gtk.Label("")
        airplane_name.set_markup(airplane_status)
        airplane_name.get_style_context().add_class("general_desc")
        airplane_name_box.pack_start(airplane_name, False, True, 0)
        
        airplane_conn_box.pack_start(airplane_device_box, False, True, 0)
        airplane_conn_box.pack_start(airplane_name_box, False, True, 0)
        
        airplane_box.pack_start(airplane_icon, False, True, 10)
        airplane_box.pack_start(airplane_conn_box, False, True, 0)
        
        # This separator fix the box width
        fix_separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        fix_separator.set_opacity(0.0)
        fix_separator.set_size_request(120, 1)
        
        # Finally all baxes are packaged
        main_box.pack_start(network_box, False, True, 10)
        main_box.pack_start(fix_separator, True, True, 0)
        main_box.pack_start(bluetooth_box, True, True, 0)
        main_box.pack_start(airplane_box, True, True, 10)
        
        self.pack_start(main_box, True, True, 0)
        self.get_style_context().add_class("styledwidgetbox")

