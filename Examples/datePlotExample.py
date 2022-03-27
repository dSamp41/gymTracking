import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime

data = np.array([2,4,6,8,10])
dateArray = np.array([datetime.datetime(2022, 1, 1), datetime.datetime(2022, 2, 1), datetime.datetime(2022, 3, 1), datetime.datetime(2022, 4, 1), datetime.datetime(2022, 5, 1)])

dateToPlot = dates.date2num()


plt.plot(data)
plt.show()