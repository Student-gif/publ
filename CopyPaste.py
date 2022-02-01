from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class lessons():
    teacher='v'
    week=-1
    weelday=-1
    num=-1
    auditory=""
    teacherId=-1
    lesson= ''
    def __init__(self,teacher='', week=-1,weelday=-1,num=-1,auditory="",teacherId=-1, lesson= ''):
        self.teacher=teacher
        self.week = week
        self.weelday = weelday
        self.num = num
        self.auditory = auditory
        self.teacherId = teacherId
        self.lesson = lesson

class QListensW(QWidget):
   
    data=lessons()
    def __init__(self,data, *args, **kwargs):
        
        self.data=data
        super(QListensW, self).__init__(*args, **kwargs)
        lay = QVBoxLayout(self)
        lable=QLabel()
        lable.setText(data.teacher)
        lableSecond=QLabel()
        lableThird=QLabel()
        lableSecond.setText(data.auditory)
        lableThird.setText(data.lesson)
        lay.addWidget(lableThird)
        lay.addWidget(lableSecond)
        lay.addWidget(lable)
        self.setLayout(lay)
        


    
         