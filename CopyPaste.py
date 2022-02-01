from exel import *

class CellObj(Table):
    def __init__(self):
        super().__init__()
        self.makeObj()
        self.teacherid= 1
        self.group ="Чип" 
        self.lesson = 'русский'
    def makeObj(self,teacherid,group,lesson):
        object = [lesson,group,teacherid]
        return object


