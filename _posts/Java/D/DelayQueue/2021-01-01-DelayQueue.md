---
title: DelayQueue
permalink: /Java/DelayQueue/
date: 2021-01-11
key: Java.D.DelayQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DelayQueue.description }}

## Sintaxis
~~~java
public class DelayQueue<E extends Delayed> extends AbstractQueue<E> implements BlockingQueue<E>
~~~

## Constructores
* [DelayQueue()](/Java/DelayQueue/DelayQueue/)

## Métodos
* [add()](/Java/DelayQueue/add/)
* [clear()](/Java/DelayQueue/clear/)
* [drainTo()](/Java/DelayQueue/drainTo/)
* [iterator()](/Java/DelayQueue/iterator/)
* [offer()](/Java/DelayQueue/offer/)
* [peek()](/Java/DelayQueue/peek/)
* [poll()](/Java/DelayQueue/poll/)
* [put()](/Java/DelayQueue/put/)
* [remainingCapacity()](/Java/DelayQueue/remainingCapacity/)
* [remove()](/Java/DelayQueue/remove/)
* [take()](/Java/DelayQueue/take/)
* [toArray()](/Java/DelayQueue/toArray/)

## Ejemplo
~~~java
{{ site.data.Java.D.DelayQueue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DelayQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
