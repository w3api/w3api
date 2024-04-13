---
title: SynchronousQueue
permalink: /Java/SynchronousQueue/
date: 2021-01-11
key: Java.S.SynchronousQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SynchronousQueue.description }}

## Sintaxis
~~~java
public class SynchronousQueue<E> extends AbstractQueue<E> implements BlockingQueue<E>, Serializable
~~~

## Constructores
* [SynchronousQueue()](/Java/SynchronousQueue/SynchronousQueue/)

## Métodos
* [clear()](/Java/SynchronousQueue/clear)
* [contains()](/Java/SynchronousQueue/contains)
* [containsAll()](/Java/SynchronousQueue/containsAll)
* [drainTo()](/Java/SynchronousQueue/drainTo)
* [isEmpty()](/Java/SynchronousQueue/isEmpty)
* [iterator()](/Java/SynchronousQueue/iterator)
* [offer()](/Java/SynchronousQueue/offer)
* [peek()](/Java/SynchronousQueue/peek)
* [poll()](/Java/SynchronousQueue/poll)
* [put()](/Java/SynchronousQueue/put)
* [remainingCapacity()](/Java/SynchronousQueue/remainingCapacity)
* [remove()](/Java/SynchronousQueue/remove)
* [removeAll()](/Java/SynchronousQueue/removeAll)
* [retainAll()](/Java/SynchronousQueue/retainAll)
* [size()](/Java/SynchronousQueue/size)
* [spliterator()](/Java/SynchronousQueue/spliterator)
* [take()](/Java/SynchronousQueue/take)
* [toArray()](/Java/SynchronousQueue/toArray)
* [toString()](/Java/SynchronousQueue/toString)

## Ejemplo
~~~java
{{ site.data.Java.S.SynchronousQueue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SynchronousQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
