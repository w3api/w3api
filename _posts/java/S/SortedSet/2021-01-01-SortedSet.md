---
title: SortedSet
permalink: Java/SortedSet
date: 2021-01-11
key: JavaJava.S.SortedSet
category: java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SortedSet.description }}

## Sintaxis
~~~java
public interface SortedSet<E> extends Set<E>
~~~

## Métodos
* [comparator()](/Java/SortedSet/comparator)
* [first()](/Java/SortedSet/first)
* [headSet()](/Java/SortedSet/headSet)
* [last()](/Java/SortedSet/last)
* [spliterator()](/Java/SortedSet/spliterator)
* [subSet()](/Java/SortedSet/subSet)
* [tailSet()](/Java/SortedSet/tailSet)

## Ejemplo
~~~java
{{ site.data.Java.S.SortedSet.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SortedSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
