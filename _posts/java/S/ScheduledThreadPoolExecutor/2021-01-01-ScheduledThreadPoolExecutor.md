---
title: ScheduledThreadPoolExecutor
permalink: Java/ScheduledThreadPoolExecutor
date: 2021-01-11
key: JavaJava.S.ScheduledThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ScheduledThreadPoolExecutor.description }}

## Sintaxis
~~~java
public class ScheduledThreadPoolExecutor extends ThreadPoolExecutor implements ScheduledExecutorService
~~~

## Constructores
* [ScheduledThreadPoolExecutor()](/Java/ScheduledThreadPoolExecutor/ScheduledThreadPoolExecutor/)

## Métodos
* [decorateTask()](/Java/ScheduledThreadPoolExecutor/decorateTask)
* [execute()](/Java/ScheduledThreadPoolExecutor/execute)
* [getContinueExistingPeriodicTasksAfterShutdownPolicy()](/Java/ScheduledThreadPoolExecutor/getContinueExistingPeriodicTasksAfterShutdownPolicy)
* [getExecuteExistingDelayedTasksAfterShutdownPolicy()](/Java/ScheduledThreadPoolExecutor/getExecuteExistingDelayedTasksAfterShutdownPolicy)
* [getQueue()](/Java/ScheduledThreadPoolExecutor/getQueue)
* [getRemoveOnCancelPolicy()](/Java/ScheduledThreadPoolExecutor/getRemoveOnCancelPolicy)
* [schedule()](/Java/ScheduledThreadPoolExecutor/schedule)
* [scheduleAtFixedRate()](/Java/ScheduledThreadPoolExecutor/scheduleAtFixedRate)
* [scheduleWithFixedDelay()](/Java/ScheduledThreadPoolExecutor/scheduleWithFixedDelay)
* [setContinueExistingPeriodicTasksAfterShutdownPolicy()](/Java/ScheduledThreadPoolExecutor/setContinueExistingPeriodicTasksAfterShutdownPolicy)
* [setExecuteExistingDelayedTasksAfterShutdownPolicy()](/Java/ScheduledThreadPoolExecutor/setExecuteExistingDelayedTasksAfterShutdownPolicy)
* [setRemoveOnCancelPolicy()](/Java/ScheduledThreadPoolExecutor/setRemoveOnCancelPolicy)
* [shutdown()](/Java/ScheduledThreadPoolExecutor/shutdown)
* [shutdownNow()](/Java/ScheduledThreadPoolExecutor/shutdownNow)
* [submit()](/Java/ScheduledThreadPoolExecutor/submit)

## Ejemplo
~~~java
{{ site.data.Java.S.ScheduledThreadPoolExecutor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScheduledThreadPoolExecutor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
