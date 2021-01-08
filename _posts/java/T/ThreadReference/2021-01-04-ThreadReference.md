---
title: ThreadReference
permalink: Java/ThreadReference
date: 2021-01-04
key: JavaJava.T.ThreadReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadReference.description }}

## Sintaxis
~~~java
public interface ThreadReference extends ObjectReference
~~~

## Campos
* [THREAD_STATUS_MONITOR](/Java/ThreadReference/THREAD_STATUS_MONITOR)
* [THREAD_STATUS_NOT_STARTED](/Java/ThreadReference/THREAD_STATUS_NOT_STARTED)
* [THREAD_STATUS_RUNNING](/Java/ThreadReference/THREAD_STATUS_RUNNING)
* [THREAD_STATUS_SLEEPING](/Java/ThreadReference/THREAD_STATUS_SLEEPING)
* [THREAD_STATUS_UNKNOWN](/Java/ThreadReference/THREAD_STATUS_UNKNOWN)
* [THREAD_STATUS_WAIT](/Java/ThreadReference/THREAD_STATUS_WAIT)
* [THREAD_STATUS_ZOMBIE](/Java/ThreadReference/THREAD_STATUS_ZOMBIE)

## Métodos
* [currentContendedMonitor()](/Java/ThreadReference/currentContendedMonitor)
* [forceEarlyReturn()](/Java/ThreadReference/forceEarlyReturn)
* [frame()](/Java/ThreadReference/frame)
* [frameCount()](/Java/ThreadReference/frameCount)
* [frames()](/Java/ThreadReference/frames)
* [interrupt()](/Java/ThreadReference/interrupt)
* [isAtBreakpoint()](/Java/ThreadReference/isAtBreakpoint)
* [isSuspended()](/Java/ThreadReference/isSuspended)
* [name()](/Java/ThreadReference/name)
* [ownedMonitors()](/Java/ThreadReference/ownedMonitors)
* [ownedMonitorsAndFrames()](/Java/ThreadReference/ownedMonitorsAndFrames)
* [popFrames()](/Java/ThreadReference/popFrames)
* [resume()](/Java/ThreadReference/resume)
* [status()](/Java/ThreadReference/status)
* [stop()](/Java/ThreadReference/stop)
* [suspend()](/Java/ThreadReference/suspend)
* [suspendCount()](/Java/ThreadReference/suspendCount)
* [threadGroup()](/Java/ThreadReference/threadGroup)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadReference.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
