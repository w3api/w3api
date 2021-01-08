---
title: IntStream.mapToDouble()
permalink: Java/IntStream/mapToDouble
date: 2021-01-04
key: JavaJava.I.IntStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="mapToDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DoubleStream mapToDouble(IntToDoubleFunction mapper)
~~~

## Parámetros
* **IntToDoubleFunction mapper**,  {% include w3api/param_description.html metodo=_data parametro="IntToDoubleFunction mapper" %}

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
