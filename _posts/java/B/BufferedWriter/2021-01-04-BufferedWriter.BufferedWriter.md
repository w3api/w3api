---
title: BufferedWriter.BufferedWriter()
permalink: Java/BufferedWriter/BufferedWriter
date: 2021-01-04
key: JavaJava.B.BufferedWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedWriter.constructores valor="BufferedWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedWriter(Writer out)
public BufferedWriter(Writer out, int sz)
~~~

## Parámetros
* **Writer out**,  {% include w3api/param_description.html metodo=_data parametro="Writer out" %}
* **int sz**,  {% include w3api/param_description.html metodo=_data parametro="int sz" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BufferedWriter](/Java/BufferedWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BufferedWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
