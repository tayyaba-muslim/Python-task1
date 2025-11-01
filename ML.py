# import libraries
#terminal p ye sary Libraries instal krna 
import pandas as pd         #terminal p import "pip install pandas"
import numpy as np             #"pip install numpy"
import matplotlib.pyplot as plt   #"pip install matplotlib"
import seaborn as sns             #"pip install seaborn"
from sklearn.experimental import enable_iterative_imputer  # enable the experimental feature
from sklearn.impute import SimpleImputer, IterativeImputer




# Load the data
data = sns.load_dataset('titanic')
data.head()

# Load titanic dataset
data = sns.load_dataset('titanic')

# Visualize the data
plt.figure(figsize=(8, 5))
sns.heatmap(data.isnull(), cbar=False)
plt.show()

data.info()
data.isnull().sum().sort_values(ascending=False)
round(data.isnull().sum() / len(data) * 100, 2).sort_values(ascending=False)

# load titanic dataset
data = sns.load_dataset('titanic')

# calculate missing values
print("----------------------------------------")
print(f"Missing values in each column:\n{data.isnull().sum().sort_values(ascending=False)}")
print("----------------------------------------")
print(f"Percentage of missing values in each column:\n{round(data.isnull().sum() / len(data) * 100, 2).sort_values(ascending=False)}")
data.head()

round(data['age'].mean(), 2)
data['age'].median()
# Mean of age to fill age missing values
data['age'] = data['age'].fillna(data['age'].median())
# drop deck column
data.drop('deck', axis=1, inplace=True)

data.head()
data['embark_town'].value_counts()
# replacing embarked missing values with mode
data['embark_town'] = data['embark_town'].fillna(data['embark_town'].mode()[0])
data['embarked'] = data['embarked'].fillna(data['embarked'].mode()[0])

data.isnull().sum().sort_values(ascending=False)
#we can also impute using sk learn
# import libraries


df = sns.load_dataset('titanic')
# impute age column using simpleimputer from sklearn
imputer = SimpleImputer(strategy='mean')
df['age'] = imputer.fit_transform(df[['age']])

df.isnull().sum().sort_values(ascending=False)
df.head()
#multivariate imputation
df = sns.load_dataset('titanic')


# impute age column using iterativeimputer from sklearn
imputer = IterativeImputer(max_iter=20, n_nearest_features=5)
df['age'] = imputer.fit_transform(df[['age']])
#ffill and backward fill
df = sns.load_dataset('titanic')
df.isnull().sum().sort_values(ascending=False)
# using forward fill impute age column
df['age'] = df['age'].bfill()

#using KNN imputer
from sklearn.impute import KNNImputer

# impute age column using KNNImputer from sklearn
imputer = KNNImputer(n_neighbors=5)
df['age'] = imputer.fit_transform(df[['age']])
# drop rows having missing values
df.dropna(inplace=True)
df.info()
df.isnull().sum().sort_values(ascending=False)