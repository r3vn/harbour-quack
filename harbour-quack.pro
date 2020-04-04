# NOTICE:
#
# Application name defined in TARGET has a corresponding QML filename.
# If name defined in TARGET is changed, the following needs to be done
# to match new name:
#   - corresponding QML filename must be changed
#   - desktop icon filename must be changed
#   - desktop filename must be changed
#   - icon definition filename in desktop file must be changed
#   - translation filenames have to be changed

# The name of your application
TARGET = harbour-quack

CONFIG += sailfishapp

SOURCES += src/harbour-quack.cpp

service-dir.path = /usr/share/harbour-quack/service
service-dir.files = service/*.py

service-hid.path = /usr/share/harbour-quack/service/HID
service-hid.files = service/HID/*.sh

service-layouts.path = /usr/share/harbour-quack/service/layouts
service-layouts.files = service/layouts/*.py

systemd-dbus.path = /usr/share/dbus-1/system-services
systemd-dbus.files = systemd/com.quack.hid.service

systemd-config.path = /etc/dbus-1/system.d
systemd-config.files = systemd/com.quack.hid.conf

systemd-main.path = /etc/systemd/system
systemd-main.files = systemd/quackHID.service

INSTALLS += service-dir \
    service-layouts \
    service-hid \
    systemd-dbus \
    systemd-config \
    systemd-main

DISTFILES += qml/harbour-quack.qml \
    qml/cover/CoverPage.qml \
    qml/pages/FirstPage.qml \
    rpm/harbour-quack.changes.in \
    rpm/harbour-quack.changes.run.in \
    rpm/harbour-quack.spec \
    rpm/harbour-quack.yaml \
    translations/*.ts \
    harbour-quack.desktop

SAILFISHAPP_ICONS = 86x86 108x108 128x128 172x172

# to disable building translations every time, comment out the
# following CONFIG line
CONFIG += sailfishapp_i18n

# German translation is enabled as an example. If you aren't
# planning to localize your app, remember to comment out the
# following TRANSLATIONS line. And also do not forget to
# modify the localized app name in the the .desktop file.
TRANSLATIONS += translations/harbour-quack-de.ts
