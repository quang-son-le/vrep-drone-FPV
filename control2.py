

import vrep


import time
import keyboard 
import numpy as np
import math
a = np.zeros(3, dtype = float)
rot = np.zeros(3, dtype = float)
print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19998,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')

    # Now try to retrieve data in a blocking fashion (i.e. a service call):
    res,objs=vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_blocking)
    
    if res==vrep.simx_return_ok:
        print ('Number of objects in the scene: ',len(objs))
    else:
        print ('Remote API function call returned with error code: ',res)

    time.sleep(2)
    number,objecthandle=vrep.simxGetObjectHandle(clientID,'Quadricopter_target', vrep.simx_opmode_blocking)
    while( a[0]==0 and a[1]==0 and a[2]==0):
     es,a=vrep.simxGetObjectPosition(clientID,objecthandle,-1,vrep.simx_opmode_oneshot)
    es,rot=vrep.simxGetObjectOrientation(clientID,objecthandle,-1,vrep.simx_opmode_oneshot)
    print(rot)
    # Now retrieve streaming data (i.e. in a non-blocking fashion):
    startTime=time.time()
    #vrep.simxGetIntegerParameter(clientID,vrep.sim_intparam_mouse_x,vrep.simx_opmode_streaming) # Initialize streaming
    while True:
       # used try so that if user pressed other than the given key error will not be shown
       
      if keyboard.is_pressed("8"): 
       print('cos')
       print(math.cos(rot[2]))
       a[1]+=0.003*math.cos(rot[2])
       a[0]+=0.003*math.sin(rot[2])
       vrep.simxSetObjectPosition(clientID,objecthandle,-1,a,vrep.simx_opmode_oneshot)
       print(a)
      if keyboard.is_pressed("2"): 
       
       a[1]-=0.001*math.cos(rot[2])
       a[0]-=0.001*math.sin(rot[2])  
       vrep.simxSetObjectPosition(clientID,objecthandle,-1,a,vrep.simx_opmode_oneshot)
       print(a)
      if keyboard.is_pressed("4"): 
       a[0]-=0.001*math.cos(rot[2])
       a[1]-=0.001*math.sin(rot[2])    
       vrep.simxSetObjectPosition(clientID,objecthandle,-1,a,vrep.simx_opmode_oneshot)
       print(a)
      if keyboard.is_pressed("6"): 
       a[0]+=0.001*math.cos(rot[2])
       a[1]+=0.001*math.sin(rot[2]) 
       vrep.simxSetObjectPosition(clientID,objecthandle,-1,a,vrep.simx_opmode_oneshot)
       print(a)
      if keyboard.is_pressed("home"): 
       
       a[2]+=0.0006  
       vrep.simxSetObjectPosition(clientID,objecthandle,-1,a,vrep.simx_opmode_oneshot)
      if keyboard.is_pressed("end"): 
       
       a[2]-=0.0006 
       vrep.simxSetObjectPosition(clientID,objecthandle,-1,a,vrep.simx_opmode_oneshot)
      if keyboard.is_pressed("page up"): 
       rot[2]+=0.0004
       
       vrep.simxSetObjectOrientation(clientID,objecthandle,-1,rot,vrep.simx_opmode_oneshot)
      if keyboard.is_pressed("page down"): 
       rot[2]-=0.0004
       
       vrep.simxSetObjectOrientation(clientID,objecthandle,-1,rot,vrep.simx_opmode_oneshot)
       
      if keyboard.is_pressed('q'): 
       break;
     
          #break  # if user pressed a key other than the given key the loop will break

    
    vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!',vrep.simx_opmode_oneshot)
    vrep.simxGetPingTime(clientID)
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
