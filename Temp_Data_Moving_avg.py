import os
import csv
import queue
import numpy as np

WINDOW_SIZE = 100

def movingAvgWindow(window, input_value, std, avg, current_index, window_end):   # pop last value, add input_value
    window.get()
    window.put(input_value)
    l = list(window.queue)
    x = np.asarray(l)
    sd = np.std(x)
    if(sd < std):
        average_temp = np.mean(x)
        return window, sd, average_temp, current_index
    else:
        return window, std, avg, window_end


def centerPointWindow(fullList):
    truncateList = []
    print('length of center point list: ', len(fullList))
    for i in range( int(len(fullList)/2 - WINDOW_SIZE/2), int(len(fullList)/2 + WINDOW_SIZE/2) ):
        truncateList.append(fullList[i])

    x = np.asarray(truncateList).astype(np.float)
    sd = np.std(x)
    mean = np.mean(x)

    return sd, mean

def main():
    CWD = 'D:\Cubeworks_Code\data\\'
    os.chdir(CWD)          #File that contains the csv files to be sorted through
    id = []
    avg_temp = []
    deviation = []
    data_window = []
    center_sd_list = []
    center_mean_list = []
    window = queue.Queue(maxsize = WINDOW_SIZE)

    for f in os.listdir():
        filepath = CWD + f
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            i = 0
            tempData = []
            center_point_list = []
            std = 10000
            avg = 0
            window_end = 0
            for line in csv_reader:
                if(i == 0):
                    chip_ID = line[0].split(':')
                if(i > 20):
                    center_point_list.append(line[2])
                    if(window.full() == False):
                        window.put(float(line[2]))
                    else:
                        window, std, avg, window_end = movingAvgWindow(window, float(line[2]), std, avg, i, window_end)

                i += 1

            center_sd, center_mean = centerPointWindow(center_point_list)


            id.append(chip_ID[1])
            avg_temp.append(avg)
            deviation.append(std)
            data_window.append(window_end)
            center_sd_list.append(center_sd)
            center_mean_list.append(center_mean)




    with open('D:\Cubeworks_Code\chip_ids(' + id[0] + '-' + id[-1] + ' ).csv', 'w', newline ='') as w:
        writer = csv.writer(w)
        writer.writerow(['chip ID', 'Avg Temp', 'std', 'start', 'end', 'center point mean', 'center point std'])
        for i in range(len(id)):
            writer.writerow([id[i], avg_temp[i], deviation[i], data_window[i] - WINDOW_SIZE, data_window[i], center_mean_list[i], center_sd_list[i]])

if __name__ == '__main__':
    main()
