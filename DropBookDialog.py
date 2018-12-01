import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *


class DropBookDialog(QDialog):
    drop_book_successful_signal = pyqtSignal()
    drop_back_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(DropBookDialog, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QFormLayout()
        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        title_font = QFont()
        title_font.setPixelSize(20)
        font = QFont()
        font.setPixelSize(20)
        button_font = QFont()
        button_font.setPixelSize(16)
        edit_font = QFont()
        edit_font.setPixelSize(16)

        self.title_label = QLabel('删除书籍')
        self.title_label.setFont(title_font)

        self.book_name_label = QLabel('书   名：')
        self.book_name_label.setFont(font)
        self.book_name_edit = QLineEdit()
        self.book_name_edit.setFont(edit_font)
        self.book_name_edit.setReadOnly(True)
        self.book_name_edit.setFixedHeight(28)
        self.book_name_edit.setFixedWidth(180)
        self.book_name_edit.setStyleSheet("background-color:#F5F5F5")

        self.book_id_label = QLabel('书   号：')
        self.book_id_label.setFont(font)
        self.book_id_edit = QLineEdit()
        self.book_id_edit.setFont(edit_font)
        self.book_id_edit.setReadOnly(False)
        self.book_id_edit.setFixedWidth(180)
        self.book_id_edit.setFixedHeight(28)

        self.author_name_label = QLabel('作   者：')
        self.author_name_label.setFont(font)
        self.author_name_edit = QLineEdit()
        self.author_name_edit.setFont(edit_font)
        self.author_name_edit.setReadOnly(True)
        self.author_name_edit.setFixedWidth(180)
        self.author_name_edit.setFixedHeight(28)
        self.author_name_edit.setStyleSheet("background-color:#F5F5F5")

        self.publisher_label = QLabel('出 版 社：')
        self.publisher_label.setFont(font)
        self.publisher_edit = QLineEdit()
        self.publisher_edit.setFont(edit_font)
        self.publisher_edit.setReadOnly(True)
        self.publisher_edit.setFixedWidth(180)
        self.publisher_edit.setFixedHeight(28)
        self.publisher_edit.setStyleSheet("background-color:#F5F5F5")


        self.publish_date_label =QLabel('出版日期：')
        self.publish_date_label.setFont(font)
        self.publish_date_edit = QLineEdit()
        self.publish_date_edit.setFont(edit_font)
        self.publish_date_edit.setReadOnly(True)
        self.publish_date_edit.setFixedWidth(180)
        self.publish_date_edit.setFixedHeight(28)
        self.publish_date_edit.setStyleSheet("background-color:#F5F5F5")

        self.drop_book_button = QPushButton('删除书籍')
        self.drop_book_button.setFont(button_font)
        self.drop_book_button.setFixedHeight(32)
        self.drop_book_button.setFixedWidth(120)

        self.back_button = QPushButton('返  回')
        self.back_button.setFont(button_font)
        self.back_button.setFixedWidth(120)
        self.back_button.setFixedHeight(32)

        self.layout.addRow('', self.title_label)
        self.layout.addRow(self.book_name_label, self.book_name_edit)
        self.layout.addRow(self.book_id_label, self.book_id_edit)
        self.layout.addRow(self.author_name_label, self.author_name_edit)
        self.layout.addRow(self.publisher_label, self.publisher_edit)
        self.layout.addRow(self.publish_date_label, self.publish_date_edit)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.v_layout.addWidget(self.widget)
        self.v_layout1 = QVBoxLayout()
        # self.drop_book_button.setStyleSheet('background:#fff')
        self.v_layout1.addWidget(self.drop_book_button, Qt.AlignRight)
        self.v_layout1.addWidget(self.back_button, Qt.AlignCenter)
        self.v_layout1.setContentsMargins(90, 20,  90, 40)
        self.widget1 = QWidget()
        self.widget1.setFixedWidth(300)
        self.widget1.setFixedHeight(200)
        # self.widget1.setStyleSheet('background:#888888')

        self.widget1.setLayout(self.v_layout1)
        self.v_layout.addWidget(self.widget1, Qt.AlignHCenter)

        # self.layout.addRow('', self.drop_book_button)
        # self.layout.addWidget(self.back_button)
        # self.layout.addRow('', self.back_button)

        self.title_label.setMargin(7)
        self.layout.setVerticalSpacing(10)

        self.drop_book_button.clicked.connect(self.drop_book_button_clicked)
        self.book_id_edit.textChanged.connect(self.book_id_edit_changed)
        self.back_button.clicked.connect(self.back_button_clicked)

        self.setWindowTitle('删 除 书 籍')
        self.setGeometry(400, 250, 300, 500)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.setWindowModality(Qt.WindowModal)
        self.show()

    def drop_book_button_clicked(self):
        book_id = self.book_id_edit.text()
        if book_id == '':
            print(QMessageBox.warning(self, '提醒', '请输入书号！', QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            # 打开数据库，建立连接
            db = QSqlDatabase.addDatabase("QMYSQL")
            db.setHostName('localhost')
            db.setDatabaseName('book_management_system')
            db.setUserName('root')
            db.setPassword('wadden@mysql')
            db.open()
            if db.isOpen():
                print('成功连接到数据库')
            else:
                print('数据库连接失败')

            query = QSqlQuery()
            sql = "SELECT NumBorrowed FROM book WHERE BookId='%s'" % (book_id)
            query.exec_(sql)

            if query.first():
                if query.value('NumBorrowed') > 0:
                    print(QMessageBox.information(self, '警告', '有书籍未归还，删除书籍失败！', QMessageBox.Yes, QMessageBox.Yes))
                    return
                else:
                    delect_sql = "DELETE FROM book WHERE BookId = '%s'" % (book_id)
                    query.exec_(delect_sql)
                    db.commit()
                    print(QMessageBox.information(self, '提示', '书籍删除成功', QMessageBox.Yes,  QMessageBox.Yes))
                    self.drop_book_successful_signal.emit()
                    self.close()
            else:
                print(QMessageBox.information(self, '提示', '未查询到该书籍，请重新输入书籍号', QMessageBox.Yes, QMessageBox.Yes))
                self.book_id_edit.clear()


    def book_id_edit_changed(self):
        book_id = self.book_id_edit.text()
        if book_id == '':
            self.book_name_edit.clear()
            self.publisher_edit.clear()
            self.publish_date_edit.clear()
            self.author_name_edit.clear()
        else:
            # 打开数据库，建立连接
            db = QSqlDatabase.addDatabase("QMYSQL")
            db.setHostName('localhost')
            db.setDatabaseName('book_management_system')
            db.setUserName('root')
            db.setPassword('wadden@mysql')
            db.open()
            if db.isOpen():
                print('成功连接到数据库')
            else:
                print('数据库连接失败')

            query = QSqlQuery()
            sql = "SELECT BookName, BookId, Author, Publisher, PublishTime FROM book WHERE BookId='%s'" % (book_id)
            query.exec_(sql)
            print('运行到sql后面')
            if query.first():
                print('运行到判断')
                self.book_name_edit.setText(str(query.value('BookName')))
                self.author_name_edit.setText(str(query.value('Author')))
                self.publisher_edit.setText(str(query.value('Publisher')))
                self.publish_date_edit.setText(query.value('PublishTime').toString('yyyy-MM-dd'))
            else:
                self.book_name_edit.clear()
                self.publisher_edit.clear()
                self.publish_date_edit.clear()
                self.author_name_edit.clear()
            return

    def back_button_clicked(self):
        self.drop_back_successful_signal.emit()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DropBookDialog()
    sys.exit(app.exec_())