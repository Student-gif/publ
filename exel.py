

import os
from re import I

from QListenW import QListensW,lessonData
import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
conn = sqlite3.connect("exl.db")
cursor = conn.cursor()
 
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
        for i in range(2,52):
            self.tableWidget.setColumnWidth(i,80)
        self.tableWidget.setColumnWidth(1,60)
        self.tableWidget.setColumnWidth(0,40)
        self.tableWidget.setSpan(0,0,1,2)


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
        #присвоение табличного виджета

        for i in range(2,52):
            for g in range(1,43):
                self.tableWidget.setCellWidget(g,i,QListensW(lessonData()))
        
        #second column color and №
        for i in range(2,43,7):
            for j in range(0,7):
                
                self.tableWidget.setItem(i+j-1, 1, QTableWidgetItem())
                self.tableWidget.item(i+j-1,1).setText(str(j+1))
                self.tableWidget.item(i+j-1,1).setTextAlignment(Qt.AlignVCenter|Qt.AlignCenter)
        c = cursor.execute('SELECT  * FROM GROUPS')
        
        
        #??????
        groups = []
        for j in c:
            for h in j:
                groups.append(h)


        for i in range(2,52):
            self.tableWidget.setItem(0, i, QTableWidgetItem())
            self.tableWidget.item(0, i).setBackground(QColor(220,0,0)) 
            self.tableWidget.item(0, i).setText(groups[i-2])

           
                

               
 
 
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

        
        index = self.tableWidget.selectedIndexes()
        if action == item1:
            
            self.index2 = self.tableWidget.cellWidget(index[0].row(),index[0].column())
            
           
            
           
        #       print ('Вы выбрали первый вариант, текущее содержание текста строки:', ),
        #       c=self.tableWidget.selectedIndexes()
        #       if c.__len__()<2:
        #           print(c[0].column())
        #           h = QListensW.staticData.auditory
        #           
        #           print(h)
        #       else:
        #           pass

        
                



        if action == item2:
            print ('Вы выбрали второй вариант, текущее содержание текста строки:',)
            self.v = self.tableWidget.setCellWidget(index[0].row(),index[0].column(),QListensW(self.index2.staticData))
            print(self.v)
                                 
                     
        if action == item3:
                                 print ('Вы выбрали третий вариант, текущее содержание текста строки:', ),
def addToClipBoard(less:lessonData):
    command="echo "+less.__str__()+" | click"
    os.system(command=command)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())