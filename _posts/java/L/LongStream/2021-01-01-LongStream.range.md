---
title: LongStream.range()
permalink: /Java/LongStream/range/
date: 2021-01-11
key: Java.L.LongStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="range" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static LongStream range(long startInclusive, long endExclusive)
~~~

## Parámetros
* **long endExclusive**,  {% include w3api/param_description.html metodo=_dato parametro="long endExclusive" %}
* **long startInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="long startInclusive" %}

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
