This repo contains microROS dev environments, GPIO hardware controls, and programming scripts used by the BYU FRoSt lab's **Cooperative Underwater Group of Autonomous Robots (CoUGARs)**. 
If you're doing code development, feel free to clone this repo directly, make a new branch, and start coding and pushing some changes.
Otherwise (if you're looking to set up a new Coug-UV from scratch), see this repo for instructions on how to get our custom Docker image running instead: https://github.com/snelsondurrant/CougarsSetup

A quick high-level overview of the repo:
- **control/** - PlatformIO dev environment for the control Teensy (runs low-level controller).
Source code and header files are included in "control/src/" and "control/include/", and dependencies can be imported by modifying the "control/platformio.ini" file.
Different sensors can be enabled/disabled by commenting out the #define statements at the top of "control/src/main.cpp" and rebuilding.
- **gpio/** - python scripts for GPIO hardware control.
We'd recommend not running these scripts directly; instead, use the bash scripts in the top-level directory.
- **sensors/** - PlatformIO dev environment for the sensors Teensy.
Source code and header files are included in "sensors/src/" and "sensors/include/", and dependencies can be imported by modifying the "sensors/platformio.ini" file.
Different sensors can be enabled/disabled by commenting out the #define statements at the top of "sensors/src/main.cpp" and rebuilding.
- **scripts (build_control.sh, upload_control.sh, etc)** - automates helpful software tasks on the AUV.
For example, running "bash msg_update.sh" will remove the microROS library from both workspaces and rebuilds them using updated message and service declarations from frost_interfaces.
A description of what each script does is included as a header comment in the file.
A quick note: our custom Docker image runs "init.sh" automatically on startup, and running it manually may mess up the Teensy power states (requiring a reboot).
So probably don't do that.
