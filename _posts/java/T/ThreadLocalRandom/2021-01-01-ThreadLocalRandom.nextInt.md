---
title: ThreadLocalRandom.nextInt()
permalink: Java/ThreadLocalRandom/nextInt
date: 2021-01-11
key: JavaJava.T.ThreadLocalRandom
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocalRandom.metodos valor="nextInt" %}

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
