---
title: SAXParserFactory.getFeature()
permalink: Java/SAXParserFactory/getFeature
date: 2021-01-11
key: JavaJava.S.SAXParserFactory
category: java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAXParserFactory.metodos valor="getFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean getFeature(String name) throws ParserConfigurationException, SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/), [ParserConfigurationException](/Java/ParserConfigurationException/)

## Clase Padre
[SAXParserFactory](/Java/SAXParserFactory/)

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
