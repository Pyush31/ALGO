import time
import random
import csv
import pandas as pd
import matplotlib.pyplot as plt
import math
 
class sortedList():
    def __init__(self,data,comparisions,runningTime):
        self.data = data
        self.comparisions = comparisions
        self.runningTime = runningTime
 
    def __str__(self):
        return f'{self.comparisions:<7} \t {self.runningTime:<7}'
 
class timeComplexity():
    def __init__(self,avg,best,worst):
            self.avg = avg
            self.best = best
            self.worst = worst
        
    def __str__(self):
        return f'{len(self.avg.data):<7}  {self.avg.__str__()} \t {self.best.__str__()} \t {self.worst.__str__()}'
 
# Merge Sort
def merge(left,right,original):
    counter = 0
    i = j = k = 0 
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            counter += 1
            original[k] = left[i]
            i += 1
        else:
            counter += 1
            original[k] = right[j]
            j += 1
        k += 1
    while(i < len(left)):
        original[k] = left[i]
        i += 1
        k += 1
    while(j < len(right)):
        original[k] = right[j]
        j += 1
        k += 1
    return counter

def mergeSort(n):
    counter = 0
    if len(n) == 1:
        return sortedList(n,0,0)
    start = time.time()
    left = n[0:len(n)//2]
    right = n[len(n)//2:]
    counter += mergeSort(left).comparisions
    counter += mergeSort(right).comparisions
    counter += merge(left,right,n)
    end = time.time()
    runningTime = round(end-start)
    return sortedList(n,counter,runningTime)
 
def getNumbers():
    try:
        numbersFile = open('numbers.txt', "r")
        numbers = []
        for number in numbersFile:
            numbers.append(int(number))
    except FileNotFoundError:
        print("File Not Found")
        exit(-1)
    finally:
        numbersFile.close()
    return numbers
 
def getData(numbers):
    data = []
    sampleSpaceSize = 1
    for i in range(1000):
        sampleSpaceSize = random.randint(1,1000)
        startIndex = random.randint(0,len(numbers)-sampleSpaceSize)
        sampleSpace = numbers[startIndex:startIndex+sampleSpaceSize]
        avg = mergeSort(sampleSpace)
        best = mergeSort(sampleSpace)
        sampleSpace.reverse()
        worst = mergeSort(sampleSpace)
        data.append(timeComplexity(avg,best,worst))
    sampleSpaceSize = 1
    try:
        with open('comparisions.csv', mode='w') as c:
            writer = csv.writer(c)
            writer.writerow(['SIZE','AVERAGE','BEST','WORST'])
            for t in data:
                writer.writerow([len(t.avg.data),t.avg.comparisions,t.best.comparisions,t.worst.comparisions])
    except RuntimeError:
        print(RuntimeError)
    
    # Ploting the Graph
    comparisions = pd.read_csv('comparisions.csv')
    comparisions = comparisions.sort_values("SIZE")
    size = comparisions["SIZE"]
    plt.plot(size,comparisions["WORST"])
    plt.plot(size,comparisions["AVERAGE"])
    plt.plot(size,comparisions["BEST"])
    plt.plot(size,[x*math.log2(x) for x in size],'--')
    plt.legend(["WORST","AVERAGE","BEST","nlogn"])
    plt.xlabel('Input Size')
    plt.ylabel('Number of Comparisons')
    plt.ylim(0, 20000)
    plt.xlim(0, 1000)
    plt.savefig('graph.png')
    plt.show()
    
 
getData(getNumbers())