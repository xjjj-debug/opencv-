import cv2

def remove_noise(image):
    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用高斯滤波平滑图像
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 使用自适应阈值处理图像
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 使用形态学操作去除干扰线
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    #二值图取反
    dst = cv2.bitwise_not(opening)
    return dst

# 读取验证码图片
image = cv2.imread('001.JPG')

# 去除干扰线
processed_image = remove_noise(image)

# 显示处理后的图像
cv2.imshow('Processed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




