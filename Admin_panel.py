# Aplikacja pozwalająca Adminowi na zmiany i edycje danych bez znajomości struktury danych
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QTableWidget, QMessageBox, \
    QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# --------------------------------------------------------
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.label1 = QLabel(self)
        self.button1 = QPushButton("Show", self)
        self.button2 = QPushButton("Delete", self)
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
        self.table.itemChanged.connect(self.updating)

    def set_labels(self):
        self.label1.move(14, 14)
        self.label1.setText("Choose table: ")

    def set_buttons(self):
        self.button1.move(150, 8)
        self.button1.clicked.connect(self.show_table)
        self.button2.move(10, 350)
        self.button2.clicked.connect(self.deleting)

    def choose_table(self):
        self.cb.move(90, 10)
        self.cb.addItems(["city", "client", "flat", "rent"])

    def show_table(self):
        self.table.move(10, 40)
        self.table.resize(800, 300)
        if not self.db.open():
            QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
            return False
        else:
            x = 0
            question = "SELECT * FROM " + self.cb.currentText()
            self.table.setRowCount(0)

            if self.cb.currentText() == "city":
                self.table.setColumnCount(3)
                x = 3
                self.table.setHorizontalHeaderLabels(["ID_CITY", "NAME", "ZIP_CODE"])
            if self.cb.currentText() == "client":
                self.table.setColumnCount(6)
                x = 6
                self.table.setHorizontalHeaderLabels(
                    ["ID_CLIENT", "NICKNAME", "NAME", "SURNAME", "ID_NUMBER", "CARD_NUMBER"])
            if self.cb.currentText() == "flat":
                self.table.setColumnCount(11)
                x = 11
                self.table.setHorizontalHeaderLabels(["ID_FLAT", "AVAILABILITY", "START_DATE", "END_DATE", "PRICE",
                                                      "NUMBER_OF_ROOMS", "AMOUNT_OF_PEOPLE", "ANIMALS", "CHILDS",
                                                      "PARKING_SPACE", "ID_CITY"])
            if self.cb.currentText() == "rent":
                self.table.setColumnCount(5)
                x = 5
                self.table.setHorizontalHeaderLabels(["ID_RENT", "ID_FLAT", "ID_CLIENT", "START_DATE", "END_DATE"])

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
        self.db.close()
        return True

    def updating(self):
        ok = self.db.open()
        if not ok:
            QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
            return False
        else:
            column = self.table.currentColumn()
            row = self.table.currentRow()
            if column < 0 or row < 0:
                return False

            id = self.table.item(row, 0).text()
            value = self.table.currentItem().text()

            if self.cb.currentText() == "city":
                columns = ["id_city", "name", "zip_code"]
            if self.cb.currentText() == "client":
                columns = ["id_client", "nickname", "name", "surname", "id_number", "card_number"]
            if self.cb.currentText() == "flat":
                columns = ["id_flat", "availability", "start_date", "end_date", "price", "number_of_rooms",
                           "amount_of_people", "animals", "childs", "parking_space", "id_city"]
            if self.cb.currentText() == "rent":
                columns = ["id_rent", "id_flat", "id_client", "start_date", "end_date"]

            query = QSqlQuery()
            question = "UPDATE " + self.cb.currentText() + " SET " + columns[column] + " = '" + value +"' WHERE " + columns[0] + " = " + id
            print(question)
            query.prepare(question)
            ok = query.exec_()
            if not ok:
                QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
        self.db.commit()
        self.db.close()
        return True

    def deleting(self):
        ok = self.db.open()
        if not ok:
            QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
            return False
        else:
            rows = self.table.selectionModel().selectedRows()
            index = []

            if self.cb.currentText() == "city":
                column = "id_city"
            if self.cb.currentText() == "client":
                column = "id_client"
            if self.cb.currentText() == "flat":
                column = "id_flat"
            if self.cb.currentText() == "rent":
                column = "id_rent"

            for i in rows:
                index.append(i.row())
            index.sort(reverse = True)

            for i in index:
                id = self.table.item(i, 0).text()
                self.table.removeRow(i)
                question = "DELETE FROM " + self.cb.currentText() + " WHERE " + column + " = " + id
                print(question)
                query = QSqlQuery()
                query.prepare(question)
                ok = query.exec_()
                if not ok:
                    QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
        self.db.close()
        return True
# --------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
