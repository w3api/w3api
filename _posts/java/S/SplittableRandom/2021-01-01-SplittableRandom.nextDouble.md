---
title: SplittableRandom.nextDouble()
permalink: /Java/SplittableRandom/nextDouble/
date: 2021-01-11
key: Java.S.SplittableRandom
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SplittableRandom.metodos valor="nextDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double nextDouble()
public double nextDouble(double bound)
public double nextDouble(double origin, double bound)
~~~

## Parámetros
* **double origin**,  {% include w3api/param_description.html metodo=_dato parametro="double origin" %}
* **double bound**,  {% include w3api/param_description.html metodo=_dato parametro="double bound" %}

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
