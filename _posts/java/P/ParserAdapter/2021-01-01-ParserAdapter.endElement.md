---
title: ParserAdapter.endElement()
permalink: Java/ParserAdapter/endElement
date: 2021-01-11
key: JavaJava.P.ParserAdapter
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParserAdapter.metodos valor="endElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void endElement(String qName) throws SAXException
~~~

## Parámetros
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[ParserAdapter](/Java/ParserAdapter/)

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
