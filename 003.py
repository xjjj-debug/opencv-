import cv2
import numpy as np

def find_similarity(image,template):
    # 将图片转化为灰度图
    gray = cv2.cvtColor(image,code=cv2.COLOR_BGR2GRAY)

    #将检测图像和模版各自标准化
    match = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    #找出匹配度大于0.9的匹配点
    location = np.where(match>0.9)

    #求出模版图案的长宽
    w,h = template.shape[0:2]
    #循环遍历匹配点,画出矩形框
    for p in zip(*location[::-1]):
        x1,y1 = p[0],p[1]
        x2,y2 = x1+w,y1+h
        cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)
    return image

image = cv2.imread("003.jpg")
template0 = cv2.imread("0030.jpg", 0)
template1 = cv2.imread("0031.jpg", 0)
template2 = cv2.imread("0032.jpg", 0)

Processed_Image0 = find_similarity(image,template0)
Processed_Image1 = find_similarity(Processed_Image0,template1)
Processed_Image2 = find_similarity(Processed_Image1,template2)

cv2.imshow('Processed Image', Processed_Image0)
cv2.waitKey(0)
cv2.destroyAllWindows()
