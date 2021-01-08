---
title: StampedLock
permalink: Java/StampedLock
date: 2021-01-04
key: JavaJava.S.StampedLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StampedLock.description }}

## Sintaxis
~~~java
public class StampedLock extends Object implements Serializable
~~~

## Constructores
* [StampedLock()](/Java/StampedLock/StampedLock/)

## Métodos
* [asReadLock()](/Java/StampedLock/asReadLock)
* [asReadWriteLock()](/Java/StampedLock/asReadWriteLock)
* [asWriteLock()](/Java/StampedLock/asWriteLock)
* [getReadLockCount()](/Java/StampedLock/getReadLockCount)
* [isLockStamp()](/Java/StampedLock/isLockStamp)
* [isOptimisticReadStamp()](/Java/StampedLock/isOptimisticReadStamp)
* [isReadLocked()](/Java/StampedLock/isReadLocked)
* [isReadLockStamp()](/Java/StampedLock/isReadLockStamp)
* [isWriteLocked()](/Java/StampedLock/isWriteLocked)
* [isWriteLockStamp()](/Java/StampedLock/isWriteLockStamp)
* [readLock()](/Java/StampedLock/readLock)
* [readLockInterruptibly()](/Java/StampedLock/readLockInterruptibly)
* [toString()](/Java/StampedLock/toString)
* [tryConvertToOptimisticRead()](/Java/StampedLock/tryConvertToOptimisticRead)
* [tryConvertToReadLock()](/Java/StampedLock/tryConvertToReadLock)
* [tryConvertToWriteLock()](/Java/StampedLock/tryConvertToWriteLock)
* [tryOptimisticRead()](/Java/StampedLock/tryOptimisticRead)
* [tryReadLock()](/Java/StampedLock/tryReadLock)
* [tryUnlockRead()](/Java/StampedLock/tryUnlockRead)
* [tryUnlockWrite()](/Java/StampedLock/tryUnlockWrite)
* [tryWriteLock()](/Java/StampedLock/tryWriteLock)
* [unlock()](/Java/StampedLock/unlock)
* [unlockRead()](/Java/StampedLock/unlockRead)
* [unlockWrite()](/Java/StampedLock/unlockWrite)
* [validate()](/Java/StampedLock/validate)
* [writeLock()](/Java/StampedLock/writeLock)
* [writeLockInterruptibly()](/Java/StampedLock/writeLockInterruptibly)

## Ejemplo
~~~java
{{ site.data.Java.S.StampedLock.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StampedLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
