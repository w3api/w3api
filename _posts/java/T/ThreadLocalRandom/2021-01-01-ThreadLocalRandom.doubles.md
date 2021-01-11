---
title: ThreadLocalRandom.doubles()
permalink: Java/ThreadLocalRandom/doubles
date: 2021-01-11
key: JavaJava.T.ThreadLocalRandom
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocalRandom.metodos valor="doubles" %}

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
[ThreadLocalRandom](/Java/ThreadLocalRandom/)

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
