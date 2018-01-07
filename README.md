# Raspberry Pi Alarm Clock
This project takes a Raspberry Pi and, web-enabling it, turns it into an alarm
clock. The Pi controls a daylight lamp connected to a [Revolt PX-1672](http://www.revolt-power.de/USB-Dongle-PX-1674-919.shtml) RC plug.

The alarm is configured through a web interface, and has been optimized for
both desktop and mobile. Instructions for building it below!

![Web](https://i.imgur.com/l2SCImB.jpg)
<img alt="Mobile1" src="https://i.imgur.com/55pL5aV.png" width=250 />
<img alt="Mobile2" src="https://i.imgur.com/PpwkZcm.png" width=250 />
<img alt="Mobile3" src="https://i.imgur.com/yriXSCj.png" width=250 />

Much thanks to [ajpierce](https://github.com/ajpierce/) for his original work, which i effortless forked and edited to suit my needs. 

## Install Prerequisites
Install `git` and `screen` so we can check out the code and run it in the
background.
```
sudo apt-get update
sudo apt-get install git screen
```

Next, install virtualenv for python by following the Initial Setup section of
[this guide](http://raspberry.io/wiki/how-to-get-python-on-your-raspberrypi/).

## Install Alarm Software
First, become root. Then, navigate to the directory in which the code will
live, and create a virtual environment:
```
sudo su -
cd /opt
virtuanenv pi_alarm_env
cd pi_alarm_env
```
Next, check out the project from git, and install the python libraries:
```
git clone https://github.com/ajpierce/pi_alarm.git
./pi_alarm/script/setup.sh
```

## Fire up the software!
As root,
```
cd /opt/pi_alarm_env/pi_alarm
./run.py
```

If all goes well, you the Flask webserver should let you know that the
application is running on `0.0.0.0:99`.

Navigate to the IP address Port 99 of your Raspberry Pi from a browser on another
computer (or your mobile phone). 


## Configure the server to run on boot
To ensure the alarm starts on boot, follow the guide [here](http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html),
but your script will be the simple one outlined below:

```
#!/bin/bash
screen -S alarm python /opt/pi_alarm_env/pi_alarm/run.py
```

This starts a new screen (with the name "alarm" and invokes python to start
the alarm clock server.
