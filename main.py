
# Imports
import numpy as np
import datetime as dt
from yfinance import download
from math import pi
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice


def loadData(ticker1, ticker2, start, end):
    """
    """
    return download(ticker1, start, end), download(ticker2, start, end)


def getFigureResult(sync_axis):
    """
    """
    if sync_axis is not None:
        return figure(
            x_axis_type="datetime",
            toold="pan, wheel_zoom, box_zoom, reset, save", width=1000,
            x_range=sync_axis)
    return figure(
        x_axis_type="datetime",
        toold="pan, wheel_zoom, box_zoom, reset, save", width=1000)


def plotDatas(data, indicators, sync_axis=None):
    """
    """
    dataFrame = data
    gain = dataFrame.Close > dataFrame.Open
    loss = dataFrame.Open > dataFrame.Close
    width = 43200000
    figureResult = getFigureResult(sync_axis)
    figureResult.xasis.major_label_orientation = pi / 4
    figureResult.grid.grid_line_alpha = 0.25
    figureResult.segment(dataFrame.index, dataFrame.High,
                         dataFrame.index, dataFrame.Low)


def onButtonClick(ticker1, ticker2, start, end, indicators):
    """
    """
    dataFrame1, dataFrame2 = loadData(ticker1, ticker2, start, end)
    plot1 = plotDatas(dataFrame1, indicators)
    plot2 = plotDatas(dataFrame2, indicators, sync_axis=plot1.x_range)
    curdoc().clear()
    curdoc().add_root(layout)
    curdoc().add_root(row(plot1, plot2))


stockText1 = TextInput(title="Stock 1")
stockText2 = TextInput(title="Stock 2")
dataPickerFrom = DatePicker(
    title="Start Date",
    value="2020-01-01",
    min_date="2000-01-01",
    max_date=dt.date.today()
)

dataPickerTo = DatePicker(
    title="End Date",
    value="2020-02-01",
    min_date="2000-01-01",
    max_date=dt.date.today()
)

indicatorsCHoice = MultiChoice(
    options=["100 Day SMA", "30 Day SMA", "Linear Regression Line"])

loadButton = Button(label="Load Data", button_type="success")
loadButton.on_click(onButtonClick(stockText1.value, stockText2.value,
                                  dataPickerFrom.value, dataPickerTo.value,
                                  indicatorsCHoice.value))
layout = column(stockText1, stockText2, dataPickerFrom,
                dataPickerTo, indicatorsCHoice, loadButton)

curdoc().clear()
curdoc().add_root(layout)
