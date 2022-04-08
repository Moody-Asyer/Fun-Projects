#import numpy as np #butuh numpy
#from scipy import stats #butuh scipy

#np.mean atau np.median dll

#atau bisa pakai

#import statistics as st
size = int(input())
numbers = list(map(int, input().split()))
print(st.mean(numbers))
print(st.median(numbers))
print((st.mode(numbers)[0])
#https://www.hackerrank.com/challenges/s10-basic-statistics/problem