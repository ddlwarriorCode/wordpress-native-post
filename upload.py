import base64
import json
import os
import threading
import time

import markdown
import requests
from PySide6.QtCore import Signal, QSettings
from PySide6.QtWidgets import QWidget, QSizePolicy, QFileDialog

from myutils import showMsgBox
from upload_ui import Ui_Form


class MetaInfo(QWidget):
    preShowCatalogSignal = Signal()
    afterShowCatalogSignal = Signal(str)
    prePostSignal = Signal()
    afterPostSignal = Signal(str)
    checkFailureSignal = Signal(str)
    missUserInfo = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        objs = self.findChildren(QWidget)
        for obj in objs:  # 控件自适应窗口大小
            obj.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setLayout(self.ui.globalLayout)
        self.setContentsMargins(15, 15, 15, 15)
        self.setWindowTitle('wordpress-native-post')
        self.ui.post.clicked.connect(self.postBlog)
        self.ui.selectFile.clicked.connect(self.getFileName)
        self.ui.showCatalog.clicked.connect(self.showCatalog)
        self.preShowCatalogSignal.connect(self.preShowCatalogSlot)
        self.prePostSignal.connect(self.prePostSlot)
        self.afterShowCatalogSignal.connect(self.afterShowCatalogSlot)
        self.afterPostSignal.connect(self.afterPostSlot)
        self.ui.saveConfiguration.clicked.connect(self.saveConfiguration)
        self.checkFailureSignal.connect(self.checkFailureSlot)
        self.missUserInfo.connect(self.checkFailureSlot)
        # 读取配置文件中信息
        settings = QSettings('myapp', 'upload')
        self.ui.host.setText(settings.value('host', ''))
        self.ui.user.setText(settings.value('user', ''))
        self.ui.password.setText(settings.value('password', ''))

    @staticmethod
    def checkFailureSlot(msg):
        showMsgBox(msg)

    def saveConfiguration(self):
        settings = QSettings('myapp', 'upload')
        settings.setValue('host', self.ui.host.text())
        settings.setValue('user', self.ui.user.text())
        settings.setValue('password', self.ui.password.text())
        showMsgBox('保存成功')

    def preShowCatalogSlot(self):
        self.switchShowCatalog()

    def prePostSlot(self):
        self.switchPost()

    def afterShowCatalogSlot(self, msg):
        self.switchShowCatalog()
        showMsgBox(msg)

    def afterPostSlot(self, msg):
        self.switchPost()
        showMsgBox(msg)

    def switchShowCatalog(self):
        if self.ui.showCatalog.isEnabled():
            self.ui.showCatalog.setEnabled(False)
        else:
            self.ui.showCatalog.setEnabled(True)

    def switchPost(self):
        if self.ui.post.isEnabled():
            self.ui.post.setEnabled(False)
        else:
            self.ui.post.setEnabled(True)

    def getUrlAndHeader(self, method):
        url = "https://" + self.ui.host.text() + "/wp-json/wp/v2/" + method
        user = self.ui.user.text()
        password = self.ui.password.text()
        credentials = user + ':' + password
        token = base64.b64encode(credentials.encode())
        header = {'Authorization': 'Basic ' + token.decode('utf-8')}
        return [url, header]

    def showCatalog(self):
        threading.Thread(target=self.showCatalogTask).start()

    def checkUserInfo(self):
        if self.ui.host.text() == '':
            self.missUserInfo.emit('缺少博客域名或IP地址')
            return False
        if self.ui.user.text() == '':
            self.missUserInfo.emit('缺少用户名')
            return False
        if self.ui.password.text() == '':
            self.missUserInfo.emit('缺少 Rest Api 密码')
            return False
        return True

    def showCatalogTask(self):
        if not self.checkUserInfo():
            return
        self.preShowCatalogSignal.emit()
        url, header = self.getUrlAndHeader("categories")
        response = requests.get(url, headers=header)
        if response.status_code != requests.codes.ok:
            msg = '发布失败,返回结果:' + str(response)
        else:
            data = json.loads(response.text)
            msg = ''
            for category in data:
                msg += '分类 ID:' + str(category['id']) + '\t分类名称:' + category['name'] + '\n'
        self.afterShowCatalogSignal.emit(msg)

    def postBlog(self):
        threading.Thread(target=self.postBlogTask).start()

    def isValid(self):
        if self.ui.title.text() == '':
            self.checkFailureSignal.emit('文章标题不能为空')
            return False
        if self.ui.slug.text() == '':
            self.checkFailureSignal.emit('用于唯一标识的英文别名不能为空')
            return False
        if not os.path.isfile(self.ui.filename.text()):
            self.checkFailureSignal.emit('文件路径不正确，请检查并修改')
            return False
        return True

    def postBlogTask(self):
        if not self.checkUserInfo():
            return
        if not self.isValid():
            return
        self.prePostSignal.emit()
        with open(self.ui.filename.text(), 'r', encoding='utf-8') as f:
            content = f.read()
        content = markdown.markdown(content)
        post = {
            'title': self.ui.title.text(),
            'slug': self.ui.slug.text(),
            'status': 'publish',
            'content': content,
            'date': time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())
        }
        categories = self.ui.categories.text()
        if categories == '':
            post['categories'] = 1
        else:
            post['categories'] = categories
        url, header = self.getUrlAndHeader("posts")
        response = requests.post(url, headers=header, json=post)
        if response.status_code == requests.codes.ok | response.status_code == requests.codes.created:
            msg = '发布成功'
        else:
            msg = '发布失败,返回结果:' + str(response)
        self.afterPostSignal.emit(msg)

    def getFileName(self):
        fileName = QFileDialog.getOpenFileName(self, "选择本地文件", "", "*.md;*.txt")[0]
        self.ui.filename.setText(fileName)
