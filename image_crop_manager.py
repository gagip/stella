import cv2
import numpy as np
import requests
from average_hash_matching import *

'https://ellegotr8125.cdn-nhncommerce.com/data/goods/2022/img_s/6I75203_400_01.jpg'
'https://www.dlm1947.com/data/goods/2022/product/6I75203_detail_01.jpg'
url = 'https://www.dlm1947.com/data/goods/2022/product/6I75481_detail_01.jpg'
image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
image: np.ndarray = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
height, width = image.shape[:2] 

ret, thresh = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)
cv2.imshow('dd', thresh[:, 0:width])

# dst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image', dst)



# query_hash = img2hash(image)
# cv2.imshow('image', image)
# cv2.waitKey(2)  # 2ms간 대기
# a_hash = img2hash(image)
# dst = hamming_distance(query_hash, a_hash)
# if dst/256 < 0.2:  # 해밍거리 20% 이내만 출력 (80% 이상 닮은꼴)
#     print(dst/256)
cv2.waitKey(0)
cv2.destroyAllWindows()
