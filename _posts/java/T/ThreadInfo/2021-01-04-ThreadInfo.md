---
title: ThreadInfo
permalink: Java/ThreadInfo
date: 2021-01-04
key: JavaJava.T.ThreadInfo
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadInfo.description }}

## Sintaxis
~~~java
public class ThreadInfo extends Object
~~~

## Métodos
* [from()](/Java/ThreadInfo/from)
* [getBlockedCount()](/Java/ThreadInfo/getBlockedCount)
* [getBlockedTime()](/Java/ThreadInfo/getBlockedTime)
* [getLockedMonitors()](/Java/ThreadInfo/getLockedMonitors)
* [getLockedSynchronizers()](/Java/ThreadInfo/getLockedSynchronizers)
* [getLockInfo()](/Java/ThreadInfo/getLockInfo)
* [getLockName()](/Java/ThreadInfo/getLockName)
* [getLockOwnerId()](/Java/ThreadInfo/getLockOwnerId)
* [getLockOwnerName()](/Java/ThreadInfo/getLockOwnerName)
* [getPriority()](/Java/ThreadInfo/getPriority)
* [getStackTrace()](/Java/ThreadInfo/getStackTrace)
* [getThreadId()](/Java/ThreadInfo/getThreadId)
* [getThreadName()](/Java/ThreadInfo/getThreadName)
* [getThreadState()](/Java/ThreadInfo/getThreadState)
* [getWaitedCount()](/Java/ThreadInfo/getWaitedCount)
* [getWaitedTime()](/Java/ThreadInfo/getWaitedTime)
* [isDaemon()](/Java/ThreadInfo/isDaemon)
* [isInNative()](/Java/ThreadInfo/isInNative)
* [isSuspended()](/Java/ThreadInfo/isSuspended)
* [toString()](/Java/ThreadInfo/toString)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadInfo.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
