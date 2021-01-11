---
title: ContentHandler.endElement()
permalink: Java/ContentHandler-org-xml-sax/endElement
date: 2021-01-11
key: JavaJava.C.ContentHandler-org-xml-sax
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContentHandler-org-xml-sax.metodos valor="endElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void endElement(String uri, String localName, String qName) throws SAXException
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[ContentHandler](/Java/ContentHandler-org-xml-sax/)

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
