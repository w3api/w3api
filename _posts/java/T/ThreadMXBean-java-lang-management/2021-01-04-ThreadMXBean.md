---
title: ThreadMXBean
permalink: Java/ThreadMXBean-java-lang-management
date: 2021-01-04
key: JavaJava.T.ThreadMXBean-java-lang-management
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadMXBean-java-lang-management.description }}

## Sintaxis
~~~java
public interface ThreadMXBean extends PlatformManagedObject
~~~

## Métodos
* [dumpAllThreads()](/Java/ThreadMXBean-java-lang-management/dumpAllThreads)
* [findDeadlockedThreads()](/Java/ThreadMXBean-java-lang-management/findDeadlockedThreads)
* [findMonitorDeadlockedThreads()](/Java/ThreadMXBean-java-lang-management/findMonitorDeadlockedThreads)
* [getAllThreadIds()](/Java/ThreadMXBean-java-lang-management/getAllThreadIds)
* [getCurrentThreadCpuTime()](/Java/ThreadMXBean-java-lang-management/getCurrentThreadCpuTime)
* [getCurrentThreadUserTime()](/Java/ThreadMXBean-java-lang-management/getCurrentThreadUserTime)
* [getDaemonThreadCount()](/Java/ThreadMXBean-java-lang-management/getDaemonThreadCount)
* [getPeakThreadCount()](/Java/ThreadMXBean-java-lang-management/getPeakThreadCount)
* [getThreadCount()](/Java/ThreadMXBean-java-lang-management/getThreadCount)
* [getThreadCpuTime()](/Java/ThreadMXBean-java-lang-management/getThreadCpuTime)
* [getThreadInfo()](/Java/ThreadMXBean-java-lang-management/getThreadInfo)
* [getThreadUserTime()](/Java/ThreadMXBean-java-lang-management/getThreadUserTime)
* [getTotalStartedThreadCount()](/Java/ThreadMXBean-java-lang-management/getTotalStartedThreadCount)
* [isCurrentThreadCpuTimeSupported()](/Java/ThreadMXBean-java-lang-management/isCurrentThreadCpuTimeSupported)
* [isObjectMonitorUsageSupported()](/Java/ThreadMXBean-java-lang-management/isObjectMonitorUsageSupported)
* [isSynchronizerUsageSupported()](/Java/ThreadMXBean-java-lang-management/isSynchronizerUsageSupported)
* [isThreadContentionMonitoringEnabled()](/Java/ThreadMXBean-java-lang-management/isThreadContentionMonitoringEnabled)
* [isThreadContentionMonitoringSupported()](/Java/ThreadMXBean-java-lang-management/isThreadContentionMonitoringSupported)
* [isThreadCpuTimeEnabled()](/Java/ThreadMXBean-java-lang-management/isThreadCpuTimeEnabled)
* [isThreadCpuTimeSupported()](/Java/ThreadMXBean-java-lang-management/isThreadCpuTimeSupported)
* [resetPeakThreadCount()](/Java/ThreadMXBean-java-lang-management/resetPeakThreadCount)
* [setThreadContentionMonitoringEnabled()](/Java/ThreadMXBean-java-lang-management/setThreadContentionMonitoringEnabled)
* [setThreadCpuTimeEnabled()](/Java/ThreadMXBean-java-lang-management/setThreadCpuTimeEnabled)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadMXBean-java-lang-management.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadMXBean-java-lang-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
