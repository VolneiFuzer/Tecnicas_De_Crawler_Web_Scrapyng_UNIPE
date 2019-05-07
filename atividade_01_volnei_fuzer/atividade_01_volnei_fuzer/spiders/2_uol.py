import scrapy

#from scrapy.utils.response import open_in_browser

# Para retirar o log, deve rodar o comando: scrapy runspider --nolog 2_uol.py

class UolSpider(scrapy.Spider):
    
    name = "Uol"

    start_urls = {
        'https://www.uol.com.br/'
    }

    def parse(self, response):
        #open_in_browser(response)
        
        resultado = response.css('.currency_quote')
        
        print('A cotação atual do dólar é: ' + str(resultado.css('::text').extract_first()))