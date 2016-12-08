
# coding: utf-8

# In[1]:

import serial
import time


# In[2]:

ser = serial.Serial('/dev/ttyACM1', 9600) #my particular arduino doesn't like other baud rates


# In[3]:

def getSerialData():
    msg = msg.rstrip(b'\r\n')
    msg = msg.rsplit(b',')
    
    if len(msg) == 2:
        return_numbers = []

        for number in msg:
            try:
                return_numbers.append(int(number))
            except:
                return_numbers.append(float(number))

        return return_numbers
    else:
        return [2,2] #error message which indicates that python recieved a wrong len msg


# In[4]:

heaterOn=1
motorOn=1


# In[5]:

while True:
    # Serial write section
#     print ("Python value sent: ")
#     print ([heaterOn, motorOn])
    ser.write(bytearray([heaterOn, motorOn]))

    # Serial read section
    try:
        msg = ser.readline() # read everything in the input buffer
        parsedData = bitsToNumberList(msg)

#         print ("Parsed Data: {}".format(parsedData))
    except:
        pass


# In[6]:

print(ser.is_open)
ser.close()
print(ser.is_open)


# In[ ]:



