import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file
df = pd.read_excel("Job_Application.xlsx")  


print(df.head())

# Convert dates
df['Date Applied'] = pd.to_datetime(df['Date Applied'], errors='coerce')
df['Response Date'] = pd.to_datetime(df['Response Date'], errors='coerce')

# Add Response Time column
df['Response Time'] = (df['Response Date'] - df['Date Applied']).dt.days

# Fill missing values
df['Platform'] = df['Platform'].fillna("Unknown")
df['Status'] = df['Status'].fillna("Applied")

# Total applications
print("Total Applications:", len(df))

# Status breakdown
print("\nStatus Counts:\n", df['Status'].value_counts())

# Platform breakdown
print("\nPlatform Success:\n", df.groupby('Platform')['Status'].value_counts())

# Average response time
print("\nAvg Response Time:", df['Response Time'].mean())




sns.set(style="whitegrid")

# Pie Chart 
df['Status'].value_counts().plot.pie(autopct='%1.1f%%', figsize=(6,6), title='Application Status Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Bar Chart 
pivot = df[df['Status'].isin(['Offer', 'Interviewing'])].groupby(['Platform', 'Status']).size().unstack()
pivot.plot(kind='bar', stacked=True, figsize=(8,6), colormap="viridis", title='Platform Success Rate')
plt.ylabel("Number of Applications")
plt.tight_layout()
plt.show()

