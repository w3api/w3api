---
title: ErrorHandler.warning()
permalink: Java/ErrorHandler/warning
date: 2021-01-11
key: JavaJava.E.ErrorHandler
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ErrorHandler.metodos valor="warning" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void warning(SAXParseException exception) throws SAXException
~~~

## Parámetros
* **SAXParseException exception**,  {% include w3api/param_description.html metodo=_dato parametro="SAXParseException exception" %}

## Excepciones
[SAXException](/Java/SAXException/), [SAXParseException](/Java/SAXParseException/)

## Clase Padre
[ErrorHandler](/Java/ErrorHandler/)

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
