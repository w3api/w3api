---
title: DoubleStream.reduce()
permalink: /Java/DoubleStream/reduce/
date: 2021-01-11
key: Java.D.DoubleStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="reduce" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
double reduce(double identity, DoubleBinaryOperator op)
OptionalDouble reduce(DoubleBinaryOperator op)
~~~

## Parámetros
* **double identity**,  {% include w3api/param_description.html metodo=_dato parametro="double identity" %}
* **DoubleBinaryOperator op**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleBinaryOperator op" %}

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
