---
title: SplittableRandom.nextLong()
permalink: Java/SplittableRandom/nextLong
date: 2021-01-11
key: JavaJava.S.SplittableRandom
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SplittableRandom.metodos valor="nextLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long nextLong()
public long nextLong(long bound)
public long nextLong(long origin, long bound)
~~~

## Parámetros
* **long origin**,  {% include w3api/param_description.html metodo=_dato parametro="long origin" %}
* **long bound**,  {% include w3api/param_description.html metodo=_dato parametro="long bound" %}

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
