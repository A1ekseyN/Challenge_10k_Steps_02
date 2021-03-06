# Version - 0.1.8c

# Фичи:
# + Пройденое расстояние в км
# + Пройденое расстояние в среднем в день
# + Выполняется ли условие по прохождению 10.000 шагов в день Yes / No
# + Дописать калькулятор, который считае на сколько % перевыполнен план по количеству шагов в 10000
# + Добавить тексту цветов. Что бы информация визуально выделялась
# + Добавить отображение Min / Max количества шагов на протяжении дня за время челенджа
# + Добавить км за вчера и цветовую индикацию как у пройденых шагов
# + Добавить расчёт пройденого растояния, по разным городам. От Киева, и в сторону Львова. Добавил расстояние от Житомира, так, как лучше ориентируюсь в этом направлении
# + Количество kcal (1 kcal = 35 шагов) (Нужно уточнить сколько шагов нужно сделать что бы сжечь 1 ккал)
# + Добавить сколько шагов нужно сделать для прибытия в следующий город
# + Переписать код f" формат. Без использования кучи "+". А то, сложно править код, и нифига не понятно
# + Вычисление запаса шагов, до среднего значения в 10к.
# + Добавлена статистика по количеству сожжённых кг жира, и статистика по эквиваленту Big Mac
# + Изменено отображение общего кол-ва шагов
# + Добавлен показатель общего запаса шагов
# + Добавлено отображение кол-ва дней в которые пройдено более 10к шагов, и пересчет в %.
# + Добавлена статистика по дням недели.
# + Отображение количества последних дней, за которые пройдено более 10к шагов.

# В среднем kcal в день. Пока не понятно или это вообще стоит считать.

# Поправить отображения цветов (В Среднем за день), возможно и в других местах. Прописан постоянный цвет, а нужно, что бы цвет менялся в зависимости от выполнения условия или его не выполнения
# Добавить отрисовку графиков (Пока, вообще не понимаю как это работает)
# Разобраться с окончаниями переменных: "дней", "шагов".
# Дописать код, который будет менять окончание переменной "дней", "шагов", в зависимости от нужного окончания
# Дописать прогнозирование: Сколько дней в запасе без движения. (Нужно разобраться как работает округление.
# Статистика по времени прогулок. В MiFit появилась статистика времени по дням. Сколько времени в день длилась прогулка. (Можно использовать вложенные словари)
# Добавить статистику по часам прогулок: в котором часу больше сделано шагов, относительно времени соток, времени в конкретный день.
# Влияния кол-ва пройденных шагов на количество сна.

# Начало Challenge - 26.08.2021 (Чт).


#############################################################
# Сама программа
#############################################################


from colorama import Fore, Back, Style
import math
import time

import matplotlib.pyplot as plt

start_time = time.time()


# Список количества шагов по дням + основные переменные, которые вычисляются
# 30-й день - 24.09.2021
# 97-й день - 31.11.2021
# 128-й день - 31.12.2021
# 138-й день - 11.01.2022 (Конец челенджа) (Для поиска: 11072, 8220)
# 144-й день - 16.01.2022
# 159-й день - 31.01.2022
# 187-й день - 28.02.2022
# 199-й день - 12.03.2022 (Для поиска: 4258, 6479, 6078, 11259, 6542, 10124, 11722, 12180)
# 211-й день - 25.03.2022 (Для поиска: 10730, 11807, 10005)
# 219-й день - 29.03.2022 (Для поиска: 11876, 7303, 10592, 10014, 13469,  10006, 6392, 7756)
# 241-й день - 23.04.2022 (Для поиска: 6926, 10765, 8092)
# 263-й день - 15.05.2022 (Для поиска: 4190, 10224, 6228)
# 314-й день - 05.07.2022 (Для поиска: 7088, 4622, 7145)

