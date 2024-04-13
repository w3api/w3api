---
title: ReentrantLock
permalink: /Java/ReentrantLock/
date: 2021-01-11
key: Java.R.ReentrantLock
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReentrantLock.description }}

## Sintaxis
~~~java
public class ReentrantLock extends Object implements Lock, Serializable
~~~

## Constructores
* [ReentrantLock()](/Java/ReentrantLock/ReentrantLock/)

## Métodos
* [getHoldCount()](/Java/ReentrantLock/getHoldCount)
* [getOwner()](/Java/ReentrantLock/getOwner)
* [getQueuedThreads()](/Java/ReentrantLock/getQueuedThreads)
* [getQueueLength()](/Java/ReentrantLock/getQueueLength)
* [getWaitingThreads()](/Java/ReentrantLock/getWaitingThreads)
* [getWaitQueueLength()](/Java/ReentrantLock/getWaitQueueLength)
* [hasQueuedThread()](/Java/ReentrantLock/hasQueuedThread)
* [hasQueuedThreads()](/Java/ReentrantLock/hasQueuedThreads)
* [hasWaiters()](/Java/ReentrantLock/hasWaiters)
* [isFair()](/Java/ReentrantLock/isFair)
* [isHeldByCurrentThread()](/Java/ReentrantLock/isHeldByCurrentThread)
* [isLocked()](/Java/ReentrantLock/isLocked)
* [lock()](/Java/ReentrantLock/lock)
* [lockInterruptibly()](/Java/ReentrantLock/lockInterruptibly)
* [newCondition()](/Java/ReentrantLock/newCondition)
* [toString()](/Java/ReentrantLock/toString)
* [tryLock()](/Java/ReentrantLock/tryLock)
* [unlock()](/Java/ReentrantLock/unlock)

## Ejemplo
~~~java
{{ site.data.Java.R.ReentrantLock.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReentrantLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
