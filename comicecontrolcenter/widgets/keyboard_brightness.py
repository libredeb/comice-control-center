import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio


class KbdBrightnessBox(Gtk.Box):

    def __init__(self):
        """ Keyboard Brightness Box."""
        super().__init__()
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        open_button = Gtk.Button()
        open_button.set_always_show_image(True)
        open_button.connect("clicked", self.do_open_kbdbrightness_app)
        open_button.get_style_context().add_class("widgetbutton")
        
        kbdbrightness_icon = Gtk.Image.new_from_file("icons/kbdbrightness.png")
        kbd_label = Gtk.Label("")
        kbd_label.set_markup ("Keyboard")
        kbd_label.get_style_context().add_class("general_widget_title")
        brightness_label = Gtk.Label("")
        brightness_label.set_markup ("Brightness")
        brightness_label.get_style_context().add_class("general_widget_title")
        
        grid = Gtk.Grid()
        grid.attach(kbdbrightness_icon,0,0,1,1)
        grid.attach(kbd_label,0,1,1,1)
        grid.attach(brightness_label,0,2,1,1)
        grid.show_all()
        open_button.add (grid)
        
        # Finally all baxes are packaged
        main_box.pack_start(open_button, False, True, 0)
        
        self.pack_start(main_box, True, True, 0)
        self.get_style_context().add_class("styledwidgetbox")
    
    def do_open_kbdbrightness_app(self, event):
        try:
            GLib.spawn_command_line_async("""/bin/bash -c '/usr/bin/gnome-control-center keyboard &'""")
        except:
            print("Error opening APP.KBD_BRIGHTNESS")

