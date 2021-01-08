---
title: IntStream.flatMap()
permalink: Java/IntStream/flatMap
date: 2021-01-04
key: JavaJava.I.IntStream
category: java
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
* **IntFunction&lt;? extends IntStream&gt; mapper**,  {% include w3api/param_description.html metodo=_data parametro="IntFunction<? extends IntStream> mapper" %}

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
