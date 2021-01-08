---
title: PriorityBlockingQueue.PriorityBlockingQueue()
permalink: Java/PriorityBlockingQueue/PriorityBlockingQueue
date: 2021-01-04
key: JavaJava.P.PriorityBlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PriorityBlockingQueue.constructores valor="PriorityBlockingQueue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PriorityBlockingQueue()
public PriorityBlockingQueue(int initialCapacity)
public PriorityBlockingQueue(int initialCapacity, Comparator<? super E> comparator)
public PriorityBlockingQueue(Collection<? extends E> c)
~~~

## Parámetros
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends E> c" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **Comparator&lt;? super E&gt; comparator**,  {% include w3api/param_description.html metodo=_data parametro="Comparator<? super E> comparator" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PriorityBlockingQueue](/Java/PriorityBlockingQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PriorityBlockingQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
