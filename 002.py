import cv2
import numpy as np

def keep_edge(image):
    np.set_printoptions(threshold=np.inf)#以防数组元素过多，输出省略号

    #运用HSV图
    hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_range = np.array([0, 43, 46])
    high_range = np.array([10, 255, 255])
    th = cv2.inRange(hue_image, low_range, high_range)
    index1 = th == 255

    #初始化图像
    img = np.zeros(image.shape, np.uint8)
    img[:, :] = (255, 255, 255)
    img[index1] = image[index1]
    return img

image = cv2.imread('002.JPG')

Processed_Image = keep_edge(image)

cv2.imshow('Processed Image', Processed_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()
