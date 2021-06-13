---
title: Attributes2Impl.isSpecified()
permalink: /Java/Attributes2Impl/isSpecified/
date: 2021-01-11
key: Java.A.Attributes2Impl
category: Java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.5', 'SAX 2.0 (extensions Java 1.1 alpha)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attributes2Impl.metodos valor="isSpecified" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isSpecified(int index)
public boolean isSpecified(String qName)
public boolean isSpecified(String uri, String localName)
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[Attributes2Impl](/Java/Attributes2Impl/)

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
