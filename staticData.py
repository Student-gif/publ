import string
import sqlite3

g = ' '
#print(','.join('"'+h.strip().__str__()+'"' for h in g.split('	')))
GROUPS=["ЧИПфд-01-21","ЧИПфд-02-21","ЧСАфд-01-21","ЧСАфд-02-21","ЧИПфд-01-20","ЧСАфд-01-20","ЧПКфд-01-20","ЧПКфд-02-20","ЧИПфд-01-19","ЧСАфд-01-19","ЧПКфд-01-19","ЧИПфд-01-18","ЧСАфд-01-18","ЧПКфд-01-18","ЧЭБфд-01-21","ЧЭБфд-02-21","ЧЭБфд-01-20","ЧЭБфд-02-20","ЧЭБфд-01-19","ЧФУфд-01-21","ЧФУфд-02-21","ЧФУфд-01-20","ЧФУфд-02-20","ЧФУфд-01-19","ЧФУфд-02-19","ЧФУфд-01-18","ЧФУфд-02-18","ЧСЛфд-01-21","ЧСЛфд-01-20","ЧСЛфд-01-19","ЧСЛфд-01-18","ЧНПфд-01-21","ЧДЗфд-01-21","ЧНПфд-01-20","ЧДЗфд-01-20","ЧНПфд-01-19","ЧДЗфд-01-19","ЧДЗфд-01-18","ЧПВфд-01-21","ЧПВфд-02-21","ЧРРфд-01-21","ЧППфд-01-20","ЧПВфд-01-20","ЧРРфд-01-20","ЧППфд-01-19","ЧПВфд-01-19","ЧРРрд-01-19","ЧППфд-01-18","ЧПВфд-01-18","ЧРРфд-01-18"]
PREPODS=['Андросова П.К.',
'Аникина Г.Ю.',
'Антонова Е.И.',
'Бараш Л.А.',
'Белоусова И.А.',
'Великанов Е.Э.',
'Вершинина Н.П.',
'Габуния А.Я.',
'Горнушкина О.Н.',
'Горохова А.А.',
'Григорьева О.А.',
'Догадов Д.И.',
'Дымов Е.В.',
'Жук Л.И.',
'Зорова О.В.',
'Игошев М.В.',
'Иджиян Т.Ю.',
'Исаева В.В.',
'Истягина И.В.',
'Казакова Н.А.',
'Казарова Л.Р.',
'Караманян М.И.',
'Карпов А.И.',
'Каспарян К.И.',
'Кислова М.Е.',
'Корниенко Н.Я.',
'Кузнецова О.О.',
'Лежнева О.Д.',
'Ливенцова Т.Д.',
'Макарова К.Б.',
'Мелентьева А.Д.',
'Миносян Р.Х.',
'Муллакова А. М.',
'Муллакова А.М.',
'Нагорняя М.В.',
'Нубарян В.А.',
'Огаркова Л.А.',
'Панова Н.А.',
'Пересунько-Гончарова Т.В.',
'Подгорнова Т.П.',
'Родионова И.А.',
'Сарахатунова И.В.',
'Сигова Е.В.',
'Силаев А.И.',
'Слюсаренко Л.Э.',
'Соболева Н.Л.',
'Суркова Ю.А.',
'Сущенко С.С.',
'Талантова Е.А.',
'Цатурян С.А.',
'Цымбалова Ю.С.',
'Чайкина М.Л.',
'Чехова Т.М.',
'Юргина Л.А.',
'Яворский В.Н.',
'Жук Л.И./Иджиян Т.Ю.']
AUDITORIES=['1-5',
'1-6',
'1-7',
'1-8',
'1-9',
'1-11',
'1-13',
'1-15',
'1-16',
'1-17',
'1-Лаб',
'1-УТЦ',
'3-30',
'3-30а',
'3-34',
'3-Лаб',
'4-26',
'4-27',
'4-29',
'4-31',
'4-32',
'4-33',
'1-стадион',
'2-стадион',
'3-стадион',
'1-ЭИОС',
'1-13/1-15',
'1-5/1-15',
'1-5/1-6',]

 
conn = sqlite3.connect("exl.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
   AUDITORIES TEXT,
   PREPODS TEXT,
   GROUPS TEXT);
""")
for i in GROUPS:
    pass
conn.commit()


 