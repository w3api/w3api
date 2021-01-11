---
title: ForkJoinTask
permalink: Java/ForkJoinTask
date: 2021-01-11
key: JavaJava.F.ForkJoinTask
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.ForkJoinTask.description }}

## Sintaxis
~~~java
public abstract class ForkJoinTask<V> extends Object implements Future<V>, Serializable
~~~

## Constructores
* [ForkJoinTask()](/Java/ForkJoinTask/ForkJoinTask/)

## Métodos
* [adapt()](/Java/ForkJoinTask/adapt)
* [cancel()](/Java/ForkJoinTask/cancel)
* [compareAndSetForkJoinTaskTag()](/Java/ForkJoinTask/compareAndSetForkJoinTaskTag)
* [complete()](/Java/ForkJoinTask/complete)
* [completeExceptionally()](/Java/ForkJoinTask/completeExceptionally)
* [exec()](/Java/ForkJoinTask/exec)
* [fork()](/Java/ForkJoinTask/fork)
* [get()](/Java/ForkJoinTask/get)
* [getException()](/Java/ForkJoinTask/getException)
* [getForkJoinTaskTag()](/Java/ForkJoinTask/getForkJoinTaskTag)
* [getPool()](/Java/ForkJoinTask/getPool)
* [getQueuedTaskCount()](/Java/ForkJoinTask/getQueuedTaskCount)
* [getRawResult()](/Java/ForkJoinTask/getRawResult)
* [getSurplusQueuedTaskCount()](/Java/ForkJoinTask/getSurplusQueuedTaskCount)
* [helpQuiesce()](/Java/ForkJoinTask/helpQuiesce)
* [inForkJoinPool()](/Java/ForkJoinTask/inForkJoinPool)
* [invoke()](/Java/ForkJoinTask/invoke)
* [invokeAll()](/Java/ForkJoinTask/invokeAll)
* [isCompletedAbnormally()](/Java/ForkJoinTask/isCompletedAbnormally)
* [isCompletedNormally()](/Java/ForkJoinTask/isCompletedNormally)
* [join()](/Java/ForkJoinTask/join)
* [peekNextLocalTask()](/Java/ForkJoinTask/peekNextLocalTask)
* [pollNextLocalTask()](/Java/ForkJoinTask/pollNextLocalTask)
* [pollSubmission()](/Java/ForkJoinTask/pollSubmission)
* [pollTask()](/Java/ForkJoinTask/pollTask)
* [quietlyComplete()](/Java/ForkJoinTask/quietlyComplete)
* [quietlyInvoke()](/Java/ForkJoinTask/quietlyInvoke)
* [quietlyJoin()](/Java/ForkJoinTask/quietlyJoin)
* [reinitialize()](/Java/ForkJoinTask/reinitialize)
* [setForkJoinTaskTag()](/Java/ForkJoinTask/setForkJoinTaskTag)
* [setRawResult()](/Java/ForkJoinTask/setRawResult)
* [tryUnfork()](/Java/ForkJoinTask/tryUnfork)

## Ejemplo
~~~java
{{ site.data.Java.F.ForkJoinTask.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForkJoinTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
