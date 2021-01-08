---
title: ThreadLocalRandom.ints()
permalink: Java/ThreadLocalRandom/ints
date: 2021-01-04
key: JavaJava.T.ThreadLocalRandom
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocalRandom.metodos valor="ints" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IntStream ints()
public IntStream ints(int randomNumberOrigin, int randomNumberBound)
public IntStream ints(long streamSize)
public IntStream ints(long streamSize, int randomNumberOrigin, int randomNumberBound)
~~~

## Parámetros
* **long streamSize**,  {% include w3api/param_description.html metodo=_data parametro="long streamSize" %}
* **int randomNumberOrigin**,  {% include w3api/param_description.html metodo=_data parametro="int randomNumberOrigin" %}
* **int randomNumberBound**,  {% include w3api/param_description.html metodo=_data parametro="int randomNumberBound" %}

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
{%- for _ldc in site.data.Java.T.ThreadLocalRandom.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
