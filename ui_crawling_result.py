# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\workspace\python\stella\crawling_result.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(699, 665)
        self.imageLabel = QtWidgets.QLabel(Form)
        self.imageLabel.setGeometry(QtCore.QRect(390, 50, 261, 431))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 316, 561))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.titleEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.titleEdit.setReadOnly(True)
        self.titleEdit.setObjectName("titleEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.productNameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.productNameEdit.setReadOnly(True)
        self.productNameEdit.setObjectName("productNameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productNameEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.productNumEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.productNumEdit.setReadOnly(True)
        self.productNumEdit.setObjectName("productNumEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.productNumEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.regularPriceEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regularPriceEdit.sizePolicy().hasHeightForWidth())
        self.regularPriceEdit.setSizePolicy(sizePolicy)
        self.regularPriceEdit.setReadOnly(True)
        self.regularPriceEdit.setObjectName("regularPriceEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.regularPriceEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.salePriceEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.salePriceEdit.setText("")
        self.salePriceEdit.setReadOnly(True)
        self.salePriceEdit.setObjectName("salePriceEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.salePriceEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.colorList = QtWidgets.QListWidget(self.formLayoutWidget)
        self.colorList.setObjectName("colorList")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.colorList)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 620, 256, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prevButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout_2.addWidget(self.prevButton)
        self.pageLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pageLabel.setObjectName("pageLabel")
        self.horizontalLayout_2.addWidget(self.pageLabel)
        self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(380, 490, 281, 112))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.linkButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.linkButton.setObjectName("linkButton")
        self.verticalLayout.addWidget(self.linkButton)
        self.imageIinkButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.imageIinkButton1.setObjectName("imageIinkButton1")
        self.verticalLayout.addWidget(self.imageIinkButton1)
        self.imageIinkButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.imageIinkButton2.setObjectName("imageIinkButton2")
        self.verticalLayout.addWidget(self.imageIinkButton2)
        self.imageIinkButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.imageIinkButton3.setObjectName("imageIinkButton3")
        self.verticalLayout.addWidget(self.imageIinkButton3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.imageLabel.setText(_translate("Form", "Image"))
        self.label.setText(_translate("Form", "제목"))
        self.label_2.setText(_translate("Form", "상품 이름"))
        self.label_3.setText(_translate("Form", "상품 번호"))
        self.label_4.setText(_translate("Form", "정가"))
        self.label_5.setText(_translate("Form", "할인가"))
        self.label_6.setText(_translate("Form", "색깔"))
        self.prevButton.setText(_translate("Form", "이전"))
        self.pageLabel.setText(_translate("Form", "1/20"))
        self.nextButton.setText(_translate("Form", "다음"))
        self.linkButton.setText(_translate("Form", "상품 사이트로 이동"))
        self.imageIinkButton1.setText(_translate("Form", "이미지1 링크"))
        self.imageIinkButton2.setText(_translate("Form", "이미지2 링크"))
        self.imageIinkButton3.setText(_translate("Form", "이미지3 링크"))
