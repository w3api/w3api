---
title: BufferedReader.BufferedReader()
permalink: /Java/BufferedReader/BufferedReader/
date: 2021-01-11
key: Java.B.BufferedReader
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedReader.constructores valor="BufferedReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedReader(Reader in)
public BufferedReader(Reader in, int sz)
~~~

## Parámetros
* **int sz**,  {% include w3api/param_description.html metodo=_dato parametro="int sz" %}
* **Reader in**,  {% include w3api/param_description.html metodo=_dato parametro="Reader in" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BufferedReader](/Java/BufferedReader/)

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
