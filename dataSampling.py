import plotly.figure_factory as ff 
import csv
import pandas as pd 
import random 
import statistics 
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()

populationMean=statistics.mean(data)

populationStdev=statistics.stdev(data)
print(populationMean)
print(populationStdev)

def showFig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    
    mean=statistics.mean(dataSet)
    return mean

def setup():
    meanList=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMean(100)
        meanList.append(setOfMeans)

    showFig(meanList)

    mean=statistics.mean(meanList)
    print("Mean Of Sampling Distribution: ",mean)

setup()

def standardDeviation():
    meanList=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMean(100)
        meanList.append(setOfMeans)

    stdev=statistics.stdev(meanList)
    print("Standard Dev for sampling data: ",stdev)

standardDeviation()
