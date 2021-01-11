---
title: SplittableRandom.doubles()
permalink: Java/SplittableRandom/doubles
date: 2021-01-11
key: JavaJava.S.SplittableRandom
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SplittableRandom.metodos valor="doubles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DoubleStream doubles()
public DoubleStream doubles(double randomNumberOrigin, double randomNumberBound)
public DoubleStream doubles(long streamSize)
public DoubleStream doubles(long streamSize, double randomNumberOrigin, double randomNumberBound)
~~~

## Parámetros
* **double randomNumberBound**,  {% include w3api/param_description.html metodo=_dato parametro="double randomNumberBound" %}
* **double randomNumberOrigin**,  {% include w3api/param_description.html metodo=_dato parametro="double randomNumberOrigin" %}
* **long streamSize**,  {% include w3api/param_description.html metodo=_dato parametro="long streamSize" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SplittableRandom](/Java/SplittableRandom/)

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
