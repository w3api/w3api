---
title: ThreadLocalRandom.nextLong()
permalink: Java/ThreadLocalRandom/nextLong
date: 2021-01-11
key: JavaJava.T.ThreadLocalRandom
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocalRandom.metodos valor="nextLong" %}

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
