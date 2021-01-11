---
title: DoubleStream.limit()
permalink: Java/DoubleStream/limit
date: 2021-01-11
key: JavaJava.D.DoubleStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="limit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DoubleStream limit(long maxSize)
~~~

## Parámetros
* **long maxSize**,  {% include w3api/param_description.html metodo=_dato parametro="long maxSize" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DoubleStream](/Java/DoubleStream/)

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
