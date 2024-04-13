---
title: StringBuffer.offsetByCodePoints()
permalink: /Java/StringBuffer/offsetByCodePoints/
date: 2021-01-11
key: Java.S.StringBuffer
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuffer.metodos valor="offsetByCodePoints" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int offsetByCodePoints(int index, int codePointOffset)
~~~

## Parámetros
* **int codePointOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int codePointOffset" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

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
