---
title: StringBuffer.StringBuffer()
permalink: /Java/StringBuffer/StringBuffer/
date: 2021-01-11
key: Java.S.StringBuffer
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuffer.constructores valor="StringBuffer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuffer()
public StringBuffer(int capacity)
public StringBuffer(CharSequence seq)
public StringBuffer(String str)
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **CharSequence seq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence seq" %}
* **int capacity**,  {% include w3api/param_description.html metodo=_dato parametro="int capacity" %}

## Excepciones
[NegativeArraySizeException](/Java/NegativeArraySizeException/)

## Clase Padre
[StringBuffer](/Java/StringBuffer/)

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
