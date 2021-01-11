---
title: Semaphore
permalink: Java/Semaphore
date: 2021-01-11
key: JavaJava.S.Semaphore
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Semaphore.description }}

## Sintaxis
~~~java
public class Semaphore extends Object implements Serializable
~~~

## Constructores
* [Semaphore()](/Java/Semaphore/Semaphore/)

## Métodos
* [acquire()](/Java/Semaphore/acquire)
* [acquireUninterruptibly()](/Java/Semaphore/acquireUninterruptibly)
* [availablePermits()](/Java/Semaphore/availablePermits)
* [drainPermits()](/Java/Semaphore/drainPermits)
* [getQueuedThreads()](/Java/Semaphore/getQueuedThreads)
* [getQueueLength()](/Java/Semaphore/getQueueLength)
* [hasQueuedThreads()](/Java/Semaphore/hasQueuedThreads)
* [isFair()](/Java/Semaphore/isFair)
* [reducePermits()](/Java/Semaphore/reducePermits)
* [release()](/Java/Semaphore/release)
* [toString()](/Java/Semaphore/toString)
* [tryAcquire()](/Java/Semaphore/tryAcquire)

## Ejemplo
~~~java
{{ site.data.Java.S.Semaphore.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Semaphore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
