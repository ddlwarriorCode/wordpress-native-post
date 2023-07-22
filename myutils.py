from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox


def showMsgBox(msg):
    msgBox = QMessageBox()
    msgBox.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
    msgBox.setWindowTitle(' ')
    msgBox.setText(msg)
    msgBox.exec()
