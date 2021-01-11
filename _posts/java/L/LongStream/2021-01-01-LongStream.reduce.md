---
title: LongStream.reduce()
permalink: Java/LongStream/reduce
date: 2021-01-11
key: JavaJava.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="reduce" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long reduce(long identity, LongBinaryOperator op)
OptionalLong reduce(LongBinaryOperator op)
~~~

## Parámetros
* **long identity**,  {% include w3api/param_description.html metodo=_dato parametro="long identity" %}
* **LongBinaryOperator op**,  {% include w3api/param_description.html metodo=_dato parametro="LongBinaryOperator op" %}

## Clase Padre
[LongStream](/Java/LongStream/)

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
