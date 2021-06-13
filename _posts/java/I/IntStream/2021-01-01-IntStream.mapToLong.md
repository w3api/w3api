---
title: IntStream.mapToLong()
permalink: /Java/IntStream/mapToLong/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="mapToLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LongStream mapToLong(IntToLongFunction mapper)
~~~

## Parámetros
* **IntToLongFunction mapper**,  {% include w3api/param_description.html metodo=_dato parametro="IntToLongFunction mapper" %}

## Clase Padre
[IntStream](/Java/IntStream/)

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
