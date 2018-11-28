import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *


class AddBookDialog(QDialog):
    add_book_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(AddBookDialog, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.layout.setVerticalSpacing(10)

        font = QFont()
        font.setPixelSize(20)
        title_label_font = QFont()
        title_label_font.setPixelSize(20)

        self.title_label = QLabel(' 添加书籍')
        self.title_label.setFont(title_label_font)
        self.title_label.setMargin(8)

        self.book_name_label = QLabel("书   名:")
        self.book_name_label.setFont(font)
        self.book_name_edit = QLineEdit()
        self.book_name_edit.setFont(font)
        self.book_name_edit.setFixedWidth(180)
        self.book_name_edit.setFixedHeight(28)

        self.book_id_label = QLabel('书   号:')
        self.setFont(font)
        self.book_id_edit = QLineEdit()
        self.setFont(font)

        self.author_label = QLabel('作   者:')
        self.setFont(font)
        self.author_edit = QLineEdit()
        self.author_edit.setFont(font)

        self.publisher_label = QLabel('出 版 社:')
        self.publisher_label.setFont(font)
        self.publisher_edit = QLineEdit()
        self.publisher_edit.setFont(font)

        self.abstract_label = QLabel('摘   要:')
        self.abstract_label.setFont(font)
        self.abstract_edit = QLineEdit()
        self.abstract_edit.setFont(font)

        self.publish_date_label = QLabel('出版日期:')
        self.publish_date_label.setFont(font)
        self.publish_date_edit = QDateTimeEdit()
        self.publish_date_edit.setDisplayFormat("yyyy-mm-dd")
        self.publish_date_edit.setFont(font)

        self.add_num_label = QLabel('数   量:')
        self.add_num_label.setFont(font)
        self.add_num_edit = QLineEdit()
        self.add_num_edit.setFont(font)
        self.add_num_edit.setValidator(QIntValidator())

        self.add_book_button = QPushButton('添 加')
        button_font = QFont()
        button_font.setPixelSize(16)
        self.add_book_button.setFixedHeight(32)
        self.add_book_button.setFixedWidth(140)

        self.layout.addRow('', self.title_label)
        self.layout.addRow(self.book_name_label, self.book_name_edit)
        self.layout.addRow(self.book_id_label, self.book_id_edit)
        self.layout.addRow(self.author_label, self.author_edit)
        self.layout.addRow(self.publisher_label, self.publisher_edit)
        self.layout.addRow(self.abstract_label, self.abstract_edit)
        self.layout.addRow(self.publish_date_label, self.publish_date_edit)
        self.layout.addRow(self.add_num_label, self.add_num_edit)
        self.layout.addRow('',  self.add_book_button)

        self.add_book_button.clicked.connect(self.add_book_button_clicked)

        self.setWindowTitle('添加书籍')
        self.setGeometry(250, 250, 300, 500)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.setWindowModality(Qt.WindowModal)
        self.show()

    def add_book_button_clicked(self):
        book_name = self.book_name_edit.text()
        book_id = self.book_id_edit.text()
        author = self.author_edit.text()
        publisher = self.publisher_edit.text()
        abstract = self.abstract_edit.text()
        publish_date = self.publish_date_edit.text()
        add_num = self.add_num_edit.text()

        if book_name == '' or book_id == '' or author == '' or publisher == '' or abstract == '' or publish_date == '' or add_num == '':
            print(QMessageBox.warning(self, '警告', '请填写完整！', QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            # 数据库连接
            db = QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName('localhost')
            db.setDatabaseName('book_management_system')
            db.setUserName('root')
            db.setPassword('wadden@mysql')
            db.open()
            print(db.lastError().text())
            if db.isOpen():
                print('成功连接到数据库')
            else:
                print('数据库连接失败')

            query = QSqlQuery()
            sql = "SELECT * FROM book WHERE BookId='%s'" % (book_id)
            query.exec_(sql)
            print('执行到query')
            if query.first():
                print(QMessageBox.warning(self, '提示', '书籍已经存在,添加书籍失败！', QMessageBox.Yes, QMessageBox.Yes))
                self.clear_edit()
            else:
                add_num = int(add_num)
                print('执行到插入前面')
                insert_book_sql = "INSERT INTO book VALUES ('%s','%s','%s','%s','%s','%s',%d,0)"%(book_id,book_name,publisher,publish_date,author,abstract,add_num)
                print('执行到query.exec_(insert_book_sql)前面')
                query.exec_(insert_book_sql)
                print('执行到query.exec_(insert_book_sql)')
                db.commit()
                print(QMessageBox.information(self, '提示', '添加书籍成功！', QMessageBox.Yes, QMessageBox.Yes))
                self.add_book_success_signal.emit()
                self.close()
                self.clear_edit()
            return
    def clear_edit(self):
        self.book_name_edit.clear()
        self.book_id_edit.clear()
        self.author_edit.clear()
        self.add_num_edit.clear()
        self.publish_date_edit.clear()
        self.abstract_edit.clear()
        self.publisher_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddBookDialog()
    sys.exit(app.exec_())






