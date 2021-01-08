---
title: StringBuffer.codePointCount()
permalink: Java/StringBuffer/codePointCount
date: 2021-01-04
key: JavaJava.S.StringBuffer
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuffer.metodos valor="codePointCount" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int codePointCount(int beginIndex, int endIndex)
~~~

## Parámetros
* **int endIndex**,  {% include w3api/param_description.html metodo=_data parametro="int endIndex" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_data parametro="int beginIndex" %}

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
{%- for _ldc in site.data.Java.S.StringBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
