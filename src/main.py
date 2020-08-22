import os

import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GLib

class RunCat:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__)) 
        self.timeout_interval = 100
        self.frame = 0

        self.indicator = appindicator.Indicator.new(
            "RunCat",
            self.current_dir + "/0.png",
            appindicator.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

        self.timeout = GLib.timeout_add(int(self.timeout_interval), self.timeout_callback)

        self.init_menus()

    def init_menus(self):
        self.menu = Gtk.Menu()
        self.create_menu("quit",Gtk.main_quit)
        self.indicator.set_menu(self.menu)

    def create_menu(self, name, func):
        item = Gtk.MenuItem(name)
        item.connect("activate",func , name)
        self.menu.append(item)
        item.show()

    def timeout_callback(self):
        img_name = str(self.frame) + ".png"
        self.indicator.set_icon(self.current_dir +"/"+ img_name)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

        self.frame += 1
        if self.frame > 4:
            self.frame = 0
        return True


if __name__ == "__main__":
    run_cat = RunCat()
    Gtk.main()

