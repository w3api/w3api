---
title: ConcurrentSkipListSet.ConcurrentSkipListSet()
permalink: Java/ConcurrentSkipListSet/ConcurrentSkipListSet
date: 2021-01-11
key: JavaJava.C.ConcurrentSkipListSet
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListSet.constructores valor="ConcurrentSkipListSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConcurrentSkipListSet()
public ConcurrentSkipListSet(Collection<? extends E> c)
public ConcurrentSkipListSet(Comparator<? super E> comparator)
public ConcurrentSkipListSet(SortedSet<E> s)
~~~

## Parámetros
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> c" %}
* **SortedSet&lt;E&gt; s**,  {% include w3api/param_description.html metodo=_dato parametro="SortedSet<E> s" %}
* **Comparator&lt;? super E&gt; comparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super E> comparator" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentSkipListSet](/Java/ConcurrentSkipListSet/)

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
