---
title: LongStream.mapToDouble()
permalink: Java/LongStream/mapToDouble
date: 2021-01-11
key: JavaJava.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="mapToDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DoubleStream mapToDouble(LongToDoubleFunction mapper)
~~~

## Parámetros
* **LongToDoubleFunction mapper**,  {% include w3api/param_description.html metodo=_dato parametro="LongToDoubleFunction mapper" %}

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
