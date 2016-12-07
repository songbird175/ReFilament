
# coding: utf-8

# In[ ]:

import serial
import time


# In[ ]:

ser = serial.Serial('/dev/ttyACM0', 9600)


# In[ ]:

def bitsToNumberList(msg):
    msg = msg.rstrip(b'\r\n')
    msg = msg.rsplit(b',')

    return_numbers = []

    for number in msg:
        try:
            return_numbers.append(int(number))
        except:
            return_numbers.append(float(number))
            
    return return_numbers


# In[ ]:

desiredTemp = 200
desiredSpeed = int(.33 * 256)
onOff = 0
P = 10
I = int(.05 * 256)


# In[ ]:

while True:
    # Serial write section
    print ("Python value sent: ")
    print ([desiredTemp, desiredSpeed, onOff, P, I])
    ser.write(bytearray([desiredTemp, desiredSpeed, onOff, P, I]))

    # Serial read section
    msg = ser.readline() # read everything in the input buffer
    print ("Message from arduino: ")
    print (bitsToNumberList(msg))


# In[ ]:

ser.close()
ser.is_open


# In[ ]:



