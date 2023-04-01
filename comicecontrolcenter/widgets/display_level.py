import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio
from comicecontrolcenter.functions.brightness_device import BrightnessInformation


class DisplayLevelBox(Gtk.Box):

    def __init__(self):
        """ Display Level Box."""
        super().__init__()
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        slider_icon_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        
        # Custom Function
        brightness = BrightnessInformation()
        
        display_name_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        display_name = Gtk.Label("")
        display_name.set_markup("<b>Display</b>")
        display_name.get_style_context().add_class("general_title")
        display_name_box.pack_start(display_name, False, True, 0)
        
        ad1 = Gtk.Adjustment(0, 0, 100, 1, 1, 0)
        self.slider = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        self.slider.set_draw_value(False)
        self.slider.set_hexpand(True)
        self.slider.set_valign(Gtk.Align.START)
        self.slider.connect("move-slider", self.scale_moved)
        self.slider.get_style_context().add_class("widgetslider")
        self.slider.set_value(brightness.get_current_brightness())
        display_btn = Gtk.Button()
        display_btn.get_style_context().add_class("sliderbutton")
        display_icon = Gtk.Image.new_from_file("icons/control-display.png")
        grid = Gtk.Grid()
        grid.attach(display_icon,0,0,1,1)
        grid.show_all()
        display_btn.add (grid)
        display_btn.connect("clicked", self.do_open_display_app)
        fix_separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        fix_separator.set_opacity(0.0)
        slider_icon_box.pack_start(self.slider, False, True, 0)
        slider_icon_box.pack_start(fix_separator, False, True, 6)
        slider_icon_box.pack_start(display_btn, False, True, 0)
        
        bottom_separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        bottom_separator.set_opacity(0.0)
        
        content_box.pack_start(display_name_box, False, True, 10)
        content_box.pack_start(slider_icon_box, False, True, 0)
        content_box.pack_start(bottom_separator, False, True, 5)
        
        # All boxes are packaged
        main_box.pack_start(content_box, False, True, 8)
        
        self.pack_start(main_box, True, True, 8)
        self.get_style_context().add_class("styledwidgetbox")

        self.slider.connect("value_changed", self.scale_moved)
        
    def scale_moved(self, event):
        try:
            GLib.spawn_command_line_async(f"""/bin/bash -c 'dbus-send \
                                                            --session \
                                                            --type=method_call \
                                                            --dest="org.gnome.SettingsDaemon.Power" \
                                                            /org/gnome/SettingsDaemon/Power \
                                                            org.freedesktop.DBus.Properties.Set \
                                                            string:"org.gnome.SettingsDaemon.Power.Screen" \
                                                            string:"Brightness" \
                                                            variant:int32:{int(self.slider.get_value())}'""")
        except:
            print("Error changing the value of your display brightness level")

    def do_open_display_app(self, event):
        try:
            GLib.spawn_command_line_async("""/bin/bash -c '/usr/bin/gnome-control-center display &'""")
        except:
            print("Error opening APP.DISPLAY")