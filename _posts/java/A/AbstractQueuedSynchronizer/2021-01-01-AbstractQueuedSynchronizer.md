---
title: AbstractQueuedSynchronizer
permalink: Java/AbstractQueuedSynchronizer
date: 2021-01-11
key: JavaJava.A.AbstractQueuedSynchronizer
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractQueuedSynchronizer.description }}

## Sintaxis
~~~java
public abstract class AbstractQueuedSynchronizer extends AbstractOwnableSynchronizer implements Serializable
~~~

## Constructores
* [AbstractQueuedSynchronizer()](/Java/AbstractQueuedSynchronizer/AbstractQueuedSynchronizer/)

## Métodos
* [acquire()](/Java/AbstractQueuedSynchronizer/acquire)
* [acquireInterruptibly()](/Java/AbstractQueuedSynchronizer/acquireInterruptibly)
* [acquireShared()](/Java/AbstractQueuedSynchronizer/acquireShared)
* [acquireSharedInterruptibly()](/Java/AbstractQueuedSynchronizer/acquireSharedInterruptibly)
* [compareAndSetState()](/Java/AbstractQueuedSynchronizer/compareAndSetState)
* [getExclusiveQueuedThreads()](/Java/AbstractQueuedSynchronizer/getExclusiveQueuedThreads)
* [getFirstQueuedThread()](/Java/AbstractQueuedSynchronizer/getFirstQueuedThread)
* [getQueuedThreads()](/Java/AbstractQueuedSynchronizer/getQueuedThreads)
* [getQueueLength()](/Java/AbstractQueuedSynchronizer/getQueueLength)
* [getSharedQueuedThreads()](/Java/AbstractQueuedSynchronizer/getSharedQueuedThreads)
* [getState()](/Java/AbstractQueuedSynchronizer/getState)
* [getWaitingThreads()](/Java/AbstractQueuedSynchronizer/getWaitingThreads)
* [getWaitQueueLength()](/Java/AbstractQueuedSynchronizer/getWaitQueueLength)
* [hasContended()](/Java/AbstractQueuedSynchronizer/hasContended)
* [hasQueuedPredecessors()](/Java/AbstractQueuedSynchronizer/hasQueuedPredecessors)
* [hasQueuedThreads()](/Java/AbstractQueuedSynchronizer/hasQueuedThreads)
* [hasWaiters()](/Java/AbstractQueuedSynchronizer/hasWaiters)
* [isHeldExclusively()](/Java/AbstractQueuedSynchronizer/isHeldExclusively)
* [isQueued()](/Java/AbstractQueuedSynchronizer/isQueued)
* [owns()](/Java/AbstractQueuedSynchronizer/owns)
* [release()](/Java/AbstractQueuedSynchronizer/release)
* [releaseShared()](/Java/AbstractQueuedSynchronizer/releaseShared)
* [setState()](/Java/AbstractQueuedSynchronizer/setState)
* [toString()](/Java/AbstractQueuedSynchronizer/toString)
* [tryAcquire()](/Java/AbstractQueuedSynchronizer/tryAcquire)
* [tryAcquireNanos()](/Java/AbstractQueuedSynchronizer/tryAcquireNanos)
* [tryAcquireShared()](/Java/AbstractQueuedSynchronizer/tryAcquireShared)
* [tryAcquireSharedNanos()](/Java/AbstractQueuedSynchronizer/tryAcquireSharedNanos)
* [tryRelease()](/Java/AbstractQueuedSynchronizer/tryRelease)
* [tryReleaseShared()](/Java/AbstractQueuedSynchronizer/tryReleaseShared)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractQueuedSynchronizer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractQueuedSynchronizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
