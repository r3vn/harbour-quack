import QtQuick 2.0
import Sailfish.Silica 1.0
import Sailfish.Pickers 1.0
import Nemo.DBus 2.0

Page {
    id: page

    property string selectedFile

    function get_device_status(){
        daemon.call("get_status",[], function (result) {
            // Get HID device status from dbus
            console.log(result)
            return result
        })
    }

    Component.onCompleted: {
        console.log(get_device_status())
        if (get_device_status()){
            // HID device enabled
            console.log("ok true")
            hid_enabler.text = qsTr("Disable HID device (bugged)")
            kb_layout_box.enabled = true
            pickerBox.enabled =  true

        } else {
            hid_enabler.text = qsTr("Enable HID device")
            kb_layout_box.enabled = false
            pickerBox.enabled =  false
        }
    }

    // The effective value will be restricted by ApplicationWindow.allowedOrientations
    allowedOrientations: Orientation.All

    // To enable PullDownMenu, place our content in a SilicaFlickable
    SilicaFlickable {
        anchors.fill: parent
        contentHeight: column.height

        PullDownMenu {
            MenuItem {
                id: hid_enabler
                onClicked: {
                    if (get_device_status()){
                        // HID device enabled
                        daemon.call("enable_hid",[], function (result) {
                            if (result){
                                this.text = qsTr("Disable HID device (bugged)")
                                kb_layout_box.enabled = !kb_layout_box.enabled
                                pickerBox.enabled = !pickerBox.enabled
                            }
                        })

                    } else {
                        // HID device disabled
                        daemon.call("enable_hid",[], function (result) {
                            if (result){
                                this.text = qsTr("Enable HID device")
                                kb_layout_box.enabled = !kb_layout_box.enabled
                                pickerBox.enabled = !pickerBox.enabled
                            }
                        })
                    }
                }
            }
        }

        Component {
            id: filePickerPage
            FilePickerPage {
                nameFilters: [ '*.txt', '*.quack', '*.duck' ]
                onSelectedContentPropertiesChanged: {
                    page.selectedFile = selectedContentProperties.filePath
                    quackButton.enabled = true
                }
            }
        }

        Column {
            id: column

            width: page.width
            spacing: Theme.paddingLarge

            PageHeader {
                title: qsTr("Duckyscripts")
            }

            ValueButton {
                id: pickerBox
                label: "Script"
                value: selectedFile ? selectedFile : "None"
                onClicked: pageStack.push(filePickerPage)
            }

            ComboBox {
                id: kb_layout_box
                width: parent.width
                label: qsTr("Keyboard layout")

                menu: ContextMenu {
                    MenuItem { text: "us" }
                    MenuItem { text: "it" }
                }
            }

            ButtonLayout{
                Button {
                    //anchors.horizontalCenter: parent.horizontalCenter
                    id: quackButton
                    enabled: false
                    text: qsTr("Quaack!")
                    onClicked: daemon.call("exec_script",[page.selectedFile], function (result) {})
                }
            }
        }
    }

    Item {
        DBusInterface {
            id: daemon

            bus: DBus.SystemBus
            service: 'com.quack.hid'
            iface: 'com.quack.hid'
            path: '/com/quack/hid'
        }
    }
}
