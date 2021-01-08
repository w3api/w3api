---
title: XMLReader.getFeature()
permalink: Java/XMLReader/getFeature
date: 2021-01-04
key: JavaJava.X.XMLReader
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLReader.metodos valor="getFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean getFeature(String name) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[SAXNotSupportedException](/Java/SAXNotSupportedException/), [SAXNotRecognizedException](/Java/SAXNotRecognizedException/)

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
