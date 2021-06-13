---
title: PriorityQueue.PriorityQueue()
permalink: /Java/PriorityQueue/PriorityQueue/
date: 2021-01-11
key: Java.P.PriorityQueue
category: Java
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
* **SortedSet&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="SortedSet<? extends E> c" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}
* **Comparator&lt;? super E&gt; comparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super E> comparator" %}
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> c" %}
* **PriorityQueue&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="PriorityQueue<? extends E> c" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PriorityQueue](/Java/PriorityQueue/)

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
