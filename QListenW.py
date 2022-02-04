from distutils.command.upload import upload
from email.headerregistry import Group
from multiprocessing import Event
import re

import PyQt5
from Logick import Lessons,Prepods,Auditories,Groups
from dataclasses import dataclass
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Logick import Lessons
    
class lessonData():
    teacher: str = ""
    auditory:str = ""
    lesson:str = ""
    week: int = -1
    weekday: int = -1
    num:int = -1
    teacherId:int = -1
    
    def updatedata(self,data):
        ar=data.split(';')
        self.teacher=ar[0]
        self.auditory =ar[1]
        self.lesson=ar[2]
        return True
    def __str__(self) -> str:
        return f'{self.teacher};{self.auditory};{self.lesson};{self.week.__str__()};{self.weekday};{self.num};{self.teacherId}'
    



class QListensW(QWidget):
    
    staticData = lessonData

    def __init__(self,staticData, *args, **kwargs):
        self.staticData=staticData
        super(QListensW, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)

        self.setLayout(lay)
        self.lineEditTeacher = QLineEdit()
      
        self.lineEditGroups = QLineEdit()
        self.lineEditLesson = QLineEdit()
                  
        completerTeacher = QCompleter([s[0].__str__() for s in Prepods], self.lineEditTeacher)
        completerAuditory = QCompleter([s[0].__str__() for s in Groups], self.lineEditGroups)
        completerLesson = QCompleter([s[0].__str__() for s in Lessons], self.lineEditLesson)

        self.lineEditTeacher.setCompleter(completerTeacher)
        self.lineEditGroups.setCompleter(completerAuditory)
        self.lineEditLesson.setCompleter(completerLesson)     
        
        lay.addWidget(self.lineEditTeacher)
        lay.addWidget(self.lineEditLesson)
        lay.addWidget(self.lineEditGroups)

        self.lineEditLesson.editingFinished.connect(self.CustomEventEnter)
        self.lineEditTeacher.editingFinished.connect(self.CustomEventEnter)
        self.lineEditGroups.editingFinished.connect(self.CustomEventEnter)

        self.uploadUi()

    def update(self,data):
        self.staticData.updatedata(data)
        self.uploadUi()

    def uploadUi(self):
        self.lineEditTeacher.setText(self.staticData.teacher)
        self.lineEditGroups.setText(self.staticData.auditory)
        self.lineEditLesson.setText(self.staticData.lesson)
     

    
    def CustomEventEnter(self):
        print('event')
        self.staticData.auditory = self.lineEditGroups.text()
        self.staticData.lesson = self.lineEditLesson.text()
        self.staticData.teacher = self.lineEditTeacher.text()
