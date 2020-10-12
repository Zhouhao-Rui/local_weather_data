# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings
from weather.items import WeatherDayItem, WeatherHourItem


class WeatherPipeline:
    def __init__(self):
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.dayWeather = tdb[settings['MONGODB_DAYCOLLNAME']]
        self.hourWeather = tdb[settings['MONGODB_HOURCOLLNAME']]

    def process_item(self, item, spider):
        if item.__class__ == WeatherDayItem:
            dayItem = dict(item)
            self.dayWeather.insert(dayItem)
            return item
        if item.__class__ == WeatherHourItem:
            hourItem = dict(item)
            self.hourWeather.insert(hourItem)
            return item
