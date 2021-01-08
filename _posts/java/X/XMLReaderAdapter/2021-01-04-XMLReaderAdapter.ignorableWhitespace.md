---
title: XMLReaderAdapter.ignorableWhitespace()
permalink: Java/XMLReaderAdapter/ignorableWhitespace
date: 2021-01-04
key: JavaJava.X.XMLReaderAdapter
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLReaderAdapter.metodos valor="ignorableWhitespace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void ignorableWhitespace(char[] ch, int start, int length) throws SAXException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **char[] ch**,  {% include w3api/param_description.html metodo=_data parametro="char[] ch" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[XMLReaderAdapter](/Java/XMLReaderAdapter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLReaderAdapter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
