---
title: LinkedBlockingQueue.LinkedBlockingQueue()
permalink: Java/LinkedBlockingQueue/LinkedBlockingQueue
date: 2021-01-11
key: JavaJava.L.LinkedBlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedBlockingQueue.constructores valor="LinkedBlockingQueue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LinkedBlockingQueue()
public LinkedBlockingQueue(int capacity)
public LinkedBlockingQueue(Collection<? extends E> c)
~~~

## Parámetros
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> c" %}
* **int capacity**,  {% include w3api/param_description.html metodo=_dato parametro="int capacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinkedBlockingQueue](/Java/LinkedBlockingQueue/)

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
