---
title: DocumentHandler.ignorableWhitespace()
permalink: Java/DocumentHandler/ignorableWhitespace
date: 2021-01-04
key: JavaJava.D.DocumentHandler
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentHandler.metodos valor="ignorableWhitespace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void ignorableWhitespace(char[] ch, int start, int length) throws SAXException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **char[] ch**,  {% include w3api/param_description.html metodo=_data parametro="char[] ch" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[DocumentHandler](/Java/DocumentHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocumentHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
