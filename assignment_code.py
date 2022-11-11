import matplotlib.pyplot as plt
import pandas as pd



#Reading the data from dataset
data = pd.read_csv("https://s3-eu-west-1.amazonaws.com/datagovuk-production-ckan-organogram/organogram-december-2021/resources/2022-10-05T09-15-50Z-2022-10-05-organogram-junior.csv")
    

#dataframe view
data.head()

#checking the null values in the dataset.
data.isnull().sum()

#checking the description of the data
data.describe()                   

#checking each column uniqueness with pd.unique()
df1 = pd.DataFrame(pd.unique(data[['Generic Job Title']].values.ravel('K')))
df2 = pd.DataFrame(pd.unique(data[['Grade']].values.ravel('K')))
df3 = pd.DataFrame(pd.unique(data[['Payscale Minimum (£)']].values.ravel('K')))
df4 = pd.DataFrame(pd.unique(data[['Payscale Maximum (£)']].values.ravel('K')))


#concating all the unique data through pd.concat()
dff = pd.concat([df1,df2,df3,df4],axis=1)

#creating columns for the dataset
dff.columns = ['Generic Job Title','Grade', 'Payscale Minimum (£)', 'Payscale Maximum (£)']


#Write linePlot function to create Line Plot.
def linePlot(linePlotData):  
    
    linePlotData.plot(x="Generic Job Title",y=['Payscale Minimum (£)','Payscale Maximum (£)'],kind='line',figsize=(15, 5))
    
    plt.title("Payscale of Different Job Title")     #set the tile of the plot
    plt.xlabel("Generic Job Title")     #setting the label of the x-axis
    plt.ylabel("Payscale")       #setting the label of the y-axis
    plt.show()             
    
#Calling the multiPlot function for the dataframe to plot the MultiLine Plot.
linePlot(dff)


#Write Pie plot function to create Pie Plot.
def piePlot(pieData):
    cols = ['r','magenta','c','g', 'orange','pink','yellow']  #defining cols - color list for the pie plot.
    plt.pie(pieData['Payscale Minimum (£)'],
    labels =pieData['Generic Job Title'],
    colors = cols,
    startangle = 90,
    shadow = True,
    autopct ='%1.1f%%')
    plt.title('Payscale of Different Job Title')   #set the tile of the plot
    
#Calling the PiePlot function to plot the pie Plot.
piePlot(dff)

#Write Hist plot function to create Hist Plot.
def barPlot(barData):  #write the HistPlot to plot the histogram plot.
    barData.plot(x="Grade",y=['Payscale Minimum (£)','Payscale Maximum (£)'],kind='bar',figsize=(15, 5))  
    plt.title("Payscale of Different Job Title")  #set the tile of the plot.
    plt.xlabel("Generic Job Title")     #setting the label of the x-axis.
    plt.ylabel("Payscale")              #setting the label of the y-axis.
    
#calling the histPlot function to plot.
barPlot(dff)



