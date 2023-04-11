import mediapipe as mp
import cv2
import handRecognition as hr
import numpy as np
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volrange=volume.GetVolumeRange()
minvol=volrange[0]
maxvol=volrange[1]

#volume.SetMasterVolumeLevel(-20.0, None)



cap = cv2.VideoCapture(0)
detector=hr.handdetector(detectcon=0.7)
wcam=1000
hcam=500

cap.set(3,wcam)
cap.set(4,hcam)
while (True):
    success, img = cap.read()
    detector.findhands(img)
    list=detector.findpos(img,draw=False)
    if(len(list)!=0):
        x1,y1=list[4][1],list[4][2]
        x2,y2=list[8][1],list[8][2]
        cv2.circle(img,(x1,y1),15,(144,255,144),cv2.FILLED)
        cv2.circle(img, (x2,y2), 15, (144, 255, 144), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        x3,y3=((x1+x2)//2),((y1+y2)//2)
        cv2.circle(img,(x3,y3),10,(255,255,0),cv2.FILLED)

        length=math.hypot(x2-x1,y2-y1)
        #-----volume 50,300------------
        vol=np.interp(length,[50,270],[0,100])
        volume.SetMasterVolumeLevelScalar(vol/100, None)

    cv2.imshow("video",img)
    cv2.waitKey(1)