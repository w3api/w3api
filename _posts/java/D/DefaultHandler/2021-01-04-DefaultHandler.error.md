---
title: DefaultHandler.error()
permalink: Java/DefaultHandler/error
date: 2021-01-04
key: JavaJava.D.DefaultHandler
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultHandler.metodos valor="error" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void error(SAXParseException e) throws SAXException
~~~

## Parámetros
* **SAXParseException e**,  {% include w3api/param_description.html metodo=_data parametro="SAXParseException e" %}

## Excepciones
[ErrorHandler.warning(org.xml.sax.SAXParseException)](/Java/ErrorHandler.warning(org.xml.sax.SAXParseException)/), [SAXException](/Java/SAXException/)

## Clase Padre
[DefaultHandler](/Java/DefaultHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
