from resources.current_data import CreateCurrentData
from resources.weather_apis import ListCreateWeatherApis
from resources.weather_prediction import CreatePrediction

routes = (
    (ListCreateWeatherApis, "/weather-apis"),
    (CreateCurrentData, "/current"),
    (CreatePrediction, "/prediction"),
)
