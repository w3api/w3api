---
title: BlockingQueue.offer()
permalink: Java/BlockingQueue/offer
date: 2021-01-04
key: JavaJava.B.BlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BlockingQueue.metodos valor="offer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean offer(E e)
boolean offer(E e, long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **E e**,  {% include w3api/param_description.html metodo=_data parametro="E e" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BlockingQueue](/Java/BlockingQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BlockingQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
