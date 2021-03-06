---
title: SAXParserFactory.setFeature()
permalink: /Java/SAXParserFactory/setFeature/
date: 2021-01-11
key: Java.S.SAXParserFactory
category: Java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAXParserFactory.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setFeature(String name, boolean value) throws ParserConfigurationException, SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/), [ParserConfigurationException](/Java/ParserConfigurationException/), [NullPointerException](/Java/NullPointerException/)

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
