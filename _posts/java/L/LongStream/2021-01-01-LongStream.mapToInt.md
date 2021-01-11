---
title: LongStream.mapToInt()
permalink: Java/LongStream/mapToInt
date: 2021-01-11
key: JavaJava.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="mapToInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
IntStream mapToInt(LongToIntFunction mapper)
~~~

## Parámetros
* **LongToIntFunction mapper**,  {% include w3api/param_description.html metodo=_dato parametro="LongToIntFunction mapper" %}

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
