
import mediapipe as mp
import cv2


class handdetector():
    def __init__(self,mode=False, maxhands=2,complex=1,detectcon=0.5,trackcon=0.5):
        self.mode=mode
        self.maxhands =maxhands
        self.complex= complex
        self.detectcon = detectcon
        self.trackcon = trackcon


        self.mphands=mp.solutions.hands
        self.hands=self.mphands.Hands( self.mode, self.maxhands,self.complex,self.detectcon ,self.trackcon)
        self.mpDraw=mp.solutions.drawing_utils

    def findhands(self,img,draw=True):

        IMGrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(IMGrgb)

        if (self.results.multi_hand_landmarks):
            for hlm in self.results.multi_hand_landmarks:
                if(draw):
                    self.mpDraw.draw_landmarks(img,hlm,self.mphands.HAND_CONNECTIONS)
        return img

    def findpos(self,img,handno=0,draw=True):
        listlm=[]
        if (self.results.multi_hand_landmarks):
            myh=self.results.multi_hand_landmarks[handno]

            for id , lm in enumerate(myh.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                listlm.append([id,cx,cy])
                if(draw):
                    cv2.circle(img, (cx, cy), 10, (144, 238, 144), cv2.FILLED)
        return listlm
    def findlen(self):
        #-------------finding length between two points-----------------
        pass

def main():
   pass

if __name__ =='__main__':
    main()