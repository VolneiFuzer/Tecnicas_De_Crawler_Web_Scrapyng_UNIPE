import scrapy
# from scrapy.utils.response import open_in_browser

class YahooSpider(scrapy.Spider):
   
    name = "Yahoo"

    start_urls = {
        'https://br.noticias.yahoo.com/'
    }

    def parse(self, response):
        #open_in_browser(response)
        
        resultados = response.css('.js-stream-content')

        for resultado in resultados:
            print('Titulo: ' + str(resultado.css('::text').extract()))
