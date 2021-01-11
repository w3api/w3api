---
title: DoubleStream.of()
permalink: Java/DoubleStream/of
date: 2021-01-11
key: JavaJava.D.DoubleStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static DoubleStream of(double t)
static DoubleStream of(double... values)
~~~

## Parámetros
* **double... values**,  {% include w3api/param_description.html metodo=_dato parametro="double... values" %}
* **double t**,  {% include w3api/param_description.html metodo=_dato parametro="double t" %}

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
