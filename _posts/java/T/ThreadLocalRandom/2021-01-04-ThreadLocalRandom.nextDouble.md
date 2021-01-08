---
title: ThreadLocalRandom.nextDouble()
permalink: Java/ThreadLocalRandom/nextDouble
date: 2021-01-04
key: JavaJava.T.ThreadLocalRandom
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocalRandom.metodos valor="nextDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double nextDouble()
public double nextDouble(double bound)
public double nextDouble(double origin, double bound)
~~~

## Parámetros
* **double bound**,  {% include w3api/param_description.html metodo=_data parametro="double bound" %}
* **double origin**,  {% include w3api/param_description.html metodo=_data parametro="double origin" %}

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
