---
title: LineNumberReader.LineNumberReader()
permalink: Java/LineNumberReader/LineNumberReader
date: 2021-01-11
key: Java.L.LineNumberReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineNumberReader.constructores valor="LineNumberReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LineNumberReader(Reader in)
public LineNumberReader(Reader in, int sz)
~~~

## Parámetros
* **int sz**,  {% include w3api/param_description.html metodo=_dato parametro="int sz" %}
* **Reader in**,  {% include w3api/param_description.html metodo=_dato parametro="Reader in" %}

## Clase Padre
[LineNumberReader](/Java/LineNumberReader/)

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
