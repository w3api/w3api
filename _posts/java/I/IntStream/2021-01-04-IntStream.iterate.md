---
title: IntStream.iterate()
permalink: Java/IntStream/iterate
date: 2021-01-04
key: JavaJava.I.IntStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="iterate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static IntStream iterate(int seed, IntPredicate hasNext, IntUnaryOperator next)
static IntStream iterate(int seed, IntUnaryOperator f)
~~~

## Parámetros
* **IntPredicate hasNext**,  {% include w3api/param_description.html metodo=_data parametro="IntPredicate hasNext" %}
* **IntUnaryOperator f**,  {% include w3api/param_description.html metodo=_data parametro="IntUnaryOperator f" %}
* **IntUnaryOperator next**,  {% include w3api/param_description.html metodo=_data parametro="IntUnaryOperator next" %}
* **int seed**,  {% include w3api/param_description.html metodo=_data parametro="int seed" %}

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
