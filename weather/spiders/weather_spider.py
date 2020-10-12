import scrapy
from weather.items import WeatherDayItem, WeatherHourItem


class WeatherspiderSpider(scrapy.Spider):
    name = 'weather_spider'
    allowed_domains = ['https://www.timeanddate.com/weather/ireland']
    city_names = ["Athlone", "Ennis", "Port Laoise", "Belmullet", "Galway", "Skibbereen", "Carlow", "Kilkenny",
                  "Sligo", "Carrickmacross", "Letterkenny", "Tralee", "Cork", "Limerick", "Tullamore", "Drogheda",
                  "Longford", "Waterville", "Dublin", "Mullingar", "Westport", "Dundalk", "Navan"]
    base_url = 'https://www.timeanddate.com/weather/ireland/'

    def start_requests(self):
        for city in self.city_names:
            day_url = self.base_url + city
            hour_url = self.base_url + city + '/hourly'

            yield scrapy.Request(url=day_url, callback=self.parse_day, meta={"name": city})

            yield scrapy.Request(url=hour_url,
                                 callback=self.parse_hour,
                                 meta={"name": city})

    def parse_hour(self, response):
        hours = response.css("#wt-hbh tbody tr")
        for hour in hours:
            weatherHourItem = WeatherHourItem()
            weatherHourItem['city'] = response.meta["name"]
            weatherHourItem['hourTime'] = hour.css("th::text").extract()[0]
            weatherHourItem['weatherPic'] = hour.css(".wt-ic .mtt::attr(src)").extract()[0]
            weatherHourItem['weatherTemprature'] = hour.css("td:nth-child(3)::text").extract()[0]
            weatherHourItem['weatherDescription'] = hour.css(".small::text").extract()[0]
            weatherHourItem['feelLike'] = hour.css("td:nth-child(5)::text").extract()[0]
            weatherHourItem['wind'] = hour.css("td:nth-child(6)::text").extract()[0]
            weatherHourItem['windDirection'] = hour.css("td:nth-child(7) span::attr(title)").extract()[0]
            weatherHourItem['humidity'] = hour.css("td:nth-child(8)::text").extract()[0]
            weatherHourItem['fallChance'] = hour.css("td:nth-child(9)::text").extract()[0]
            weatherHourItem['amount'] = hour.css("td:nth-child(10)::text").extract()[0]
            yield weatherHourItem

    def parse_day(self, response):
        days = response.css(".wa")
        for day in days:
            weatherDayItem = WeatherDayItem()
            weatherDayItem['city'] = response.meta["name"]
            weatherDayItem['dateTime'] = day.css(".wt-dn::text").extract()[0]
            weatherDayItem['weatherDescription'] = day.css(".mtt::attr(title)").extract()[0]
            weatherDayItem['weatherPic'] = day.css(".mtt::attr(src)").extract()[0]
            weatherDayItem['dayTemperature'] = day.css("p").extract()[0]
            yield weatherDayItem
