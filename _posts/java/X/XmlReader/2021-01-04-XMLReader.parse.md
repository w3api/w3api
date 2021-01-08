---
title: XMLReader.parse()
permalink: Java/XMLReader/parse
date: 2021-01-04
key: JavaJava.X.XMLReader
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLReader.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void parse(String systemId) throws IOException, SAXException
void parse(InputSource input) throws IOException, SAXException
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **InputSource input**,  {% include w3api/param_description.html metodo=_data parametro="InputSource input" %}

## Excepciones
[SAXException](/Java/SAXException/), [IOException](/Java/IOException/)

## Clase Padre
[XMLReader](/Java/XMLReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
