---
title: ReentrantReadWriteLock.WriteLock
permalink: Java/ReentrantReadWriteLock/WriteLock
date: 2021-01-11
key: JavaJava.R.ReentrantReadWriteLock.WriteLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReentrantReadWriteLock.WriteLock.description }}

## Sintaxis
~~~java
public static class ReentrantReadWriteLock.WriteLock extends Object implements Lock, Serializable
~~~

## Constructores
* [ReentrantReadWriteLock.WriteLock()](/Java/ReentrantReadWriteLock/WriteLock/ReentrantReadWriteLock/WriteLock/)

## Métodos
* [getHoldCount()](/Java/ReentrantReadWriteLock/WriteLock/getHoldCount)
* [isHeldByCurrentThread()](/Java/ReentrantReadWriteLock/WriteLock/isHeldByCurrentThread)
* [lock()](/Java/ReentrantReadWriteLock/WriteLock/lock)
* [lockInterruptibly()](/Java/ReentrantReadWriteLock/WriteLock/lockInterruptibly)
* [newCondition()](/Java/ReentrantReadWriteLock/WriteLock/newCondition)
* [toString()](/Java/ReentrantReadWriteLock/WriteLock/toString)
* [tryLock()](/Java/ReentrantReadWriteLock/WriteLock/tryLock)
* [unlock()](/Java/ReentrantReadWriteLock/WriteLock/unlock)

## Ejemplo
~~~java
{{ site.data.Java.R.ReentrantReadWriteLock.WriteLock.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReentrantReadWriteLock.WriteLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
