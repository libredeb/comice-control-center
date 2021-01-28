import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio
from comicecontrolcenter.functions.do_not_disturb import DoNotDisturbInformation


class DisturbBox(Gtk.Box):

    def __init__(self):
        """ Disturb Box."""
        super().__init__()
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        # Do Not Disturb feature - icon and label
        disturb = DoNotDisturbInformation()
        
        disturb_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        disturb_name_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        disturb_icon = None
        if disturb.get_state():
            disturb_icon = Gtk.Image.new_from_file("icons/disturb.png")
        else:
            disturb_icon = Gtk.Image.new_from_file("icons/disturb-d.png")
        
        disturb_1st_line_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        disturb_1st_line = Gtk.Label("")
        disturb_1st_line.set_markup ("<b>Do Not</b>")
        disturb_1st_line.get_style_context().add_class("general_title")
        disturb_1st_line_box.pack_start(disturb_1st_line, False, True, 0)
        
        disturb_2nd_line_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        disturb_2nd_line = Gtk.Label("")
        disturb_2nd_line.set_markup("<b>Disturb</b>")
        disturb_2nd_line.get_style_context().add_class("general_title")
        width_separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        width_separator.set_opacity(0.0)
        disturb_2nd_line_box.pack_start(disturb_2nd_line, False, True, 0)
        disturb_2nd_line_box.pack_start(width_separator, False, True, 20)
        
        disturb_name_box.pack_start(disturb_1st_line_box, False, True, 0)
        disturb_name_box.pack_start(disturb_2nd_line_box, False, True, 0)
        
        disturb_box.pack_start(disturb_icon, False, True, 10)
        disturb_box.pack_start(disturb_name_box, False, True, 0)
        
        # Finally all baxes are packaged
        main_box.pack_start(disturb_box, False, True, 16)
        
        self.pack_start(main_box, True, True, 0)
        self.get_style_context().add_class("styledwidgetbox")

