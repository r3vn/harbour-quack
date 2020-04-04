#!/usr/bin/env python3

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

import time
import importlib
import subprocess
import os
import dbus
import dbus.service

DBUS_IFACE="com.quack.hid"
DBUS_PATH ="/com/quack/hid"

class QuackService(dbus.service.Object):

    def __init__(self):

        # Null char
        self.NULL_CHAR = chr(0)

        # HID device status
        self.HID = os.path.exists("/sys/kernel/config/usb_gadget/quack_hid/idVendor")
        self.HID_DEVICE="/dev/hidg0"

        # load default keyboard layout
        self.set_layout("us")

        # init dbus
        bus_name = dbus.service.BusName(DBUS_IFACE, bus=dbus.SystemBus())
        dbus.service.Object.__init__(self, bus_name, DBUS_PATH)

    def write_report(self, report):
        """ send key press """

        if os.path.exists(self.HID_DEVICE):
            with open(self.HID_DEVICE, 'rb+') as fd:
                fd.write(report.encode())


    @dbus.service.method(DBUS_IFACE)
    def get_layouts(self):
        """ get available keyboard layouts """

        layouts = os.listdir("%/layouts/" % os.path.dirname(os.path.abspath(__file__)))
        out     = []

        for layout_file in layouts:
            if layout_file != "__init__.py" and layout_file != "__pycache__":

                # remove ".py" extension from name
                out.append(layout_file.replace(".py",""))

        return out

    @dbus.service.method(DBUS_IFACE)
    def set_layout(self, layout):
        """ change keyboard layout """

        # import keyboard map
        selected  = importlib.import_module('layouts.%s' % layout)
        us_layout = importlib.import_module('layouts.us')

        us_layout.kbd["keycode"].update(selected.kbd["keycode"])

        # set keys
        self.keymod  = us_layout.kbd["modifiers"] # generic modifiers from us layout
        self.keycode = us_layout.kbd["keycode"] # updated with selected layout
        self.shifted = selected.kbd["shifted"] # selected layout shifted keys
        self.altgr   = selected.kbd["altgr"] # selected layout altgr keys

        return True

    @dbus.service.method(DBUS_IFACE)
    def enable_hid(self):
        """ execute enable HID script """
        if not self.HID:
            try:
                subprocess.check_output([ '%s/HID/enable_hid.sh' % os.path.dirname(os.path.abspath(__file__)) ])

                # change HID status
                self.HID = True

            except:
                return False

        return True

    @dbus.service.method(DBUS_IFACE)
    def disable_hid(self):
        """ execute disable HID script """
        if self.HID:
            subprocess.check_output([ '%s/HID/disable_hid.sh' % os.path.dirname(os.path.abspath(__file__)) ])

            # change HID status
            self.HID = False

        return True

    def do_string(self, input_string):
        """ STRING test """
        for ch in input_string:

            if ch.isupper(): # ABCDEF
                self.write_report(self.keymod["SHIFT"]+self.NULL_CHAR+self.keycode[ch.lower()]+self.NULL_CHAR*5)

            else:

                if ch in self.shifted: # /()=?"!$
                    self.write_report(self.keymod["SHIFT"]+self.NULL_CHAR+self.keycode[ self.shifted[ch] ]+self.NULL_CHAR*5)

                elif ch in self.altgr: # @#][
                    self.write_report(self.keymod["RIGHT_ALT"]+self.NULL_CHAR+self.keycode[ self.altgr[ch] ]+self.NULL_CHAR*5)

                else: # abcdef
                    self.write_report(self.NULL_CHAR*2+self.keycode[ch]+self.NULL_CHAR*5)

            time.sleep(0.01)
            self.write_report(self.NULL_CHAR*8) # release key

        # string autoenter
        #write_report(NULL_CHAR*2+self.keycode["ENTER"]+NULL_CHAR*5)
        #write_report(NULL_CHAR*8) # release key

        return True

    def do_key(self, kk):
        """ ex. ENTER """
        self.write_report(self.NULL_CHAR*2+self.keycode[kk]+self.NULL_CHAR*5)
        time.sleep(0.01)
        self.write_report(self.NULL_CHAR*8) # release key

    def do_shortcut(self, line):
        """ ALT TAB """

        cmd = line.split()
        if len(cmd)==3:
            self.write_report(self.keymod[cmd[0]]+self.keymod[cmd[1]]+self.keycode[cmd[2]]+self.NULL_CHAR*5)
        elif len(cmd)==2:
            self.write_report(self.keymod[cmd[0]]+self.NULL_CHAR+self.keycode[cmd[1]]+self.NULL_CHAR*5)
        else:
            print("shortcut ignored")
            return    False

        time.sleep(0.01)
        self.write_report(self.NULL_CHAR*8) # release key

        return True

    @dbus.service.method(DBUS_IFACE)
    def parse_line(self, line, last_cmd=""):
        """ parse rubberducky script's line """

        if ' ' in line:
            # multi cmd
            cmd = line.split(' ', 1)

            if cmd[0].lower() == "string":
                """ string input function """
                self.do_string(cmd[1])

            elif cmd[0].lower() == "rem":
                """ comment """
                return False # no history

            elif cmd[0].lower() == "delay":
                """ delay function convert to time.sleep() """
                time.sleep(int(cmd[1])/100)

            elif cmd[0].lower() == "repeat":
                """ repeat function """
                for i in range(0,int(cmd[1])):
                    self.parse_line(last_cmd)

                return False # no history

            elif cmd[0] in self.keymod:
                """ SHORTCUT """
                self.do_shortcut(line)
        else:
            try:
                ## test ex. DOWN
                self.do_key(line.upper())
            except Exception as E:
                print("error: ")
                print(E)

        return True # save history

    @dbus.service.method(DBUS_IFACE)
    def get_status(self):
        """ Get HID device status """
        return self.HID


    @dbus.service.method(DBUS_IFACE)
    def exec_script(self, script_path):
        """ read rubberducky scripts """

        file = open(script_path)
        ff = file.read().splitlines()

        last_line = ""

        for line in ff:
            self.parse_line(line, last_line)
            last_line = line

        return True


if __name__ == "__main__":
    DBusGMainLoop(set_as_default=True)
    myservice = QuackService()
    loop = GLib.MainLoop()

    loop.run()
