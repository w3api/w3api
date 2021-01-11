---
title: ReentrantReadWriteLock.ReadLock
permalink: Java/ReentrantReadWriteLock/ReadLock
date: 2021-01-11
key: JavaJava.R.ReentrantReadWriteLock.ReadLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReentrantReadWriteLock.ReadLock.description }}

## Sintaxis
~~~java
public static class ReentrantReadWriteLock.ReadLock extends Object implements Lock, Serializable
~~~

## Constructores
* [ReentrantReadWriteLock.ReadLock()](/Java/ReentrantReadWriteLock/ReadLock/ReentrantReadWriteLock/ReadLock/)

## Métodos
* [lock()](/Java/ReentrantReadWriteLock/ReadLock/lock)
* [lockInterruptibly()](/Java/ReentrantReadWriteLock/ReadLock/lockInterruptibly)
* [newCondition()](/Java/ReentrantReadWriteLock/ReadLock/newCondition)
* [toString()](/Java/ReentrantReadWriteLock/ReadLock/toString)
* [tryLock()](/Java/ReentrantReadWriteLock/ReadLock/tryLock)
* [unlock()](/Java/ReentrantReadWriteLock/ReadLock/unlock)

## Ejemplo
~~~java
{{ site.data.Java.R.ReentrantReadWriteLock.ReadLock.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReentrantReadWriteLock.ReadLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
