from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from weather.spiders.weather_spider import WeatherspiderSpider

process = CrawlerProcess(get_project_settings())
sched = TwistedScheduler()
sched.add_job(process.crawl, 'cron', args=[WeatherspiderSpider], hour='0-23')
sched.start()
process.start(False)    # Do not stop reactor after spider closes



