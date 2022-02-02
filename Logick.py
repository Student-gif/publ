import sqlite3
conn = sqlite3.connect("exl.db")
cursor = conn.cursor()
Groups = cursor.execute('SELECT * FROM GROUPS').fetchall()
Auditories = cursor.execute('SELECT Auditories FROM AUDITORIES').fetchall()
Prepods = cursor.execute('SELECT PREPODS FROM PREPODS WHERE IdTeacher>0').fetchall()
Lessons = cursor.execute('SELECT NameLesson FROM LESSONS WHERE NameLesson not Null').fetchall()
