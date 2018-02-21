#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:06:40 2017

@author: keianarei
"""

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.plotly import plot
from plotly.graph_objs import Scatter,Data,Layout,Figure

my_fig = py.get_figure("dfreder1",69)
data = my_fig.get_data()
raw_data = data[0]

manip_data = {}
for year in raw_data['x']:
    if year in manip_data:
        manip_data[year] += 1
    else:
        manip_data[year] = 1

manip_data[1858]=manip_data.pop('(21658')

fin_data = []
for year in manip_data:
    if year == 1900:
        fin_data.append(manip_data[year])
        x = fin_data.index(manip_data[year])
    elif year == 1901:
        fin_data.append(manip_data[year] + fin_data[x])
    elif isinstance(year, int) and year > 1901:
        x += 1
        fin_data.append(manip_data[year] + fin_data[x])

# Basic Plotly
x = range(1900,2011,1)
y = fin_data

trace = Scatter(x = x, y = y, line=dict(color='#FFA500'),fill='tonexty',\
                hoverlabel = dict(font=dict(family='Times New Roman')))
data = Data([trace])
layout = Layout(title = "Total Bridges Built in CA Since 1900", width=600,\
                height=400, font=dict(family='Times New Roman'))
figure = Figure(data = data, layout = layout)
plot(figure,filename = "Scatter")

layout["xaxis"] = go.XAxis(title = "Year", dtick=10)
layout["yaxis"] = go.YAxis(title = "Total Bridges")

# One thing about these graph objects that's nicer than dictionaries
# is that you can also access the keys with the dot notation


# Like all graph objects, you can substitute a regular dictionary for XAxis/YAxis objects
# layout.yaxis = {"title":"y"} 
# But then we wouldn't be able to do layout.yaxis.title = "y"
# it would have to be layout.yaxis["title"] = "y"

figure = Figure(data = data, layout = layout)
plot(figure,filename = "Scatter")
py.image.save_as(figure, filename='Assignment7M.png', scale=3)
