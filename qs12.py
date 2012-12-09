#!/opt/local/bin/python

import numpy as np

'''
    Question 1
    In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times.. Download the text file here. This file describes a set of jobs with positive and integral weights and lengths. It has the format
    [number_of_jobs]
    [job_1_weight] [job_1_length]
    [job_2_weight] [job_2_length]
    ...
    For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. You should NOT assume that edge weights or lengths are distinct.
    
    Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
'''

'''
    Question 2
    For this problem, use the same data set as in the previous problem. Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
'''

### sort the data into greedy order
def sort1(data):
    id = np.argsort(data[:,0]-data[:,1])
    return np.array([data[id[::-1],0],data[id[::-1],1]]).transpose()

def sort2(data):
    id = np.argsort(data[:,0]-data[:,1])
    return np.array([data[id[::-1],0],data[id[::-1],1]]).transpose()

def computeTime(data):
    b = np.cumsum(data[:,1])
    return np.sum(data[:,0]*b)

if __name__ == "__main__":
    data = np.loadtxt('jobs.txt',skiprows=1)
    sortdata = sort(data)
    print computeTime(sortdata)
    