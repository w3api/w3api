---
title: ThreadGroup
permalink: Java/ThreadGroup
date: 2021-01-04
key: JavaJava.T.ThreadGroup
category: java
tags: ['java se', 'java.lang', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadGroup.description }}

## Sintaxis
~~~java
public class ThreadGroup extends Object implements Thread.UncaughtExceptionHandler
~~~

## Constructores
* [ThreadGroup()](/Java/ThreadGroup/ThreadGroup/)

## Métodos
* [activeCount()](/Java/ThreadGroup/activeCount)
* [activeGroupCount()](/Java/ThreadGroup/activeGroupCount)
* [allowThreadSuspension()](/Java/ThreadGroup/allowThreadSuspension)
* [checkAccess()](/Java/ThreadGroup/checkAccess)
* [destroy()](/Java/ThreadGroup/destroy)
* [enumerate()](/Java/ThreadGroup/enumerate)
* [getMaxPriority()](/Java/ThreadGroup/getMaxPriority)
* [getName()](/Java/ThreadGroup/getName)
* [getParent()](/Java/ThreadGroup/getParent)
* [interrupt()](/Java/ThreadGroup/interrupt)
* [isDaemon()](/Java/ThreadGroup/isDaemon)
* [isDestroyed()](/Java/ThreadGroup/isDestroyed)
* [list()](/Java/ThreadGroup/list)
* [parentOf()](/Java/ThreadGroup/parentOf)
* [resume()](/Java/ThreadGroup/resume)
* [setDaemon()](/Java/ThreadGroup/setDaemon)
* [setMaxPriority()](/Java/ThreadGroup/setMaxPriority)
* [stop()](/Java/ThreadGroup/stop)
* [suspend()](/Java/ThreadGroup/suspend)
* [toString()](/Java/ThreadGroup/toString)
* [uncaughtException()](/Java/ThreadGroup/uncaughtException)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadGroup.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadGroup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
