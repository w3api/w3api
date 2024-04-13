---
title: IntStream.flatMap()
permalink: /Java/IntStream/flatMap/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="flatMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
IntStream flatMap(IntFunction<? extends IntStream> mapper)
~~~

## Parámetros
* **IntFunction&lt;? extends IntStream&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="IntFunction<? extends IntStream> mapper" %}

## Clase Padre
[IntStream](/Java/IntStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
