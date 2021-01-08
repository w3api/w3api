---
title: PriorityQueue.PriorityQueue()
permalink: Java/PriorityQueue/PriorityQueue
date: 2021-01-04
key: JavaJava.P.PriorityQueue
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PriorityQueue.constructores valor="PriorityQueue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PriorityQueue()
public PriorityQueue(int initialCapacity)
public PriorityQueue(int initialCapacity, Comparator<? super E> comparator)
public PriorityQueue(Collection<? extends E> c)
public PriorityQueue(Comparator<? super E> comparator)
public PriorityQueue(PriorityQueue<? extends E> c)
public PriorityQueue(SortedSet<? extends E> c)
~~~

## Parámetros
* **Comparator&lt;? super E&gt; comparator**,  {% include w3api/param_description.html metodo=_data parametro="Comparator<? super E> comparator" %}
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends E> c" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **PriorityQueue&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="PriorityQueue<? extends E> c" %}
* **SortedSet&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="SortedSet<? extends E> c" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PriorityQueue](/Java/PriorityQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PriorityQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
