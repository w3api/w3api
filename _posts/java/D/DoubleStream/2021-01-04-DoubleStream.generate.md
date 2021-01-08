---
title: DoubleStream.generate()
permalink: Java/DoubleStream/generate
date: 2021-01-04
key: JavaJava.D.DoubleStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="generate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static DoubleStream generate(DoubleSupplier s)
~~~

## Parámetros
* **DoubleSupplier s**,  {% include w3api/param_description.html metodo=_data parametro="DoubleSupplier s" %}

## Clase Padre
[DoubleStream](/Java/DoubleStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DoubleStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
