---
title: ParserAdapter.parse()
permalink: /Java/ParserAdapter/parse/
date: 2021-01-11
key: Java.P.ParserAdapter
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParserAdapter.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void parse(String systemId) throws IOException, SAXException
public void parse(InputSource input) throws IOException, SAXException
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **InputSource input**,  {% include w3api/param_description.html metodo=_dato parametro="InputSource input" %}

## Excepciones
[SAXException](/Java/SAXException/), [IOException](/Java/IOException/)

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
