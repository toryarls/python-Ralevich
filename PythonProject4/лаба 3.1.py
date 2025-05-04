import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Загружаем набор данных iris
iris_data = load_iris()
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = iris_data.target

# Определяем классы для цветов
iris_df['species'] = iris_df['target'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

# Нормализация данных с использованием Min-Max Scaling
scaler = MinMaxScaler()
iris_df[['sepal length (cm)', 'sepal width (cm)']] = scaler.fit_transform(iris_df[['sepal length (cm)', 'sepal width (cm)']])

# Стандартизация данных с использованием Z-score Scaling
scaler = StandardScaler()
iris_df[['sepal length (cm)', 'sepal width (cm)']] = scaler.fit_transform(iris_df[['sepal length (cm)', 'sepal width (cm)']])

# Задаем цвета для каждого вида
colors = {'Setosa': 'red', 'Versicolor': 'blue', 'Virginica': 'green'}

# Строим диаграмму рассеяния
plt.figure(figsize=(10, 6))
for species, color in colors.items():
    subset = iris_df[iris_df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'],
                color=color, label=species, s=100)

# Добавляем заголовок и метки
plt.title('Диаграмма рассеяния для набора данных iris (нормализованные и стандартизированные)')
plt.xlabel('Длина чашелистика (нормализованная и стандартизированная)')
plt.ylabel('Ширина чашелистика (нормализованная и стандартизированная)')
plt.legend(title='Вид')
plt.grid(True)
plt.show()