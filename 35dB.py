import csv
import numpy as np
from collections import defaultdict

EXPECTED_PACKETS = 20





def main():
    FILEPATH = 'D:\Cubeworks_Code\Gateway_logs\\ah100_Nates_data (1).csv'

    with open(FILEPATH, 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        data_dict = defaultdict(list)


        for line in csv_reader:
            chip_ID = line[6]
            data_dict[chip_ID].append(line[4])


    chip_ids = []
    maxdB = []              #max, min, avg will hold values for final output csv
    mindB = []
    avgPackets = []

    tempList = []
    for key in range (1, len(data_dict)):

        #print(list(data_dict.values())[key])
        chip_ids.append(list(data_dict)[key])
        tempList = list(data_dict.values())[key]
        print(list(data_dict)[key])
        print(tempList)
        print("avg packets: ", len(tempList)/20)
        avgPackets.append(len(tempList)/20)
        maxdB.append(max(tempList))
        mindB.append(min(tempList))


        #print(max(list(data_dict().values())[key]))

    with open("D:\Cubeworks_Code\dBdataNEW.csv", 'w', newline = '') as w:
        writer = csv.writer(w)
        writer.writerow(['Chip Id', 'Avg Packets', 'Max dB', 'Min dB'])
        for i in range(len(chip_ids)):
            writer.writerow([chip_ids[i], avgPackets[i], maxdB[i], mindB[i]])




    #print(list(data_dict.values())[1])
    #print(type(data_dict.values()))
    #print(len(list(data_dict.values())[1]))

if __name__ == '__main__':
    main()
