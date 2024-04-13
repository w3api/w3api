---
title: LongStream.flatMap()
permalink: /Java/LongStream/flatMap/
date: 2021-01-11
key: Java.L.LongStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="flatMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LongStream flatMap(LongFunction<? extends LongStream> mapper)
~~~

## Parámetros
* **LongFunction&lt;? extends LongStream&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="LongFunction<? extends LongStream> mapper" %}

## Clase Padre
[LongStream](/Java/LongStream/)

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
