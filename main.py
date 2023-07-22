import sys

import qdarkstyle
from PySide6.QtWidgets import QApplication

from upload import MetaInfo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    metaInfo = MetaInfo()
    metaInfo.show()
    sys.exit(app.exec())
