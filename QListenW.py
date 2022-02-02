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
    




class QListensW(QWidget):\
    
    staticData = lessonData

    def __init__(self,staticdata, *args, **kwargs):
        
        self.data=staticdata
        super(QListensW, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)
        
       
        
        lable=QLabel()
        
        #lable.setText(data.teacher)
        #lableSecond=QLabel()
        #lableThird=QLabel()
        #lableSecond.setText(data.auditory)
        #lableThird.setText(data.lesson)
       #lay.addWidget(lableThird)
       # lay.addWidget(lableSecond)
       # lay.addWidget(lable)
        #self.combo.addItems([i])
        self.setLayout(lay)
        self.lineEditTeacher = QLineEdit()
      
        self.lineEditAuditory = QLineEdit()
        self.lineEditLesson = QLineEdit()

        self.tipTeacher = [] 
        self.tipLessons = []
        self.tipAuditories = []
        
        for g in Prepods:
           for i in g:
               self.tipTeacher.append(i)
               
        print(self.tipAuditories)
        for g in Lessons:
           for i in g:
               self.tipLessons.append(i)   
        for g in Auditories:
           for i in g:
               self.tipAuditories.append(i)    
        completerTeacher = QCompleter(self.tipTeacher, self.lineEditTeacher)
        completerAuditory = QCompleter(self.tipAuditories, self.lineEditAuditory)
        completerLesson = QCompleter(self.tipLessons, self.lineEditLesson)

        self.lineEditTeacher.setCompleter(completerTeacher)
        self.lineEditAuditory.setCompleter(completerAuditory)
        self.lineEditLesson.setCompleter(completerLesson)     
        self.lineEditTeacher.setText(staticdata.teacher)
        self.lineEditAuditory.setText(staticdata.auditory)
        self.lineEditLesson.setText(staticdata.lesson)
        lay.addWidget(self.lineEditTeacher)
        lay.addWidget(self.lineEditLesson)
        lay.addWidget(self.lineEditAuditory)