# Массив по количеству пройденных шагов в день
STEPS = [10360, 16765, 10527, 16828, 10230, 10203, 10691, 10258, 10331, 13555, 13111, 10148, 11006, 10956, 11183, 10308, 10270, 10791, 10391, 10193, 10786, 10008, 10064, 10724, 12560, 13188, 10057, 10831, 10314, 10811, 10226, 10055, 10705, 10272, 10617, 10153, 10299, 10867, 10796, 11196, 10669, 10452, 10594, 16675, 11161, 12918, 10315, 11860, 10334, 11126, 10279, 11065, 10523, 11553, 10425, 10089, 10618, 10567, 10888, 10463, 10845, 12171, 10107, 10101, 10221, 10199, 10716, 11570, 10054, 10250, 14385, 13306, 13232, 10037, 12036, 10288, 10075, 12174, 11660, 10642, 10393, 11421, 11523, 10506, 11644, 10001, 13336, 11975, 11096, 10006, 10457, 10676, 10075, 10546, 12568, 10542, 11138, 10284, 10095, 10362, 15955, 11461, 10592, 10680, 10809, 10034, 10633, 10636, 10396, 13052, 10313, 10692, 10063, 11012, 10033, 10299, 12011, 10615, 10964, 11159, 11485, 10466, 10619, 13599, 10579, 10172, 10322, 10400, 12236, 10437, 10639, 14110, 12101, 10022, 10027, 11260, 10449, 11072, 8220, 5987, 5723, 5117, 9531, 14491, 7639, 4393, 6999, 10099, 13892, 6532, 20215, 10036, 4608, 12357, 6813, 8030, 3047, 12059, 2133, 2968, 6151, 7106, 8160, 5799, 4577, 5183, 6791, 5828, 11233, 6063, 2919, 5762, 8229, 4725, 2325, 3093, 5859, 3621, 9186, 6197, 6892, 10081, 11918, 9817, 18567, 17743, 9443, 15476, 2902, 5928, 949, 965, 4258, 6479, 6078, 11259, 6542, 10124, 11722, 12180, 11601, 10583, 12855, 10491, 10055, 2260, 11390, 4276, 10730, 11807, 10005, 11876, 7303, 10592, 10014, 13469, 10006, 6392, 7756, 10055, 12014, 9041, 10050, 10305, 10043, 8992, 3127, 10034, 11065, 8661, 10052, 10411, 10398, 10030, 10031, 5640, 10152, 10064, 6926, 10765, 8092, 4227, 6689, 4746, 10028, 6016, 7649, 7398, 3973, 8094, 4747, 5897, 6190, 6191, 9446, 10664, 5878, 8838, 6426, 5119, 4190, 10224, 6228, 5417, 3689, 4328, 6491, 10313, 8257, 10951, 11751, 10451, 4834, 6437, 5138, 2997, 10394, 5205, 5608, 6524, 5580, 5681, 5502, 5798, 6201, 10640, 7014, 7410, 6188, 6695, 6466, 3045, 4134, 5067, 12088, 4490, 10136, 5688, 5570, 5013, 4643, 6619, 3746, 3150, 4171, 7306, 3830, 4576, 4080, 3105, 6727, 7088, 4622, 7145, ]
steps_sum = sum(STEPS)  # Общие количество пройденых шагов
steps_average = int(steps_sum / len(STEPS))        # Среднее количество пройденых шагов в день
steps_max = max(STEPS)  # Показывает максимальное число пройденых шагов на протяжении одного дня
steps_min = min(STEPS)  # Показывает минимальное число пройденых шагов на протяжении одного дня

STEP_ONE_DISTANCE = 0.0007 # Длина одного шага в км
distance_km_sum = (round(steps_sum * STEP_ONE_DISTANCE, 1))     # Пройденая дистанкия в км
distance_km_average = (round(distance_km_sum / len(STEPS), 1))  # Средняя пройденая дистанция в км
distance_day_km = (round(STEPS[-1] * STEP_ONE_DISTANCE, 2))     # Пройденое расстояние за последний день
percentage_difference = (STEPS[-1] - steps_average) / steps_average * 100   # Разница в % между количеством шагов пройденых вреча, и общим средним количеством шагов
percentage_difference_round = (round(percentage_difference, 2))

