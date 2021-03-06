import math
import sys
import time


def euclidean_distance(data1, data2):
    d = 0.0
    for i in range(0, len(data1)):
        x = (data1[i] - data2[i]) ** 2
        d += x
    return math.sqrt(d)


def minimum_d(datapoint, Centers):
    mindistance = sys.maxsize
    for center in Centers:
        x = euclidean_distance(datapoint, center)
        if (x < mindistance):
            mindistance = x
    return mindistance


def distortion(Data, Centers):
    distortion = 0
    for data in Data:
        distortion += minimum_d(data, Centers) ** 2

    return 1 / len(Data) * distortion


if __name__ == '__main__':
    start_time = time.time()
    INPUT_FILE_NAME = "rosalind_ba8b.txt"
    OUTPUT_FILE_NAME = "ba8b.txt"
    file = open(INPUT_FILE_NAME, "r")
    k, m = map(int, file.readline().split())
    centers = []
    data_points = []
    mode = 0
    for line in file:
        if line.__contains__("-"):
            mode = 1
            continue
        if mode == 0:
            centers.append(list(map(float, line.split())))
        else:
            data_points.append(list(map(float, line.split())))
    file.close()
    file = open(OUTPUT_FILE_NAME, "w")
    file.write(str(round(distortion(data_points, centers), 3)))
    print(time.time() - start_time)
