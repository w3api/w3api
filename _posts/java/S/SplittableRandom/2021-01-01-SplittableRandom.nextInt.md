---
title: SplittableRandom.nextInt()
permalink: Java/SplittableRandom/nextInt
date: 2021-01-11
key: JavaJava.S.SplittableRandom
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SplittableRandom.metodos valor="nextInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int nextInt()
public int nextInt(int bound)
public int nextInt(int origin, int bound)
~~~

## Parámetros
* **int bound**,  {% include w3api/param_description.html metodo=_dato parametro="int bound" %}
* **int origin**,  {% include w3api/param_description.html metodo=_dato parametro="int origin" %}

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
