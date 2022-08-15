import cv2
import sys


import find_bounding_box


def renew_bounding_box(frame):
   
    detections = find_bounding_box.butterfly_capture(frame)
    tracker_list = []

    for a_bounding_box in detections:
        tracker = cv2.TrackerKCF_create()
        ok = tracker.init(frame, a_bounding_box)
        tracker_list.append(tracker)

    return tracker_list
    
if __name__ == '__main__' :
    video = cv2.VideoCapture("butterfly.mp4")

    if not video.isOpened():
        print("Could not open the video")
        sys.exit()

    ok, frame = video.read()
    if not ok:
        print('Cannot read the video file')
        sys.exit()


    frameTime = 1
    ret, frame1 = video.read()
    
    detections = find_bounding_box.butterfly_capture(frame1)

   
    tracker_list = []

    for a_bounding_box in detections:
        tracker = cv2.TrackerKCF_create()
        ok = tracker.init(frame, a_bounding_box)
        tracker_list.append(tracker)


    starting_time = cv2.getTickCount()

    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break

        timer = cv2.getTickCount()

        # Ideally, it will count how many seconds the video is playing. but 
        # the object detection model is too slow, so this "seconds" is long than the actual time

        seconds = round((timer - starting_time)/ cv2.getTickFrequency())
        
        #renew bounging box for each 5 seconds
        if seconds%5==0:
            tracker_list = renew_bounding_box(frame)

        num = 0
        for tracker in tracker_list:
            
            ok, bbox = tracker.update(frame)

            
            if ok:
                num+=1
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
           
                cv2.putText(frame,str(num), (p1[0],p1[1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,255,255),2)

                # if the bufferfly is in the boundary of a frame,it has a change(not a must) that it is frame in or out
                if p1[0]<5 or p1[0]>715 or p1[1]<5 or p1[1]>1275:
                    cv2.rectangle(frame,p1, p2, (50,170,50), 2, 1)

            else:
                cv2.putText(frame,'Lost tracking at: ' +str(seconds)+'senconds.', (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,255,255),2)
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
               
            

        if num>1:
            cv2.putText(frame,'There are ' +str(num)+ ' butterflies.', (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0),2)
        else:
            cv2.putText(frame,'There is ' +str(num)+ ' butterfly.', (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0),2)
     
        cv2.imshow('result',frame)

        # Exit if ESC pressed
        k = cv2.waitKey(frameTime) & 0xff
        if k == 27 : break