---
title: ArrayBlockingQueue.toArray()
permalink: Java/ArrayBlockingQueue/toArray
date: 2021-01-11
key: JavaJava.A.ArrayBlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayBlockingQueue.metodos valor="toArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object[] toArray()
<T> T[] toArray(T[] a)
~~~

## Parámetros
* **T[] a**,  {% include w3api/param_description.html metodo=_dato parametro="T[] a" %}

## Clase Padre
[ArrayBlockingQueue](/Java/ArrayBlockingQueue/)

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
