# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

# url_list = []

class ToScrapeCSSSpider(scrapy.Spider):
    name = "iu"
    # start_urls = ['https://iustudio.tistory.com/1585',]
    start_urls = ['https://iustudio.tistory.com/1250']
    # start_urls += ["https://iustudio.tistory.com/" + str(i) for i in range(1300,1250,-1)]
    print(start_urls)
    # # parsing the url into parts
    # start_url = start_urls[0].split('/')
    # stand_url = "https://iustudio.tistory.com/"
    # url_code = int(start_url[3])
    #
    # # store all into url_list
    # for code in range(url_code, 1580, -1):
    #     start_urls.append(stand_url + str(code))

    def parse(self, response):
        clean_image_urls = []

        # retreive image url
        raw_image_urls = response.css('div.imageblock img').xpath('@src').getall()
        if raw_image_urls is None:
            raw_image_urls = response.css('span.imageblock img').xpath('@src').getall()
        if raw_image_urls is None:
            raw_image_urls = response.css('figure.imageblock img').xpath('@src').getall()

        for image_url in raw_image_urls:
            clean_image_urls.append(image_url)

        yield {
        # note key has to be "image_urls"
            "image_urls" : clean_image_urls
        }
