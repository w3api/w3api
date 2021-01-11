---
title: ThreadPoolExecutor
permalink: Java/ThreadPoolExecutor
date: 2021-01-11
key: JavaJava.T.ThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadPoolExecutor.description }}

## Sintaxis
~~~java
public class ThreadPoolExecutor extends AbstractExecutorService
~~~

## Constructores
* [ThreadPoolExecutor()](/Java/ThreadPoolExecutor/ThreadPoolExecutor/)

## Métodos
* [afterExecute()](/Java/ThreadPoolExecutor/afterExecute)
* [allowCoreThreadTimeOut()](/Java/ThreadPoolExecutor/allowCoreThreadTimeOut)
* [allowsCoreThreadTimeOut()](/Java/ThreadPoolExecutor/allowsCoreThreadTimeOut)
* [beforeExecute()](/Java/ThreadPoolExecutor/beforeExecute)
* [execute()](/Java/ThreadPoolExecutor/execute)
* [finalize()](/Java/ThreadPoolExecutor/finalize)
* [getActiveCount()](/Java/ThreadPoolExecutor/getActiveCount)
* [getCompletedTaskCount()](/Java/ThreadPoolExecutor/getCompletedTaskCount)
* [getCorePoolSize()](/Java/ThreadPoolExecutor/getCorePoolSize)
* [getKeepAliveTime()](/Java/ThreadPoolExecutor/getKeepAliveTime)
* [getLargestPoolSize()](/Java/ThreadPoolExecutor/getLargestPoolSize)
* [getMaximumPoolSize()](/Java/ThreadPoolExecutor/getMaximumPoolSize)
* [getPoolSize()](/Java/ThreadPoolExecutor/getPoolSize)
* [getQueue()](/Java/ThreadPoolExecutor/getQueue)
* [getRejectedExecutionHandler()](/Java/ThreadPoolExecutor/getRejectedExecutionHandler)
* [getTaskCount()](/Java/ThreadPoolExecutor/getTaskCount)
* [getThreadFactory()](/Java/ThreadPoolExecutor/getThreadFactory)
* [isTerminating()](/Java/ThreadPoolExecutor/isTerminating)
* [prestartAllCoreThreads()](/Java/ThreadPoolExecutor/prestartAllCoreThreads)
* [prestartCoreThread()](/Java/ThreadPoolExecutor/prestartCoreThread)
* [purge()](/Java/ThreadPoolExecutor/purge)
* [remove()](/Java/ThreadPoolExecutor/remove)
* [setCorePoolSize()](/Java/ThreadPoolExecutor/setCorePoolSize)
* [setKeepAliveTime()](/Java/ThreadPoolExecutor/setKeepAliveTime)
* [setMaximumPoolSize()](/Java/ThreadPoolExecutor/setMaximumPoolSize)
* [setRejectedExecutionHandler()](/Java/ThreadPoolExecutor/setRejectedExecutionHandler)
* [setThreadFactory()](/Java/ThreadPoolExecutor/setThreadFactory)
* [shutdown()](/Java/ThreadPoolExecutor/shutdown)
* [shutdownNow()](/Java/ThreadPoolExecutor/shutdownNow)
* [terminated()](/Java/ThreadPoolExecutor/terminated)
* [toString()](/Java/ThreadPoolExecutor/toString)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadPoolExecutor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadPoolExecutor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
