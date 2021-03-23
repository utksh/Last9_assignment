
from statsmodels.tsa.holtwinters import ExponentialSmoothing


class modelling:
    def __init__(self, seasonality, period):
        self.trend = seasonality
        self.period = period
        self.model = None
        
    def train(self,df):
        self.model = ExponentialSmoothing(df, trend=self.trend,
                             seasonal='additive', seasonal_periods=self.period).fit(damping_slope= 1)
    def predict(self):
        predictions = pd.DataFrame(self.model.forecast(14), columns = ['electricity_consumption'])
        
        return predictions