# Вычисляет % на сколько больше хожу шагов, чем 10k. Пока нормально не работает, не понимаю, как считаются %.
percentage_difference_10k = (round(steps_average / 10000 * 10, 2))   # Разница в % между 10.000 шагами и средним кол-вом пройденых шагов за все время

# Проверка или выполняется challenge, и переменная стрелочек
challenge_last_day = None     # Проверяет или за последний день пройдено более 10к шагов
challenge_average = None     # Проверяет или среднее значение за все дни более 10к шагов
challenge_row = None     # Переменная для стрелочек вниз и вверх в юникоде

# Формула для расчёта запаса шагов до среднего значения в 10к
stock_steps_to_10k_per_day = ((steps_average - 10000) * len(STEPS))
#stock_days_steps_to_10k_per_day = (stock_steps_to_10k_per_day / 10000) # Формула расчёта количества дней в запасе.

# Цикл подсчёта количества дней, где шагов более 10к за день.
steps_more_10k = STEPS[:]
steps_more_10k.sort()

for steps_without_smaller_10k_cycle in steps_more_10k:
    if steps_more_10k[0] <= 10000:
        del steps_more_10k[0]

# Цикл для посчёта сколько последних дней выполняется челендж.
# Количество последних дней, за которые пройдено более 10к шагов на протяжении дня.
steps_flipped = STEPS[::-1] # Перевернутый список шагов по дням.
challenge_last_days_go_on = 0 # Переменная для вывода количества последних дней выполнения челенджа.

while steps_flipped [0] >= 10000:
    challenge_last_days_go_on += 1 # Кол-во последних дней, за которые пройдено более 10к шагов.
    del steps_flipped[0]

# Считает % дней, в которых пройдено более 10к шагов на протяжении дня
percent_steps_more_10k = ((len(steps_more_10k) / len(STEPS)) * 100)

# Переменные для городов, которые высчитываются из общего пройденого расстояния в км:
travel_city = None      # Переменная для постройки пройденных городов
travel_next_city_distance_km = None     # Сколько осталось км до следующего города
travel_next_city = None     # Название следующего города
travel_predict_next_city_days = None    # Сколько дней идти до следующего города. Высчитывается из среднего кол-ва шагов в день
travel_predict_word_ending_days = None      # Уточнения окончания день/дня/дней, в переменной travel_predict_next_city_days
travel_steps_next_city = None      # Переменная для расчета кол-ва шагов до следующего города

# Переменные для kcal. + расчёты для кВт и литров бензина (1 kcal = 35 шагов), (1л бензина = 10500 ккал)
STEPS_FOR_ONE_KCAL = 35    # Сколько шагов на 1 kcal
kcal_sum = int(steps_sum / STEPS_FOR_ONE_KCAL)    # Общее кол-во затраченых kcal, за все время
kcal_last_day = int(STEPS[-1] / STEPS_FOR_ONE_KCAL)    # Кол-во kcal потраченых за последний день
KCAL_TO_KWT = 0.859845    # Коефициент для расчета, сколько ккал на один Ватт. 1 ккал = 1,163 Вт
kwt_sum = (round((kcal_sum * KCAL_TO_KWT) / 1000, 2))    # Расчёт, столько всего затрачено кВт, за все время
petrol_economy_liter = (round(kcal_sum / 10500, 1))   # Расчёт, сколько бензина съекономлена за все время. В 1л бензина - 10500 ккал
BIG_MAC_KCAL = 257
big_mac_used = int(kcal_sum / BIG_MAC_KCAL)
kcal_to_fat = (round((kcal_sum / 9) / 1000, 2)) # Расчёт потреченных кг жира

# Срезы данных для подсчёта статистики по конкретным дням недели.
# Начало Challenge - 26.08.2021 (Чт). # Важно для правильного подсчёта первого дня.

