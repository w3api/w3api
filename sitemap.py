# Split sitemap in files with no more than 50.000 entries
from bs4 import BeautifulSoup
import math, shutil

__PATH__ = '_site/'

# Método que genera el sitemap dado diccionario URL
def generate_sitemap(number,urls):    
    file = f"{__PATH__}sitemap-{number}.xml"
    f = open(file, "w")
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in urls:
        f.write(str(url)+'\n')
    f.write('</urlset>')
    f.close()

#copio el sitemap.xml a uno temporal sitemap-temp.xml
shutil.copy(f"{__PATH__}sitemap.xml",f"{__PATH__}sitemap-temp.xml")

with open(f"{__PATH__}sitemap-temp.xml") as fp:
    soup = BeautifulSoup(fp, 'xml')

# Calculamos el números de ficheros a crear
urls = soup.find_all("url")
numero = len(urls)
numeroficheros = math.ceil(numero / 50000)

# Generamos los ficheros
for i in range(numeroficheros):
    generate_sitemap(i+1,urls[50000*(i):50000*(i+1)])
 
# Generamos el sitemap general
file = f"{__PATH__}sitemap.xml"
f = open(file, "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')  
f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')    
for i in range(numeroficheros):
    f.write("<sitemap>\n")
    f.write(f"<loc>https://www.w3api.com/sitemap-{i+1}.xml</loc>\n")
    f.write("</sitemap>\n")
f.write('</sitemapindex>')
f.close()
