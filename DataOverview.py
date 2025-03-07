import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

sets = [
	r'mahatiratusher/heart-disease-risk-prediction-dataset',
	r'sampadab17/network-intrusion-detection',
	r'uciml/red-wine-quality-cortez-et-al-2009', 
 	r'sanskar457/fraud-transaction-detection',
  	]

file_path = ""

print('''
	1. Heart Risk
	2. Network Intrusion
	3. Red Wine Quality
	4. Transaction
	''')

chosenSet = sets[int(input())-1]

df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  chosenSet,
  file_path,
)

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
