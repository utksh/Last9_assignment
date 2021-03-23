class outlier_detection():
    
    def __init__(self,df):
        
        self.PERIOD = 12        
        self.SF = 1.96 
        self.GAMMA =0.3684211
        self.UB = []            
        self.LB = []
        self.df = df
        
    def model_fitting(self):
        model = ExponentialSmoothing(
    self.df, trend='additive', seasonal='additive').fit()
        prediction_all = model.predict(
    start=self.df.iloc[:, 0].index[0], end=self.df.iloc[:, 0].index[-1])
        
        return prediction_all
    
    def compute_outlier(self, predictions):
        prediction_all = self.model_fitting()
        difference_array = []
        dt = []
        difference_table = {"actual": self.df.iloc[:, 0], "predicted": prediction_all, "difference": difference_array, "UB": self.UB, "LB": self.LB}
        
        for i in range(len(prediction_all)):
            diff = self.df.iloc[:, 0][i]-prediction_all[i]
            if i < self.PERIOD:
                dt.append(self.GAMMA*abs(diff))
            else:
                dt.append(self.GAMMA*abs(diff) + (1-self.GAMMA)*dt[i-self.PERIOD])

            difference_array.append(diff)
            self.UB.append(prediction_all[i]+self.SF*dt[i])
            self.LB.append(prediction_all[i]-self.SF*dt[i])

        difference = pd.DataFrame(difference_table)
        
        model_ub = ExponentialSmoothing(difference.iloc[:, 3], trend='additive', seasonal='additive').fit()
        model_lb = ExponentialSmoothing(difference.iloc[:, 4], trend='additive', seasonal='additive').fit()
        predict_ub = model_ub.forecast(14)
        predict_lb = model_lb.forecast(14)
        self.UB.extend(predict_ub)
        self.LB.extend(predict_lb)
        
        normal = []
        normal_date = []
        anomaly = []
        anomaly_date = []
        
        df_3 = pd.concat([df, predictions])
        
        for i in range(len(df_3.iloc[:, 0].index)):
            if (self.UB[i] <= df_3.iloc[:, 0][i] or self.LB[i] >= df_3.iloc[:, 0][i]) and i > self.PERIOD:
                anomaly_date.append(df_3.iloc[:, 0].index[i])
                anomaly.append(df_3.iloc[:, 0][i])

            else:
                normal_date.append(df_3.iloc[:, 0].index[i])
                normal.append(df_3.iloc[:, 0][i])
        
        anomaly = pd.DataFrame({"date": anomaly_date, "value": anomaly})
        anomaly.set_index('date', inplace=True)
        normal = pd.DataFrame({"date": normal_date, "value": normal})
        normal.set_index('date', inplace=True)
        
        anomaly_forecast = anomaly[anomaly.index >= '2021-03-15']
        
        if anomaly_forecast.empty == True:
            return('No anomaly in forecast')
        else:
            return anomaly_forecast
        

        
