# IBB Arena setup


## Hardware
### parts list
* Raspberry pi 4
* 48v DC PSU
* Arduino nano/every
* 3 way relay (any high amp 12v relay will work, all spinners hooked into this)
* Relay control board
* 48v Relay
* Wago connectors (optional but useful for neatness)
* Alifa Wifi Card

### Wiring diagram
TODO
## Software
The arena software is made up of three parts,
* API
* WebUI
* Access point
all setup and installation is handled by the setup.sh file this must be ran as root 

```
sudo chmod +X setup.sh
sudo ./setup.sh
```

this install has been test on a raspberry pi 4 running the miniamal raspian OS, insure python is installed, this is not done in the script to avoid other versions being installed which will cause issues 

the setup script can be ran many times without issue, this is also how you update the code.

when installed there will be two services setup on the pi you can check there status by running 

```
sudo systemctl status arenaapi
sudo systemctl status arenaweb
```

Files for both will be stored in 
```
/var/www/html/
```
Logs can be found at 
```
/var/log/
```