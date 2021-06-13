---
title: LongStream.of()
permalink: Java/LongStream/of
date: 2021-01-11
key: Java.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static LongStream of(long t)
static LongStream of(long... values)
~~~

## Parámetros
* **long... values**,  {% include w3api/param_description.html metodo=_dato parametro="long... values" %}
* **long t**,  {% include w3api/param_description.html metodo=_dato parametro="long t" %}

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
