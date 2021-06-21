---
title: ParserAdapter.ParserAdapter()
permalink: /Java/ParserAdapter/ParserAdapter/
date: 2021-01-11
key: Java.P.ParserAdapter
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParserAdapter.constructores valor="ParserAdapter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ParserAdapter() throws SAXException
public ParserAdapter(Parser parser)
~~~

## Parámetros
* **Parser parser**,  {% include w3api/param_description.html metodo=_dato parametro="Parser parser" %}

## Excepciones
[SAXException](/Java/SAXException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ParserAdapter](/Java/ParserAdapter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
