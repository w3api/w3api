---
title: Collection
permalink: /Java/Collection/
date: 2021-01-11
key: Java.C.Collection
category: Java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Collection.description }}

## Sintaxis
~~~java
public interface Collection<E> extends Iterable<E>
~~~

## Métodos
* [add()](/Java/Collection/add)
* [addAll()](/Java/Collection/addAll)
* [clear()](/Java/Collection/clear)
* [contains()](/Java/Collection/contains)
* [containsAll()](/Java/Collection/containsAll)
* [equals()](/Java/Collection/equals)
* [hashCode()](/Java/Collection/hashCode)
* [isEmpty()](/Java/Collection/isEmpty)
* [iterator()](/Java/Collection/iterator)
* [parallelStream()](/Java/Collection/parallelStream)
* [remove()](/Java/Collection/remove)
* [removeAll()](/Java/Collection/removeAll)
* [removeIf()](/Java/Collection/removeIf)
* [retainAll()](/Java/Collection/retainAll)
* [size()](/Java/Collection/size)
* [spliterator()](/Java/Collection/spliterator)
* [stream()](/Java/Collection/stream)
* [toArray()](/Java/Collection/toArray)

## Ejemplo
~~~java
{{ site.data.Java.C.Collection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
