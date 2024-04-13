---
title: ThreadLocalRandom.longs()
permalink: /Java/ThreadLocalRandom/longs/
date: 2021-01-11
key: Java.T.ThreadLocalRandom
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocalRandom.metodos valor="longs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LongStream longs()
public LongStream longs(long streamSize)
public LongStream longs(long randomNumberOrigin, long randomNumberBound)
public LongStream longs(long streamSize, long randomNumberOrigin, long randomNumberBound)
~~~

## Parámetros
* **long randomNumberBound**,  {% include w3api/param_description.html metodo=_dato parametro="long randomNumberBound" %}
* **long randomNumberOrigin**,  {% include w3api/param_description.html metodo=_dato parametro="long randomNumberOrigin" %}
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
