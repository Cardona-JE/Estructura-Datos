import scrapy

class MercadoLibreItem(scrapy.Item):
    Nombre = scrapy.Field()
    Precio = scrapy.Field()
    Imagen = scrapy.Field()
    Enlace = scrapy.Field()