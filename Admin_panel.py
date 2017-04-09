# Aplikacja pozwalająca Adminowi na zmiany i edycje danych bez znajomości struktury danych
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QTableWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# --------------------------------------------------------
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.label1 = QLabel(self)
        self.button1 = QPushButton("Show", self)
        self.cb = QComboBox(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Admin Panel")
        self.move(10, 10)
        self.resize(820, 500)

        self.set_labels()
        self.set_buttons()
        self.table.close()
        self.choose_table()
        self.db.setDatabaseName("./DataBase/database.db")
        self.show()

    def set_labels(self):
        self.label1.move(14, 14)
        self.label1.setText("Choose table: ")

    def set_buttons(self):
        self.button1.move(150, 8)
        self.button1.clicked.connect(self.show_table)

    def choose_table(self):
        self.cb.move(90, 10)
        self.cb.addItems(["city", "client", "flat", "rent"])

    def show_table(self):
        if not self.db.open():
            QMessageBox.critical(None, "Cannot open database",
                                 "Unable to establish a database connection.\n"
                                 "This example needs SQLite support. Please read the Qt SQL "
                                 "driver documentation for information how to build it.\n\n"
                                 "Click Cancel to exit.",
                                 QMessageBox.Cancel)
            return False
        else:
            x = 0
            question = "SELECT * FROM " + self.cb.currentText()
            self.table.setRowCount(0)

            if self.cb.currentText() == "city":
                self.table.setColumnCount(3)
                x = 3
                self.table.setHorizontalHeaderLabels(["ID_CITY", "NAME", "ZIP_CODE"])
                row = 0
            if self.cb.currentText() == "client":
                self.table.setColumnCount(6)
                x = 6
                self.table.setHorizontalHeaderLabels(["ID_CLIENT", "NICKNAME", "NAME", "SURNAME", "ID_NUMBER", "CARD_NUMBER"])
                row = 0
            if self.cb.currentText() == "flat":
                self.table.setColumnCount(11)
                x = 11
                self.table.setHorizontalHeaderLabels(["ID_FLAT", "AVAILABILITY", "START_DATE", "END_DATE", "PRICE",
                                                      "NUMBER_OF_ROOMS", "AMOUNT_OF_PEOPLE", "ANIMALS", "CHILDS",
                                                      "PARKING_SPACE", "ID_CITY"])
                row = 0
            if self.cb.currentText() == "rent":
                self.table.setColumnCount(5)
                x = 5
                self.table.setHorizontalHeaderLabels(["ID_CITY", "NAME", "ZIP_CODE"])
                row = 0

            query = QSqlQuery(question)
            while query.next():
                self.table.insertRow(row)

                if x >= 3:
                    i0 = QTableWidgetItem(str(query.value(0)))
                    self.table.setItem(row, 0, i0)
                    i1 = QTableWidgetItem(str(query.value(1)))
                    self.table.setItem(row, 1, i1)
                    i2 = QTableWidgetItem(str(query.value(2)))
                    self.table.setItem(row, 2, i2)
                if x >= 5:
                    i3 = QTableWidgetItem(str(query.value(3)))
                    self.table.setItem(row, 3, i3)
                    i4 = QTableWidgetItem(str(query.value(4)))
                    self.table.setItem(row, 4, i4)
                if x >= 6:
                    i5 = QTableWidgetItem(str(query.value(5)))
                    self.table.setItem(row, 5, i5)
                if x >= 11:
                    i6 = QTableWidgetItem(str(query.value(6)))
                    self.table.setItem(row, 6, i6)
                    i7 = QTableWidgetItem(str(query.value(7)))
                    self.table.setItem(row, 7, i7)
                    i8 = QTableWidgetItem(str(query.value(8)))
                    self.table.setItem(row, 8, i8)
                    i9 = QTableWidgetItem(str(query.value(9)))
                    self.table.setItem(row, 9, i9)
                    i10 = QTableWidgetItem(str(query.value(10)))
                    self.table.setItem(row, 10, i10)
                row = row + 1

            self.table.show()
            self.table.move(10, 40)
            self.table.resize(800, 300)
        return True


# --------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
