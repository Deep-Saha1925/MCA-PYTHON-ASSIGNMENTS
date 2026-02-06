import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'D:\PYTHON ASSIGNMENTS\DATA ANALYSIS\DATA\train_titanic.csv')

# Survival based on gender

gender_counts = df['Sex'].value_counts()

plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel('Gender')
plt.ylabel('Count')

# Show count on top of each bar
for i, count in enumerate(gender_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

plt.show()
