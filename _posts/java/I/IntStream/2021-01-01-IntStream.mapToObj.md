---
title: IntStream.mapToObj()
permalink: /Java/IntStream/mapToObj/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="mapToObj" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> Stream<U> mapToObj(IntFunction<? extends U> mapper)
~~~

## Parámetros
* **IntFunction&lt;? extends U&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="IntFunction<? extends U> mapper" %}

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
