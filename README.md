# Raspberry Pi Fan Manager
This is a project that controls a fan attached to GPIO pin 18 (BCM pin layout) via a transistor circuit. With this you can turn on and off a fan with a shell script. 
There are two circuits you can use:
1. Basic circuit:
  ![basic circuit](https://github.com/scamdotnet/fan-manager/blob/master/fan_manager_basic_circuit.svg)
  This circuit is the most simple version (that is safe for the rasperry pi) with a 5 volt fan (I got mine for a fan case for the raspberry pi) Note: do not use any other fan as it may be bad for your raspberry pi!
2. Full circuit:
  ![full circuit](https://github.com/scamdotnet/fan-manager/blob/master/fan_manager_full_circuit.svg)
  This is the full circuit that has two switches (one sets the control from raspberry pi to manual mode, the other turns on and off the fan in manual mode)
What ever circuit you use, the program should work the same way
