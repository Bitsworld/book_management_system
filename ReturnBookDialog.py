import sys
import time
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ReturnBookDialog(QDialog):
    return_book_success_signal = pyqtSignal()
    back_button_signal = pyqtSignal()

    def __init__(self, student_id, parent=None):
        super(ReturnBookDialog, self).__init__(parent)
        self.student_id = student_id
        print('界面加载之前')
        self.initUI()

    def initUI(self):
        self.form_layout = QFormLayout()

        font = QFont()
        font.setPixelSize(20)
        title_label_font = QFont()
        title_label_font.setPixelSize(20)
        button_font = QFont()
        button_font.setPixelSize(18)

        self.title_label = QLabel(' 书籍归还')
        self.title_label.setFont(title_label_font)
        self.title_label.setMargin(8)

        self.return_student_label = QLabel('还 书 人：')
        self.return_student_label.setFont(font)
        self.return_student_edit = QLineEdit()
        self.return_student_edit.setFont(font)
        self.return_student_edit.setFixedHeight(28)
        self.return_student_edit.setFixedWidth(180)
        self.return_student_edit.setStyleSheet("background:#F0F0F0")
        self.return_student_edit.setReadOnly(True)
        self.return_student_edit.setText(self.student_id)

        self.book_name_label = QLabel("书   名:")
        self.book_name_label.setFont(font)
        self.book_name_edit = QLineEdit()
        self.book_name_edit.setFont(font)
        self.book_name_edit.setFixedWidth(180)
        self.book_name_edit.setFixedHeight(28)
        self.book_name_edit.setStyleSheet("background:#F0F0F0")
        self.book_name_edit.setReadOnly(True)

        self.book_id_label = QLabel('书   号:')
        self.book_id_label.setFont(font)
        self.book_id_edit = QLineEdit()
        self.book_id_edit.setFont(font)

        self.author_label = QLabel('作   者:')
        self.author_label.setFont(font)
        self.author_edit = QLineEdit()
        self.author_edit.setFont(font)
        self.author_edit.setStyleSheet("background:#F0F0F0")
        self.author_edit.setReadOnly(True)

        self.publisher_label = QLabel('出 版 社:')
        self.publisher_label.setFont(font)
        self.publisher_edit = QLineEdit()
        self.publisher_edit.setFont(font)
        self.publisher_edit.setStyleSheet("background:#F0F0F0")
        self.publisher_edit.setReadOnly(True)

        self.abstract_label = QLabel('摘   要:')
        self.abstract_label.setFont(font)
        self.abstract_edit = QTextEdit()
        abstract_font = QFont()
        abstract_font.setPixelSize(15)
        self.abstract_edit.setFont(abstract_font)
        self.abstract_edit.setFixedHeight(100)
        self.abstract_edit.setStyleSheet("background:#F0F0F0")
        self.abstract_edit.setReadOnly(True)

        self.publish_date_label = QLabel('出版日期:')
        self.publish_date_label.setFont(font)
        self.publish_date_edit = QDateTimeEdit()
        self.publish_date_edit.setDisplayFormat("yyyy-mm-dd")
        self.publish_date_edit.setFont(font)
        self.publish_date_edit.setStyleSheet("background:#F0F0F0")
        self.publish_date_edit.setReadOnly(True)

        self.return_button = QPushButton('归  还')
        self.return_button.setFixedHeight(32)
        self.return_button.setFixedWidth(120)
        self.return_button.setFont(button_font)
        self.back_button = QPushButton('返  回')
        self.back_button.setFont(button_font)
        self.back_button.setFixedWidth(120)
        self.back_button.setFixedHeight(32)

        self.form_layout.addRow('', self.title_label)
        self.form_layout.addRow(self.return_student_label, self.return_student_edit)
        self.form_layout.addRow(self.book_name_label, self.book_name_edit)
        self.form_layout.addRow(self.book_id_label, self.book_id_edit)
        self.form_layout.addRow(self.author_label, self.author_edit)
        self.form_layout.addRow(self.publisher_label, self.publisher_edit)
        self.form_layout.addRow(self.abstract_label, self.abstract_edit)
        self.form_layout.addRow(self.publish_date_label, self.publish_date_edit)
        self.form_layout.addRow('', self.return_button)
        self.form_layout.addRow('', self.back_button)
        self.form_layout.setVerticalSpacing(10)

        self.setLayout(self.form_layout)

        self.return_button.clicked.connect(self.return_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.book_id_edit.textChanged.connect(self.book_id_edit_text_changed)

        self.setWindowTitle('书籍归还')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.resize(300, 500)
        self.move((screen.width() - size.width()) / 2+100, (screen.height() - size.height()) / 2 - 80)
        self.setWindowIcon(QIcon("./imagesSourse/user_icon2.png"))
        self.show()

    def book_id_edit_text_changed(self):
        book_id = self.book_id_edit.text()
        if book_id == '':
            self.book_name_edit.clear()
            self.author_edit.clear()
            self.publisher_edit.clear()
            self.abstract_edit.clear()
            self.publish_date_edit.clear()
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
            select_book_from_user_book_sql = "SELECT * FROM user_book WHERE StudentId = '%s' AND BookId = '%s'" % (self.student_id, book_id)
            print(select_book_from_user_book_sql)
            query.exec_(select_book_from_user_book_sql)

            if query.first():
                select_book_from_book_sql = "SELECT * FROM book WHERE  BookId = '%s'" % book_id
                print(select_book_from_book_sql)
                query.exec_(select_book_from_book_sql)
                query.first()
                self.book_name_edit.setText(str(query.value('BookName')))
                self.author_edit.setText(str(query.value('Author')))
                self.publisher_edit.setText(str(query.value('Publisher')))
                self.abstract_edit.setText(str(query.value('Abstract')))
                self.publish_date_edit.setDate(QDate.fromString(query.value('PublishTime').toString('yyyy-MM-dd'), 'yyyy-MM-dd'))

            return

    def return_button_clicked(self):
        book_id = self.book_id_edit.text()
        book_name = self.book_name_edit.text()
        if book_name == '':
            print(QMessageBox.warning(self, '提示', '请输入未归还书籍的书号！', QMessageBox.Yes, QMessageBox.Yes))
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

            should_back_time_book_sql = "SELECT ReturnTime FROM user_book WHERE StudentId = '%s' AND BookId = '%s'" % (self.student_id, book_id)
            query.exec_(should_back_time_book_sql)
            query.first()
            should_back_time = QDate(query.value('ReturnTime'))
            print(should_back_time)

            update_book_sql = "UPDATE book SET NumBorrowed = NumBorrowed-1 WHERE BookId = '%s'" % book_id
            query.exec_(update_book_sql)
            update_user_book_sql = "UPDATE user_book SET BorrowState = 1 WHERE StudentId = '%s' AND BookId = '%s'" % (self.student_id, book_id)
            query.exec_(update_user_book_sql)

            should_back_time_book_sql = "SELECT ReturnTime FROM user_book WHERE StudentId = '%s' AND BookId = '%s'" % (self.student_id, book_id)
            query.exec_(should_back_time_book_sql)
            query.first()
            should_back_time = QDate(query.value('ReturnTime'))
            if should_back_time.daysTo(QDate.currentDate()) > 0:
                print(QMessageBox.information(self, '提示', '还书成功！\n 超期时间：%d' % should_back_time, QMessageBox.Yes, QMessageBox.Yes))
            else:
                print(QMessageBox.information(self, '提示', '还书成功！', QMessageBox.Yes, QMessageBox.Yes))
            self.return_book_success_signal.emit()
            self.close()

    def back_button_clicked(self):
        self.back_button_signal.emit()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReturnBookDialog('2016141462225')
    sys.exit(app.exec_())
