---
title: LongStream.iterate()
permalink: Java/LongStream/iterate
date: 2021-01-04
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
* **long seed**,  {% include w3api/param_description.html metodo=_data parametro="long seed" %}
* **LongPredicate hasNext**,  {% include w3api/param_description.html metodo=_data parametro="LongPredicate hasNext" %}
* **LongUnaryOperator f**,  {% include w3api/param_description.html metodo=_data parametro="LongUnaryOperator f" %}
* **LongUnaryOperator next**,  {% include w3api/param_description.html metodo=_data parametro="LongUnaryOperator next" %}

## Clase Padre
[LongStream](/Java/LongStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
