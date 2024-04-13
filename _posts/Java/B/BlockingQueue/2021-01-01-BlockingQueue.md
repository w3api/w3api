---
title: BlockingQueue
permalink: /Java/BlockingQueue/
date: 2021-01-11
key: Java.B.BlockingQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BlockingQueue.description }}

## Sintaxis
~~~java
public interface BlockingQueue<E> extends Queue<E>
~~~

## Métodos
* [add()](/Java/BlockingQueue/add)
* [contains()](/Java/BlockingQueue/contains)
* [drainTo()](/Java/BlockingQueue/drainTo)
* [offer()](/Java/BlockingQueue/offer)
* [poll()](/Java/BlockingQueue/poll)
* [put()](/Java/BlockingQueue/put)
* [remainingCapacity()](/Java/BlockingQueue/remainingCapacity)
* [remove()](/Java/BlockingQueue/remove)
* [take()](/Java/BlockingQueue/take)

## Ejemplo
~~~java
{{ site.data.Java.B.BlockingQueue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BlockingQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
