---
title: BlockingDeque
permalink: /Java/BlockingDeque/
date: 2021-01-11
key: Java.B.BlockingDeque
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BlockingDeque.description }}

## Sintaxis
~~~java
public interface BlockingDeque<E> extends BlockingQueue<E>, Deque<E>
~~~

## Métodos
* [add()](/Java/BlockingDeque/add/)
* [addFirst()](/Java/BlockingDeque/addFirst/)
* [addLast()](/Java/BlockingDeque/addLast/)
* [contains()](/Java/BlockingDeque/contains/)
* [element()](/Java/BlockingDeque/element/)
* [iterator()](/Java/BlockingDeque/iterator/)
* [offer()](/Java/BlockingDeque/offer/)
* [offerFirst()](/Java/BlockingDeque/offerFirst/)
* [offerLast()](/Java/BlockingDeque/offerLast/)
* [peek()](/Java/BlockingDeque/peek/)
* [poll()](/Java/BlockingDeque/poll/)
* [pollFirst()](/Java/BlockingDeque/pollFirst/)
* [pollLast()](/Java/BlockingDeque/pollLast/)
* [push()](/Java/BlockingDeque/push/)
* [put()](/Java/BlockingDeque/put/)
* [putFirst()](/Java/BlockingDeque/putFirst/)
* [putLast()](/Java/BlockingDeque/putLast/)
* [remove()](/Java/BlockingDeque/remove/)
* [removeFirstOccurrence()](/Java/BlockingDeque/removeFirstOccurrence/)
* [removeLastOccurrence()](/Java/BlockingDeque/removeLastOccurrence/)
* [size()](/Java/BlockingDeque/size/)
* [take()](/Java/BlockingDeque/take/)
* [takeFirst()](/Java/BlockingDeque/takeFirst/)
* [takeLast()](/Java/BlockingDeque/takeLast/)

## Ejemplo
~~~java
{{ site.data.Java.B.BlockingDeque.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BlockingDeque.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
