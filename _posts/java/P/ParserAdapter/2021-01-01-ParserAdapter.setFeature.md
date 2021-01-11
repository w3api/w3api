---
title: ParserAdapter.setFeature()
permalink: Java/ParserAdapter/setFeature
date: 2021-01-11
key: JavaJava.P.ParserAdapter
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParserAdapter.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFeature(String name, boolean value) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/)

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
