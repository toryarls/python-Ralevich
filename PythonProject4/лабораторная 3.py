import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris_data = load_iris()
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = iris_data.target

iris_df['species'] = iris_df['target'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

colors = {'Setosa': 'red', 'Versicolor': 'blue', 'Virginica': 'green'}

plt.figure(figsize=(10, 6))
for species, color in colors.items():
    subset = iris_df[iris_df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'],
                color=color, label=species, s=100)


plt.title('Диаграмма рассеяния для набора данных iris')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Ширина чашелистика (см)')
plt.legend(title='Вид')
plt.grid(True)
plt.show()