---
title: XMLReaderAdapter.endElement()
permalink: /Java/XMLReaderAdapter/endElement/
date: 2021-01-11
key: Java.X.XMLReaderAdapter
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLReaderAdapter.metodos valor="endElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void endElement(String uri, String localName, String qName) throws SAXException
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[XMLReaderAdapter](/Java/XMLReaderAdapter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
