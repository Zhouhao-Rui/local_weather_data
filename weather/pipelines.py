# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings
from weather.items import WeatherDayItem, WeatherHourItem

city_names = ["Athlone", "Ennis", "Port Laoise", "Belmullet", "Galway", "Skibbereen", "Carlow", "Kilkenny",
                  "Sligo", "Carrickmacross", "Letterkenny", "Tralee", "Cork", "Limerick", "Tullamore", "Drogheda",
                  "Longford", "Waterville", "Dublin", "Mullingar", "Westport", "Dundalk", "Navan"]

db_day_city_names = {}
db_hour_city_names = {}


class WeatherPipeline:
    def __init__(self):
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]

        # self.dayWeather = tdb[settings['MONGODB_DAYCOLLNAME']]
        # self.hourWeather = tdb[settings['MONGODB_HOURCOLLNAME']]

        # 根据不同的城市map到不同的collection
        for city in city_names:
            city_day_weather_name = "dayWeather_" + city
            city_hour_weather_name = "hourWeather_" + city
            db_day_city_names[city_day_weather_name] = tdb[city_day_weather_name]
            db_hour_city_names[city_hour_weather_name] = tdb[city_hour_weather_name]

        # 先将collection中的内容全部清空
        for (key, item) in db_day_city_names.items():
            item.remove()
        for (key, item) in db_hour_city_names.items():
            item.remove()

    # 进行插值
    def process_item(self, item, spider):

        if item.__class__ == WeatherDayItem:
            dayItem = dict(item)
            city = dayItem['city']
            city_name = "dayWeather_" + city
            db_day_city_names[city_name].insert(dayItem)
            return item
        if item.__class__ == WeatherHourItem:
            hourItem = dict(item)
            city = hourItem['city']
            city_name = "hourWeather_" + city
            db_hour_city_names[city_name].insert(hourItem)
            return item
