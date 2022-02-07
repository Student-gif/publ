import os
import win32clipboard
from QListenW import QListensW,lessonData
import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import Logick
 
layout = QHBoxLayout()
class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
    
    def initUI(self):
                 # Установить заголовок и начальный размер
        self.setWindowTitle('Ядро Расписание')
        
        
        self.tableWidget = QTableWidget(43, len(Logick.Auditories))
        #ширина ячеек
        for i in range(43):
            self.tableWidget.setRowHeight(i,80)

        # Установить горизонтальный заголовок таблицы
        for i in range(2,52):
            self.tableWidget.setColumnWidth(i,80)
        # отрисовка окна индикации
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
        
        #TODO счётчик дней недели и номера пары
        for i in range(2,52):

            for g in range(1,43):
               
                self.tableWidget.setCellWidget(g,i,QListensW(lessonData()))

        
        #Конфигурации столбца с занятиями 
        for i in range(2,43,7):
            for j in range(0,7):
                
                self.tableWidget.setItem(i+j-1, 1, QTableWidgetItem())
                self.tableWidget.item(i+j-1,1).setText(str(j+1))
                self.tableWidget.item(i+j-1,1).setTextAlignment(Qt.AlignVCenter|Qt.AlignCenter)
        #распаковка данных Аудитории с бд  
        h=[x[0] for x in Logick.Auditories]
        #конфигурация виджетов аудиторий
        for i in range(2,len(h)):
            self.tableWidget.setItem(0, i, QTableWidgetItem())
            self.tableWidget.item(0, i).setBackground(QColor(220,0,0)) 
            self.tableWidget.item(0, i).setText(h[i-2])
                 # Разрешить щелчок правой кнопкой мыши для создания меню
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                 # Привязать контекстное меню к функции слота generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        #инициализация таблицы
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
    
    def generateMenu(self, pos):
    
        menu = QMenu()
        item1 = menu.addAction (u'копировать')
        item2 = menu.addAction (u'вставить')
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
                         # Показать текст данных выбранной строки
        # копипаста 
        index = self.tableWidget.selectedIndexes()
        if action == item1:
            #self.indexData = self.tableWidget.cellWidget(index[0].row(),index[0].column())
            addToClipBoard = self.tableWidget.cellWidget(index[0].row(),index[0].column()).staticData
            data = addToClipBoard.__str__()
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(data)
            win32clipboard.CloseClipboard()


        if action == item2:
            print ('Вы выбрали второй вариант, текущее содержание текста строки:',)
            #self.v = self.tableWidget.setCellWidget(index[0].row(),index[0].column(),QListensW(self.index2.staticData))
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()
            
            w=self.tableWidget.cellWidget(index[0].row(),index[0].column())
            w.update(data)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())