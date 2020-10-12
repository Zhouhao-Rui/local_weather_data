# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherHourItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    hourTime = scrapy.Field()
    weatherPic = scrapy.Field()
    weatherTemprature = scrapy.Field()
    weatherDescription = scrapy.Field()
    feelLike = scrapy.Field()
    wind = scrapy.Field()
    windDirection = scrapy.Field()
    humidity = scrapy.Field()
    fallChance = scrapy.Field()
    amount = scrapy.Field()


class WeatherDayItem(scrapy.Item):
    city = scrapy.Field()
    dateTime = scrapy.Field()
    weatherPic = scrapy.Field()
    dayTemperature = scrapy.Field()
    weatherDescription = scrapy.Field()
