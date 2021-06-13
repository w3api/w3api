---
title: AbstractQueuedLongSynchronizer
permalink: /Java/AbstractQueuedLongSynchronizer/
date: 2021-01-11
key: Java.A.AbstractQueuedLongSynchronizer
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractQueuedLongSynchronizer.description }}

## Sintaxis
~~~java
public abstract class AbstractQueuedLongSynchronizer extends AbstractOwnableSynchronizer implements Serializable
~~~

## Constructores
* [AbstractQueuedLongSynchronizer()](/Java/AbstractQueuedLongSynchronizer/AbstractQueuedLongSynchronizer/)

## Métodos
* [acquire()](/Java/AbstractQueuedLongSynchronizer/acquire)
* [acquireInterruptibly()](/Java/AbstractQueuedLongSynchronizer/acquireInterruptibly)
* [acquireShared()](/Java/AbstractQueuedLongSynchronizer/acquireShared)
* [acquireSharedInterruptibly()](/Java/AbstractQueuedLongSynchronizer/acquireSharedInterruptibly)
* [compareAndSetState()](/Java/AbstractQueuedLongSynchronizer/compareAndSetState)
* [getExclusiveQueuedThreads()](/Java/AbstractQueuedLongSynchronizer/getExclusiveQueuedThreads)
* [getFirstQueuedThread()](/Java/AbstractQueuedLongSynchronizer/getFirstQueuedThread)
* [getQueuedThreads()](/Java/AbstractQueuedLongSynchronizer/getQueuedThreads)
* [getQueueLength()](/Java/AbstractQueuedLongSynchronizer/getQueueLength)
* [getSharedQueuedThreads()](/Java/AbstractQueuedLongSynchronizer/getSharedQueuedThreads)
* [getState()](/Java/AbstractQueuedLongSynchronizer/getState)
* [getWaitingThreads()](/Java/AbstractQueuedLongSynchronizer/getWaitingThreads)
* [getWaitQueueLength()](/Java/AbstractQueuedLongSynchronizer/getWaitQueueLength)
* [hasContended()](/Java/AbstractQueuedLongSynchronizer/hasContended)
* [hasQueuedPredecessors()](/Java/AbstractQueuedLongSynchronizer/hasQueuedPredecessors)
* [hasQueuedThreads()](/Java/AbstractQueuedLongSynchronizer/hasQueuedThreads)
* [hasWaiters()](/Java/AbstractQueuedLongSynchronizer/hasWaiters)
* [isHeldExclusively()](/Java/AbstractQueuedLongSynchronizer/isHeldExclusively)
* [isQueued()](/Java/AbstractQueuedLongSynchronizer/isQueued)
* [owns()](/Java/AbstractQueuedLongSynchronizer/owns)
* [release()](/Java/AbstractQueuedLongSynchronizer/release)
* [releaseShared()](/Java/AbstractQueuedLongSynchronizer/releaseShared)
* [setState()](/Java/AbstractQueuedLongSynchronizer/setState)
* [toString()](/Java/AbstractQueuedLongSynchronizer/toString)
* [tryAcquire()](/Java/AbstractQueuedLongSynchronizer/tryAcquire)
* [tryAcquireNanos()](/Java/AbstractQueuedLongSynchronizer/tryAcquireNanos)
* [tryAcquireShared()](/Java/AbstractQueuedLongSynchronizer/tryAcquireShared)
* [tryAcquireSharedNanos()](/Java/AbstractQueuedLongSynchronizer/tryAcquireSharedNanos)
* [tryRelease()](/Java/AbstractQueuedLongSynchronizer/tryRelease)
* [tryReleaseShared()](/Java/AbstractQueuedLongSynchronizer/tryReleaseShared)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractQueuedLongSynchronizer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractQueuedLongSynchronizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
