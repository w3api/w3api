---
title: LongStream.iterate()
permalink: Java/LongStream/iterate
date: 2021-01-11
key: JavaJava.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="iterate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static LongStream iterate(long seed, LongPredicate hasNext, LongUnaryOperator next)
static LongStream iterate(long seed, LongUnaryOperator f)
~~~

## Parámetros
* **LongUnaryOperator next**,  {% include w3api/param_description.html metodo=_dato parametro="LongUnaryOperator next" %}
* **LongPredicate hasNext**,  {% include w3api/param_description.html metodo=_dato parametro="LongPredicate hasNext" %}
* **long seed**,  {% include w3api/param_description.html metodo=_dato parametro="long seed" %}
* **LongUnaryOperator f**,  {% include w3api/param_description.html metodo=_dato parametro="LongUnaryOperator f" %}

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
