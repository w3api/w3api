---
title: ReentrantReadWriteLock
permalink: /Java/ReentrantReadWriteLock/
date: 2021-01-11
key: Java.R.ReentrantReadWriteLock
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReentrantReadWriteLock.description }}

## Sintaxis
~~~java
public class ReentrantReadWriteLock extends Object implements ReadWriteLock, Serializable
~~~

## Constructores
* [ReentrantReadWriteLock()](/Java/ReentrantReadWriteLock/ReentrantReadWriteLock/)

## Métodos
* [getOwner()](/Java/ReentrantReadWriteLock/getOwner)
* [getQueuedReaderThreads()](/Java/ReentrantReadWriteLock/getQueuedReaderThreads)
* [getQueuedThreads()](/Java/ReentrantReadWriteLock/getQueuedThreads)
* [getQueuedWriterThreads()](/Java/ReentrantReadWriteLock/getQueuedWriterThreads)
* [getQueueLength()](/Java/ReentrantReadWriteLock/getQueueLength)
* [getReadHoldCount()](/Java/ReentrantReadWriteLock/getReadHoldCount)
* [getReadLockCount()](/Java/ReentrantReadWriteLock/getReadLockCount)
* [getWaitingThreads()](/Java/ReentrantReadWriteLock/getWaitingThreads)
* [getWaitQueueLength()](/Java/ReentrantReadWriteLock/getWaitQueueLength)
* [getWriteHoldCount()](/Java/ReentrantReadWriteLock/getWriteHoldCount)
* [hasQueuedThread()](/Java/ReentrantReadWriteLock/hasQueuedThread)
* [hasQueuedThreads()](/Java/ReentrantReadWriteLock/hasQueuedThreads)
* [hasWaiters()](/Java/ReentrantReadWriteLock/hasWaiters)
* [isFair()](/Java/ReentrantReadWriteLock/isFair)
* [isWriteLocked()](/Java/ReentrantReadWriteLock/isWriteLocked)
* [isWriteLockedByCurrentThread()](/Java/ReentrantReadWriteLock/isWriteLockedByCurrentThread)
* [toString()](/Java/ReentrantReadWriteLock/toString)

## Ejemplo
~~~java
{{ site.data.Java.R.ReentrantReadWriteLock.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReentrantReadWriteLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
