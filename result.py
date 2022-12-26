import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import pandas as pd
import requests
import webbrowser

from utils import *

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(resource_path("crawling_result.ui"))[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    
    def __init__(self) :
        self.index = 0
        self.data = pd.read_csv('6i7.csv')
        super().__init__()
        self.setupUi(self)

        self.linkButton.clicked.connect(self.open_link)
        self.prevButton.clicked.connect(self.prev)
        self.nextButton.clicked.connect(self.next)

        self.show_info(self.index)
        
    def show_info(self, index):
        row = self.data.loc[index]
        max_page = len(self.data)
        self.titleEdit.setText(row['title'])
        self.productNameEdit.setText(row['product_title'])
        self.productNumEdit.setText(row['product_num'])
        self.regularPriceEdit.setText(str(row['regular_price']))
        self.salePriceEdit.setText(str(row['sale_price']))
        self.colorList.clear()
        for color in row['color'].split(','):
            self.colorList.addItem(color)
        self.pageLabel.setText(f'{index+1}/{max_page}')
        
        self.imageLabel: QLabel
        self.imageLabel.setPixmap(self.load_image_from_url(row['image']))
    
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
        webbrowser.open(self.data.loc[self.index]['link'])
        
    def load_image_from_url(self, url):
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(url).content)
        return pixmap

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()