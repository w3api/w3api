---
title: BufferedReader.mark()
permalink: /Java/BufferedReader/mark/
date: 2021-01-11
key: Java.B.BufferedReader
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedReader.metodos valor="mark" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void mark(int readAheadLimit) throws IOException
~~~

## Parámetros
* **int readAheadLimit**,  {% include w3api/param_description.html metodo=_dato parametro="int readAheadLimit" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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