day_monday = STEPS[slice(4, None, 7)]
day_monday_average = int((sum(day_monday)) / (len(day_monday)))
day_tuesday = STEPS[slice(5, None, 7)]
day_tuesday_average = int((sum(day_tuesday)) / (len(day_tuesday)))
day_wednesday = STEPS[slice(6, None, 7)]
day_wednesday_average = int((sum(day_wednesday)) / (len(day_wednesday)))
day_thursday = STEPS[slice(0, None, 7)]
day_thursday_average = int((sum(day_thursday)) / (len(day_thursday)))
day_friday = STEPS[slice(1, None, 7)]
day_friday_average = int((sum(day_friday)) / (len(day_friday)))
day_saturday = STEPS[slice(2, None, 7)]
day_saturday_average = int((sum(day_saturday)) / (len(day_saturday)))
day_sunday = STEPS[slice(3, None, 7)]
day_sunday_average = int((sum(day_sunday)) / (len(day_sunday)))


# Переменная для отображения среднего количества шагов за день + показатели Min и Max шагов за день.
# Словарь с информацией для статистики по дням.
avarage_steps_days_of_week = {
    "понедельник": {
        "average_day": (day_monday_average),
        "min_day": min(day_monday),
        "max_day": max(day_monday),
        },
    "вторник": {
        "average_day": (day_tuesday_average),
        "min_day": min(day_tuesday),
        "max_day": max(day_tuesday),
        },
    "среда": {
        "average_day": (day_wednesday_average),
        "min_day": min(day_wednesday),
        "max_day": max(day_wednesday),
        },
    "четверг": {
        "average_day": (day_thursday_average),
        "min_day": min(day_thursday),
        "max_day": max(day_thursday),
        },
    "пятница": {
        "average_day": (day_friday_average),
        "min_day": min(day_monday),
        "max_day": max(day_monday),
        },
    "суббота": {
        "average_day": (day_saturday_average),
        "min_day": min(day_saturday),
        "max_day": max(day_saturday),
        },
    "воскресение": {
        "average_day": (day_sunday_average),
        "min_day": min(day_sunday),
        "max_day": max(day_sunday),
        }
    }


# Вроде как не нужен этот код. Но, нужно будет проводить. Программа и без него работает. Но, зачем-то он нужен.
#days_of_week_sum = [sum(day_monday), sum(day_tuesday), sum(day_wednesday), sum(day_thursday), sum(day_friday), sum(day_saturday), sum(day_sunday)]


# Проверяет или за последний день пройдено более 10к шагов.
if STEPS[-1] >= 10000:
    challenge_last_day = Fore.GREEN + "больше" + Style.RESET_ALL
else:
    challenge_last_day = Fore.RED + "меньше" + Style.RESET_ALL

# Проверяет или среднее значение за все дни более 10к шагов.
if STEPS[-1] >= steps_average:
    challenge_average = Fore.CYAN + "+"
else:
    challenge_average = Fore.RED

# Проверяет или за последний день пройдено более 10к шагов.
if STEPS[-1] >= steps_average:
    challenge_row = "🠕"
else:
    challenge_row = "🠗"

# Вычисление из общего пройденного растояния город, в который я на данный момент дошел. Старт из Житомира.
# Города: Житомир, Новоград, Ровно, Дубно, Львов, Краковец, Dolny Kubin, Братислава, Грац, Njivice (Krk),
# Затем высчитывает дистанцию до следующего города, и прогнознозированное время прибытия в днях.

### Названия городов для правильного расчёта расстояния: Житомир => Dolny Kubin, Братислава

if distance_km_sum >= 84.8:
    travel_city = "Житомир => Новоград"
if distance_km_sum >= 1724:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk"
    travel_next_city_distance_km = round(1987 - (distance_km_sum), 2)
    travel_next_city = "Венеция в Италии"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 1987:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция"
    travel_next_city_distance_km = round(4337 - (distance_km_sum), 2)
    travel_next_city = "Тарифа в Испания"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 4337:
    travel_city = "Житомир => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция => Тарифа"



# Вычисление количества шагов до следующего города
travel_steps_next_city = round(travel_next_city_distance_km / STEP_ONE_DISTANCE)

# Вычисление окончания в слове "День" для прогнозиварония времени прибытья в следующий город.
if travel_predict_next_city_days == 1:
    travel_predict_word_ending_days = "день"
