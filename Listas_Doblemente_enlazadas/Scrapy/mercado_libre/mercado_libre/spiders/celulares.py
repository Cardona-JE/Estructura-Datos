import scrapy
from mercado_libre.items import MercadoLibreItem

class CelularesSpider(scrapy.Spider):
    name = "celulares"
    start_urls = ['https://www.mercadolibre.com.co/c/celulares-y-telefonos']

    def parse(self, response):
        contenedores_celular = response.css('div.dynamic-carousel__item-container')

        for contenedor in contenedores_celular:
            elemento_nombre = contenedor.css('h3.dynamic-carousel__title::text').get()
            elemento_precio = contenedor.css('span.dynamic-carousel__price span::text').get()
            elemento_imagen = contenedor.css('img.dynamic-carousel__img::attr(data-src)').get()
            elemento_enlace = contenedor.css('a.splinter-link::attr(href)').get()

            if elemento_nombre and elemento_precio and elemento_imagen and elemento_enlace:
                nombre = elemento_nombre.strip()
                precio = elemento_precio.strip()
                enlace = elemento_enlace
                imagen_url = elemento_imagen

                item = MercadoLibreItem()
                item['Nombre'] = nombre
                item['Precio'] = precio
                item['Imagen'] = imagen_url
                item['Enlace'] = enlace

                yield item
