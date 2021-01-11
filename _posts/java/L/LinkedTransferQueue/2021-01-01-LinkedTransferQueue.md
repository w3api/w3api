---
title: LinkedTransferQueue
permalink: Java/LinkedTransferQueue
date: 2021-01-11
key: JavaJava.L.LinkedTransferQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LinkedTransferQueue.description }}

## Sintaxis
~~~java
public class LinkedTransferQueue<E> extends AbstractQueue<E> implements TransferQueue<E>, Serializable
~~~

## Constructores
* [LinkedTransferQueue()](/Java/LinkedTransferQueue/LinkedTransferQueue/)

## Métodos
* [add()](/Java/LinkedTransferQueue/add)
* [contains()](/Java/LinkedTransferQueue/contains)
* [drainTo()](/Java/LinkedTransferQueue/drainTo)
* [forEach()](/Java/LinkedTransferQueue/forEach)
* [isEmpty()](/Java/LinkedTransferQueue/isEmpty)
* [iterator()](/Java/LinkedTransferQueue/iterator)
* [offer()](/Java/LinkedTransferQueue/offer)
* [put()](/Java/LinkedTransferQueue/put)
* [remainingCapacity()](/Java/LinkedTransferQueue/remainingCapacity)
* [remove()](/Java/LinkedTransferQueue/remove)
* [removeAll()](/Java/LinkedTransferQueue/removeAll)
* [removeIf()](/Java/LinkedTransferQueue/removeIf)
* [retainAll()](/Java/LinkedTransferQueue/retainAll)
* [size()](/Java/LinkedTransferQueue/size)
* [spliterator()](/Java/LinkedTransferQueue/spliterator)
* [toArray()](/Java/LinkedTransferQueue/toArray)
* [transfer()](/Java/LinkedTransferQueue/transfer)
* [tryTransfer()](/Java/LinkedTransferQueue/tryTransfer)

## Ejemplo
~~~java
{{ site.data.Java.L.LinkedTransferQueue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkedTransferQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
