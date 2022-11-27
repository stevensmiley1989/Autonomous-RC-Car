import cv2
import numpy as np
import requests
import urllib
import singleinference_yolov7
from singleinference_yolov7 import SingleInference_YOLOV7
from threading import Thread
from multiprocessing import Process, Queue
import time
class VC:
    '''
    Created by Steven Smiley on 11/27/2022
    
    This class runs OpenCV on an incoming html video feed from an IP Camera.
    
    It expects a url_path like 'http://10.5.1.236:8080/video'
    '''
    def __init__(self,url):
        self.url=url
        self.frame=None
        self.show_video=False
    def run(self):
        self.thread=Thread(target=self.run_cam)
        self.thread.setDaemon(True)
        self.thread.start()
    def run_cam(self):
        self.vid=cv2.VideoCapture(self.url)
        while True:
            try:
                new_frame,self.frame=self.vid.read()
                if new_frame:
                    if self.show_video:
                        cv2.imshow('IPWebcam',self.frame)
                else:
                    pass
            except:
                self.vid=cv2.VideoCapture(self.url)
            if self.show_video:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    

def main(queue=None,img_size=640,path_yolov7_weights="weights/best.pt",url_path='http://10.5.1.236:8080/video'):
    #INPUTS
    path_img_i=None

    #INITIALIZE THE app
    app=SingleInference_YOLOV7(img_size,path_yolov7_weights,path_img_i,device_i='0',conf_thres=0.55,iou_thres=0.5)
    #APP SWAP NAMES
    replace_dic={"person":"Steven"}
    app.replace_dic=replace_dic
    #LOAD & INFERENCE
    app.load_model() #Load the yolov7 model

    #INITIALIZE The webcamera
    url=url_path
    myvideo=VC(url)
    myvideo.run()
    while True:
        try:
            if type(myvideo.frame)!=type(None):
                cv2matrix_i=myvideo.frame
                app.load_cv2mat(cv2matrix_i) #load the OpenCV matrix, note could directly feed a cv2matrix here as app.load_cv2mat(cv2matrix)
                app.inference() #make single inference
                cv2.imshow('OUTPUT',app.image)
                cv2.waitKey(1)
                if type(queue)!=type(None):
                    # print(f'''
                    # app.predicted_bboxes_PascalVOC\n
                    # \t name,x0,y0,x1,y1,score,image.shape[0],image.shape[1]\n
                    # {app.predicted_bboxes_PascalVOC}''')
                    while queue.qsize()>2:
                        try:
                            queue.get(False)
                        except:
                            pass
                        #print('queue.qsize()',queue.qsize())
                    queue.put(app.predicted_bboxes_PascalVOC)



        except:
                del myvideo.thread
                cv2.destroyAllWindows()
                myvideo=VC(url)
                myvideo.run()
    cv2.destroyAllWindows()
if __name__=='__main__':  
    queue=Queue()
    img_size=640
    p1=Process(target=main,args=(queue,img_size,))
    p1.start()



