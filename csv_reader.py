import csv
import numpy as np

filepath = 'D:\Cubeworks_Code\data\datalog_0551_2020-10-27T9_06_28.csv'

with open(filepath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    i = 0
    tempData = []
    for line in csv_reader:

        if(i == 0):
            chip_ID = line[0].split(':')
        if(i > 2100 and i < 6000):
            tempData.append(float(line[2]))
        i += 1

    x = np.asarray(tempData)
    avg = np.mean(x)
    std = np.std(x)
    print('chip_ID:', chip_ID[1])
    print('avg temp = ', avg)
    print('standard deviation = ', std)