elif travel_predict_next_city_days < 5:
    travel_predict_word_ending_days = "дня"
else:
    travel_predict_word_ending_days = "дней"


# Построение графика по шагам.
def steps_graph():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(STEPS, linewidth = 1, c=(0, 0.7, 1))

    # Назначение заголовка диаграмы и меток осей.
    ax.set_title("График количества шагов", fontsize = 10)
    ax.set_xlabel("Количество дней", fontsize = 10)
    ax.set_ylabel("Количество шагов", fontsize = 10)

    # Назначение размера шрифта делений на осях
    ax.tick_params(axis='both', labelsize = 10)

    plt.show()


############################################
# Вывод информции на экран
############################################
print("🏃 🚗")
print(Fore.CYAN + "===============================================" + Style.RESET_ALL + Fore.MAGENTA + "===" + Style.RESET_ALL)


print(f"Всего за {str(len(STEPS))} дня пройдено - {Fore.GREEN}{steps_sum:,.0f}{Style.RESET_ALL} шагов. (Вчера: + {Fore.MAGENTA}{(STEPS[-1]):,.0f}{Style.RESET_ALL}) ({challenge_average}{str(percentage_difference_round)} %{Style.RESET_ALL}) {challenge_row} :: (Min: {steps_min:,.0f} / Max: {steps_max:,.0f}).")

print(f"В среднем, в день: {Fore.GREEN}{steps_average:,.0f}{Style.RESET_ALL} шагов. (Запас: {stock_steps_to_10k_per_day:,.0f} шагов).")

print(f"\nОбщее расстояние: {Fore.CYAN}{distance_km_sum:,.0f}{Style.RESET_ALL} км (+ {str(distance_day_km)} км)")
print(f"В среднем: {str(distance_km_average)} км в день.")
print(f"\nМаршрут прошел по городам: {travel_city}")
print(f"До города {travel_next_city} осталось: {Fore.CYAN}{str(travel_next_city_distance_km)}{Style.RESET_ALL} км, или {travel_steps_next_city:,.0f} шага. Прогнозированное, прибытие через {travel_predict_next_city_days} {travel_predict_word_ending_days}.")

print(f"\nНа ходьбу затрачено: {Fore.CYAN}{kcal_sum:,.0f}{Style.RESET_ALL} kcal, (вчера {kcal_last_day} kcal).")
print(f"Эквивалент: {Fore.CYAN}{kcal_to_fat}{Style.RESET_ALL} кг жира, {Fore.CYAN}{kwt_sum}{Style.RESET_ALL} кВт, {Fore.CYAN}{petrol_economy_liter}{Style.RESET_ALL} л бензина, или {Fore.CYAN}{big_mac_used}{Style.RESET_ALL} Big Mac.")

print(f"\nЧелендж выполняется последние {Fore.CYAN}{challenge_last_days_go_on}{Style.RESET_ALL} дней. За вчера пройдено {challenge_last_day} 10к шагов.")
print(f"По статистике: {len(steps_more_10k)} из {str(len(STEPS))} дней ({(round(percent_steps_more_10k, 1))} %), за которые пройдено более 10к шагов, на протяжении дня.")

# Отображение среднего количества шагов в день в разные дни недели.
print(f"\n--- Статистика по среднему кол-ву шагов, в разные дни недели: ---")
for day, value in avarage_steps_days_of_week.items():
    print(f"\t- {day.title()}: {value['average_day']} шагов.")

# Отображение максимального и минимального кол-ва шагов в день, в разные дни недели.
print(f"\n--- Статистика по максимальному и минимальному кол-ву шагов в разные дни недели: ---")
for day, value in avarage_steps_days_of_week.items():
    print(f"\t- {day.title()}: Min: {value['min_day']:,.0f} / Max: {value['max_day']:,.0f}.")



# Вывод построения графика.
steps_graph()

print(Fore.CYAN + "\n==============================================="+ Style.RESET_ALL)


#print("--- %s seconds ---" % (time.time() - start_time))
