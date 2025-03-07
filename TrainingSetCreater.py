import random as rand

data = list()

training = list()

test = list()

order = [0,1,2,3,4]

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

x = 1

with open(chosenSet, mode='r') as file:
	for line in file:
		data.append(line)

print("import done")

with open(trainingSave, mode='w') as file:
	file.write(data[0])

with open(testSave, mode='w') as file:
	file.write(data[0])

data.pop(0)


rand.shuffle(data)


split_index = int(0.8 * len(data))  
training = data[:split_index]  
test = data[split_index:]

print("shuffle done")

with open(trainingSave, mode='a') as file:
	while len(training) > 0:
		file.write(training[0])
		training.pop(0)

with open(testSave, mode='a') as file:
	while len(test) > 0:
		file.write(test[0])
		test.pop(0)