---
title: LinkedBlockingQueue
permalink: Java/LinkedBlockingQueue
date: 2021-01-11
key: JavaJava.L.LinkedBlockingQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LinkedBlockingQueue.description }}

## Sintaxis
~~~java
public class LinkedBlockingQueue<E> extends AbstractQueue<E> implements BlockingQueue<E>, Serializable
~~~

## Constructores
* [LinkedBlockingQueue()](/Java/LinkedBlockingQueue/LinkedBlockingQueue/)

## Métodos
* [clear()](/Java/LinkedBlockingQueue/clear)
* [contains()](/Java/LinkedBlockingQueue/contains)
* [drainTo()](/Java/LinkedBlockingQueue/drainTo)
* [forEach()](/Java/LinkedBlockingQueue/forEach)
* [iterator()](/Java/LinkedBlockingQueue/iterator)
* [offer()](/Java/LinkedBlockingQueue/offer)
* [put()](/Java/LinkedBlockingQueue/put)
* [remainingCapacity()](/Java/LinkedBlockingQueue/remainingCapacity)
* [remove()](/Java/LinkedBlockingQueue/remove)
* [removeAll()](/Java/LinkedBlockingQueue/removeAll)
* [removeIf()](/Java/LinkedBlockingQueue/removeIf)
* [retainAll()](/Java/LinkedBlockingQueue/retainAll)
* [size()](/Java/LinkedBlockingQueue/size)
* [spliterator()](/Java/LinkedBlockingQueue/spliterator)
* [toArray()](/Java/LinkedBlockingQueue/toArray)

## Ejemplo
~~~java
{{ site.data.Java.L.LinkedBlockingQueue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkedBlockingQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
