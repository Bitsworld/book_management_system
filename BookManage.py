import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from AddBookDialog import AddBookDialog
# from DropBookDialog Import DropBookDialog
from BookStorageView import BookStorageView


class BookManage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置全局布局
        self.layout = QHBoxLayout()
        self.buttonLayout = QVBoxLayout()
        self.setLayout(self.layout)

        font = QFont()
        font.setPixelSize(16)

        self.add_book_button = QPushButton('添加书籍')
        self.add_book_button.setFont(font)
        self.add_book_button.setFixedWidth(100)
        self.add_book_button.setFixedHeight(40)

        self.drop_book_button = QPushButton('删除书籍')
        self.drop_book_button.setFont(font)
        self.drop_book_button.setFixedHeight(40)
        self.drop_book_button.setFixedWidth(100)

        self.revise_book_button = QPushButton('修改信息')
        self.revise_book_button.setFont(font)
        self.revise_book_button.setFixedWidth(100)
        self.revise_book_button.setFixedHeight(40)

        self.buttonLayout.addWidget(self.add_book_button)
        self.buttonLayout.addWidget(self.drop_book_button)
        self.buttonLayout.addWidget(self.revise_book_button)

        self.layout.addLayout(self.buttonLayout)
        self.storage_view = BookStorageView()
        self.layout.addWidget(self.storage_view)

        self.add_book_button.clicked.connect(self.add_book_button_clicked)
        self.drop_book_button.clicked.connect(self.drop_book_button_clicked)
        self.revise_book_button.clicked.connect(self.revise_book_button_clicked)

        self.setWindowTitle('欢迎注册图书管理系统')
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.show()

    def add_book_button_clicked(self):
        pass
        '''
        add_dialog = AddBookDialog(self)
        add_dialog.add_book_signal.connect(self.storage_view.search_button_clicked())
        add_dialog.show()
        add_dialog.exec_()
        '''

    def drop_book_button_clicked(self):
        pass
        '''
        drop_dialog = DropDialog(self)
        drop_dialog.drop_book_successful_signal.connect(self.storage_view.search_button_clicked())
        drop_dialog.show()
        drop_dialog.exec_
        '''

    def revise_book_button_clicked(self):
        pass
        '''
        revise_dialog = ReviseDialog(self)
        revise_dialog.revise_book_successful_signal.connect(self.storage_view.search_button_clicked())
        revise_dialog.show()
        revise_dialog.exec_
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BookManage()
    sys.exit(app.exec_())

