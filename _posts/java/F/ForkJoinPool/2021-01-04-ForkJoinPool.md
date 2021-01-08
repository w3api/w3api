---
title: ForkJoinPool
permalink: Java/ForkJoinPool
date: 2021-01-04
key: JavaJava.F.ForkJoinPool
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.ForkJoinPool.description }}

## Sintaxis
~~~java
public class ForkJoinPool extends AbstractExecutorService
~~~

## Constructores
* [ForkJoinPool()](/Java/ForkJoinPool/ForkJoinPool/)

## Campos
* [defaultForkJoinWorkerThreadFactory](/Java/ForkJoinPool/defaultForkJoinWorkerThreadFactory)

## Métodos
* [awaitQuiescence()](/Java/ForkJoinPool/awaitQuiescence)
* [awaitTermination()](/Java/ForkJoinPool/awaitTermination)
* [commonPool()](/Java/ForkJoinPool/commonPool)
* [drainTasksTo()](/Java/ForkJoinPool/drainTasksTo)
* [execute()](/Java/ForkJoinPool/execute)
* [getActiveThreadCount()](/Java/ForkJoinPool/getActiveThreadCount)
* [getAsyncMode()](/Java/ForkJoinPool/getAsyncMode)
* [getCommonPoolParallelism()](/Java/ForkJoinPool/getCommonPoolParallelism)
* [getFactory()](/Java/ForkJoinPool/getFactory)
* [getParallelism()](/Java/ForkJoinPool/getParallelism)
* [getPoolSize()](/Java/ForkJoinPool/getPoolSize)
* [getQueuedSubmissionCount()](/Java/ForkJoinPool/getQueuedSubmissionCount)
* [getQueuedTaskCount()](/Java/ForkJoinPool/getQueuedTaskCount)
* [getRunningThreadCount()](/Java/ForkJoinPool/getRunningThreadCount)
* [getStealCount()](/Java/ForkJoinPool/getStealCount)
* [getUncaughtExceptionHandler()](/Java/ForkJoinPool/getUncaughtExceptionHandler)
* [hasQueuedSubmissions()](/Java/ForkJoinPool/hasQueuedSubmissions)
* [invoke()](/Java/ForkJoinPool/invoke)
* [invokeAll()](/Java/ForkJoinPool/invokeAll)
* [isQuiescent()](/Java/ForkJoinPool/isQuiescent)
* [isShutdown()](/Java/ForkJoinPool/isShutdown)
* [isTerminated()](/Java/ForkJoinPool/isTerminated)
* [isTerminating()](/Java/ForkJoinPool/isTerminating)
* [managedBlock()](/Java/ForkJoinPool/managedBlock)
* [pollSubmission()](/Java/ForkJoinPool/pollSubmission)
* [shutdown()](/Java/ForkJoinPool/shutdown)
* [shutdownNow()](/Java/ForkJoinPool/shutdownNow)
* [submit()](/Java/ForkJoinPool/submit)
* [toString()](/Java/ForkJoinPool/toString)

## Ejemplo
~~~java
{{ site.data.Java.F.ForkJoinPool.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForkJoinPool.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
