import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import pandas as pd
import requests
import webbrowser
import clipboard
from plyer import notification
from collections import defaultdict

from utils import *
from config import *

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(resource_path("crawling_result.ui"))[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self, file_name):
        self.index = 0
        self.data = pd.read_csv(f'data/{file_name}.csv')
        super().__init__()
        self.setupUi(self)

        self.linkButton.clicked.connect(self.open_link)
        self.prevButton.clicked.connect(self.prev)
        self.nextButton.clicked.connect(self.next)
        self.imageIinkButton1.clicked.connect(self.copyImageLink1)
        self.imageIinkButton2.clicked.connect(self.copyImageLink2)
        self.imageIinkButton3.clicked.connect(self.copyImageLink3)
        self.manTopButton.clicked.connect(lambda: self.copySize(KEY_MAN_UP_SIZE))
        self.manBottomButton.clicked.connect(lambda: self.copySize(KEY_MAN_BOTTOM_SIZE))
        self.womanTopButton.clicked.connect(lambda: self.copySize(KEY_WOMAN_UP_SIZE))
        self.womanBottomButton.clicked.connect(lambda: self.copySize(KEY_WOMAN_BOTTOM_SIZE))
        self.hatButton.clicked.connect(lambda: self.copySize(KEY_HAT_SIZE))
        self.checkBoxComplete.stateChanged.connect(self.complete_job)
        self.progressSheetButton.clicked.connect(self.move_progress_sheet)
        self.show_info(self.index)

    def show_info(self, index):
        row = self.data.loc[index]
        max_page = len(self.data)
        self.titleEdit.setText(row[KEY_TITLE])
        self.productNameEdit.setText(row[KEY_PRODUCT_NAME])
        self.productNumEdit.setText(row[KEY_PRODUCT_NUM])
        self.regularPriceEdit.setText(str(row[KEY_REGULAR_PRICE]))
        self.salePriceEdit.setText(str(row[KEY_SALE_PRICE]))
        self.colorEdit.setText(row[KEY_COLORS])
        self.pageLabel.setText(f'{index+1}/{max_page}')

        self.imageLabel: QLabel
        self.imageLabel.setPixmap(
            self.load_image_from_url(row[KEY_IMAGE_LINK]))

    def prev(self):
        if self.index == 0:
            return
        self.index -= 1
        self.show_info(self.index)

    def next(self):
        if self.index >= len(self.data) - 1:
            return
        self.index += 1
        self.show_info(self.index)

    def open_link(self):
        webbrowser.open(self.data.loc[self.index][KEY_LINK])

    def load_image_from_url(self, url):
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(url).content)
        return pixmap

    def copyImageLink1(self):
        clipboard.copy(self.data.loc[self.index][KEY_IMAGE_LINK])
        notification.notify(
            title='이미지1 링크 복사 성공',
            message='링크를 복사했습니다. ctrl+v로 붙여넣기 가능합니다.',
        )

    def copyImageLink2(self):
        detail_image = self.data.loc[self.index][KEY_DETAIL_IMAGES_LINK]
        clipboard.copy(detail_image.split(',')[0])
        notification.notify(
            title='이미지2 링크 복사 성공',
            message='링크를 복사했습니다. ctrl+v로 붙여넣기 가능합니다.',
        )

    def copyImageLink3(self):
        detail_image = self.data.loc[self.index][KEY_DETAIL_IMAGES_LINK]
        clipboard.copy(detail_image.split(',')[1])
        notification.notify(
            title='이미지3 링크 복사 성공',
            message='링크를 복사했습니다. ctrl+v로 붙여넣기 가능합니다.',
        )
        
    def copySize(self, key: int):
        size_data_set = defaultdict(lambda: '', SIZE_DATA_SET)
        size = size_data_set[key]
        clipboard.copy(size)
        notification.notify(
            title='사이즈 복사',
            message='링크를 복사했습니다. ctrl+v로 붙여넣기 가능합니다.',
        )

    def move_progress_sheet(self):
        """ 구글 스프레드시트로 이동 """
        pass
    
    def complete_job(self, state):
        """ 작업 완료 시 이벤트 처리 """
        is_complete = state == Qt.CheckState.Checked
        
        print(is_complete)
        pass

if __name__ == "__main__":
    use_file_name = input(f'엑셀 파일 이름 (default: {DEFAULT_SEARCH_KEYWORD}): ')
    file_name = use_file_name if use_file_name else DEFAULT_SEARCH_KEYWORD

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass(file_name)

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
