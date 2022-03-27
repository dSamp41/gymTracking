#https://datatofish.com/matplotlib-charts-tkinter-gui/

import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import plotly.express as px

def buildGraph_PLT(df: DataFrame, eserc: str):
    '''
    Costruisce grafico di boxplot

    Parameters
    ----------
    df: DataFrame con i dati memorizzati
    eserc: Nome esercizio da plottare
    '''

    root = tk.Tk() 
  
    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    avgs = [np.mean(arr) for arr in df[eserc]]   #array delle medie

    ax1.boxplot(df[eserc])
    ax1.plot(range(1, len(df[eserc])+1), avgs)
    #return root
    root.mainloop()


def buildGraph(df: DataFrame, eserc: str):
    ''' https://plotly.com/python/getting-started/#installation
    Costruisce grafico di boxplot

    Parameters
    ----------
    df: DataFrame con i dati memorizzati
    eserc: Nome esercizio da plottare
    '''

    avgs = [np.mean(arr) for arr in df[eserc]]   #array delle medie

    fig = px.line(data_frame=df[[eserc]], x="Data", y="Peso")#x=np.arange(1, len(df[eserc])+1), y=avgs)
    fig.show()
