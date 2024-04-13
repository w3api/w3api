---
title: IntStream.reduce()
permalink: /Java/IntStream/reduce/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="reduce" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int reduce(int identity, IntBinaryOperator op)
OptionalInt reduce(IntBinaryOperator op)
~~~

## Parámetros
* **IntBinaryOperator op**,  {% include w3api/param_description.html metodo=_dato parametro="IntBinaryOperator op" %}
* **int identity**,  {% include w3api/param_description.html metodo=_dato parametro="int identity" %}

## Clase Padre
[IntStream](/Java/IntStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
