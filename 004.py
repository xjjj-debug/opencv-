import cv2
import numpy as np

def process(image):
    # 运用HSV图
    hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # HSV黄色范围
    low_range = np.array([11, 150, 60])
    high_range = np.array([25, 255, 255])
    img = cv2.inRange(hue_image, low_range, high_range)

    # 形态学
    line = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15), (-1, -1))
    # 黑帽
    mask = cv2.morphologyEx(img, cv2.MORPH_OPEN, line)

    # 轮廓提取, 发现最大轮廓
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    index = -1
    max = 0
    for c in range(len(contours)):
        area = cv2.contourArea(contours[c])
        if area > max:
            max = area
            index = c

    # 绘制
    if index >= 0:
        rect = cv2.minAreaRect(contours[index])
        # 椭圆拟合（1.目标图像2.长短轴3.颜色4.边界线粗细5.边界线类型）
        cv2.ellipse(image, rect, (255, 0, 0), 2, 8)
        # 中心点定位
        cv2.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (0, 255, 0), 2, 8, 0)
    return image


# 读取视频
capture = cv2.VideoCapture("004.mp4")
# 循环处理每一帧
while(True):
    ret, frame = capture.read()
    if ret is True:
        cv2.imshow("video-input", frame)
        result = process(frame)
        cv2.imshow("result", result)
        cv2.waitKey(50)
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()