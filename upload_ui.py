# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(433, 478)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 391, 421))
        self.globalLayout = QVBoxLayout(self.layoutWidget)
        self.globalLayout.setObjectName(u"globalLayout")
        self.globalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.host = QLineEdit(self.layoutWidget)
        self.host.setObjectName(u"host")

        self.horizontalLayout_8.addWidget(self.host)


        self.globalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.user = QLineEdit(self.layoutWidget)
        self.user.setObjectName(u"user")

        self.horizontalLayout_10.addWidget(self.user)


        self.globalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.password = QLineEdit(self.layoutWidget)
        self.password.setObjectName(u"password")

        self.horizontalLayout_11.addWidget(self.password)


        self.globalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.saveConfiguration = QPushButton(self.layoutWidget)
        self.saveConfiguration.setObjectName(u"saveConfiguration")

        self.horizontalLayout_9.addWidget(self.saveConfiguration)


        self.globalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.title = QLineEdit(self.layoutWidget)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)


        self.globalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.slug = QLineEdit(self.layoutWidget)
        self.slug.setObjectName(u"slug")

        self.horizontalLayout_2.addWidget(self.slug)


        self.globalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.categories = QLineEdit(self.layoutWidget)
        self.categories.setObjectName(u"categories")

        self.horizontalLayout_3.addWidget(self.categories)

        self.showCatalog = QPushButton(self.layoutWidget)
        self.showCatalog.setObjectName(u"showCatalog")

        self.horizontalLayout_3.addWidget(self.showCatalog)


        self.globalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.filename = QLineEdit(self.layoutWidget)
        self.filename.setObjectName(u"filename")

        self.horizontalLayout_4.addWidget(self.filename)

        self.selectFile = QPushButton(self.layoutWidget)
        self.selectFile.setObjectName(u"selectFile")

        self.horizontalLayout_4.addWidget(self.selectFile)


        self.globalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.post = QPushButton(self.layoutWidget)
        self.post.setObjectName(u"post")

        self.horizontalLayout_12.addWidget(self.post)


        self.globalLayout.addLayout(self.horizontalLayout_12)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"WordPress\u7f51\u7ad9\u57df\u540d\u6216ip", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Rest Api\u5bc6\u7801", None))
        self.saveConfiguration.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u4ee5\u4e0a\u914d\u7f6e\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6807\u9898", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u82f1\u6587\u522b\u540d\uff08\u552f\u4e00\u6807\u8bc6\uff09", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5206\u7c7bID", None))
        self.showCatalog.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u5206\u7c7b\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u8def\u5f84", None))
        self.selectFile.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.post.setText(QCoreApplication.translate("Form", u"\u53d1\u5e03", None))
    # retranslateUi

