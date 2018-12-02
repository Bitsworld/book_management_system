import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class ReviseBookDialog(QDialog):
    revise_successful_signal = pyqtSignal()
    revise_back_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(ReviseBookDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.h_layout_revise_button = QHBoxLayout()
        self.h_layout_back_button = QHBoxLayout()
        self.fally_layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(20)
        title_label_font = QFont()
        title_label_font.setPixelSize(20)
        button_font = QFont()
        button_font.setPixelSize(18)

        self.title_label = QLabel(' 修改书籍')
        self.title_label.setFont(title_label_font)
        self.title_label.setMargin(8)

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

        self.add_num_label = QLabel('数   量:')
        self.add_num_label.setFont(font)
        self.add_num_edit = QLineEdit()
        self.add_num_edit.setFont(font)
        self.add_num_edit.setValidator(QIntValidator())
        self.add_num_edit.setStyleSheet("background:#F0F0F0")
        self.add_num_edit.setReadOnly(True)

        self.form_layout.addRow('', self.title_label)
        self.form_layout.addRow(self.book_name_label, self.book_name_edit)
        self.form_layout.addRow(self.book_id_label, self.book_id_edit)
        self.form_layout.addRow(self.author_label, self.author_edit)
        self.form_layout.addRow(self.publisher_label, self.publisher_edit)
        self.form_layout.addRow(self.abstract_label, self.abstract_edit)
        self.form_layout.addRow(self.publish_date_label, self.publish_date_edit)
        self.form_layout.addRow(self.add_num_label, self.add_num_edit)
        self.form_layout.setSpacing(10)
        '''
        self.book_name_revise = QLabel('修改')
        self.book_name_revise.setFixedHeight(20)
        # self.book_name_revise.setStyleSheet('background:#fff')
        self.book_name_revise.setStyleSheet('color:red')
        #self.book_name_revise.setFixedWidth(180)
        self.book_id_revise = QLabel('')
        self.book_id_revise.setFixedHeight(20)
        # self.book_id_revise.setStyleSheet('background:#6EC21B')
        self.book_id_revise.setStyleSheet('color:red')
        self.author_revise = QLabel('修改')
        self.author_revise.setFixedHeight(20)
        # self.author_revise.setStyleSheet('background:#6EC21B')
        self.author_revise.setStyleSheet('color:red')
        self.publisher_revise = QLabel('修改')
        self.publisher_revise.setFixedHeight(20)
        # self.publisher_revise.setStyleSheet('background:#6EC21B')
        self.publisher_revise.setStyleSheet('color:red')
        self.abstract_revise = QLabel('修改')
        self.abstract_revise.setFixedHeight(20)
        # self.abstract_revise.setStyleSheet('background:#6EC21B')
        self.abstract_revise.setStyleSheet('color:red')
        self.publish_date_revise = QLabel('修改')
        self.publish_date_revise.setFixedHeight(20)
        # self.publish_date_revise.setStyleSheet('background:#6EC21B')
        self.publish_date_revise.setStyleSheet('color:red')
        self.book_num_revise = QLabel('修改')
        self.book_num_revise.setFixedHeight(20)
        # self.book_num_revise.setStyleSheet('background:#6EC21B')
        self.book_num_revise.setStyleSheet('color:red')

        self.v_layout.addStretch(6)
        self.v_layout.addWidget(self.book_name_revise)
        self.v_layout.addStretch(6)
        self.v_layout.addWidget(self.author_revise)
        self.v_layout.addStretch(1)
        self.v_layout.addWidget(self.publisher_revise)
        self.v_layout.addStretch(9)
        self.v_layout.addWidget(self.abstract_revise)
        self.v_layout.addStretch(1)
        self.v_layout.addWidget(self.publish_date_revise)
        self.v_layout.addStretch(1)
        self.v_layout.addWidget(self.book_num_revise)
        '''


        self.revise_button = QPushButton('确认修改')
        self.revise_button.setFixedHeight(32)
        self.revise_button.setFixedWidth(120)
        self.revise_button.setFont(button_font)
        self.back_button = QPushButton('返  回')
        self.back_button.setFont(button_font)
        self.back_button.setFixedWidth(120)
        self.back_button.setFixedHeight(32)

        self.h_layout_revise_button.addWidget(self.revise_button, Qt.AlignCenter)
        self.h_layout_back_button.addWidget(self.back_button, Qt.AlignCenter)

        form_widget = QWidget()
        # form_widget.setStyleSheet('background:#eaeaea')
        form_widget.setFixedHeight(400)
        '''
        v_widget = QWidget()
        v_widget.setFixedHeight(350)
        v_widget.setFixedWidth(40)
        '''
        # v_widget.setStyleSheet('background:#f6a4ef')
        h_revise_widget = QWidget()
        h_back_widget = QWidget()

        form_widget.setLayout(self.form_layout)
        # v_widget.setLayout(self.v_layout)

        self.h_layout.addWidget(form_widget, 0, Qt.AlignLeft|Qt.AlignTop)
        # self.h_layout.addWidget(v_widget, 0, Qt.AlignTop)

        h_revise_widget.setLayout(self.h_layout_revise_button)
        h_back_widget.setLayout(self.h_layout_back_button)

        widget = QWidget()
        widget.setLayout(self.h_layout)

        self.fally_layout.addWidget(widget)
        self.fally_layout.addWidget(h_revise_widget)
        self.fally_layout.addWidget(h_back_widget)

        self.setLayout(self.fally_layout)

        self.book_id_edit.textChanged.connect(self.book_id_edit_changed)
        self.revise_button.clicked.connect(self.revise_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

        self.setWindowTitle('修 改 书 籍')
        self.setGeometry(400, 250, 300, 500)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.setWindowModality(Qt.WindowModal)
        self.show()

    def book_id_edit_changed(self):
        book_id = self.book_id_edit.text()
        if book_id == '':
            self.book_name_edit.clear()
            self.author_edit.clear()
            self.publisher_edit.clear()
            self.abstract_edit.clear()
            self.publish_date_edit.clear()
            self.add_num_edit.clear()

            self.book_name_edit.setReadOnly(True)
            self.author_edit.setReadOnly(True)
            self.publisher_edit.setReadOnly(True)
            self.abstract_edit.setReadOnly(True)
            self.publish_date_edit.setReadOnly(True)
            self.add_num_edit.setReadOnly(True)

            self.book_name_edit.setStyleSheet("background:#F0F0F0")
            self.author_edit.setStyleSheet("background:#F0F0F0")
            self.publisher_edit.setStyleSheet("background:#F0F0F0")
            self.abstract_edit.setStyleSheet("background:#F0F0F0")
            self.publish_date_edit.setStyleSheet("background:#F0F0F0")
            self.add_num_edit.setStyleSheet("background:#F0F0F0")
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
            sql = "SELECT BookName, BookId, Author, Publisher, Abstract, PublishTime,NumStorage FROM book WHERE BookId='%s'" % (book_id)
            query.exec_(sql)
            print('运行到sql后面')
            if query.first():
                print('运行到判断')
                self.book_name_edit.setText(str(query.value('BookName')))
                self.author_edit.setText(str(query.value('Author')))
                self.publisher_edit.setText(str(query.value('Publisher')))
                self.abstract_edit.setText(str(query.value('Abstract')))
                self.publish_date_edit.setDate(QDate.fromString(query.value('PublishTime').toString('yyyy-MM-dd'),  'yyyy-MM-dd'))
                self.add_num_edit.setText(str(query.value('NumStorage')))
                # self.publish_date_edit.setText(query.value('PublishTime').toString('yyyy-MM-dd'))
                self.book_name_edit.setReadOnly(False)
                self.author_edit.setReadOnly(False)
                self.publisher_edit.setReadOnly(False)
                self.abstract_edit.setReadOnly(False)
                self.publish_date_edit.setReadOnly(False)
                self.add_num_edit.setReadOnly(False)

                self.book_name_edit.setStyleSheet("background:#fff")
                self.author_edit.setStyleSheet("background:#fff")
                self.publisher_edit.setStyleSheet("background:#fff")
                self.abstract_edit.setStyleSheet("background:#fff")
                self.publish_date_edit.setStyleSheet("background:#fff")
                self.add_num_edit.setStyleSheet("background:#fff")
            else:
                self.book_name_edit.clear()
                self.author_edit.clear()
                self.publisher_edit.clear()
                self.abstract_edit.clear()
                self.publish_date_edit.clear()
                self.add_num_edit.clear()

                self.book_name_edit.setReadOnly(True)
                self.author_edit.setReadOnly(True)
                self.publisher_edit.setReadOnly(True)
                self.abstract_edit.setReadOnly(True)
                self.publish_date_edit.setReadOnly(True)
                self.add_num_edit.setReadOnly(True)

                self.book_name_edit.setStyleSheet("background:#F0F0F0")
                self.author_edit.setStyleSheet("background:#F0F0F0")
                self.publisher_edit.setStyleSheet("background:#F0F0F0")
                self.abstract_edit.setStyleSheet("background:#F0F0F0")
                self.publish_date_edit.setStyleSheet("background:#F0F0F0")
                self.add_num_edit.setStyleSheet("background:#F0F0F0")
            return

    def revise_button_clicked(self):
        book_id = self.book_id_edit.text()
        book_name = self.book_name_edit.text()
        author = self.author_edit.text()
        publisher = self.publisher_edit.text()
        abstract = self.abstract_edit.toPlainText()
        publish_date = self.publish_date_edit.text()
        add_num = self.add_num_edit.text()
        if book_id == '':
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
            sql = "SELECT BookName, BookId, Author, Publisher, Abstract, PublishTime,NumStorage FROM book WHERE BookId='%s'" % (book_id)
            query.exec_(sql)
            print('运行到sql后面')
            if query.first():
                print('运行到判断')
                updata_sql = "UPDATE book SET BookName = '%s', Publisher = '%s',PublishTime = '%s', Author = '%s',  Abstract = '%s', NumStorage = %d WHERE BookId = '%s'" % (book_name, publisher, publish_date, author, abstract, int(add_num), book_id)
                print(updata_sql)
                query.exec_(updata_sql)
                db.commit()
                self.revise_successful_signal.emit()
                print(QMessageBox.information(self, '提示', '书籍信息更新成功', QMessageBox.Yes, QMessageBox.Yes))
                self.close()
            else:
                print(QMessageBox.information(self, '提示', '请输入正确的书号！', QMessageBox.Yes, QMessageBox.Yes))
                return


    def back_button_clicked(self):
        self.revise_back_signal.emit()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReviseBookDialog()
    sys.exit(app.exec_())
