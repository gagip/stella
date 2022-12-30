import cv2

def img2hash(img):
    """
    이미지를 16X16 크기의 평균 해시로 변환하는 함수
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (16, 16))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi

def hamming_distance(a, b):
    """
    해밍거리 측정 함수
    """
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a != b).sum()

    return distance