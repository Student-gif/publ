
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
 
 
class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
 
    def initUI(self):
                 # Установить заголовок и начальный размер
        self.setWindowTitle('QTableWidget demo')
        self.resize(500, 300)

        layout = QHBoxLayout()
        self.tableWidget = QTableWidget(42, 52)
        for i in range(42):
            self.tableWidget.setRowHeight(i,5)   
                 # Установить горизонтальный заголовок таблицы
        self.tableWidget.setHorizontalHeaderLabels (['Группы', 'пол', 'вес'])
        thing1 = 0  
        for i in range(6):
            self.tableWidget.setSpan(thing1,0,7,1)
            self.tableWidget.setItem(thing1, 0, QTableWidgetItem())
            self.tableWidget.item(thing1, 0).setBackground(QColor(100,100,150))    
            thing1 += 7
        for i in range(1,43,7):
            for j in range(0,7):
                self.tableWidget.setItem(i+j-1, 1, QTableWidgetItem())
                self.tableWidget.item(i+j-1,1).setText(str(j+1))
                     # Установить горизонтальное автоматическое масштабирование окна заполнения
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
 
                 # Разрешить щелчок правой кнопкой мыши для создания меню
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
                 # Привязать контекстное меню к функции слота generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        
 
    def generateMenu(self, pos):
                 # Рассчитать, сколько существует данных, по умолчанию -1,
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
 
                 # В таблице только две допустимые данные, поэтому всплывающее меню с правой кнопкой мыши поддерживают только первые две строки
        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction (u'Option one ')
            item2 = menu.addAction (u'Option 2 ')
            item3 = menu.addAction (u'Option 3 ')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
                         # Показать текст данных выбранной строки
            if action == item1:
                                 print ('Вы выбрали первый вариант, текущее содержание текста строки:', self.tableWidget.item (row_num, 0) .text (),
                      self.tableWidget.item(row_num, 1).text(),
                      self.tableWidget.item(row_num, 2).text())
            if action == item2:
                                 print ('Вы выбрали второй вариант, текущее содержание текста строки:', self.tableWidget.item (row_num, 0) .text (),
                      self.tableWidget.item(row_num, 1).text(),
                      self.tableWidget.item(row_num, 2).text())
            if action == item3:
                                 print ('Вы выбрали третий вариант, текущее содержание текста строки:', self.tableWidget.item (row_num, 0) .text (),
                      self.tableWidget.item(row_num, 1).text(),
                      self.tableWidget.item(row_num, 2).text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())