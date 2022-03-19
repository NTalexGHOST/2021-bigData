# 2021-bigData
ННГАСУ курс по Большим данным

Презентация по курсу (обновляемая): https://docs.google.com/presentation/d/1xZ51nq1IWvccSrLzHo_QyaDQPvMBiWeUhoyPND-ARzo/edit?usp=sharing

Для работы необходим python 3.9 и выше.
Библиотеки: numpy, pandas, matplotlib, tensorflow
Редактор любой. Из неплохих: IDLE (родной, идёт вместе с установщиком), Visual Studio Code, notepad++, PyCharm, vim (для любителей сначала страдать, потом наслаждаться)

Работа с блокнотами онлайн, с возможностью подключения удалённых мощностей гугла (GPU, TPU): https://colab.research.google.com/

Таблица, где я буду отмечать сданные работы: https://docs.google.com/spreadsheets/d/1SdM8fmd4IY8SIh5mzM9gXIXM3aq-ea-w3NJa8Zn_gX4/edit?usp=sharing

Сервер в Дискорд, где буду дублировать: https://discord.gg/MzPkCYf4Dh
Мой контакт: nsmorozov@rf.unn.ru

В своей папке можете делать все что угодно, в чужие не залезать, в корневую тоже. Я буду ориентироваться на файлы, где в названии будет номер лабораторной.
<details>
	<summary>Big data</summary>
# [1] Map-reduce и предобработка данных

Сделать с изменёнными файлами действия, аналогичные проведенным в примере из папки **\_lab-1**

# [2] Работа с данными по GoT (файл \_lab-2\GoT\battles.csv) до 26.11

1. Построить графики зависимости (как в абсолютных значениях, так и в нормированных, два графика) следующего:

	a) гистограмма (bars) количества битв в год с группировкой по домам-защитникам (если нет дома - отбросить данные); 

	b) суммарная длина всех имен королей-нападающих (если больше одного раза - складывать каждый раз) за каждый год;

	c) круговая диаграмма битв, которые начинал каждый из домов (если отсутствует или несколько - объединять в отдельную группу "None");

	d) считая, что каждая битва длилась в среднем 1 месяц (с учетом подготовки и восстановления), посчитать сколько в каждом году воевал каждый из королей (как нападавших, так и защищающихся). 

2. Кроме графика, вывести сведенную в одну таблицу с данными, по которым данные графики строили.

3. Разбивку, кто какой из пунктов делает смотрите в таблице.
</details>

# Интеллектуальный анализ данных
Презентация по курсу (обновляемая): https://docs.google.com/presentation/d/1rMirhHDHlBHSE8TmHPv4mUuaSaGsJ82O2CVv8BqwssI/edit?usp=sharing
# [1] Статистический анализ
1) Сгруппировать оценки по:


	a) годам проведения дегустации (Review date);
	
	
	b) первой цифре поля REF;
	
	
	c) стране компании (Company location);
	
	
	d) происхождению какао-бобов (Broad bean origin).
	
	
2) Оценить: дисперсию, среднее, медианное, и СКО поля "Rating" для каждого поля отдельно. Сравнить с аналогичными показателями общего поля "Rating" (по всему списку);


4) (общее) Оценить величины дисперсии и размаха (max-min) рейтинга ("Rating") для различного содержания какао в процентах ("Cocoa Percent").
