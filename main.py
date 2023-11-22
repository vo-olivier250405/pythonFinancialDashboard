
# Imports
import math
import numpy as np
import datetime as dt
from yfinance import download
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice


def loadData(ticker1, ticker2, start, end):
    """
    """
    return download(ticker1, start, end), download(ticker2, start, end)


def plotDatas(data, indicators, sync_axis=None):
    """
    """
    pass


def onButtonClick(ticke1, ticker2, start, end, indicators):
    """
    """
    pass


stockText1 = TextInput(title="Stock 1")
stockText2 = TextInput(title="Stock 2")
dataPickerFrom = DatePicker(
    title="Start Date",
    value="2020-01-01",
    min_date="2000-01-01",
    max_date=dt.datetime.now()
)

