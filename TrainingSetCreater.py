import pandas as pd
import random

sets = [
    r'C:\Users\Brh22\Desktop\9785\Datasets\heart_disease_risk_dataset_earlymed.csv',
    r'C:\Users\Brh22\Desktop\9785\Datasets\Network_Intrusion_Detection_Final_Transactions.csv',
    r'C:\Users\Brh22\Desktop\9785\Datasets\winequality-red.csv'
]

finalSets = [
    r'C:\Users\Brh22\Desktop\9785\Datasets\Data\HeartDiseaseRiskTraining.csv',
    r'C:\Users\Brh22\Desktop\9785\Datasets\Data\HeartDiseaseRiskTest.csv',
    r'C:\Users\Brh22\Desktop\9785\Datasets\Data\NetworkIntrusionTraining.csv',
    r'C:\Users\Brh22\Desktop\9785\Datasets\Data\NetworkIntrusionTest.csv',
    r'C:\Users\Brh22\Desktop\9785\Datasets\Data\WineQualityTraining.csv',
    r'C:\Users\Brh22\Desktop\9785\Datasets\Data\WineQualityTest.csv'
]

print('''
    1. Heart Risk
    2. Network Intrusion
    3. Red Wine Quality
    ''')

choice = int(input()) - 1

chosenSet = sets[choice]


if choice == 0:
    trainingSave = finalSets[0]
    testSave = finalSets[1]
elif choice == 1:
    trainingSave = finalSets[2]
    testSave = finalSets[3]
else:
    trainingSave = finalSets[4]
    testSave = finalSets[5]

df = pd.read_csv(chosenSet)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)


split_index = int(0.8 * len(df))
train_df = df[:split_index]
test_df = df[split_index:]

test_df = test_df.drop(test_df.columns[len(test_df.columns)-1], axis=1)

train_df.to_csv(trainingSave, index=False)
test_df.to_csv(testSave, index=False)
