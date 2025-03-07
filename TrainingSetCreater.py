import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

data = list()

training = list()

test = list()

order = [0,1,2,3,4]

sets = [
	r'mahatiratusher/heart-disease-risk-prediction-dataset',
	r'sampadab17/network-intrusion-detection',
	r'uciml/red-wine-quality-cortez-et-al-2009', 
 	r'sanskar457/fraud-transaction-detection',
  	]


finalSets = [
	r'HeartDiseaseRiskTraining.csv',
	r'HeartDiseaseRiskTest.csv',
	r'NetworkIntrusionTraining.csv',
	r'NetworkIntrusionTest.csv',
	r'WineQualityTraining.csv',
	r'WineQualityTest.csv'
	r'FraudTransactionTraining.csv',
	r'FraudTransactionTest.csv'
	]

print('''
	1. Heart Risk
	2. Network Intrusion
	3. Red Wine Quality
	4. Fraud Transactions
	''')


choice = int(input())-1

chosenSet = sets[choice]

if choice == 0:  
    trainingSave = finalSets[0]
    testSave = finalSets[1]
elif choice == 1:  
    trainingSave =  finalSets[2]
    testSave =  finalSets[3]
else:  
    trainingSave =  finalSets[4]
    testSave =  finalSets[5]

data = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  chosenSet,
  file_path,
)



# Shuffle the data
data = data.sample(frac=1).reset_index(drop=True)


# Split the data (80% for training, 20% for testing)
split_index = int(0.8 * len(data))
train_data = data[:split_index]
test_data = data[split_index:]

# Save the data to CSV files
train_data.to_csv(trainingSave, index=False)
test_data.to_csv(testSave, index=False)
