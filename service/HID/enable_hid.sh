#!/bin/bash
mkdir -p /sys/kernel/config/usb_gadget/quack_hid

echo 0x1d6b > /sys/kernel/config/usb_gadget/quack_hid/idVendor # Linux Foundation
echo 0x0104 > /sys/kernel/config/usb_gadget/quack_hid/idProduct # Multifunction Composite Gadget
echo 0x0100 > /sys/kernel/config/usb_gadget/quack_hid/bcdDevice # v1.0.0
echo 0x0200 > /sys/kernel/config/usb_gadget/quack_hid/bcdUSB # USB2
mkdir -p /sys/kernel/config/usb_gadget/quack_hid/strings/0x409
echo "fedcba9876543210" > /sys/kernel/config/usb_gadget/quack_hid/strings/0x409/serialnumber
echo "Quaaack" > /sys/kernel/config/usb_gadget/quack_hid/strings/0x409/manufacturer
echo "Quack USB Device" > /sys/kernel/config/usb_gadget/quack_hid/strings/0x409/product
mkdir -p /sys/kernel/config/usb_gadget/quack_hid/configs/c.1/strings/0x409
echo "Config 1: ECM network" > /sys/kernel/config/usb_gadget/quack_hid/configs/c.1/strings/0x409/configuration
echo 250 > /sys/kernel/config/usb_gadget/quack_hid/configs/c.1/MaxPower

# Add functions here
mkdir -p /sys/kernel/config/usb_gadget/quack_hid/functions/hid.usb0
echo 1 > /sys/kernel/config/usb_gadget/quack_hid/functions/hid.usb0/protocol
echo 1 > /sys/kernel/config/usb_gadget/quack_hid/functions/hid.usb0/subclass
echo 8 > /sys/kernel/config/usb_gadget/quack_hid/functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > /sys/kernel/config/usb_gadget/quack_hid/functions/hid.usb0/report_desc
ln -s /sys/kernel/config/usb_gadget/quack_hid/functions/hid.usb0 /sys/kernel/config/usb_gadget/quack_hid/configs/c.1/
# End functions

ls /sys/class/udc > /sys/kernel/config/usb_gadget/quack_hid/UDC

