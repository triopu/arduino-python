# Arduino-Python
Connect Arduino with Python
This code will connect your Arduino with your PC using Python.
Arduino will send data (from analogRead) to your computer, and the python code will record time and data that sent by Arduino

1. Python:
- Install Panda: pip install pandas
- Install Python Serial: pip install pyserial
2. Connect Arduino
- Find Connected Port
- Change '/dev/ttyACM1' in 'arduino = serial.Serial('/dev/ttyACM1', 115200)' with corresponding port
