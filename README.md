# comice-control-center
A simply control center to monitor connections such as WiFi, Bluetooth, etc. The brightness level of the Monitor and sound volume.

It is being developed for **comiceOS**.

## Screenshot
![Screenshot](https://raw.githubusercontent.com/libredeb/comice-control-center/main/screenshots/screenshot.png)


## Compilation

1. Install build dependencies:

* For Ubuntu:
    ```bash
    $ sudo apt-get install python3 python3-pip python3-dbus dbus util-linux gsettings-desktop-schemas wireless-tools iw iproute2 alsa-utils pulseaudio-utils
    ```

* For Fedora:
    ```bash
    $ sudo dnf install python3 python3-dbus dbus util-linux gsettings-desktop-schemas wireless-tools iproute alsa-utils pulseaudio-utils
    ```

2. Install python3 (pip) dependencies:
    ```bash
    $ sudo pip3 install -r requirements.txt
    ```

3. Run `comice-control-center` standalone:
    ```bash
    $ ./comice-control-center
    ```

    > **NOTE:** if you are in a `Wayland` session, you will need to specify the X11 compatibility with by adding the environment variable `GDK_BACKEND=x11` at the begging of the run command for the application to work properly.
    > For example:
    > ```bash
    > $ GDK_BACKEND=x11 ./comice-control-center
    > ```

## Changelog
**Version 0.0.1**
* First version
* Implemented widgets for connections, sound volume and monitor brightness
* Reusable functions

