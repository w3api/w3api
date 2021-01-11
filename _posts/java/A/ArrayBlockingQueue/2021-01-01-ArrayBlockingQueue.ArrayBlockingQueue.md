---
title: ArrayBlockingQueue.ArrayBlockingQueue()
permalink: Java/ArrayBlockingQueue/ArrayBlockingQueue
date: 2021-01-11
key: JavaJava.A.ArrayBlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayBlockingQueue.constructores valor="ArrayBlockingQueue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ArrayBlockingQueue(int capacity)
public ArrayBlockingQueue(int capacity, boolean fair)
public ArrayBlockingQueue(int capacity, boolean fair, Collection<? extends E> c)
~~~

## Parámetros
* **boolean fair**,  {% include w3api/param_description.html metodo=_dato parametro="boolean fair" %}
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> c" %}
* **int capacity**,  {% include w3api/param_description.html metodo=_dato parametro="int capacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
