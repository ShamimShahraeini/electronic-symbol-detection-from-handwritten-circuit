import cv2
import numpy
from phase1 import *
from phase2 import *
from phase3 import *

image = cv2.imread('MidtermSamples/im3.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
arr = numpy.array(img)
# print(type(arr))
# print(np.shape(arr))
# print(arr.dtype)

############################################################
# # # pahse 1:(A)
removed_A_noise = median_filter(arr, 3)
# print(type(removed_A_noise))
# print(np.shape(removed_A_noise))
# print(removed_A_noise.dtype)
# # # pahse 1:(B)

removed_B_noise = gaussian_filter(removed_A_noise, 3)
# print(np.shape(removed_B_noise))
# # # pahse 1:(C)
# removed_C_noise = box_filter(removed_B_noise, 5)

############################################################
# # # pahse 2:
rotated_img = auto_rotate(removed_B_noise)
# print(numpy.shape(rotated_img))

############################################################
# # # pahse 3:
clr_img = cv2.cvtColor(rotated_img, cv2.COLOR_GRAY2BGR)
result = circuit_detection(clr_img)
# print(numpy.shape(result))

############################################################

cv2.imwrite('result.jpg', result)