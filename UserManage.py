import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from AddUserDialog import AddUserDialog
# from DropUserDialog import DropUserDialog
from UserStorageView import UserStorageView
from ReviseUserDialog import ReviseUserDialog


class UserManage(QWidget):
    def __init__(self,  parent=None):
        super(UserManage, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 设置全局布局
        self.layout = QHBoxLayout()
        self.buttonLayout = QVBoxLayout()
        self.setLayout(self.layout)

        font = QFont()
        font.setPixelSize(16)

        self.add_user_button = QPushButton('添加读者')
        self.add_user_button.setFont(font)
        self.add_user_button.setFixedWidth(100)
        self.add_user_button.setFixedHeight(40)

        self.drop_user_button = QPushButton('删除读者')
        self.drop_user_button.setFont(font)
        self.drop_user_button.setFixedHeight(40)
        self.drop_user_button.setFixedWidth(100)

        self.revise_user_button = QPushButton('修改读者')
        self.revise_user_button.setFont(font)
        self.revise_user_button.setFixedWidth(100)
        self.revise_user_button.setFixedHeight(40)

        self.not_back_user_button = QPushButton('超期读者')
        self.not_back_user_button.setFont(font)
        self.not_back_user_button.setFixedWidth(100)
        self.not_back_user_button.setFixedHeight(40)

        self.buttonLayout.addWidget(self.add_user_button)
        self.buttonLayout.addWidget(self.drop_user_button)
        self.buttonLayout.addWidget(self.revise_user_button)
        self.buttonLayout.addWidget(self.not_back_user_button)

        self.layout.addLayout(self.buttonLayout)
        self.storage_view = UserStorageView()
        self.layout.addWidget(self.storage_view)

        self.add_user_button.clicked.connect(self.add_user_button_clicked)
        self.drop_user_button.clicked.connect(self.drop_user_button_clicked)
        self.revise_user_button.clicked.connect(self.revise_user_button_clicked)
        self.not_back_user_button.clicked.connect(self.not_back_user_button_clicked)


        self.setWindowTitle('读者管理')
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.show()

    def add_user_button_clicked(self):
        add_user_dialog = AddUserDialog(self)
        # add_dialog.exec_()
        add_user_dialog.add_user_success_signal.connect(self.storage_view.search_button_clicked)
        add_user_dialog.show()

    def drop_user_button_clicked(self):
        self.storage_view.drop_user()

    def revise_user_button_clicked(self):
        select_user_id = self.storage_view.get_revise_user_id()
        print(select_user_id)
        if select_user_id == None:
            print(QMessageBox.information(self, '提示', '请选择要修改的用户', QMessageBox.Yes, QMessageBox.Yes))
        else:
            revise_dialog = ReviseUserDialog(select_user_id, self)
            self.storage_view.search_button_clicked()
            revise_dialog.revise_user_successful_signal.connect(self.storage_view.search_button_clicked)
            # revise_dialog.revise_back_signal.connect(self.storage_view.search_button_clicked)
            revise_dialog.show()

    def not_back_user_button_clicked(self):
        self.storage_view.no_back_book_user()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserManage()
    sys.exit(app.exec_())
