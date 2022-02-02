from multiprocessing import Event

import PyQt5
from Logick import Lessons,Prepods,Auditories
from dataclasses import dataclass
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Logick import Lessons
@dataclass      
class lessonData():
    teacher: str = None
    auditory:str = None
    lesson:str = None
    week: int = -1
    weekday: int = -1
    num:int = -1
    teacherId:int = -1
    def __str__(self) -> str:
        return f'{self.teacher}|{self.auditory}|{self.lesson}|{self.week.__str__()}|{self.weekday}|{self.num}|{self.teacherId}'
    




class QListensW(QWidget):
    
    staticData = lessonData

    def __init__(self,staticdata, *args, **kwargs):
        
        self.data=staticdata
        super(QListensW, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)

        self.setLayout(lay)
        self.lineEditTeacher = QLineEdit()
      
        self.lineEditAuditory = QLineEdit()
        self.lineEditLesson = QLineEdit()
                  
        completerTeacher = QCompleter([s[0].__str__() for s in Prepods], self.lineEditTeacher)
        completerAuditory = QCompleter([s[0].__str__() for s in Auditories], self.lineEditAuditory)
        completerLesson = QCompleter([s[0].__str__() for s in Lessons], self.lineEditLesson)

        self.lineEditTeacher.setCompleter(completerTeacher)
        self.lineEditAuditory.setCompleter(completerAuditory)
        self.lineEditLesson.setCompleter(completerLesson)     
        self.lineEditTeacher.setText(staticdata.teacher)
        self.lineEditAuditory.setText(staticdata.auditory)
        self.lineEditLesson.setText(staticdata.lesson)
        lay.addWidget(self.lineEditTeacher)
        lay.addWidget(self.lineEditLesson)
        lay.addWidget(self.lineEditAuditory)

        self.lineEditLesson.returnPressed.connect(self.CustomEventEnter)
        self.lineEditTeacher.returnPressed.connect(self.CustomEventEnter)
        self.lineEditAuditory.returnPressed.connect(self.CustomEventEnter)
                
    def CustomEventEnter(self):
        print('event')
        self.staticData.auditory = self.lineEditAuditory.text()
        self.staticData.lesson = self.lineEditLesson.text()
        self.staticData.teacher = self.lineEditTeacher.text()