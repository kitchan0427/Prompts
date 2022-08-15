import cv2
import numpy as np

def butterfly_capture(img):

    net = cv2.dnn.readNet('yolov3_for_butterflies.weights', 'yolov3_for_butterflies.cfg')

    height, width, _ = img.shape
    blob = cv2.dnn.blobFromImage(img, 1/255, (416,416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()

    layerOutputs = net.forward(output_layers_names)
    boxes = []

    for detection in layerOutputs[0]:

        confidence = detection[4]

        if confidence > 0.2:

            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            x = int(center_x - w/2)
            y = int(center_y - h/2)

            boxes.append([x, y, w, h])
            
    return boxes