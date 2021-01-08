---
title: ListIterator
permalink: Java/ListIterator
date: 2021-01-04
key: JavaJava.L.ListIterator
category: java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.ListIterator.description }}

## Sintaxis
~~~java
public interface ListIterator<E> extends Iterator<E>
~~~

## Métodos
* [add()](/Java/ListIterator/add)
* [hasNext()](/Java/ListIterator/hasNext)
* [hasPrevious()](/Java/ListIterator/hasPrevious)
* [next()](/Java/ListIterator/next)
* [nextIndex()](/Java/ListIterator/nextIndex)
* [previous()](/Java/ListIterator/previous)
* [previousIndex()](/Java/ListIterator/previousIndex)
* [remove()](/Java/ListIterator/remove)
* [set()](/Java/ListIterator/set)

## Ejemplo
~~~java
{{ site.data.Java.L.ListIterator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.ListIterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
