---
title: ConcurrentSkipListSet
permalink: /Java/ConcurrentSkipListSet/
date: 2021-01-11
key: Java.C.ConcurrentSkipListSet
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConcurrentSkipListSet.description }}

## Sintaxis
~~~java
public class ConcurrentSkipListSet<E> extends AbstractSet<E> implements NavigableSet<E>, Cloneable, Serializable
~~~

## Constructores
* [ConcurrentSkipListSet()](/Java/ConcurrentSkipListSet/ConcurrentSkipListSet/)

## Métodos
* [add()](/Java/ConcurrentSkipListSet/add/)
* [ceiling()](/Java/ConcurrentSkipListSet/ceiling/)
* [clear()](/Java/ConcurrentSkipListSet/clear/)
* [clone()](/Java/ConcurrentSkipListSet/clone/)
* [contains()](/Java/ConcurrentSkipListSet/contains/)
* [descendingIterator()](/Java/ConcurrentSkipListSet/descendingIterator/)
* [descendingSet()](/Java/ConcurrentSkipListSet/descendingSet/)
* [equals()](/Java/ConcurrentSkipListSet/equals/)
* [first()](/Java/ConcurrentSkipListSet/first/)
* [floor()](/Java/ConcurrentSkipListSet/floor/)
* [headSet()](/Java/ConcurrentSkipListSet/headSet/)
* [higher()](/Java/ConcurrentSkipListSet/higher/)
* [isEmpty()](/Java/ConcurrentSkipListSet/isEmpty/)
* [iterator()](/Java/ConcurrentSkipListSet/iterator/)
* [last()](/Java/ConcurrentSkipListSet/last/)
* [lower()](/Java/ConcurrentSkipListSet/lower/)
* [remove()](/Java/ConcurrentSkipListSet/remove/)
* [removeAll()](/Java/ConcurrentSkipListSet/removeAll/)
* [size()](/Java/ConcurrentSkipListSet/size/)
* [spliterator()](/Java/ConcurrentSkipListSet/spliterator/)
* [subSet()](/Java/ConcurrentSkipListSet/subSet/)
* [tailSet()](/Java/ConcurrentSkipListSet/tailSet/)

## Ejemplo
~~~java
{{ site.data.Java.C.ConcurrentSkipListSet.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentSkipListSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
