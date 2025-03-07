import pandas as pd

sets = [
	r'C:\Users\Brh22\Desktop\9785\Datasets\heart_disease_risk_dataset_earlymed.csv',
	r'C:\Users\Brh22\Desktop\9785\Datasets\Network_Intrusion_Detection_Final_Transactions.csv',
	r'C:\Users\Brh22\Desktop\9785\Datasets\winequality-red.csv', 
 	r'C:\Users\Brh22\Desktop\9785\Datasets\Transaction_Test_data.csv',
  	r'C:\Users\Brh22\Desktop\9785\Datasets\Transaction_Train_data.csv'
  	]

print('''
	1. Heart Risk
	2. Network Intrusion
	3. Red Wine Quality
	4. Transaction Test
	5. Transaction Train
	''')

chosenSet = sets[int(input())-1]

df = pd.read_csv(chosenSet)

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())