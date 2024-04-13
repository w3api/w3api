---
title: ArrayBlockingQueue
permalink: /Java/ArrayBlockingQueue/
date: 2021-01-11
key: Java.A.ArrayBlockingQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.ArrayBlockingQueue.description }}

## Sintaxis
~~~java
public class ArrayBlockingQueue<E> extends AbstractQueue<E> implements BlockingQueue<E>, Serializable
~~~

## Constructores
* [ArrayBlockingQueue()](/Java/ArrayBlockingQueue/ArrayBlockingQueue/)

## Métodos
* [add()](/Java/ArrayBlockingQueue/add)
* [clear()](/Java/ArrayBlockingQueue/clear)
* [contains()](/Java/ArrayBlockingQueue/contains)
* [drainTo()](/Java/ArrayBlockingQueue/drainTo)
* [forEach()](/Java/ArrayBlockingQueue/forEach)
* [iterator()](/Java/ArrayBlockingQueue/iterator)
* [offer()](/Java/ArrayBlockingQueue/offer)
* [put()](/Java/ArrayBlockingQueue/put)
* [remainingCapacity()](/Java/ArrayBlockingQueue/remainingCapacity)
* [remove()](/Java/ArrayBlockingQueue/remove)
* [removeAll()](/Java/ArrayBlockingQueue/removeAll)
* [removeIf()](/Java/ArrayBlockingQueue/removeIf)
* [retainAll()](/Java/ArrayBlockingQueue/retainAll)
* [size()](/Java/ArrayBlockingQueue/size)
* [spliterator()](/Java/ArrayBlockingQueue/spliterator)
* [toArray()](/Java/ArrayBlockingQueue/toArray)

## Ejemplo
~~~java
{{ site.data.Java.A.ArrayBlockingQueue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ArrayBlockingQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
