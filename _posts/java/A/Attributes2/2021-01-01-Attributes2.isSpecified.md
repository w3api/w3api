---
title: Attributes2.isSpecified()
permalink: Java/Attributes2/isSpecified
date: 2021-01-11
key: JavaJava.A.Attributes2
category: java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.5', 'SAX 2.0 (extensions Java 1.1 alpha)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attributes2.metodos valor="isSpecified" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isSpecified(int index)
boolean isSpecified(String qName)
boolean isSpecified(String uri, String localName)
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[Attributes2](/Java/Attributes2/)

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
