import numpy as np
import requests
import cv2
from average_hash_matching import *


url = 'https://www.dlm1947.com/data/goods/2022/product/6I75481_detail_01.jpg'
image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

query_hash = img2hash(image)

cv2.imshow('image', image)
cv2.waitKey(2)  # 2ms간 대기
a_hash = img2hash(image)
dst = hamming_distance(query_hash, a_hash)
if dst/256 < 0.2:  # 해밍거리 20% 이내만 출력 (80% 이상 닮은꼴)
    print(dst/256)

cv2.destroyAllWindows()
