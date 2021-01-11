---
title: DoubleStream.flatMap()
permalink: Java/DoubleStream/flatMap
date: 2021-01-11
key: JavaJava.D.DoubleStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="flatMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DoubleStream flatMap(DoubleFunction<? extends DoubleStream> mapper)
~~~

## Parámetros
* **DoubleFunction&lt;? extends DoubleStream&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleFunction<? extends DoubleStream> mapper" %}

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
