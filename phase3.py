import cv2
import numpy

def circuit_detection(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,th1 = cv2.threshold(gray,80,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    dst = cv2.cornerHarris(th1,3,3,0.06)
    dst = cv2.dilate(dst,None)
    data_final = element_detection(th1, dst)
    
    return data_final


def element_detection(th1, dst):
    data_final = numpy.zeros((len(th1),len(th1[0]), 3), dtype="uint8")
    for i in range(len(th1)):
        for j in range(len(th1[0])):
            # print(th1[i][j])
            if th1[i][j] == 255:
                data_final[i][j] = [255,255,255]

    data_final[dst>0.01*dst.max()] = [0,0,255]
    return data_final