from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *
import numpy as np
# To open a single webcam (0) ,To open multiple webcams (1)
# cap = cv2.VideoCapture(0) # For webcam

# setting width of the image by webcam,width has prop id no 3
# cap.set(3, 1280)
# cap.set(3, 640)
# setting height of the image by webcam,height has prop id no 3
# cap.set(4, 720)
# cap.set(4, 480)

# For video inputs
cap = cv2.VideoCapture("../Videos/Traffic Clip.mp4") # For videos

# Creating Model with predefined datasets of YOLO
model = YOLO("../YOLO_Weights/yolov8n.pt")

# To find out the class

classNames = ["person", "bicycle", "car", "motorbike", "bus", "train", "truck",
              "traffic light"
              ]

# To read the image


# Tracking : In first frame car having id 1 should also have id 1 in next frames
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

# limits to create a line upon passing that line cnt++
limitsIn1 = [0, 800, 850, 800]
limitsOut1 = [1100, 800, 1920, 800]
limitsIn2 = [700, 500, 850, 500]
limitsOut2 = [1000, 500, 1300, 500]
# totalCount is a list which is storing the vehicle id's which are already counted
totalCountIn1 = []
totalCountOut1 = []
totalCountIn2 = []
totalCountOut2 = []
while True:
    success, img = cap.read()
    # imgRegion = cv2.bitwise_and(img, img, mask=mask)
    #result = model(imgRegion, stream=True)

    result = model(img, stream=True)

    imgGraphics = cv2.imread("graphics-2.png", cv2.IMREAD_UNCHANGED)

    img = cvzone.overlayPNG(img, imgGraphics, (0, 0))
    img = cvzone.overlayPNG(img, imgGraphics, (640, 0))
    detections = np.empty((0, 5))


    # loop through each result and implement bounding boxes with x1,y1,x2,y2 coordinates
    for r in result:
        boxes = r.boxes
        for box in boxes:
            # Using openCV
            # x1, y1, x2, y2 = box.xyxy[0]
            # x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # print(x1, y1, x2, y2)
            # # img, point1, point2, color, thickness
            # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Using cvzone library for bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            # print(x1, y1, w, h)


            # conf = box.conf[0] decimal places
            # rounding up the confidence level to 2 decimal places
            conf = math.ceil((box.conf[0]*100))/100
            # print(conf)
            # setting the conf box so that it won't go out of the screen as object moves
            # cvzone.putTextRect(img,f'{conf:.2f}', (max(0, x1), max(35, y1)))
            # Class name
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            if currentClass == "bicycle" or currentClass == "car"\
                    or currentClass == "motorbike" or currentClass == "truck" or currentClass == "bus" and conf > 0.3:
                # cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                #                    scale=1, thickness=1, offset=3)
                # for corner rectangle(Which signifies the detection of object by YOLO)around specified objects mentioned in if condition
                # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultTracker = tracker.update(detections)
    cv2.line(img, (limitsIn1[0], limitsIn1[1]), (limitsIn1[2], limitsIn1[3]), (0, 0, 255), 3)
    cv2.line(img, (limitsOut1[0], limitsOut1[1]), (limitsOut1[2], limitsOut1[3]), (0, 0, 255), 3)
    cv2.line(img, (limitsIn2[0], limitsIn2[1]), (limitsIn2[2], limitsIn2[3]), (0, 0, 255), 3)
    cv2.line(img, (limitsOut2[0], limitsOut2[1]), (limitsOut2[2], limitsOut2[3]), (0, 0, 255), 3)

    for result in resultTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        # Corner rectangle for detection done by the tracker
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 0))
        cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)),
                           scale=2, thickness=3, offset=10)
        cx, cy = x1+w//2, y1+h//2
        cv2.circle(img, (int(cx), int(cy)), 5, (255, 0, 0), cv2.FILLED)

        # if (cx,cy) have crossed the line then update count
        if limitsIn1[0] < cx < limitsIn1[2] and limitsIn1[1]-30 < cy < limitsIn1[1]+30:
            if totalCountIn1.count(id) == 0:
                totalCountIn1.append(id)
                cv2.line(img, (limitsIn1[0], limitsIn1[1]), (limitsIn1[2], limitsIn1[3]), (0, 255, 0), 3)

        if limitsOut1[0] < cx < limitsOut1[2] and limitsOut1[1]-30 < cy < limitsOut1[1]+30:
            if totalCountOut1.count(id) == 0:
                totalCountOut1.append(id)
                cv2.line(img, (limitsOut1[0], limitsOut1[1]), (limitsOut1[2], limitsOut1[3]), (0, 255, 0), 3)

        if limitsIn2[0] < cx < limitsIn2[2] and limitsIn2[1]-25 < cy < limitsIn2[1]+25:
            if totalCountIn2.count(id) == 0:
                totalCountIn2.append(id)
                cv2.line(img, (limitsIn2[0], limitsIn2[1]), (limitsIn2[2], limitsIn2[3]), (0, 255, 0), 3)

        if limitsOut2[0] < cx < limitsOut2[2] and limitsOut2[1]-25 < cy < limitsOut2[1]+25:
            if totalCountOut2.count(id) == 0:
                totalCountOut2.append(id)
                cv2.line(img, (limitsOut2[0], limitsOut2[1]), (limitsOut2[2], limitsOut2[3]), (0, 255, 0), 3)
    # cvzone.putTextRect(img, f' Count: {len(totalCountIn)}', (50, 50))
    # cvzone.putTextRect(img, f' Count: {len(totalCountOut)}', (50, 50))

    cv2.putText(img, str(len(totalCountIn1)), (200, 80), cv2.FONT_HERSHEY_PLAIN, 5, (139,195,75), 8)
    cv2.putText(img, str(len(totalCountOut1)), (450, 80), cv2.FONT_HERSHEY_PLAIN, 5, (50,50,230), 8)
    cv2.putText(img, str(len(totalCountIn2)), (840, 80), cv2.FONT_HERSHEY_PLAIN, 5, (139,195,75), 8)
    cv2.putText(img, str(len(totalCountOut2)), (1090, 80), cv2.FONT_HERSHEY_PLAIN, 5, (50,50,230), 8)
    totalCount1 = totalCountIn1 + totalCountOut1
    totalCount2 = totalCountIn2 + totalCountOut2
    # cv2.putText(img, str(len(totalCount)), (450, 80), cv2.FONT_HERSHEY_PLAIN, 5, (50,50,230), 8)
    # cvzone.putTextRect(img, f' Count: {len(totalCount1)}', (1200, 80))
    # cvzone.putTextRect(img, f' Count: {len(totalCount2)}', (1200, 200))

    diff = abs(len(totalCountOut2) - len(totalCountOut1))
    cvzone.putTextRect(img, f' Count: {diff}', (1200, 200))

    # to show the image with a delay of 1ms
    cv2.imshow('Image', img)
    #  cv2.imshow('ImageRegion', imgRegion)
    # cv2.waitKey(0) # Press again and again any key to play
    cv2.waitKey(1) # Automatically plays the video