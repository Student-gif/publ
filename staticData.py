import sqlite3
g='Аудит,Бизнес-планирование,История искусств,Декоративно-прикладное искусство и народные промыслы,Практика производственная (преддипломная),Графический дизайн,Организация обслуживания,Биология,Иностранный язык,Правовое обеспечение профессиональной деятельности,Анатомия,Экономика отрасли,Ландшафтный дизайн,Физическая культура,Литература,Введение в специальность,включая информатику,Администрирование сетевых операционных систем,Информационное общество (включая информатику и обществознание),Информационные технологии в профессиональной деятельности,Метрология и стандартизация,Организация и ведение процессов приготовления,оформления и подготовки к реализации полуфабрикатов для блюд,кулинарных изделий сложного ассортимента,Технология сложных хлебобулочных,мучных кондитерских изделий,Информационное общество (обществознание),Психология общения,Основы анализа бухгалтерской отчётности,Компьютерная графика,География,Астрономия,Кавказская и кубанская кухня,Введение в специальность (информатика),Безопасность жизнедеятельности,Дополнительная работа под руководством преподавателя,Зарубежная кухня,Технология приготовления сложной горячей кулинарной продукции,Основы спортивной тренировки,Организация физкультурно-спортивной работы,Организация расчетов с бюджетом и внебюджетными фондами,Дискретная математика,Контроль качества продукции,1С: Бухгалтерия,Основы банковского дела,Самостоятельная работа,Практические основы бухгалтерского учета имущества организации,Бухгалтерский учет и отчетность в бюджетных организациях,История мировой культуры,Производственная практика,Дизайн в сфере применения,Практика учебная,Цветоводство и декоративное древоводство,Гигиенические основы физической культуры и спорта,Менеджмент ФК и спорта,Основы флористики,Базовые и новые физкультурно-спортивные виды деятельности с методикой оздоровительной тренировки,Русский язык,Избранный вид спорта с методикой тренировки и руководства соревновательной деятельностью спортсменов,История,Инженерная,компьютерная графика,Безопасность функционирования информационных систем,Операционные системы и среды,Правовые основы профессиональной деятельности,Приготовление,оформление и подготовка к реализации хлебобулочных,мучных кондитерских изделий разнообразного ассортимента,Технология приготовления простой и основной кулинарной продукции,Этика профессиональной деятельности,Основы бухгалтерского учета,Художественное проектирование изделий декоративно-прикладного и народного искусства,Менеджмент,Декоративная дендрология,Технология приготовления коктейлей,Родной язык,Основы безопасности жизнедеятельности,Композиция,оформление и подготовка к реализации холодных и горячих сладких блюд,десертов,напитков разнообразного ассортимента,Оборудование предприятий общественного питания,Технология физкультурно-спортивной деятельности,Налоги и налогообложение,Математика,Математическое и имитационное моделирование,Практика производственная,Иностранный язык в профессиональной деятельности,Методы расчёта основных технико-экономических показателей дзайна,Основы менеджмента  и маркетинга,Основы философии,Рисунок,Дизайн и рекламные технологии,Естествознание,Фитодизайн,Русский язык и культура речи,Основы биомеханики,История дизайна,Основы конструкторско-технологического обеспечения дизайна,Информатика,Операционные системы,Организация и контроль текущей деятельности подчиненного персонала,Приготовление и подготовка к реализации полуфабрикатов для блюд,кулинарных изделий разнообразного ассортимента,Теоретические и прикладные аспекты методической работы педагога по физической культуре и спорту,Основы проектной и компьютерной графики,Основы экономики,Защита растений,Живопись,Организация хранения и контроль запасов сырья,Информационное обеспечение профессиональной деятельности,Основы исполнительского мастерства (художественное стекло,бисер),Охрана труда,Техническое оснащение и организация рабочего места,Физика,Математика и информатика,Основы программирования,Практические основы бухгалтерского учета источников формирования имущества организации,Экономика организации,Рисунок с основами перспективы,Дизайн-проектирование (композиция,макетирование,современные концепции в искусстве),Региональные кухни,Лечебная физическая культура и массаж,Обществознание,Основы проектирования объектов садово-паркового строительства,Компьютерные сети,Проектирование предприятий общественного питания,Управление структурным подразделением организации,Перспектива,менеджмента и маркетинга,Выполнение работ по профессии Цветовод,Живопись с основами цветоведения,Физиология питания,Информационное общество (информатика),Первичная обработка продукции,Техническое оснащение организаций питания,Численные методы,Прикладная математика,Финансы,денежное обращение и кредит,Бухгалтерская технология проведения и оформления инвентаризации,Экономика,Основы врачебного контроля,Обществознание (включая Право),Организация администрирования компьютерных систем,Технология приготовления хлебобулочных изделий и хлеба,Эстетика и дизайн в оформлении кулинарных и кондитерских изделий,Педагогика,Экологические основы природопользования,Садово-парковое строительство и хозяйство,Колористика,оформление и подготовка к реализации горячих блюд,кулинарных изделий,закусок разнообразного ассортимента,Элементы высшей математики,Химия,Основы стандартизации,сертификации и метрологии,Материаловедение,Спортивная физиология,Технологии физического уровня передачи данных,Управление структурным подразделением,Маркетинг ландшафтных услуг,Учебная практика (изучение памятников искусства в других городах),Технология приготовления блюд и кулинарных изделий для диетического,лечебно-профилактического питания,Элементы математической логики,Химия с элементами биологии,Основы управления качеством,Основы информационного и библиографического поиска,Физиология с основами биохимии,Экономические и правовые основы профессиональной деятельности,Цветовод (цветоводство в благоустройстве),Технология исполнения изделий декоративно-прикладного и народного искусства (художественная роспись по дереву),Учебная практика,Выполнение работ по профессии Кассир,Шрифты и основы шрифтовой композиции (с присвоением квалификации исполнитель художественно-оформительских работ),Физическая и коллоидная химия почасовая,Системное программирование,Практические основы бухгалтерского учёта активов организации,Технология составления бухгалтерской отчётности,Химия с элементами физики,Основы бухгалтерского учета в общественном питании,Статистика,'
#print(','.join('"'+h.strip().__str__()+'"' for h in g.split(',')))
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
lessons=["Аудит","Бизнес-планирование","История искусств","Декоративно-прикладное искусство и народные промыслы","Практика производственная (преддипломная)","Графический дизайн","Организация обслуживания","Биология","Иностранный язык","Правовое обеспечение профессиональной деятельности","Анатомия","Экономика отрасли","Ландшафтный дизайн","Физическая культура","Литература","Введение в специальность","включая информатику","Администрирование сетевых операционных систем","Информационное общество (включая информатику и обществознание)","Информационные технологии в профессиональной деятельности","Метрология и стандартизация","Организация и ведение процессов приготовления","оформления и подготовки к реализации полуфабрикатов для блюд","кулинарных изделий сложного ассортимента","Технология сложных хлебобулочных","мучных кондитерских изделий","Информационное общество (обществознание)","Психология общения","Основы анализа бухгалтерской отчётности","Компьютерная графика","География","Астрономия","Кавказская и кубанская кухня","Введение в специальность (информатика)","Безопасность жизнедеятельности","Дополнительная работа под руководством преподавателя","Зарубежная кухня","Технология приготовления сложной горячей кулинарной продукции","Основы спортивной тренировки","Организация физкультурно-спортивной работы","Организация расчетов с бюджетом и внебюджетными фондами","Дискретная математика","Контроль качества продукции","1С Бухгалтерия","Основы банковского дела","Самостоятельная работа","Практические основы бухгалтерского учета имущества организации","Бухгалтерский учет и отчетность в бюджетных организациях","История мировой культуры","Производственная практика","Дизайн в сфере применения","Практика учебная","Цветоводство и декоративное древоводство","Гигиенические основы физической культуры и спорта","Менеджмент ФК и спорта","Основы флористики","Базовые и новые физкультурно-спортивные виды деятельности с методикой оздоровительной тренировки","Русский язык","Избранный вид спорта с методикой тренировки и руководства соревновательной деятельностью спортсменов","История","Инженерная","компьютерная графика","Безопасность функционирования информационных систем","Операционные системы и среды","Правовые основы профессиональной деятельности","Приготовление","оформление и подготовка к реализации хлебобулочных","мучных кондитерских изделий разнообразного ассортимента","Технология приготовления простой и основной кулинарной продукции","Этика профессиональной деятельности","Основы бухгалтерского учета","Художественное проектирование изделий декоративно-прикладного и народного искусства","Менеджмент","Декоративная дендрология","Технология приготовления коктейлей","Родной язык","Основы безопасности жизнедеятельности","Композиция","оформление и подготовка к реализации холодных и горячих сладких блюд","десертов","напитков разнообразного ассортимента","Оборудование предприятий общественного питания","Технология физкультурно-спортивной деятельности","Налоги и налогообложение","Математика","Математическое и имитационное моделирование","Практика производственная","Иностранный язык в профессиональной деятельности","Методы расчёта основных технико-экономических показателей дзайна","Основы менеджмента  и маркетинга","Основы философии","Рисунок","Дизайн и рекламные технологии","Естествознание","Фитодизайн","Русский язык и культура речи","Основы биомеханики","История дизайна","Основы конструкторско-технологического обеспечения дизайна","Информатика","Операционные системы","Организация и контроль текущей деятельности подчиненного персонала","Приготовление и подготовка к реализации полуфабрикатов для блюд","кулинарных изделий разнообразного ассортимента","Теоретические и прикладные аспекты методической работы педагога по физической культуре и спорту","Основы проектной и компьютерной графики","Основы экономики","Защита растений","Живопись","Организация хранения и контроль запасов сырья","Информационное обеспечение профессиональной деятельности","Основы исполнительского мастерства (художественное стекло","бисер)","Охрана труда","Техническое оснащение и организация рабочего места","Физика","Математика и информатика","Основы программирования","Практические основы бухгалтерского учета источников формирования имущества организации","Экономика организации","Рисунок с основами перспективы","Дизайн-проектирование (композиция","макетирование","современные концепции в искусстве)","Региональные кухни","Лечебная физическая культура и массаж","Обществознание","Основы проектирования объектов садово-паркового строительства","Компьютерные сети","Проектирование предприятий общественного питания","Управление структурным подразделением организации","Перспектива","менеджмента и маркетинга","Выполнение работ по профессии Цветовод","Живопись с основами цветоведения","Физиология питания","Информационное общество (информатика)","Первичная обработка продукции","Техническое оснащение организаций питания","Численные методы","Прикладная математика","Финансы","денежное обращение и кредит","Бухгалтерская технология проведения и оформления инвентаризации","Экономика","Основы врачебного контроля","Обществознание (включая Право)","Организация администрирования компьютерных систем","Технология приготовления хлебобулочных изделий и хлеба","Эстетика и дизайн в оформлении кулинарных и кондитерских изделий","Педагогика","Экологические основы природопользования","Садово-парковое строительство и хозяйство","Колористика","оформление и подготовка к реализации горячих блюд","кулинарных изделий","закусок разнообразного ассортимента","Элементы высшей математики","Химия","Основы стандартизации","сертификации и метрологии","Материаловедение","Спортивная физиология","Технологии физического уровня передачи данных","Управление структурным подразделением","Маркетинг ландшафтных услуг","Учебная практика (изучение памятников искусства в других городах)","Технология приготовления блюд и кулинарных изделий для диетического","лечебно-профилактического питания","Элементы математической логики","Химия с элементами биологии","Основы управления качеством","Основы информационного и библиографического поиска","Физиология с основами биохимии","Экономические и правовые основы профессиональной деятельности","Цветовод (цветоводство в благоустройстве)","Технология исполнения изделий декоративно-прикладного и народного искусства (художественная роспись по дереву)","Учебная практика","Выполнение работ по профессии Кассир","Шрифты и основы шрифтовой композиции (с присвоением квалификации исполнитель художественно-оформительских работ)","Физическая и коллоидная химия почасовая","Системное программирование","Практические основы бухгалтерского учёта активов организации","Технология составления бухгалтерской отчётности","Химия с элементами физики","Основы бухгалтерского учета в общественном питании","Статистика"]
 
conn = sqlite3.connect("exl.db")

cursor = conn.cursor()

spam = list(range(1, 187))
res = [tuple(spam[i:i + 1]) for i in range(0, len(spam), 1)]

#c = cursor.execute('SELECT * FROM GROUPS')
#c = cursor.execute('SELECT  * FROM AUDITORIES')

cursor.executemany('INSERT INTO LESSONS(IdTeacher,IdLesson) VALUES (null,?)',res)

#c = cursor.executemany('INSERT INTO AUDITORIES(Auditories,id) VALUES (?,null)',res)
#conn.commit()