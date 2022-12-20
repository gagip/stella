import numpy as np
import requests
import cv2

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

url = 'https://www.dlm1947.com/data/goods/2022/product/6I75481_detail_01.jpg'
image_nparray = np.asarray(
    bytearray(requests.get(url).content), dtype=np.uint8)
image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

image_gray = cv2.imdecode(image_nparray, cv2.IMREAD_GRAYSCALE)
ksize = 3
blur = cv2.GaussianBlur(image_gray, ksize=(ksize, ksize), sigmaX=0)
ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   # contour(외곽선)를 찾아냄.(연속된 좌표점)

# contour(외곽선)을 그림, 초록색(0 255 0), 두께 2로
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# cnt변수에 Contour[0]에 있는 2차원 연속된 좌표를 넣음.
cnt = contours[0]

# 윤곽(convex)정보 휙득
hull = cv2.convexHull(cnt, returnPoints=False)

defects = cv2.convexityDefects(cnt, hull)   #

for i in range(defects.shape[0]):

    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])

    # 바깥 최 외곽선을 이은 line 표시 (파랑색)
    cv2.line(image, start, end, [255, 0, 0], 2)

    # 내부의 꼭지점에 좌표점 표시 (빨간색)
    cv2.circle(image, far, 5, [0, 0, 255], -1)



def onMouse(event, x, y, flags, param):
    print(event, x, y, flags)
    if event == cv2.EVENT_MOUSEWHEEL:
        image


cv2.imshow('image', ResizeWithAspectRatio(image, width=1280))
cv2.imshow('image_gray', image_gray)
cv2.imshow('blur', blur)

cv2.setMouseCallback('image', onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
