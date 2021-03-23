# Last9_assignment
# Problem
Generate time series data for the Electricity meter reading of a household.
The recording is done every day at 6 PM, Daily

Example:
Time                    Units
1/3/2020  6 PM  18.2
2/3/2020 6 PM   38.1
..
23/3/2020 6 PM  540.5
....
1/4/2020 6 PM   717.5


Summertime will reflect more units being consumed, maybe humid days of monsoon as well.
So have to consider that. Generate two years dataset.
That will yield a total of 730 data points(365*2).
Forecast reading from 15th March to 28th March of 2021, to detect if it is an anomaly.

# Solution
The problem is divided into three parts:
1. Simulating electric consumption data
2. Forecasting electric consumption for future dates
3. Detect anomaly if any in forecasting values

## Generating Data
I have used a very simple approach for simulating the data for this problem. The major factor i have considered while generating daily consumption is the consumption in summer months and on weekends. Outlined two different range for daily consumption in winter and in summer where all the units have equal chance of being chosed for weekdays but on weekend making the larger values to be more probable for the selection (skewed distribution). In the end random noise is also added in the data to make it a more real world data.

## Forecasting
The Generated data has a constanct increasing trend as well as an additive seasonality, we conclude that **Holt-Winter additive model** would 
be an appropriate choice

 ## Outlier detection
 Here I have used Brutlag algorithm which is very simple statistical technique to detect outliers, it is an extension to exponential smoothing. The algorithm plots a upper bound and lower bound band on the entire data. The points that lie beyond these bands are termed as an anomaly.
 
## How to run
$ pip install -r requirements.txt <br/>
$ python run.py <br/>

## Working_notebook.ipynb shows running solution of the entire problem with detailed description at each step. which shows one point in forecasting period anomaly.
