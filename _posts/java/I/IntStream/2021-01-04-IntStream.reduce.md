---
title: IntStream.reduce()
permalink: Java/IntStream/reduce
date: 2021-01-04
key: JavaJava.I.IntStream
category: java
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
* **int identity**,  {% include w3api/param_description.html metodo=_data parametro="int identity" %}
* **IntBinaryOperator op**,  {% include w3api/param_description.html metodo=_data parametro="IntBinaryOperator op" %}

## Clase Padre
[IntStream](/Java/IntStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
