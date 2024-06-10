import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

# ====================================================================================

"""data = {

    "Набор А": [85, 90, 95, 100, 105],
    "Набор Б": [70, 80, 95, 110, 120],

}

df = pd.DataFrame(data)

stdA = df["Набор А"].std()
stdB = df["Набор Б"].std()

print(f"Стандартное отклонение 1 набор - {stdA}")
print(f"Стандартное отклонение 2 набор - {stdB}")"""

# ====================================================================================

"""data = {

    "Возраст": [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    "Зарплата": [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000],

}

df = pd.DataFrame(data)

print(f"Средний возраст - {df["Возраст"].mean()}")
print(f"Медианный возраст - {df["Возраст"].median()}")
print(f"Стандартное отклонение возраста - {df["Возраст"].std()}")

print(f"Средняя зарплата - {df["Зарплата"].mean()}")
print(f"Медианная зарплата - {df["Зарплата"].median()}")
print(f"Стандартное отклонение зарплаты - {df["Зарплата"].std()}")"""

# ====================================================================================

"""dates = pd.date_range(start="2022-07-26", periods=10, freq="D")

values = np.random.rand(10)

df = pd.DataFrame({"Дата": dates, "Значение": values})

df.set_index("Дата", inplace=True)

print(df)

month = df.resample("ME").mean()

print(month)"""

# ====================================================================================

"""data = {"values": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)

df.boxplot(column="values")
plt.show()

Q1 = df["values"].quantile(0.25)
Q3 = df["values"].quantile(0.75)
IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df["values"] >= downside) & (df["values"] <= upside)]

print(IQR)
print(downside)
print(upside)
print(df)
print(df_new)

df_new.boxplot(column="values")
plt.show()

# print(df.describe())"""

# ====================================================================================

"""data = {
    "name": ["John", "Jane", "Bob", "Alice", "Eve"],
    "gender": ["M", "F", "M", "F", "F"],
    "department": ["HR", "IT", "IT", "Marketing", "HR"]
}

df = pd.DataFrame(data)

# df["gender"] = df["gender"].map({"M": "male", "F": "female"})
# df["department"] = df["department"].map({"HR": "Human Resources", "IT": "Information Technology", "Marketing": "Marketing"})

df["gender"] = df["gender"].astype("category")
df["department"] = df["department"].astype("category")

df["department"] = df["department"].cat.add_categories(["Finance"])
print(df["department"].cat.categories)

df["department"] = df["department"].cat.remove_categories(["HR"])
print(df["department"].cat.categories)

# print(df["gender"].cat.categories)
# print(df["department"].cat.codes)

print(df)"""

# ====================================================================================

data = {
    "Ученик": ["Сергей", "Анна", "Михаил", "Вася", "Петя", "Коля", "Саша", "Толя", "Катя", "Ваня"],
    "Математика": [5, 4, 5, 3, 2, 5, 3, 5, 4, 5],
    "История": [2, 4, 3, 4, 5, 5, 4, 5, 3, 2],
    "Физика": [3, 3, 4, 5, 4, 3, 3, 4, 5, 3],
    "Химия": [5, 4, 2, 3, 4, 5, 2, 3, 5, 4],
    "Биология": [3, 4, 5, 5, 4, 3, 3, 4, 5, 3]
}

# Создание датафрейма
df = pd.DataFrame(data)

# Вывод 5 строк для проверки
# print(df.head())

# Средняя оценка по всем предметам
print(f"Средняя оценка по математике - {df["Математика"].mean()}")
print(f"Средняя оценка по истории - {df["История"].mean()}")
print(f"Средняя оценка по физике - {df["Физика"].mean()}")
print(f"Средняя оценка по химии - {df['Химия'].mean()}")
print(f"Средняя оценка по биологии - {df['Биология'].mean()}")

# Средняя медианная оценка по всем предметам
print(f"Средняя медианная оценка по математике - {df['Математика'].median()}")
print(f"Средняя медианная оценка по истории - {df['История'].median()}")
print(f"Средняя медианная оценка по физике - {df['Физика'].median()}")
print(f"Средняя медианная оценка по химии - {df['Химия'].median()}")
print(f"Средняя медианная оценка по биологии - {df['Биология'].median()}")

# Для проверки статистики
# print(df["Математика"].describe())

# Для удаления выбросов
Q1 = df["Математика"].quantile(0.25)
Q3 = df["Математика"].quantile(0.75)
IQR = Q3 - Q1

# Стандартное отклонение
print(f"Стандартное отклонение оценок по математике - {df['Математика'].std()}")

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df["Математика"] >= downside) & (df["Математика"] <= upside)]

# Отрисовка графика
df_new.boxplot(column="Математика")
plt.show()
