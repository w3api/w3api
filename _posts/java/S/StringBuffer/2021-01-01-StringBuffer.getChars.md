---
title: StringBuffer.getChars()
permalink: Java/StringBuffer/getChars
date: 2021-01-11
key: JavaJava.S.StringBuffer
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuffer.metodos valor="getChars" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)
~~~

## Parámetros
* **int dstBegin**,  {% include w3api/param_description.html metodo=_dato parametro="int dstBegin" %}
* **char[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="char[] dst" %}
* **int srcEnd**,  {% include w3api/param_description.html metodo=_dato parametro="int srcEnd" %}
* **int srcBegin**,  {% include w3api/param_description.html metodo=_dato parametro="int srcBegin" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

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
