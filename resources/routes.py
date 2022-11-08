from resources.current_data import CreateCurrentData
from resources.weather_apis import ListCreateWeatherApis
from resources.weather_prediction import (
    ListCreatePrediction,
    ListPredictionByDay,
    ListPredictionsByDayRange,
)

routes = (
    (ListCreateWeatherApis, "/weather-apis"),
    (CreateCurrentData, "/current"),
    (ListCreatePrediction, "/prediction"),
    (ListPredictionByDay, "/prediction-by-day/<string:day>"),
    (ListPredictionsByDayRange, "/prediction-by-day-range"),
)
