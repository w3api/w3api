---
title: ArrayBlockingQueue.offer()
permalink: /Java/ArrayBlockingQueue/offer/
date: 2021-01-11
key: Java.A.ArrayBlockingQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayBlockingQueue.metodos valor="offer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean offer(E e)
public boolean offer(E e, long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **E e**,  {% include w3api/param_description.html metodo=_dato parametro="E e" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [NullPointerException](/Java/NullPointerException/)

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
