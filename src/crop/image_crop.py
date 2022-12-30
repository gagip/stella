import cv2
import numpy as np

MIN_HEIGHT = 50

def separate_by_white_space(image: np.ndarray) -> list:
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_inverted = 255 - image_gray       # 흑백 반전 (흰색은 검정색으로)
    # 하얀색 라인(세로) 추출
    white_line_filter = np.sum(image_inverted, axis=1) == 0
    white_line_index = np.where(white_line_filter)[0]

    separators = np.argwhere(np.diff(white_line_index) > 1)[:,0]

    result = []     # 하얀색 외 색깔이 있는 세로 인덱스 (start_height, end_height)
    result.append((0, white_line_index[0] - 1))
    for separator in separators.tolist():
        prev_index = white_line_index[separator] + 1
        next_index = white_line_index[separator+1] - 1
        
        if next_index - prev_index > MIN_HEIGHT:
            result.append((prev_index, next_index))  
            
    return result