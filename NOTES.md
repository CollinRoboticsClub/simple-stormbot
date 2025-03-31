# Notes

XBox Controller
-> Laptop "client_with_controller.py" --WiFi Socket->
    Robot: Raspi "server_with_serial.py" --USB->
        Arduino IR (); Arduino Motors (serial in, motors out)

-> Robot: Raspi mjpeg-streamer --WiFi--> Laptop https://romi.local:8080/?action=stream


# -- TODO CODE ITEMS --
1. Set up STORM network
Field AP:
    SSID: STORMFIELD
    Password: robot2025
    1b. Set the pi up to alternatively connect to Conner/Nat's phone's hotspot or something
2. Create repo and put the scripts up there
3. Add SSH keys for Conner's laptop and perhaps any other device that we'll use as driver station on comp day


# Conner notes:
- SSH in two side-by-side tabs is useful;
    - that way you can have the videostreamer running on the left and the python server on the right

- ~/code/mjpg-streamer/josh.sh -- Read this
- python3 ~/code/socket-controller/server_with_serial.py # This will run the server!

