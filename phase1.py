import cv2
import numpy

def median_filter(img, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(img),len(img[0])), dtype="uint8")
    for i in range(len(img)):

        for j in range(len(img[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(img) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(img[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(img[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def gaussian_filter(img, filter_size):

    sigma=1
    shape=(filter_size,filter_size)
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = numpy.ogrid[-m:m+1,-n:n+1]
    kernel = numpy.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    kernel[ kernel < numpy.finfo(kernel.dtype).eps*kernel.max() ] = 0
    sumh = kernel.sum()
    if sumh != 0:
        kernel /= sumh
    data_final = cv2.filter2D(img,-1,kernel)
    return data_final


# def box_filter(img ,filterSize):
#     loc = filterSize/2
#     finalImg = numpy.ones((img.shape[0], img.shape[1]), dtype = "uint8")
#     for y in range(img.shape[0]):
#         for x in range( img.shape[1]):
            

#     return finalImg