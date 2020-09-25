# electronic-symbol-detection-from-handwritten-circuit
It’s a simple image processing project using OpenCV and vision basic knowledge to detect electrical elements in a picture of handwritten circuit.

**preproccessing of the image and becoming ready for changes(we use the array of the  image)**
```
image = cv2.imread('MidtermSamples/im3.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
arr = numpy.array(img)
```

**our samples got some noises and in case of using them for detection firt level is to get rid of noises.** 
we can use filters that we've learned such as median gaussian box filter or any other filter.
Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. It actually removes high frequency content 
median_filter:computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value.
gaussian_filter:Gaussian filtering is highly effective in removing Gaussian noise from the image.
```
# # # pahse 1:(A)
removed_A_noise = median_filter(arr, 3)
```
```
# # # pahse 1:(B)
removed_B_noise = gaussian_filter(removed_A_noise, 3)
```

**there are some other problems such as rotation of the image that we don like to see in our results.**
we can predict the angle and then rotate the image(after filtering)
we find edges in an image using the [Canny86] algorithm.
The function finds edges in the input image and marks them in the output map edges using the Canny algorithm.
The smallest value between threshold1 and threshold2 is used for edge linking.
The largest value is used to find initial segments of strong edges
Parameters:	
    image – single-channel 8-bit input image.
    edges – output edge map; it has the same size and type as image .
    threshold1 – first threshold for the hysteresis procedure.
    threshold2 – second threshold for the hysteresis procedure.
    apertureSize – aperture size for the Sobel() operator.
```
# # # pahse 2:
rotated_img = auto_rotate(removed_B_noise)
```

**and at the end image is ready to be used for detecting electronic symbols from handwriting circuit.**
we saw that corners are regions in the image with large variation in intensity in all the directions.
we use openCV function to detect corners(cv2.cornerHarris())Its arguments are :
        img - Input image, it should be grayscale and float32 type.
        blockSize - It is the size of neighbourhood considered for corner detection
        ksize - Aperture parameter of Sobel derivative used.
        k - Harris detector free parameter in the equation.

```
# # # pahse 3:
clr_img = cv2.cvtColor(rotated_img, cv2.COLOR_GRAY2BGR)
result = circuit_detection(clr_img)
```
```
cv2.imwrite('result.jpg', result)
```
