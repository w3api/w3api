---
title: DefaultHandler.fatalError()
permalink: /Java/DefaultHandler/fatalError/
date: 2021-01-11
key: Java.D.DefaultHandler
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultHandler.metodos valor="fatalError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void fatalError(SAXParseException e) throws SAXException
~~~

## Parámetros
* **SAXParseException e**,  {% include w3api/param_description.html metodo=_dato parametro="SAXParseException e" %}

## Excepciones
[SAXException](/Java/SAXException/), [ErrorHandler.fatalError(org.xml.sax.SAXParseException)](/Java/ErrorHandler.fatalError(org.xml.sax.SAXParseException)/)

## Clase Padre
[DefaultHandler](/Java/DefaultHandler/)

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
