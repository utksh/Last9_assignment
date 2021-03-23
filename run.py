from generatingData import electricity_consumption
from forecasting import modelling
from outlier_detection import outlier_detection



if __name__ == '__main__':
	data = electricity_consumption()
	df = data.genratingData(10)
	model = modelling('additive', 12)
	trained_model = model.train(df)
	predictions = trained_model.predict()
	od = outlier_detection(df)
	od.compute_outliers(predictions)