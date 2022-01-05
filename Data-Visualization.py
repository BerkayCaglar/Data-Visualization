import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from openpyxl import Workbook,load_workbook
from csv import reader
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import pandas as pd
from random import randint

liste7=[]
liste6=[]
liste5=[]
liste4=[]
liste3=[]
liste2=[]
liste1_main=[]
liste2_main=[]
liste2_main_year =[]
sozluk={}
sozluk2={}

figure(figsize=(20, 10), dpi=80)

with open('post_offices.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        liste1_main.append(row[8])
        if(row[4]=="WASHINGTON"):
            liste2_main_year.append(row[8])

def func_yil(x):
    for i in liste1_main:
        try:
            if int(i) == x:
                liste2.append(i)
            else:
                pass
        except:
            pass

def graph():
    for i in sozluk.keys():
        liste3.append(i)
    for b in sozluk.values():
        liste4.append(b)
    for p in sozluk2.keys():
        liste6.append(p)
    for o in sozluk2.values():
        liste7.append(o)
    plt.subplot(1,2,1)
    plt.plot(liste3,liste4,"blue",marker="o",markerfacecolor="red")
    plt.xlabel('Yıl')
    plt.ylabel('Kurulan Postane Sayısı')
    plt.title('US Post Ofisleri')

    plt.subplot(1,2,2)
    plt.plot(liste6,liste7,"blue",marker="o",markerfacecolor="red")
    plt.xlabel('Yıl')
    plt.ylabel('Kurulan Postane Sayısı')
    plt.title('WASHINGTON')
    
    x = []
    y = []

    fig, ax = plt.subplots()
    fig.suptitle('WASHINGTON')
    fig.supxlabel('Yıl')
    fig.supylabel('Kurulan Postane Sayısı')
    def animate(i):
        maxx=max(liste6)
        maxx2=max(liste7)
        minn=min(liste6)
        try:
            pt = liste7[0+i]
            x.append(liste6[0+i])
            y.append(pt)

            ax.clear()
            ax.plot(x, y,marker="o",markerfacecolor="red")
            ax.set_xlim([minn,maxx])
            ax.set_ylim([0,maxx2])

        except:
            pass
        
    ani = FuncAnimation(fig, animate, frames=60, interval=500, repeat=False)

    plt.show()

def func_mekan(y):
    for i in liste2_main_year:
        try:
            if int(i) == y:
                liste5.append(i)
            else:
                pass
        except:
            pass

def main():
    x = 1700
    for i in range(len(liste1_main)+1):

        liste2.clear()

        func_yil(x)
        uzunluk=len(liste2)
        sozluk[x] = uzunluk
        x+=50
        if x> 2000:
            break
    y = 1800
    for i in range(len(liste2_main_year)+1):
        liste5.clear()
        func_mekan(y)
        uzunluk=len(liste5)
        sozluk2[y] = uzunluk
        y+=10
        if y== 1940:
            break
    graph()


main()