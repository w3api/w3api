---
title: DoubleStream.iterate()
permalink: Java/DoubleStream/iterate
date: 2021-01-11
key: JavaJava.D.DoubleStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="iterate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static DoubleStream iterate(double seed, DoublePredicate hasNext, DoubleUnaryOperator next)
static DoubleStream iterate(double seed, DoubleUnaryOperator f)
~~~

## Parámetros
* **DoubleUnaryOperator f**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleUnaryOperator f" %}
* **double seed**,  {% include w3api/param_description.html metodo=_dato parametro="double seed" %}
* **DoubleUnaryOperator next**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleUnaryOperator next" %}
* **DoublePredicate hasNext**,  {% include w3api/param_description.html metodo=_dato parametro="DoublePredicate hasNext" %}

## Clase Padre
[DoubleStream](/Java/DoubleStream/)

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
