#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:29:52 2017
@author: aglick
"""


def calibration(adcPlot):
    import numpy as np
    import time
    import heapq
    import statsmodels.api as sm
    import numpy as np
    import matplotlib.pyplot as plt

    MeV = []
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    adcVal = []
    i = 0
    for row in adcPlot:
#        peakVal, peakTime = max(enumerate(row), key=operator.itemgetter(1)) #findPeaks(row)
        #print('temp = ',temp)
        #print(row)
        peakTime = row.argmax()
        #pulseIntegral = integratePulse(row,peakTime)
        #tailIntegral = integrateTail(row,peakTime)
        #tailToTotalRatio += [tailIntegral/float(pulseIntegral)]
        #adcVal += [pulseIntegral]

        if i%100000 == 0:
            print('m = ', i)
            #print('elapsed time = ',time.time()-tic,'s')
        i=i+1

    adcVal = adcPlot
    #adcVal = np.asarray(adcVal,dtype='float')
    histNADC = np.histogram(adcVal,10000)
    #d1 = histNADC[0]
    #e1 = histNADC[1]
    #f1 = e1[0:100000]
    #plt.figure(1)
    #plt.plot(f1,d1,'b-',label='Cs Plot')
    #plt.xlabel('ADC Val')
    #plt.ylabel('Counts')
    #plt.legend(loc='upper right')
    #plt.title("plane")
    #plt.plot(d,f)
    #plt.show()
    #Cs = heapq.nlargest(1,range(125000,len(f1)),key=f1.__getitem__)
    #Co1 = heapq.nlargest(1,range(250000,len(f1)),key=f1.__getitem__)
    #Co2 = heapq.nlargest(1,range(315000,len(f1)),key=f1.__getitem__)
    #f1 = np.around(f1)
    #f1 = np.array(f1,dtype='int')
    #print(f1)
    print(len(adcVal))
    index1 = (np.abs(adcVal - 1500)).argmin()
    index2 = (np.abs(adcVal - 2000)).argmin()
    index3 = (np.abs(adcVal - 2000)).argmin()
    index4 = (np.abs(adcVal - 3000)).argmin()
    print(index1)
    print(adcVal[index1])
    print(index2)
    print(adcVal[index2:index1])
    CsCompton = np.max(adcVal[index2:index1])
    print(CsCompton)
    Cs = np.max(adcVal[index3:index4])
    #for i in range(0,len(d1)):
    y = np.array([477.7,662])
    print(adcVal[Cs])
    x = np.array([CsCompton,Cs])
    print(x)
    #x = np.array(x)
    #m, b = np.polyfit(x, y, 1)

    #plt.plot(x, y, '.')
    #plt.plot(x, m*x + b, '-')


    #X = np.random.rand(100)
    #Y = X + np.random.rand(100)*0.1

    results = sm.OLS(y,sm.add_constant(x)).fit()

    #print(results.summary())

    slope, intercept = np.polyfit(x, y, 1)

    abline_values = [slope * i + intercept for i in x]
    plt.plot(x, y, 'ro')
    plt.plot(x, abline_values, 'b')
    plt.xlabel('ADC Val')
    plt.ylabel('Energy [keV]')
    plt.title('Best Fit Line')
    plt.show()


#    plt.show()


    return slope, intercept
