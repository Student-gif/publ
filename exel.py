from CopyPaste import QListensW,lessons

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

 
layout = QHBoxLayout()
class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
    
    def initUI(self):
                 # Установить заголовок и начальный размер
        self.setWindowTitle('QTableWidget demo')
        self.resize(500, 300)
        
        
        self.tableWidget = QTableWidget(43, 52)
        #ширина ячеек
        for i in range(43):
            self.tableWidget.setRowHeight(i,80)

                 # Установить горизонтальный заголовок таблицы
        for i in range(51):
            self.tableWidget.setColumnWidth(i,80)

        thing1 = 1  
        #color cells
        weekdays = ['п\nо\nн\nе\nд\nе\nл\nь\nн\nи\nк','в\nт\nо\nр\nн\nи\nк','с\nр\nе\nд\nа','ч\nе\nт\nв\nе\nр\nг','п\nя\nт\nн\nи\nц\nа','С\nу\nб\nб\nо\nт\nа']        
        for i in range(6):
            self.tableWidget.setSpan(thing1,0,7,1)
            self.tableWidget.setItem(thing1, 0, QTableWidgetItem())
            self.tableWidget.item(thing1,0).setText(weekdays[i])
            self.tableWidget.item(thing1,0).setTextAlignment(Qt.AlignVCenter|Qt.AlignCenter)
            self.tableWidget.item(thing1,0).setFont(QFont("Arial", 16))
            self.tableWidget.item(thing1, 0).setBackground(QColor(0,160,0))

                
            thing1 += 7
        self.tableWidget.setCellWidget(3,3,QListensW(lessons(teacher='bb',week=-1,weelday=-1,num=-1,auditory="das",teacherId=-1,lesson='bb')))
        
        #second column color and №
        for i in range(2,43,7):
            for j in range(0,7):
                self.tableWidget.setItem(i+j-1, 1, QTableWidgetItem())
                self.tableWidget.item(i+j-1,1).setText(str(j+1))
        for i in range(52):
            self.tableWidget.setItem(0, i, QTableWidgetItem())
            self.tableWidget.item(0, i).setBackground(QColor(220,0,0)) 
               
 
 
                 # Разрешить щелчок правой кнопкой мыши для создания меню
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                 # Привязать контекстное меню к функции слота generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        
 
    def generateMenu(self, pos):
                 # Рассчитать, сколько существует данных, по умолчанию -1,
 
                 # В таблице только две допустимые данные, поэтому всплывающее меню с правой кнопкой мыши поддерживают только первые две строки
        
        menu = QMenu()
        item1 = menu.addAction (u'копировать')
        item2 = menu.addAction (u'вставить')
        item3 = menu.addAction (u'закрыть')
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
                         # Показать текст данных выбранной строки
        if action == item1:
                print ('Вы выбрали первый вариант, текущее содержание текста строки:', ),
                self.tableWidget.selectionModel().selection().indexes()

        if action == item2:
                                 print ('Вы выбрали второй вариант, текущее содержание текста строки:',)
                     
        if action == item3:
                                 print ('Вы выбрали третий вариант, текущее содержание текста строки:', ),
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())