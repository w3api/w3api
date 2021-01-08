---
title: DoubleStream.mapToLong()
permalink: Java/DoubleStream/mapToLong
date: 2021-01-04
key: JavaJava.D.DoubleStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="mapToLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LongStream mapToLong(DoubleToLongFunction mapper)
~~~

## Parámetros
* **DoubleToLongFunction mapper**,  {% include w3api/param_description.html metodo=_data parametro="DoubleToLongFunction mapper" %}

## Clase Padre
[DoubleStream](/Java/DoubleStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DoubleStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
