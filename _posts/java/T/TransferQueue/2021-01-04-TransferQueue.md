---
title: TransferQueue
permalink: Java/TransferQueue
date: 2021-01-04
key: JavaJava.T.TransferQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TransferQueue.description }}

## Sintaxis
~~~java
public interface TransferQueue<E> extends BlockingQueue<E>
~~~

## Métodos
* [getWaitingConsumerCount()](/Java/TransferQueue/getWaitingConsumerCount)
* [hasWaitingConsumer()](/Java/TransferQueue/hasWaitingConsumer)
* [transfer()](/Java/TransferQueue/transfer)
* [tryTransfer()](/Java/TransferQueue/tryTransfer)

## Ejemplo
~~~java
{{ site.data.Java.T.TransferQueue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransferQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
