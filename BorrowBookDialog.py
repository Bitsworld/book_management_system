import sys
import time
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class BorrowBookDialog(QDialog):
    borrow_book_success_signal = pyqtSignal()
    back_success_signal = pyqtSignal()

    def __init__(self, student_id, parent=None):
        super(BorrowBookDialog, self).__init__(parent)
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

        self.title_label = QLabel(' 书籍借阅')
        self.title_label.setFont(title_label_font)
        self.title_label.setMargin(8)

        self.borrow_student_label = QLabel('借 阅 人：')
        self.borrow_student_label.setFont(font)
        self.borrow_student_edit = QLineEdit()
        self.borrow_student_edit.setFont(font)
        self.borrow_student_edit.setFixedHeight(28)
        self.borrow_student_edit.setFixedWidth(180)
        self.borrow_student_edit.setStyleSheet("background:#F0F0F0")
        self.borrow_student_edit.setReadOnly(True)
        self.borrow_student_edit.setText(self.student_id)

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

        self.borrow_button = QPushButton('借  阅')
        self.borrow_button.setFixedHeight(32)
        self.borrow_button.setFixedWidth(120)
        self.borrow_button.setFont(button_font)
        self.back_button = QPushButton('返  回')
        self.back_button.setFont(button_font)
        self.back_button.setFixedWidth(120)
        self.back_button.setFixedHeight(32)

        self.form_layout.addRow('', self.title_label)
        self.form_layout.addRow(self.borrow_student_label, self.borrow_student_edit)
        self.form_layout.addRow(self.book_name_label, self.book_name_edit)
        self.form_layout.addRow(self.book_id_label, self.book_id_edit)
        self.form_layout.addRow(self.author_label, self.author_edit)
        self.form_layout.addRow(self.publisher_label, self.publisher_edit)
        self.form_layout.addRow(self.abstract_label, self.abstract_edit)
        self.form_layout.addRow(self.publish_date_label, self.publish_date_edit)
        self.form_layout.addRow('', self.borrow_button)
        self.form_layout.addRow('', self.back_button)
        self.form_layout.setVerticalSpacing(10)

        self.setLayout(self.form_layout)

        self.borrow_button.clicked.connect(self.borrow_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.book_id_edit.textChanged.connect(self.book_id_edit_text_changed)

        self.setWindowTitle('书籍借阅')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.resize(300, 500)
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2-200)
        self.setWindowIcon(QIcon("./imagesSourse/user_icon2.png"))
        self.show()

        # # 初始化界面
        # self.setWindowTitle('图书管理系统')
        # self.setGeometry(100, 100, 700, 500)
        # self.setWindowIcon(QIcon("user_icon2.png"))
        # self.show()

    def book_id_edit_text_changed(self):
        book_id = self.book_id_edit.text()
        if book_id == '':
            self.book_name_edit.clear()
            self.author_edit.clear()
            self.publisher_edit.clear()
            self.abstract_edit.clear()
            self.publish_date_edit.clear()

            self.book_name_edit.setReadOnly(True)
            self.author_edit.setReadOnly(True)
            self.publisher_edit.setReadOnly(True)
            self.abstract_edit.setReadOnly(True)
            self.publish_date_edit.setReadOnly(True)

            self.book_name_edit.setStyleSheet("background:#F0F0F0")
            self.author_edit.setStyleSheet("background:#F0F0F0")
            self.publisher_edit.setStyleSheet("background:#F0F0F0")
            self.abstract_edit.setStyleSheet("background:#F0F0F0")
            self.publish_date_edit.setStyleSheet("background:#F0F0F0")
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
            sql = "SELECT BookName, BookId, Author, Publisher, Abstract, PublishTime,NumStorage, NumBorrowed FROM book WHERE BookId='%s'" % (book_id)
            print(sql)
            query.exec_(sql)
            print('exec')
            if query.first():
                print('运行到判断')
                self.book_name_edit.setText(str(query.value('BookName')))
                self.author_edit.setText(str(query.value('Author')))
                self.publisher_edit.setText(str(query.value('Publisher')))
                self.abstract_edit.setText(str(query.value('Abstract')))
                self.publish_date_edit.setDate(QDate.fromString(query.value('PublishTime').toString('yyyy-MM-dd'),  'yyyy-MM-dd'))
            else:
                self.book_name_edit.clear()
                self.author_edit.clear()
                self.publisher_edit.clear()
                self.abstract_edit.clear()
                self.publish_date_edit.clear()

    def borrow_button_clicked(self):
        book_id = self.book_id_edit.text()
        book_name = self.book_name_edit.text()
        if book_name == '':
            print(QMessageBox.warning(self, '提示', '请输入书号！', QMessageBox.Yes, QMessageBox.Yes))
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
            local_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            print(local_time)
            no_back_book_sql = "SELECT * FROM user_book WHERE ReturnTime < '%s' AND StudentId = '%s' AND BorrowState = 0" % (local_time, self.student_id)
            query.exec_(no_back_book_sql)
            if query.first():
                print(QMessageBox.information(self, '提示', '你有超期的书籍未归还，不能借书！', QMessageBox.Yes, QMessageBox.Yes))
                return
            else:
                if_borrow_sql = "SELECT * FROM user_book WHERE BookId = '%s' AND StudentId = '%s' AND BorrowState = 0 " % (book_id, self.student_id)
                query.exec_(if_borrow_sql)
                if query.first():
                    print(QMessageBox.warning(self, '警告', '你已经借过此书并且未归还\n  请勿重复借阅！', QMessageBox.Yes, QMessageBox.Yes))
                    return
                can_borrow_book_sql = "SELECT NumStorage, NumBorrowed FROM book"
                query.exec_(can_borrow_book_sql)
                query.first()
                if query.value('NumStorage') - query.value('NumBorrowed') <= 0:
                    print(QMessageBox.information(self, '提示', '你要借的书籍已经被借完，请选择其他书籍！', QMessageBox.Yes, QMessageBox.Yes))
                else:
                    # update_book_sql = "UPDATE book SET NumBorrowed = NumBorrowed +1 WHERE BookId = '%s'" % book_id
                    # query.exec_(update_book_sql)
                    insert_book_user_sql = "INSERT INTO user_book VALUES ('%s', '%s', '%s', '%s', 0)" % (self.student_id, book_id, str(QDate.currentDate().toPyDate()), (QDate.currentDate().addDays(30).toPyDate()) )
                    print(insert_book_user_sql)
                    query.exec_(insert_book_user_sql)
                    self.borrow_book_success_signal.emit()
                    print(QMessageBox.information(self, '提示', '书籍借阅成功，记得按期归还\n到期时间：%s' % (QDate.currentDate().addDays(30).toPyDate()) ) , QMessageBox.Yes, QMessageBox.Yes)

    def back_button_clicked(self):
        self.back_success_signal.emit()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BorrowBookDialog('2016141462226')
    sys.exit(app.exec_())