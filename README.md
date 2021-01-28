# comice-control-center
A simply control center to monitor connections such as WiFi, Bluetooth, etc. And Monitor brightness level and sound volume.

It is being developed for **comiceOS**.

## Screenshot
![Screenshot](https://raw.githubusercontent.com/libredeb/comice-control-center/main/screenshots/screenshot.png)


## Compilation

1. Install build dependencies:
```bash
sudo dnf install python3 python3-dbus util-linux gsettings-desktop-schemas wireless-tools iproute alsa-utils
```
2. Install python3 (pip) dependencies:
```bash
sudo pip3 install -r requirements.txt
```
3. Run `comice-control-center` standalone:
```bash
./comice-control-center
```

## Changelog
**Version 0.0.1**
* First version
* Implemented widgets for connections, sound volume and monitor brightness
* Reusable functions

