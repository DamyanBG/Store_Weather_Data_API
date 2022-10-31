from resources.current_data import CreateCurrentData
from resources.weather_apis import ListCreateWeatherApis

routes = ((ListCreateWeatherApis, "/weather-apis"), (CreateCurrentData, "/current"))
