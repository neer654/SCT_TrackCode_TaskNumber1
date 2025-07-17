import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

#set the file path to your CSV file
file_path = "D:/downloads/API_SP.POP.TOTL_DS2_en_csv_v2_38144/API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"

#Load the dataset (skip metadata rows)
df_raw = pd.read_csv(file_path, skiprows=4)

#Preview the dataset
print("Dataset Preview:")
print(df_raw.head())

#Bar Chart: Top 10 most populous countries in 2022
df_bar = df_raw[['Country Name', '2022']].dropna()
df_bar = df_bar.sort_values(by='2022', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='2022', y='Country Name', data=df_bar, palette='viridis')
plt.title('Top 10 Most Populous Countries in 2022')
plt.xlabel('Population')
plt.ylabel('Country')

# Format x-axis numbers with commas
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.tight_layout()
plt.savefig("top_10_population_2022.png")
plt.show()

pop_values = df_raw['2022'].dropna()

plt.figure(figsize=(10, 5))
sns.histplot(pop_values, bins=30, kde=True, color='skyblue')
plt.title('Population Distribution of All Countries (2022)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')

# Format x-axis
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.tight_layout()
plt.savefig("population_distribution_histogram.png")  # Optional: saves the histogram
plt.show()
