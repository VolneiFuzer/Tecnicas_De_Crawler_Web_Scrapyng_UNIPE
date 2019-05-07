import scrapy

# from scrapy.utils.response import open_in_browser

class MarcadoLivreSpider(scrapy.Spider):
    
    name = "Mecado Livre"

    start_urls = {
        'https://www.mercadolivre.com.br/'
    }

    def parse(self, response):
        #open_in_browser(response)
        
        resultados = response.css('.container')

        for resultado in resultados:
            print('Titulo: ' + str(resultado.css('::text').extract()))