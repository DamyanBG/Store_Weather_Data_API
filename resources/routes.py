from resources.current_data import (
    ListCreateCurrentData,
    ListCurrentDataByDay,
    ListCurrentDataByDayRange,
)
from resources.weather_apis import ListCreateWeatherApis
from resources.weather_prediction import (
    ListCreatePrediction,
    ListPredictionByDay,
    ListPredictionsByDayRange,
)

routes = (
    (ListCreateWeatherApis, "/weather-apis"),
    (ListCreateCurrentData, "/current"),
    (ListCurrentDataByDay, "/current-by-day/<string:day>"),
    (ListCurrentDataByDayRange, "/current-by-day-range"),
    (ListCreatePrediction, "/prediction"),
    (ListPredictionByDay, "/prediction-by-day/<string:day>"),
    (ListPredictionsByDayRange, "/prediction-by-day-range"),
)
