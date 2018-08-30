#Example OpenBMC REST API consumption script
#Import the openbmc Login class from openbmc.py to enable support for getting sensor data and host manipulation via BMC

import openbmc    # Import openbmc class structure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

username='root'
password='0penBmc'
box3=  openbmc.Login('10.127.91.7',username,password)
box3._login()
box3._enumerate()


print box3._gettemp('ambient_mb')
print box3._gettemp('p1_core0_temp')
print box3._gettemp('p0_core0_temp')
print box3._getspeed('fan0')
print box3._getspeed('fan1')
print box3._getspeed('fan2')
print box3._getspeed('fan3')
print box3._getspeed('fan4')
print box3._getspeed('fan5')



plt.axis([0, 100, 0, 100])
for i in range(100):
    plt.scatter(i, box3._gettemp('ambient_mb')/1000, c='red' , label='Ambient temperature')
    plt.scatter(i, box3._gettemp('p0_core0_temp')/1000, c='blue' ,label = 'CPU0 Temperature')
    plt.scatter(i, box3._gettemp('p1_core0_temp')/1000, c='black' ,label = 'CPU1 Temperature')
    plt.scatter(i, box3._getspeed('fan0'), c='green' ,label= 'Fan Speed')
    plt.scatter(i, box3._gettemp('dimm0_temp')/1000, c='cyan' , label='DIMM temperature')
    plt.scatter(i, box3._gettemp('dimm31_temp')/1000, c='magenta' , label='DIMM temperature')
    plt.scatter(i, box3._gettemp('dimm0_temp')/1000, c='cyan' , label='DIMM temperature')
    plt.scatter(i, box3._gettemp('dimm31_temp')/1000, c='cyan' , label='DIMM temperature')
    plt.pause(0.05)
plt.show()
